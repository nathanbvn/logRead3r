import tkinter as tk
from tkinter.filedialog import askopenfilename
import subprocess
from colorama import init, Fore, Style,Back
import re
import readline


readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode emacs") 
readline.parse_and_bind("set enable-keypad on")

bookopen = open("book.txt","r")
book = bookopen.read().splitlines()
bookopen.close()


HISTORY_FILE = ".logreadr_history"

try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    pass

init()

highlight = []

find = "changeme"

######## FONCTIONS


def splitter(query,delimiter) : 
	if delimiter not in query : 
		if delimiter == ";":
			return query.split(",")
		else : 
			return []
	else : 
		return query.split(delimiter)[1].split(",")

def change():
    root = tk.Tk()
    root.withdraw() 
    filename = askopenfilename()
    root.destroy() 
    return filename


def sendColor(text, search):

	ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
	text = ip_pattern.sub(lambda match: f"{Style.BRIGHT}{Fore.GREEN}{match.group(0)}{Style.RESET_ALL}", text)

	for w in book:
		pattern = re.compile(re.escape(w), re.IGNORECASE)
		text = pattern.sub(lambda match: f"{Style.BRIGHT}{Fore.MAGENTA}{match.group(0)}{Style.RESET_ALL}", text)

	for j in highlight :
		pattern = re.compile(re.escape(j), re.IGNORECASE)
		text = pattern.sub(lambda match: f"{Style.BRIGHT}{Fore.RED}{match.group(0)}{Style.RESET_ALL}", text)
		
	for i in search:
		pattern = re.compile(re.escape(i), re.IGNORECASE)
		text = pattern.sub(lambda match: f"{Style.BRIGHT}{Fore.YELLOW}{match.group(0)}{Style.RESET_ALL}", text)


	print(text)




#########

filename = change()

while True:

	try : 


		find = input("What do you want to find (; : AND | / : OR | ! : NOT) : ")

		if find == "changeme" :
			filename = change()

		elif find =="exit":
			break

		elif find== "clear":
			subprocess.run("clear",shell=True)

		elif "show" in find: 
			if "+" in find :
				highlight.append(find.split("+")[1])
			elif "-" in find : 
				try :
					highlight.remove(find.split("-")[1])
				except:
					print("Failed to remove, here is the list :",highlight)
			elif 'resetshow' in find:
				highlight = []

			else : 
				print(highlight)
		
		elif "save" in find :
			savesopen = open("saves.csv","a+")
			if "reset" in find : 
				topline = "RecordNumber,EventRecordId,TimeCreated,EventId,Level,Provider,Channel,ProcessId,ThreadId,Computer,ChunkNumber,UserId,MapDescription,UserName,RemoteHost,PayloadData1,PayloadData2,PayloadData3,PayloadData4,PayloadData5,PayloadData6,ExecutableInfo,HiddenRecord,SourceFile,Keywords,ExtraDataOffset,Payload,Comment\n"
				savesopen.seek(0)
				savesopen.truncate()
				savesopen.write(topline)
			else : 
				try : 
					lognum = find.split("save ")[1].split(' "')[0]
					logline = str(logDico[str(lognum)])+","+find.split('"')[1]+"\n"
					print(logline)
					savesopen.write(logline)
					print("Saved Log",lognum)
				except : 
					print("Failed to save the log")

			savesopen.close()
			



		else :

			logDico = {}
			logcount = 0

			f = open(filename,"r",encoding="UTF-8")

			f = f.read()

			cpt= 0

			andList = splitter(find,";")
			orList = splitter(find,"/")
			notList = splitter(find,"!")


			# Pour i = chaque ligne
			for i in f.splitlines():
				andOk = 0
				orOk = 0
				notOk = 0


				#Pour tous les elements de ma liste AND
				for j in andList:
					if j.lower() in i.lower() :
						andOk +=1


				for n in notList:
					if n.lower() in i.lower() :
						notOk += 1

				for o in orList:
					if o.lower() in i.lower():
						orOk += 1


				#Si mes deux élements sont la 
				if (andOk == len(andList) or orOk >= 1) and notOk == 0:
						print("\n")
						print("Log number :",logcount)
						print("\n")
						lineFull = ""
						csv = ""
						payload = ""
						switch = 0



						#Switch to JSON format
						for lettre in i : 
							if switch == 0 :
								if lettre == "{":
									switch = 1
									payload += "{"
								else : 
									csv += lettre
							else : 
								payload += lettre

						for line in csv.split(","):
							lineFull+= line+"   -    "


						wholeText = lineFull+"\n"+payload

						logDico[str(logcount)] = i

						sendColor(wholeText,andList)

						print("\n")
						print("\n")
						cpt += 1
						logcount +=1

			print(cpt,"elements trouvés pour :",find)
			print("\n")

	except KeyboardInterrupt:
		print("\nRecherche interrompue par l'utilisateur.\n")
		continue


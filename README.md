## logRead3r

logRead3r is a fast, interactive command-line log parser built for Digital Forensics and Incident Response (DFIR) workflows. Designed to accelerate Windows Event Log analysis, it highlights critical artifacts, supports complex search logic, and helps investigators extract meaningful evidence and build accurate timelines.
### 🔧 Installation
**📦 Requirements**

    Python 3.6+

    colorama

    tkinter (included in standard Python installations)

    readline (Unix/macOS only — handled natively; Windows users should install pyreadline3)
    

**🐍 Install dependencies**

`pip install colorama`


**📥 Clone the repository**

`git clone https://github.com/nathanbvn/logRead3r.git
cd logRead3r
python3 logRead3r.py`



### 🔍 How It Works

You select a log file (e.g. a Windows Event Log in converted .csv or .txt format).

logRead3r lets you interactively search using powerful filters:

`;` for AND

`/` for OR

`!` for NOT

It colorizes results based on:

- Predefined critical keywords (from `book.txt`)
- User-defined highlights
- Searched Keywords
- IP addresses


Logs can be saved and annotated into a `saves.csv` file for later reporting.

---

### ✨ Features
**✅ Interactive CLI Search**
Supports flexible search logic:

*Symbol	Function Example*

`;`	AND	`;password,admin;`

`/`	OR	`/error,admin,denied/`

`!`	NOT	`!password,guest!`

---

**✅ Color Highlighting**

- Green – IP addresses
- Magenta – Keywords from book.txt (e.g., malware, password)
- Red – User-defined highlights (show +keyword)
- Yellow – Search matches


---


**✅ Commands**
Command	Description

`changeme`	Open file picker to load a new log file

`exit`	Quit the program

`clear`	Clear the terminal

`show`	List current highlighted keywords

`show +term` Add a keyword to highlight in red

`show -term`	Remove a keyword from highlights

`resetshow`	Reset all user-defined highlights

`save <num> "comment"` Save a specific log entry by its number, with an optional comment

`save reset`	Reset the saves.csv file with headers


---



**✅ Annotation & Export**

Save key log entries using:
`save 4 "User logged in from suspicious IP"`


All saved entries go into `saves.csv` with the original data and your comment.

---

**📁 Files**

- `logRead3r.py` – Main program

- `book.txt` – Keyword list for automatic highlighting

- `saves.csv` – Output file for saved logs

- `.logreadr_history` – Stores your search history across sessions

---

**🧪 Supported Formats**

    Plain text or CSV log exports (such as from Windows Event Viewer)

    Entries must be line-based (one event per line), with optional embedded JSON payloads

---

**💡 Use Case Examples**

*Find logs with both "login" AND "remote" but exclude "guest"*
`;login,remote;!guest!`

*Find logs containing either "192.168.0.1"*
`192.168.0.1`
OR`
;192.168.0.1;`

*Find logs with both "login" AND "remote" OR "guest" OR "admin"*
`;login,remote;/guest,admin/`

---

**📷 Images**

*Search of `KALI` AND `Successful Logon`*

![image](https://github.com/user-attachments/assets/bd430e20-dc84-49fc-bbcc-7b92f4d4a477)

---

**🖥️ Platform Support**

    ✅ Linux

    ✅ Windows

    ⬜ macOS (untested, should work with minimal tweaks)




logRead3r was designed with speed and usability in mind—no frills, just fast, actionable log insights to help you respond faster and more effectively.

📜 License

`MIT License — use freely, contribute if you’d like!`

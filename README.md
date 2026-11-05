# GitHub Trending Tech Tracker 🚀

An automated Python data pipeline that fetches real-time trending repositories from the GitHub REST API, parses the JSON response, persists records into a local SQLite relational database, and executes threshold-based alert logic to flag high-impact projects.

---

## 🛠️ Tech Stack
* **Programming Language:** Python 3
* **API Integration:** Python `requests` library
* **Database & Storage:** SQLite3 (Local relational database with automatic timestamp logging)
* **Development Environment:** Visual Studio Code & Windows PowerShell

---

## ✨ Key Features
* **Live API Fetching:** Connects programmatically to GitHub's search API to pull the most starred Python repositories.
* **Persistent Storage:** Automatically structures and saves repository data (Name, Description, Star Count, and Timestamp) into a local SQLite database (`tracker.db`).
* **Automated Alerting Logic:** Scans stored database records using conditional queries to highlight repositories exceeding specific impact thresholds.

---

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mukeshanand534-gif/project.git](https://github.com/mukeshanand534-gif/projectgit)
   cd project

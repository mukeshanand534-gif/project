import sqlite3
import requests

# 1. Connect to local database
conn = sqlite3.connect("tracker.db")
cursor = conn.cursor()

# 2. Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS repositories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        stars INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# 3. Fetch live data from GitHub API
url = "https://api.github.com/search/repositories?q=language:python+sort:stars&order=desc"
print("Connecting to GitHub...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Success! Processing repositories...\n")

    cursor.execute("DELETE FROM repositories")

    for repo in data["items"][:10]: # Let's check top 10 this time
        name = repo["name"]
        description = repo["description"]
        stars = repo["stargazers_count"]

        # Insert into database
        cursor.execute("""
            INSERT INTO repositories (name, description, stars)
            VALUES (?, ?, ?)
        """, (name, description, stars))
    
    conn.commit()

    # 4. Smart Alert Logic: Scan database for high-impact repositories
    print("==========================================")
    print("         🚨 TECH TREND ALERTS 🚨          ")
    print("==========================================")
    
    # Query for repositories with more than 100,000 stars (or adjust as needed)
    cursor.execute("SELECT name, stars FROM repositories WHERE stars > 100000 ORDER BY stars DESC")
    high_impact_repos = cursor.fetchall()

    for repo in high_impact_repos:
        print(f"🔥 HOT REPO ALERT: '{repo[0]}' has crossed {repo[1]:,} stars!")

    print("\n--- Full Database Summary ---")
    cursor.execute("SELECT name, stars FROM repositories")
    for row in cursor.fetchall():
        print(f"📌 {row[0]} - ⭐ {row[1]:,}")

else:
    print(f"Failed to connect. Error code: {response.status_code}")

conn.close()
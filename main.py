from github import Github
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Učitaj token iz .env fajla
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

# Poveži se na GitHub
g = Github(token)

# Izaberi repozitorijum (menjam ako hoću drugi repo)
repo_name = "MrVladan/github-api-analytics"
repo = g.get_repo(repo_name)

print(f"\n📊 Statistika za repozitorijum: {repo.full_name}\n")

# Broj commit-a
commits = repo.get_commits()
print(f"🔹 Broj commit-a: {commits.totalCount}")

# Issues
open_issues = repo.get_issues(state="open").totalCount
closed_issues = repo.get_issues(state="closed").totalCount
print(f"🔹 Issues - otvoreni: {open_issues}, zatvoreni: {closed_issues}")

# Contributors
contributors_data = repo.get_contributors()
contributors_count = repo.get_contributors().totalCount
print(f"🔹 Broj contributors: {contributors_count}")

    # ----- 📊 Pie chart: Issues -----
if open_issues + closed_issues > 0:
    labels = ["Otvoreni", "Zatvoreni"]
    sizes = [open_issues, closed_issues]
    colors = ["orange", "green"]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.title(f"Issues status za {repo_name}")
    plt.savefig("issues_status.png")
    print("📈 Graf issues_status.png sačuvan.")
else:
    print("⚠️ Repo nema issues → preskačem pie chart.")


# ----- 📊 Bar chart: Contributors -----
names = []
commit_counts = []

for contributor in contributors_data:
    names.append(contributor.login)
    commit_counts.append(contributor.contributions)

plt.figure(figsize=(8, 5))
plt.bar(names, commit_counts, color="blue")
plt.xlabel("Contributors")
plt.ylabel("Broj commit-a")
plt.title(f"Doprinos po contributor-ima za {repo_name}")
plt.savefig("contributors_activity.png")
print("📈 Graf contributors_activity.png sačuvan.")

# --- Mesečna aktivnost commit-ova -> commits_activity.png ---
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

commit_dates = []
for c in commits:
    try:
        dt = c.commit.author.date
        ym = dt.strftime("%Y-%m")
        commit_dates.append(ym)
    except Exception:
        continue

if commit_dates:
    counts = Counter(commit_dates)
    months = sorted(counts.keys())
    values = [counts[m] for m in months]

    plt.figure(figsize=(9, 5))
    plt.bar(months, values)
    plt.xlabel("Mesec")
    plt.ylabel("Broj commit-ova")
    plt.title(f"Commit aktivnost po mesecima – {repo_name}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("commits_activity.png")
    print("📈 Graf commits_activity.png sačuvan.")
else:
    print("ℹ️ Nema podataka za mesečni graf commit-ova (repo bez commit-a?).")

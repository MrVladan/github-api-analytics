from github import Github
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Učitaj token iz .env fajla
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

# Poveži se na GitHub
g = Github(token)

# Izaberi repozitorijum (menjaj ako hoćeš drugi repo)
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

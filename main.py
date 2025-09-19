
from github import Github
import os
from dotenv import load_dotenv

# Učitaj token iz .env fajla
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

g = Github(token)

# Uloguj se i povuci podatke o svom nalogu
user = g.get_user()
print("Ulogovan kao:", user.login)

# Izlistaj repozitorijume
for repo in user.get_repos():
    print(repo.full_name)

import requests
import json

user_name = "TGLSpain1"

with open("Github_token.txt", "r") as f:
	password = f.read()

repo_owner_name = "tglspain1"
repo_name = "project-build-your-own-game"

base_url = "https://api.github.com"
path = f"/repos/{repo_owner_name}/{repo_name}/commits"
rate_path = "/rate_limit"

final_url = base_url + path
all_commits = requests.get(final_url, auth = (user_name, password))
commits_response = json.loads(all_commits.content)
total_commits = len(commits_response)
print(f"Total number of commits for this repository is {total_commits}")
print("finished")




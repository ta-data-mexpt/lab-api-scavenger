import requests
import json

user_name = "TGLSpain1"

with open("Github_token.txt", "r") as f:
	password = f.read()

repo_owner_name = "ta-data-mexpt"
repo_name = "project-build-your-own-game"

base_url = "https://api.github.com"
path = f"/repos/{repo_owner_name}/{repo_name}/forks"

languages = set()
i = 1
exist_more_results = True

languages = set()

while exist_more_results:
	final_url = base_url + path + f"?page={i}"
	print(final_url)
	all_forks = requests.get(final_url, auth = (user_name, password))
	forks_response = json.loads(all_forks.content)
	more_languages = {element["language"] for element in forks_response}
	languages = languages | more_languages
	next_url_element = all_forks.headers["Link"]
	check_next_url = next_url_element.split(" ")[1]
	if check_next_url == 'rel="next"':
		i += 1
	else:
		exist_more_results = False

print(languages)
print("finished")



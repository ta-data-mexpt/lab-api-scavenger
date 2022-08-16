import requests
import json
import time
import base64

# FALTA DESCODIFICAR BASE 64 CADA CONTENT, ORDENAR ARCHIVOS Y JUNTAR EN LISTA O EN STRING

user_name = "TGLSpain1"

with open("Github_token.txt", "r") as f:
	password = f.read()

repo_owner_name = "ironhack-datalabs"
repo_name = "scavenger"

base_url = "https://api.github.com"
path = f"/repos/{repo_owner_name}/{repo_name}/contents"
rate_path = "/rate_limit"
final_url = base_url + path

all_files = requests.get(final_url, auth = (user_name, password))
all_files_response = json.loads(all_files.content)
if 400 <= all_files.status_code < 500:
	print(all_files.content)

file_list = [(file["name"], file["type"]) for file in all_files_response]
folder_list = [file_element for file_element in file_list if file_element[1] == "dir"]
folder_paths = [folder[0] for folder in folder_list]

print("Getting all files")
total_files_list = []
for folder_path in folder_paths:
	folder_contents = requests.get(final_url + f"/{folder_path}", auth = (user_name, password))
	folder_contents_response = json.loads(folder_contents.content)
	total_files_list.append(folder_contents_response)
	time.sleep(0.5)

print(len(total_files_list))

total_files_list_flat = [folder_files for folder in total_files_list for folder_files in folder]
print(total_files_list_flat)

final_total_files_list = [flat_file for flat_file in total_files_list_flat if "scavengerhunt" in flat_file["name"]]

with open ("folder_contents.txt", "w") as f:
	for final_total_file in final_total_files_list:
		print(f"{final_total_file['path']}\n")
		f.write(f"{final_total_file['path']}\n")


file_names = []
with open ("folder_contents.txt", "r") as f:
	for row in f:
		name = row[:-1]
		file_names.append(name)

file_tuples = [(file_name, int(file_name.split(".")[1])) for file_name in file_names]

sorted_file_tuples = sorted(file_tuples, key = lambda x: x[1])

texts = []

for file_tuple in sorted_file_tuples:
	file_contents = requests.get(final_url + f"/{file_tuple[0]}", auth = (user_name, password))
	file_response = json.loads(file_contents.content)
	content_base64 = file_response["content"]
	content_ascii = content_base64.encode('ascii')
	content_decoded = base64.b64decode(content_ascii)
	final_content = content_decoded.decode('ascii')
	texts.append(final_content)

final_text = " ".join(texts)
print(final_text)





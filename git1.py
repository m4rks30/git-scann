import requests
username = "YOUR_USERNAME"
forked_repos = []
for page in range(1, 11):
    url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
    response = requests.get(url)
    repos = response.json()
    for repo in repos:
        if repo["fork"] and repo["source"]:
            forked_repos.append(repo["name"])
print(forked_repos)

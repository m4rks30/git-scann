from github import Github

# Replace with your access token
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

g = Github(ACCESS_TOKEN)
repo_link = "https://github.com/user/repo"
repo_name = repo_link.split('/')[-2]

repo = g.get_repo(repo_name)

files = repo.get_contents("")
for file in files:
    content = file.decoded_content
    for repo in g.get_user().get_repos():
        try:
            if repo.name != repo_name:
                contents = repo.get_contents("")
                for content_file in contents:
                    if content_file.decoded_content == content:
                        print(repo.html_url)
        except:
            pass

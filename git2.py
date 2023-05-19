import requests

headers = {
    'Authorization': 'Token TOKEN',
}

params = (
    ('q', 'similar:OWNER/REPO'),
)

response = requests.get('https://api.github.com/search/repositories', headers=headers, params=params)
if response.status_code == 200:
    repositories = response.json()['items']
    for repository in repositories:
        print(repository['full_name'])
else:
    print("There was an error with the request.")

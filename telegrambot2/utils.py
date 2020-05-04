import requests


github_url = 'https://api.github.com/users/'
github = 'https://github.com/'

def _requests(url):
    response = requests.get(url)
    if not response.ok:
        raise Exception('Böyle bir kullanıcı yok!')
    return response


def button_handler(name):
    id, name = name.split(' ')

    if id == '1':
        response = _requests(f'{github_url}{name}').json()
        response = f"""
*Kullanıcı adı*: {response['name']}
*Repo sayısı*: {response['public_repos']}
*Takip ettiği*: {response['following']}
*Takipçi*: {response['followers']}
"""
        return response
    elif id == '2':
        response = _requests(f'{github_url}{name}/received_events').json()

        results = set([rp['actor']['login'] for rp in response])

        response = ''
        for result in results:
            response += f'Kullanıcı adi: [{result}]({f"{github}{result}"}) \n'
        response = response.replace('-', '\-')
        return response

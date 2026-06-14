import requests

HOST = 'http://127.0.0.1:8000'

def test_post():
    url = f"{HOST}/user"
    
    for name in ['nandu', 'deepu', 'amma', 'nanna', 'test', 'new-test']:
        res = requests.post(url, json={'name': name})
        res.raise_for_status()
        print(res.json())

def test_ping(n=10):
    url = f"{HOST}/ping"
    for i in range(n):
        res = requests.get(url)
        res.raise_for_status()
        print(res.json())

def test_create_user():
    url = f"{HOST}/user"
    res = requests.post(url, json={'username': 'nandu', 'email': 'nk732100@gmail.com'})
    res.raise_for_status()
    print(res.json())

def test_list_users():
    url = f"{HOST}/user"
    res = requests.get(url)
    res.raise_for_status()
    print(res.json())

if __name__ == "__main__":
    # test_ping()
    # test_post()
    # test_create_user()
    test_list_users()

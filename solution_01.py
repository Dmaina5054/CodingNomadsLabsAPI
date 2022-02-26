import requests

url = ' http://demo.codingnomads.co:8080/tasks_api/users'

def fetchresponse():
    with requests.get(url) as response:
        print(response.status_code)
        print(response.encoding)
        print(response.text)
        
        
if __name__ == '__main__':
    fetchresponse()
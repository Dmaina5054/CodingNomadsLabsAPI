import requests

url = ' http://demo.codingnomads.co:8080/tasks_api/users'

def fetchresponse():
    with requests.get(url) as response:
        print(response.status_code)
        print(response.encoding)
        print(response.text)
        result_list = response.json()['data']
        print([result['email'] for result in result_list])
        
        
        
        
if __name__ == '__main__':
    fetchresponse()
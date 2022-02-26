import requests

url = 'http://demo.codingnomads.co:8080/tasks_api/users'

user = {
    "first_name":"Daniel",
    "last_name" : "Maina",
    "email":"dmaina5054@gmail.com"
}

def createuser():
    try:
        requests.post(url,data=user)
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    createuser()
    

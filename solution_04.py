import requests 

url = "http://demo.codingnomads.co:8080/tasks_api/users"

updateduser = {
    "first_name":"Daniel_two",
    "last_name" : "Maina_two",
    "email":"dmaina5054@gmail.com_two"
}
def updateuser():
    try:
        requests.put(url,data=updateduser)
    except Exception as e:
        print(e)
        
        
if __name__ == '__main__':
    updateuser()
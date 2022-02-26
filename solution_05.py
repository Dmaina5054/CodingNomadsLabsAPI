import requests

url  = "http://demo.codingnomads.co:8080/tasks_api/users"


def deleteuser():
    try:
        requests.delete(url + f"/145")
    except Exception as e:
        print(e)
        
        
if __name__ == "__main__":
    deleteuser()
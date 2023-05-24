import requests

from config.config import *

def delete_schools():
    for i in range(125,327):
        url = f"{DOMJUDGE_URL}/jury/affiliations/{i}/delete"
        response = requests.post(url,headers={"Cookie":COOKIE})
        print(response.status_code)
def delete_teams():
    for i in range(1816,2019):
        url = f"{DOMJUDGE_URL}/jury/teams/{i}/delete"
        response = requests.post(url,headers={"Cookie":COOKIE})
        print(response.status_code)

def delete_users():
    for i in range(1228,1430):
        url = f"{DOMJUDGE_URL}/jury/users/{i}/delete"
        response = requests.post(url,headers={"Cookie":COOKIE})
        print(response.status_code)

if __name__ == "__main__":
    delete_teams()
    delete_users()
    # delete_schools()
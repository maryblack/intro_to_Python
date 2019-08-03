import requests
import pprint

def get_location_info():
    rsp = requests.get("http://ip-api.com/json/")
    return rsp.json()

if __name__ == "__main__":
    pprint.pprint(get_location_info())
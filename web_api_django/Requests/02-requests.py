import requests

def main():
    response = requests.get("https://api.nationalize.io?name=george")
    if response.status_code != 200:
        print(response.status_code)
        raise Exception("an error")
    
    data = response.json()
    print(data)

if __name__ == "__main__":
    main()

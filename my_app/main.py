import requests
import fastapi

def fetch_status():
    # A simple network test using our tracked requests library
    response = requests.get("https://httpbin.org")
    return response.status_code

if __name__ == "__main__":
    print(f"FastAPI version loaded: {fastapi.__version__}")
    print(f"Requests test status: {fetch_status()}")

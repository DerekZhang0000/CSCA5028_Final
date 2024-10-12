import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up!")
            return True
        else:
            print(f"Website {url} returned status code {response.status_code}.")
            return False
    except requests.ConnectionError:
        print(f"Failed to connect to {url}.")
        return False

def check_website_retries(url, max_retries=4, interval=300):
    for attempt in range(max_retries):
        if check_website(url):
            print(f"Success on attempt {attempt + 1}.")
            break
        else:
            if attempt < max_retries - 1:
                print(f"Retrying in {interval // 60} minutes...")
                time.sleep(interval)
            else:
                print("All retry attempts failed.")

# Due to the use of the free tier on Render, the website may take a few minutes to spin up
check_website_retries('https://csca5028-final-vrrs.onrender.com')
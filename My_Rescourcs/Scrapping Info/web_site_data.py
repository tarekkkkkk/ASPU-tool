
           
                    # all web links and web contains
                    # ip or domain name


import requests
from bs4 import BeautifulSoup

def get_hyperlinks(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        return [f"Error: {e}"]

def extract_hyperlinks(url):
    hyperlinks = get_hyperlinks(url)
    for link in hyperlinks:
        print(link)

if __name__ == "__main__":
    website_url = input("Enter Website URL: ")
    extract_hyperlinks(website_url)


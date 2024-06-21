

                                  
                                    #  all info about domain name


import socket
import whois
import requests
from bs4 import BeautifulSoup

def get_domain_info(domain_or_ip):
    
    info = {}
    try:
        ip_address = socket.gethostbyname(domain_or_ip)
        info['ip_address'] = ip_address
    except socket.gaierror:
        info['ip_address'] = domain_or_ip

    try:
        w = whois.whois(domain_or_ip)
        info['domain_name'] = w.domain_name
        info['registrar'] = w.registrar
        info['creation_date'] = w.creation_date
        info['expiration_date'] = w.expiration_date
        if hasattr(w, 'country'):
            info['location'] = w.country
    except Exception as e:
        print(f"Error getting WHOIS information: {e}")

    try:
        response = requests.get(f"http://{domain_or_ip}")
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')

        links = [link.get('href') for link in soup.find_all('a', href=True)]
        print("\n")
        info['links'] = links 

        subdomains = set()
        for link in links:
            if link.startswith('http'):
                parts = link.split('/')
                if len(parts) > 2:
                    subdomain = parts[2].split('.')[0]
                    subdomains.add(subdomain)
        info['subdomains'] = list(subdomains)

    except requests.exceptions.RequestException as e:
        print(f"Error getting website information: {e}")
        
    return info

domain_or_ip = input("Enter UR ip or Url : ") 
info = get_domain_info(domain_or_ip)
for key, value in info.items():
    print(f"{key}: {value}\n")

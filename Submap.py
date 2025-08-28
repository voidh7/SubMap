import os
import wl
import requests

allowed_status = [200, 201, 202, 204, 301, 302, 307, 308]
found = 0
not_found = 0

os.system("figlet Submap")
print(" by vøidh7 \n")                                                
domine = input("What is the target (please do not hack governments of US, Brazil, or China): ")

for sub in wl.Word:
    getUrl = f"https://{sub}.{domine}"
    try:
        response = requests.get(getUrl, timeout=3)
        if response.status_code in allowed_status:
            print(f"{getUrl} exists status_code[{response.status_code}]")
            found += 1
        else:
            print(f"{getUrl} not exists status_code[{response.status_code}]")
            not_found += 1
    except requests.exceptions.RequestException:
        not_found += 1
        continue

print("\n=== Scan finished ===")
print(f"Total subdomains scanned: {len(wl.Word)}")
print(f"Found: {found}")
print(f"Not found / failed: {not_found}")

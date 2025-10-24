import requests
import xml.etree.ElementTree as ET

def scrape_exploit_db_rss():
    print("Scraping latest exploit from Exploit-DB RSS feed...\n")
    
    # Try the RSS feed URL
    rss_url = "https://www.exploit-db.com/rss.xml"
    
    try:
        # Send GET request to the RSS feed
        response = requests.get(rss_url)
        response.raise_for_status()  # Check if request was successful
        
        # Parse the XML content
        root = ET.fromstring(response.content)
        
        # Namespace for RSS feeds
        ns = {'': 'http://purl.org/rss/1.0/'}
        
        # Find the first item (latest exploit)
        item = root.find('.//item')
        
        if item is not None:
            # Extract title and link
            title = item.find('title')
            link = item.find('link')
            
            if title is not None and link is not None:
                print("1.")
                print(f"Title: {title.text}")
                print(f"Link: {link.text}")
            else:
                print("Could not find title or link in RSS feed")
        else:
            print("No exploits found in RSS feed")
            
    except Exception as e:
        print(f"Error occurred: {e}")

# Alternative method using feedparser library (more reliable)
def scrape_exploit_db_feedparser():
    print("Scraping with feedparser library...\n")
    
    try:
        # First install: pip install feedparser
        import feedparser
        
        rss_url = "https://www.exploit-db.com/rss.xml"
        
        # Parse the RSS feed
        feed = feedparser.parse(rss_url)
        
        if feed.entries:
            # Get the latest exploit (first entry)
            latest_exploit = feed.entries[0]
            
            print("1.")
            print(f"Title: {latest_exploit.title}")
            print(f"Link: {latest_exploit.link}")
        else:
            print("No entries found in RSS feed")
            
    except ImportError:
        print("Please install feedparser: pip install feedparser")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Try the XML method first
    scrape_exploit_db_rss()
    
    print("\n" + "="*50 + "\n")
    
    # Try the feedparser method (more reliable)
    scrape_exploit_db_feedparser()
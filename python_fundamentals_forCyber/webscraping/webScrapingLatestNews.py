import requests
from bs4 import BeautifulSoup

# Step 1: Visit the homepage (or category page)
homepage = "https://thehackernews.com/search/label/Cyber%20Attack" # You can modify this to get the latest news from The Hacker News
response = requests.get(homepage)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find the latest article link
latest_article = soup.find("a", class_="story-link")

if latest_article:
    article_url = latest_article["href"] 
    print(f"Latest article URL: {article_url}\n")

    # Step 3: Visit that article
    page = requests.get(article_url)
    article_soup = BeautifulSoup(page.text, "html.parser")

    # Step 4: Extract title, author, date, and content
    title = article_soup.find("h1", class_="story-title")
    p_author = article_soup.find("span", class_="p-author")
    content = article_soup.find("div", class_="articlebody clear cf")

    if title:
        print(f"Story Title:\n{title.text.strip()}\n")

    if p_author:
        author_spans = p_author.find_all("span", class_="author")
        if len(author_spans) >= 2:
            date = author_spans[0].get_text(strip=True)
            author = author_spans[1].get_text(strip=True)
            print("Date:", date)
            print("Author:", author + "\n")

    if content:
        paragraphs = content.find_all("p")
        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:
                print(text)
    else:
        print("Article content not found.")

else:
    print("No articles found on homepage.")

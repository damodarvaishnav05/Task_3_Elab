# Task 3: Web Scraper for News Headlines

# Tools: requests, BeautifulSoup

import requests
from bs4 import BeautifulSoup    # From bs4 imported Beautifulsoap

def scrape_headlines():
    try:
        # BBC News url
        url = "https://www.bbc.com/news"
        headers = {"User-Agent": "Mozilla/5.0"}  # Avoid getting blocked
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print("Failed to fetch webpage. Status Code:", response.status_code)
            return

        # HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines 
        headlines = soup.find_all("h2")

        # Save to .txt file
        with open("headlines.txt", "w", encoding="utf-8") as f:
            for idx, h in enumerate(headlines, 1):
                text = h.get_text(strip=True)
                if text:  
                    f.write(f"{idx}. {text}\n")

        print("✅ Headlines scraped and saved to headlines.txt")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    scrape_headlines()

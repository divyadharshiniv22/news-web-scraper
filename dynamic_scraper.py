from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    url = "https://www.npr.org/sections/news/"

    page.goto(url)

    page.wait_for_selector("h2")

    # wait 5 seconds
    page.wait_for_timeout(5000)

    # get page html
    # parse html
    soup = BeautifulSoup(html, "html.parser")

    # extract headlines
    headlines = soup.find_all("h2")

    print("\nNPR Headlines:\n")

    for headline in headlines:
        print(headline.text.strip())

    browser.close()
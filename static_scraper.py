import requests
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup

# requesting the website
url = "https://www.npr.org/sections/news/"

response = requests.get(url)

print("the response Code is :", response.status_code)

# Parse the HTML document
soup = BeautifulSoup(response.content, "html.parser")


# Extract the news Headlines from HTML

headlines = soup.find_all("h2")

print("\nNPR Headlines:\n")

#display the headlines

for headline in headlines:

    print (headline.text,"\n")




# Extract the URLs

# Find all anchor tags (links) from the webpage
links = soup.find_all("a")

# Print heading
print("\nNPR URLs:\n")

# Loop through each link
for link in links:

    # Extract URL from href attribute
    href = link.get("href")

    # Check whether href exists
    if href:

        # Check if URL starts with http
        # This avoids invalid or empty links
        if href.startswith("http"):

            # Print the final URL
            print(href, "\n")


# Extract Dates


# Find all date tags from the webpage
dates = soup.find_all("time")

# Print heading
print("\nNPR Dates:\n")

# Loop through each date
for date in dates:

    # Get text from the time tag
    date_text = date.text

    # Print the date
    print(date_text)



# Extract Summaries


# Find all paragraph tags from the webpage
summaries = soup.find_all("p")

# Print heading
print("\nNPR Summaries:\n")

# Loop through each summary
for summary in summaries:

    # Get text from paragraph tag
    summary_text = summary.text

    # Print the summary
    print(summary_text)

    # Print separator line
    print("-" * 60)

# Create Empty Lists
headline_list = []
url_list = []
date_list = []
summary_list = []


# Store Headlines
for headline in headlines:

    headline_list.append(headline.text.strip())


# Store URLs
for link in links:

    href = link.get("href")

    if href:

        if href.startswith("http"):

            url_list.append(href)


# Store Dates
for date in dates:

    date_list.append(date.text.strip())


# Store Summaries
for summary in summaries:

    summary_list.append(summary.text.strip())
    
# Find smallest list size

smallest_size = min(
    len(headline_list),
    len(url_list),
    len(date_list),
    len(summary_list)
)

# Make all lists equal size
headline_list = headline_list[:smallest_size]
url_list = url_list[:smallest_size]
date_list = date_list[:smallest_size]
summary_list = summary_list[:smallest_size]

# Create dictionary
data = {
    "Headline": headline_list,
    "URL": url_list,
    "Date": date_list,
    "Summary": summary_list
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print(df)

# Remove duplicate URLs
df.drop_duplicates(subset=["URL"], inplace=True)

# Display updated DataFrame
print(df)

# Save DataFrame into CSV file
df.to_csv("npr_news.csv", index=False)

print("CSV file saved successfully!")

# Create SQLite database connection
conn = sqlite3.connect("news.db")

# Save DataFrame into database table
df.to_sql("npr_news", conn, if_exists="replace", index=False)

# Close database connection
conn.close()

print("SQLite database saved successfully!")
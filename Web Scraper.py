import requests
from bs4 import BeautifulSoup
import csv
import json

# Define the URL you want to scrape
url = "https://www.geeksforgeeks.org"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data from the website (replace this with your specific logic)
    # For example, let's extract all the <a> tags and store their text and href attributes
    links = soup.find_all('a')
    
    # Create a list to store the extracted data
    data = []
    
    for link in links:
        data.append({
            "text": link.text,
            "href": link.get("href")
        })

    # Define the output file format (CSV or JSON)
    output_format = "csv"  # Change to "json" if you want JSON output

    # Store the data in the desired format
    if output_format == "csv":
        with open('data.csv', 'w', newline='') as csvfile:
            fieldnames = ["text", "href"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    elif output_format == "json":
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    print(f"Data has been scraped and saved in {output_format} format.")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)


# In this script:

# 1. We send an HTTP GET request to the specified URL using the requests library.
# 2. We parse the HTML content of the page using BeautifulSoup.
# 3. We find the elements that contain the data we want to scrape using CSS selectors.
# 4. We loop through the elements, extract the relevant information, and store it in a list.
# 5. Finally, we write the data to a CSV file using the csv module.
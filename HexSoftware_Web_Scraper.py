import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import webbrowser
from pyfiglet import Figlet

figlet = Figlet (font = 'slant')

data = []
file_path = os.path.join('Scraped_Data', 'Books.html')

def Scrape():
    current_page = 1
    
    while current_page <= number_of_pages:

        print("Scraping page: " + str(current_page))
        
        url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        current_page += 1
        
        # Check if 404 page
        if soup.title and "404" in soup.title.text:
            break
        else:
            all_books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

            for book in all_books:
                item = {
                    'Title': book.find("img").attrs['alt'],
                    'Link': "https://books.toscrape.com/catalogue/" + book.find('a').attrs['href'],
                    'Price': book.find('p', class_='price_color').text[1:],
                    'Stock': book.find('p', class_='instock availability').text.strip()
                }
                data.append(item)
        
def save_data():
    if not os.path.exists('Scraped_Data'):
        os.makedirs('Scraped_Data')
    
    # Change directory only if it exists
    
    
    # Convert data to DataFrame and save as html
    df = pd.DataFrame(data)
    df.to_html(file_path)

    print("Data saved to 'Scraped_Data\Books.html'")

def open_scraped_data():
    
    # Check if the file exists
    if os.path.exists(file_path):
        try:
            # Open the file in the browser
            webbrowser.open(f"file://{os.path.abspath(file_path)}")
        

            print("Displaying Scraped Data:")
            
        except Exception as e:
            print("Error reading HTML file:", e)
            return None
    else:
        print("File not found. Please make sure 'Books.html' has been generated in the 'Scraped_Data' folder.")
        return None


# Run the scraping and save functions
print(figlet.renderText("Welcome to WEB SCRAPER"))
number_of_pages = int(input("Enter the page number to start scraping from: "))
Scrape()
save_data()
open_scraped_data()


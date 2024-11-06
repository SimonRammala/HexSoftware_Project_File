import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import webbrowser

data = []

def Scrape():
    current_page = 1
    proceed = True

    while proceed:
        print("Scraping page: " + str(current_page))
        
        url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Check if 404 page
        if soup.title and "404" in soup.title.text:
            proceed = False
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
            
            proceed = False
            current_page += 1

def save_data():
    if not os.path.exists('Scraped_Data'):
        os.makedirs('Scraped_Data')
    
    # Change directory only if it exists
    os.chdir('Scraped_Data')
    
    # Convert data to DataFrame and save as Excel
    df = pd.DataFrame(data)
    df.to_html('Books.html')

    print("Data saved to 'Scraped_Data\Books.html'")

def open_scraped_data():
    # Set the path to the file
    file_path = os.path.join('Scraped_Data', 'Books.html')

    print(os.getcwd())
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)


        print("Displaying Scraped_Data:")

        print(df.head())  

        webbrowser.open_new_tab(file_path)
        return df
    else:
        print("File not found. Please make sure 'Books.html' has been generated.")
        return None



# Run the scraping and save functions
Scrape()
save_data()
open_scraped_data()

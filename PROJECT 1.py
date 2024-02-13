import requests
from bs4 import BeautifulSoup

Index_url = "https://books.toscrape.com/"
Category_Url_Path = "catalogue/category/books/"

def get_category_urls(base_url):
    response = requests.get(base_url)
    if not response.ok:
        print("Website unavailable or wrong URL...")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    category_list = soup.select_one('.nav.nav-list ul')
    if not category_list:
        print("No category list found...")
        return []

    categories = category_list.find_all('a')
    category_urls = {cat.get_text(strip=True): base_url + cat['href'] for cat in categories}

    return category_urls

def get_books_data(URL):
    
    response = requests.get(URL)
    data_all = {}

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")

    upc = soup.select_one("th:contains('UPC') + td").text
    title = soup.select_one("div.product_main h1").text
    price_incl_tax = soup.select_one("th:contains('Price (incl. tax)') + td").text
    price_excl_tax = soup.select_one("th:contains('Price (excl. tax)') + td").text
    number_available = soup.select_one("th:contains('Availability') + td").text

    product_description = soup.select_one("#product_description + p")
    if product_description:
        product_description = product_description.text
    else:
        product_description = 'No description available'

    category = soup.select_one(".breadcrumb li:nth-child(3) a").text.strip()
    review_rating = soup.select_one(".star-rating")["class"][1] if soup.select_one(".star-rating") else "No rating"
    image_url = Index_url + soup.select_one("div.item.active img")["src"].lstrip("../")

    data_all = {
            "Product Page URL": URL,
            "UPC": upc,
            "Title": title,
            "Price Including Tax": price_incl_tax,
            "Price Excluding Tax": price_excl_tax,
            "Number Available": number_available,
            "Product Description": product_description,
            "Category": category,
            "Review Rating": review_rating,
            "Image URL": image_url
        }

    return data_all

def get_books_page(category_url):
    book_categories = []
    current_page = 1
    while True:
        if current_page == 1:
            page_url = category_url
        else:
            page_url = category_url.replace('index.html', f'page-{current_page}.html')
        
        response = requests.get(page_url)
        if not response.ok:
            break  

        soup = BeautifulSoup(response.text, 'html.parser')
        book_links = soup.find_all('h3')
        if not book_links:
            break  
        
        for link in book_links:
            a_tag = link.find('a')  
            if a_tag and 'href' in a_tag.attrs:  
                book_url = a_tag['href']
                
                book_url = Index_url + 'catalogue/' + book_url.replace('../', '')
                book_categories.append(book_url)
        
        current_page += 1  
        
    return book_categories

def scrape_books_category(category_url):
    book_urls = get_books_page(category_url)
    all_books_data = []

    for book_url in book_urls:
        book_data = get_books_data(book_url)
        if book_data:  
            all_books_data.append(book_data)

    return all_books_data

def save_data_to_csv(data, filename):
    with open(filename, mode='w', encoding='utf-8') as file:
        for book_data in data:
            for key, value in book_data.items():
                file.write(f"- {key}: {value}\n")
            file.write("\n----------\n")

def scrape_and_save_categories(category_urls):
    for name, category_url in category_urls.items():
        print(f"Scraping category...: {name}")
        books_data = scrape_books_category(category_url)
        if books_data:
            filename = f"{name.replace(' ', '_').lower()}_books.csv"
            save_data_to_csv(books_data, filename)
            print(f"Data for category '{name}' saved to {filename}! Continuing scraping...")
        else:
            print(f"No data found for category '{name}'...")
            
if __name__ == "__main__":
    category_urls = get_category_urls(Index_url)
    scrape_and_save_categories(category_urls)

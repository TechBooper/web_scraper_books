# Book Scraper

## Code Features

This Python script is designed to extract book data from "https://books.toscrape.com/", a website dedicated to showcasing a wide variety of books across different categories. It automates the collection of information from a list of requested data and produces a csv file containing all this information as well as a directory of images containing all the images of each book and each category. 

## Features

- Extract categories: Identifies and automatically extracts book categories from the website.
- Collect book data: For each book, the script collects details including the UPC, title, price (with and without tax), availability, product description, category, critic rating, and image URL.
- Download images: Downloads and saves book images in a structured directory format.
- Pagination management: Navigates through multiple pages within each category to ensure a complete data collection.
- Save data: Saves the extracted data in CSV files, organized by book category.

## Functions

- Extract categories: The script starts by retrieving the list of book categories from the homepage of the website.

- Extract book data: For each category, it extracts the data of all listed books, managing pagination to cover all available pages.

- Download images: The image of each book is downloaded and saved in a directory named after the category.

- Save data in a CSV: Compiles and saves the book data in CSV files named according to the format <category_name>_books.csv.

## Usage

To use this script, run it in an environment where Python 3 is installed along with the required libraries: requests and BeautifulSoup4 from bs4.

## Prerequisites

- Python 3.x
- Package requests
- Package BeautifulSoup4
- You can install the required packages using pip in a terminal: pip install requests beautifulsoup4

You can open your terminal with the Windows + R command and typing "cmd" in the run bar.

To isolate these packages in a virtual environment, please follow these instructions:

Install the 'virtualenv' package with the command: pip install virtualenv
Name your environment whatever you choose (I choose the name Scraper): virtualenv Scraper
When using your environment, activate it with these commands:
Windows: Scraper\Scripts\activate
MacOS or Linux: Source Scraper\bin\activate
To deactivate your environment: deactivate

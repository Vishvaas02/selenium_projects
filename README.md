# Audible Product Web Scraper

This project is a Selenium-based web scraper that extracts product details (Title, Author, and Runtime) from Audible's search page and exports the data into a CSV file.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- pandas

## Installation

1. **Install Python**  
   Make sure you have Python installed. You can download it from [Python's official site](https://www.python.org/).

2. **Install Dependencies**  
   Install the necessary Python libraries by running the following commands:

   ```bash
   pip install selenium
   pip install pandas

## How It Works

The script uses Selenium to launch a Chrome browser instance.
It navigates to the Audible search page.
Using XPath, the script identifies product elements (Title, Author, and Runtime) from the page.
The details are stored in lists and then converted to a pandas DataFrame.
The DataFrame is exported to a CSV file named audible_products.csv.

## Output
After running the script, a CSV file named audible_products.csv will be created in your project directory. It will contain the following columns:

Title: The title of the Audible product.
Author: The author of the Audible product.
Runtime: The duration of the Audible product.

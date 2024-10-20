# Selenium Projects

This repository contains several projects using Selenium for web automation and web scraping tasks. Each project is contained in a separate folder for easy organization and management.

## Projects

### 1. Web Scraping (Folder: `webscraping`)

This project uses Selenium to scrape product information from [Audible's search page](https://www.audible.com/search). The script collects the following details for each product:

- **Title**
- **Author**
- **Runtime**

The scraped data is stored in a CSV file named `audible_products.csv`.

#### How to run the script:

1. Install the required packages:
    ```bash
    pip install selenium pandas
    ```

2. Download the Chrome WebDriver and update the path in the script accordingly.

3. Run the script using the following command:
    ```bash
    python webscraping/webscraping.py
    ```

The script will save the scraped data to `audible_products.csv`.

### 2. Date Picker Automation (Folder: `datepicker`)

This project automates interactions with a date picker element on a web page. It uses Selenium to open a webpage and interact with the date picker, selecting specific dates.

#### How to run the script:

1. Install the required packages:
    ```bash
    pip install selenium
    ```

2. Download the Chrome WebDriver and update the path in the script accordingly.

3. Run the script using the following command:
    ```bash
    python datepicker/datepicker.py
    ```

The script will open the webpage and automate date selection using the date picker.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver (or other browser driver based on the browser you use)
- Pandas (for data handling in the web scraping project)

## Setting up the environment

1. Clone the repository:
    ```bash
    git clone https://github.com/Vishvaas02/selenium_projects.git
    ```

2. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```



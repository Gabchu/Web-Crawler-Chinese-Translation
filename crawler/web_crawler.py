import requests
from bs4 import BeautifulSoup


def Crawl_and_Convert():
    # Define the URL of the EC catalog
    catalog_url = 'https://tw.carousell.com/categories/women-s-fashion-4/'

    # Fetch the content of the catalog page
    response = requests.get(catalog_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use a CSS selector to select elements with a specific class
        title_tags = soup.select(
            'p.D_pt.M_jT.D_oq.M_jJ.D_pu.M_jU.D_py.M_jY.D_p_.M_ka.D_pE.M_kf.D_pH.M_ki.D_pK')
        price_tags = soup.select(
            'p.D_pt.M_jT.D_oq.M_jJ.D_pu.M_jU.D_py.M_jY.D_p_.M_ka.D_pE.M_kf.D_pG.M_kh.D_pJ')

        product_titles = []
        product_prices = []

        # Extract and store the text from selected elements
        for title_tag in title_tags:
            product_titles.append(title_tag.get_text())

        for price_tag in price_tags:
            product_prices.append(price_tag.get_text())

        # Write the extracted titles and prices to a UTF-8 encoded file
        with open('product_data.txt', 'w', encoding='utf-8') as file:
            for product_titles, product_prices in zip(product_titles, product_prices):
                file.write("Product Titles:\n")
                for title in product_titles:
                    file.write(title)

                file.write("\nProduct Prices:\n")
                for price in product_prices:
                    file.write(price)

            print("Data has been written to product_data.txt")

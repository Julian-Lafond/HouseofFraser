import httpx
from bs4 import BeautifulSoup


url = 'https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15" #must have headers otherwise http request fails
}

def extract_product_data(product):
    try:
        name = product.find('span', class_='productdescriptionname').text
        brand = product.find('span', class_='productdescriptionbrand').text
        price = product.find('span', class_='CurrencySizeLarge curprice').text.strip()
        print(f'Brand: {brand} Name: {name} Price: {price}')
    except Exception as e:
        print(f'Error extracting product data: {e}')




def main():
    response = httpx.get(url, headers=headers)
    response_html = response.text
    
    soup = BeautifulSoup(response_html, 'html.parser')
    products = soup.find_all('div', class_='s-productthumbbox')
    for product in products:
        extract_product_data(product)
        
if __name__=='__main__':
    main()
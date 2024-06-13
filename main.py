import httpx
from bs4 import BeautifulSoup


url = 'https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15" #must have headers otherwise http request fails
}


def main():
    response = httpx.get(url, headers=headers)
    response_html = response.text
    
    soup = BeautifulSoup(response_html, 'html.parser')
    print(soup.find_all('a'))   #find all a tags


if __name__=='__main__':
    main()
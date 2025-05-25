import json
import os
import requests
import urllib.parse

from dotenv import load_dotenv

from product import Product


load_dotenv()


def fetch_product_list(query) -> list[Product]:
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/shop.json?query={encText}"

    headers = {
        "X-Naver-Client-Id": os.environ["CLIEND_ID"],
        "X-Naver-Client-Secret": os.environ["CLIENT_SECRET"]
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error Code: {response.status_code}")
        return []
    resp_j = json.loads(response.text)
    print(resp_j)

    # TODO: resp_j 내용을 사용해 Product 인스턴스의 list를 만드는 코드 작성
    product_list = []
    # TODO:

    return product_list


if __name__ == "__main__":
    print(fetch_product_list("허니트립 보스턴백"))

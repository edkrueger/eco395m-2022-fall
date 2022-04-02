import os
import json

import requests


def get_num_pages():
    """Makes a request to get the number of pages of 200 rows."""

    base_url = "https://core.dxpapi.com/api/v1/core/"

    params = {
        "account_id": 5468,
        "url": "https://www.gap.com/index.html%23brm-search%3Frequest_type: search",
        "search_type": "keyword",
        "ref_url": "https://www.gap.com/",
        "request_type": "search",
        "rows": 0,
        "start": 0,
        "fl": "sku_color,style_color_id,sku_sizes,swatch_image_attribute,pid,title,brand,price,maxSalePrice,minSalePrice,sale_price,price_type,thumb_image,sku_thumb_images,sku_swatch_images,url,price_range,sale_price_range,defaultColorMarketingMessage,styleMarketingMessage",
    }

    response = requests.get(base_url, params)

    response_json = response.json()

    return response_json["response"]["numFound"] // 200


def request_page(page_number):
    """Request a page of 200 docs and return a list of the docs.
    page_number starts at 0."""

    base_url = "https://core.dxpapi.com/api/v1/core/"

    params = {
        "account_id": 5468,
        "url": "https://www.gap.com/index.html%23brm-search%3Frequest_type: search",
        "search_type": "keyword",
        "ref_url": "https://www.gap.com/",
        "request_type": "search",
        "rows": 200,
        "start": page_number * 200,
        "fl": "sku_color,style_color_id,sku_sizes,swatch_image_attribute,pid,title,brand,price,maxSalePrice,minSalePrice,sale_price,price_type,thumb_image,sku_thumb_images,sku_swatch_images,url,price_range,sale_price_range,defaultColorMarketingMessage,styleMarketingMessage",
    }

    response = requests.get(base_url, params)
    response_json = response.json()

    return response_json["response"]["docs"]


def request_all_pages():
    """Requests all pages, return a list of the docs."""

    docs = []

    num_pages = get_num_pages()

    for page_num in range(num_pages + 1):
        new_docs = request_page(page_num)
        docs += new_docs

    return docs


def write_docs_to_jsonl(docs, path):

    with open(path, "w+", encoding="utf-8") as file:
        for doc in docs:
            file.write(json.dumps(doc) + "\n")


BASE_DIR = "artifacts"
JSONL_PATH = os.path.join(BASE_DIR, "results.jsonl")

os.makedirs(BASE_DIR, exist_ok=True)

docs = request_all_pages()
write_docs_to_jsonl(docs, JSONL_PATH)

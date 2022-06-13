from bs4 import BeautifulSoup
import requests
from app.utils import get_item
from app.models.opinion import extract_opinion
import os
import json

class Product:
    def __init__(self, opinions, product_id,product_name,opinions_count,pros_count,cons_count,average_score):
        self.product_id=product_id
        self.product_name=product_name
        self.opinions=opinions
        self.opinions_count=opinions_count
        self.pros_count=pros_count
        self.cons_count=cons_count
        self.average_score=average_score
        return self

    def __str__(self):
        return self.product_name
    

    def extract_product(self, product_id):
        url = f"https://www.ceneo.pl/{self.product_id}#tab=reviews"
        response=requests.get(url)
        page=BeautifulSoup(response.text, 'html.parser')
        self.product_name-get_item(page,"h.product-top__product-info__name")
        while(url):
            response=requests.get(url)
            page=BeautifulSoup(response.text, 'html.parser')
            opinions = page.select("div.js_product-review")
            for opinion in opinions:
                self.opinions.append(opinions)
                extract_opinion(opinion)
            try:
                url = f"https://www.ceneo.pl" + get_item(page,"a.pagination__next","href")
            except TypeError:
                url = None

    def process_stats(self):
        opinions = pd.read_json(json.damps(self.opinions))
        self.opinions_count = len(self.opinions.index),
        self.pros_count = self.opinions.pros.map(bool).sum(),
        self.cons_count = self.opinions.cons.map(bool).sum(),
        self.average_score = self.opinions.score.mean().round(2)

        return self

    def save_opinions(self):
        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")
        with open(f"app/opinions/{self.product_id}.json", "w",encoding="UTF-8") as jf:
            json.dump(self.opinions, jf, indent=4, ensure_ascii=False)
        
    def save_stats(self):
        if not os.path.exists("app/products"):
                os.makedirs("app/oproducts")
        with open(f"app/products/{self.product_id}.json", "w",encoding="UTF-8") as jf:
            json.dump(self.opinions, jf, indent=4, ensure_ascii=False)
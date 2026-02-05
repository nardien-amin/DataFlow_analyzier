import requests, csv, os
from bs4 import BeautifulSoup

class Scrap:
    def __init__(self, base_url):
        self.url = base_url
        self.dir = "data"
        if not os.path.exists(self.dir): os.makedirs(self.dir)

    def get_s(self, link):
        return BeautifulSoup(requests.get(link).text, "html.parser")

    def run(self):
        main_s = self.get_s(self.url)
        cats = main_s.find("div", class_="side_categories").find_all("a")[1:]

        for c in cats:
            name = c.text.strip()
            path = os.path.join(self.dir, f"{name}.csv")
            s = self.get_s(self.url + c["href"])
            items = s.find_all("article", class_="product_pod")

            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["Title", "Price", "Stock"])
                for i in items:
                    t = i.h3.a["title"]
                    p = i.find("p", class_="price_color").text
                    st = i.find("p", class_="instock availability").text.strip()
                    w.writerow([t, p, st])
            print(f"Done: {name}")

bot = Scrap("http://books.toscrape.com/")
bot.run()
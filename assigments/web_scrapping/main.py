from class_scrap import Scrap

if __name__ == "__main__":
    url = "http://books.toscrape.com/"
    bot = Scrap(url)
    bot.run()
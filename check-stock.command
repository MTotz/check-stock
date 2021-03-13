#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
import os


def check_stock(link):
    try:
        req = requests.get(link)
    except requests.exceptions.ConnectionError:
        print("{: >70}".format("Page not found"))
        return

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")
    prod_name = soup.find("h1", class_="product-title").get_text()
    if prod_name is None:
        prod_name = "Page not found."
        return
    stock_status = soup.find(
        "div", class_="online-availability__shipping-message").get_text()

    print("{: >50} {: >20} {: <40}".format(
        prod_name, "---------------->\t", stock_status))


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)

    print()
    with open(dirname + "/links.txt", "r") as file:
        for link in file:
            check_stock(link)
    print()

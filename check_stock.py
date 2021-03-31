#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
import os
import re


class Product:
    def __init__(self, url, nickname=None):
        req = requests.get(url)
        text = req.text
        # second term was added to avoid warning, as instructed by module terminal output
        soup = BeautifulSoup(text, features="lxml")

        self.url = url
        self.product_nickname = nickname
        self.site_name = get_site_name(url)
        self.product_name = get_product_name(url, self.site_name)

    def get_url(self):
        return self.url

    def get_product_name(self):
        return self.product_name

    def get_product_nickname(self):
        return self.product_nickname

    def get_site_name(self):
        return self.site_name

    def find_stock_status(self):
        req = requests.get(self.url)
        text = req.text
        # second term was added to avoid warning, as instructed by module terminal output
        soup = BeautifulSoup(text, features="lxml")
        stock_status = soup.find(
            "div", class_="online-availability__shipping-message").get_text()

        return stock_status


def validate_url(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False

    return True


def get_product_name(url, site):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")

    if site == "www.chapters.indigo.ca":
        product_name = soup.find("h1", class_="product-title").get_text()

    elif site == "www.lego.com":
        matches = [item for item in soup.find_all(
        ) if "data-test" in item.attrs and item["data-test"] == "product-overview-name"]
        product_name = matches[0].get_text()

    return product_name


def check_stock(url, site):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return "Page not found"

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")

    if site == "www.chapters.indigo.ca":
        stock_status = soup.find(
            "span", class_="online-availability__availability-text")

        if stock_status:
            stock_status = stock_status.get_text()
        else:
            stock_status = soup.find(
                "div", class_="online-availability__shipping-message").get_text()

    elif site == "www.lego.com":
        matches = [item for item in soup.find_all(
        ) if "data-test" in item.attrs and item["data-test"] == "product-overview-availability"]
        stock_status = matches[0].get_text()

    return stock_status


def get_site_name(url):
    return re.search(r"www.+\.c(a|om)", url).group(0)


if __name__ == "__main__":
    print(get_site_name("https://www.chapters.indigo.ca/en-ca/toys/lego-star-wars-the-child/673419342131-item.html?ikwid=the+child&ikwsec=Home&ikwidx=17#algoliaQueryId=f81ce3a14f5517e668048b311c0b42a0"))

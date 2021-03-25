#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
import os


class Product:
    def __init__(self, url, nickname=None):
        req = requests.get(url)
        text = req.text
        # second term was added to avoid warning, as instructed by module terminal output
        soup = BeautifulSoup(text, features="lxml")

        self.product_name = soup.find("h1", class_="product-title").get_text()
        self.url = url
        self.product_nickname = nickname

    def get_url(self):
        return self.url

    def get_product_name(self):
        return self.product_name

    def get_product_nickname(self):
        return self.product_nickname

    def get_stock_status(self):
        req = requests.get(link)
        text = req.text
        # second term was added to avoid warning, as instructed by module terminal output
        soup = BeautifulSoup(text, features="lxml")
        stock_status = soup.find(
            "div", class_="online-availability__shipping-message").get_text()

        return stock_status


def get_links():
    links = []
    with open("links.txt", "r") as file:
        for line in file:
            links.append(line)

    return links


def validate_url(url):
    try:
        req = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False

    return True


def check_stock(link):
    try:
        req = requests.get(link)
    except requests.exceptions.ConnectionError:
        return ("Page not found", "Page not found")

    text = req.text
    # second term was added to avoid warning, as instructed by module terminal output
    soup = BeautifulSoup(text, features="lxml")
    stock_status = soup.find(
        "span", class_="online-availability__availability-text")

    if stock_status:
        stock_status = stock_status.get_text()
    else:
        stock_status = soup.find(
            "div", class_="online-availability__shipping-message").get_text()

    return stock_status


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)

    print()
    with open(dirname + "/links.txt", "r") as file:
        for link in file:
            check_stock(link)
    print()

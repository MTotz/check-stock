from flask import Flask, render_template, url_for, redirect, request
from check_stock import check_stock, get_links

app = Flask(__name__)  # reference this file


@app.route("/")
def index():
    name = []
    status = []

    links = get_links()
    for l in links:
        product_name, stock_status = check_stock(l)
        name.append(product_name)
        status.append(stock_status)
    return render_template("index.html", length=len(links), name=name, status=status, links=links)


@app.route("/products_list")
def products():
    name = []

    links = get_links()
    for l in links:
        product_name, stock_status = check_stock(l)
        name.append(product_name)
    return render_template("products_list.html", length=len(links), name=name, links=links)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@ app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.txt")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        price = request.form.get("price")

        print("Received:", title, author, price)  

        if title and author and price:
            with open(DATA_FILE, "a") as f:
                f.write(f"{title},{author},{price}\n")
                f.flush()

            print("Written to file")  

        return redirect("/")

    books = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                if line.strip():
                    t, a, p = line.strip().split(",")
                    books.append({
                        "title": t,
                        "author": a,
                        "price": p
                    })

    return render_template("index.html", data=books)

if __name__ == "__main__":
    app.run(debug=True)

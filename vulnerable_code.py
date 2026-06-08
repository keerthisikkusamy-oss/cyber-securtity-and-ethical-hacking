from flask import Flask, request

app = Flask(__siji__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return f"<h2>Search Results for: {query}</h2>"

app.run(debug=True)
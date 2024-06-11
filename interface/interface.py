import csv
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="pages")


def parse_result_csv(str: str) -> list:
    r = csv.reader([str])
    return list(r)

@app.route('/request_search', methods=['POST'])
def get_search_results():
    print(request.form)

@app.route('/')
def homepage():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()

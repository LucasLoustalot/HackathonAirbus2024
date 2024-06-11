import csv
import json
from flask import Flask, render_template, request, Response, jsonify, make_response

app = Flask(__name__, template_folder="pages")


def parse_result_csv(lst: list[str]) -> list:
    ret_lst: list = []

    for s in lst:
        r = s.split(', ')
        ret_lst.append(r)
    return ret_lst

@app.route('/request_search', methods=['POST'])
def get_search_results():
    keywords = request.get_json()['value']
    ## Send to google search

    ## get request result
    test = ["name, location, link, contact, revenue, size, certifications, skills, main domain, main customers",
"name, location, link, contact, revenue, size, certifications, skills, main domain, main customers"]


    header = ["Name", "Location", "Link", "Contact", "Revenue", "Size", "Certifications", "Skills", "Main domain", "Main customers"]
    response = parse_result_csv(test)
    jsonResponse = {}
    data = {}
    y = 0
    for r in response:
        data.clear()
        for i in range(0, len(r) - 1):
            data[header[i]] = r[i]
        jsonResponse[y] = data
        y += 1
    print(jsonResponse)
    return jsonify(jsonResponse)

@app.route('/')
def homepage():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request, Response, jsonify
import research.researchKeyword as research

app = Flask(
    __name__, template_folder="pages", static_folder="pages", static_url_path=""
)

languages = {
    "FR": "french",
    "US": "english",
    "DE": "german",
    "CH": "chinese (simplified)",
    "IN": "hindi",
    "RS": "serbian",
    "LT": "lithuanian",
    "KR": "korean",
    "JP": "japanese",
    "BR": "portuguese",
}
data_headers = [
    "Name",
    "Location",
    "Link",
    "Contact",
    "Revenue",
    "Size",
    "Certifications",
    "Skills",
    "Main domain",
    "Main customers",
]


def parse_result_csv(lst: list[str]) -> list[str]:
    ret_lst: list = []

    for s in lst:
        r = s.split(";")
        ret_lst.append(r)
    return ret_lst


@app.route("/request_search", methods=["POST"])
def get_search_results():
    keywords = request.get_json()["value"]
    country_code = request.get_json()["country_code"]
    language = languages[country_code]

    try:
        resultCSV = research.search(keywords, country_code, language)

        #resultCSV = [
        #    "Airbus; Toulouse; https://www.airbus.com/fr/airbus-atlantic; support@airbus.com; 100M; 100K; FR; Skil; Aviation; Army",
        #    "name2; location2; link2; contact2; revenue2; size2; Airbus.com; skills2; main domain2; main customers2",
        #]

        response = parse_result_csv(resultCSV)
        jsonResponse = {}
        lens = {}
        y = 0
        for r in response:
            data = {}
            lens[y] = 0
            for i in range(0, len(r)):
                if data_headers[i] != "Links" and data_headers[i] != "Contact":
                    lens[y] += len(r[i])
                data[data_headers[i]] = r[i]
            jsonResponse[y] = data
            y += 1
        lens = dict(sorted(lens.items(), key=lambda item: item[1]))
        response = {}
        y = 0
        for val in reversed(lens.keys()):
            print("Val: " + str(val))
            response[y] = jsonResponse[val]
            y += 1
        return jsonify(response)
    except Exception as e:
        print("Error while processing: " + str(e))
        return "{}"


@app.route("/")
def homepage():
    return render_template("main.html")


def main():
    app.run()

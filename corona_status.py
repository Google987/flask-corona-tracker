import requests
from flask import Flask
from api import api_key

app = Flask(__name__)

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

@app.route("/<country_name>")
def getByCountryName(country_name):
    response = requests.request("GET", url, headers=headers)
    all_data = response.json().get("countries_stat", [])
    for countryObj in all_data:
        if(countryObj.get("country_name").lower() == country_name.lower()):
            return """
            <h1>%s</h1>
            <h2>Total cases: %s</h2>
            <h2>Total deaths: %s</h2>
            <h2>Total recovered: %s</h2>
            <h2>New deaths: %s</h2>
            <h2>New cases: %s</h2>
            <h2>Serious/critical cases: %s</h2>
            """ % (country_name, countryObj.get("cases"), countryObj.get("deaths"), countryObj.get("total_recovered"), countryObj.get("new_deaths"), countryObj.get("new_cases"), countryObj.get("serious_critical"))

    return response.text



@app.route("/")
def home():
    response = requests.request("GET", url, headers=headers)
    all_data = response.json().get("countries_stat", [])
    for countryObj in all_data:
        if(countryObj.get("country_name") == 'India'):
            return """
            <h1>%s</h1>
            <h2>Total cases: %s</h2>
            <h2>Total deaths: %s</h2>
            <h2>Total recovered: %s</h2>
            <h2>New deaths: %s</h2>
            <h2>New cases: %s</h2>
            <h2>Serious/critical cases: %s</h2>
            """ % ("India", countryObj.get("cases"), countryObj.get("deaths"), countryObj.get("total_recovered"), countryObj.get("new_deaths"), countryObj.get("new_cases"), countryObj.get("serious_critical"))

    return "all good"

# print(response.text)


if __name__ == "__main__":
    app.run(debug=True, port=5555)
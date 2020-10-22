import requests
from flask import Flask, render_template, request, redirect
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
            return render_template('index.html', countryObj=countryObj)
            
    return response.text



@app.route("/")
def home():
    response = requests.request("GET", url, headers=headers)
    all_data = response.json().get("countries_stat", [])
    for countryObj in all_data:
        if(countryObj.get("country_name").lower() == 'india'):
            return render_template('index.html', countryObj=countryObj)
            
    return "all good"

# print(response.text)


if __name__ == "__main__":
    app.run(debug=True, port=5555)
import requests


def get_data(query):
    url = 'http://api.weatherapi.com/v1/forecast.json?key=d9e0a428adc3473ea81175507221411&q=' + query + '&days=7'
    response = requests.get(url)
    data = response.json()
    return data, response.status_code

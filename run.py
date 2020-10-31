import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/detik_popular')
def detik_popular():
    html_ = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'framebar'})

    soup = BeautifulSoup(html_.text, 'html.parser')

    popular_area = soup.find(attrs={'class': 'grid-row list-content'})

    titles = popular_area.findAll(attrs={'class': 'media__title'})
    images = popular_area.findAll(attrs={'class': 'media__image'})

    return render_template('detik-scraper.html', images=images)

@app.route('/idr_rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr_rates.html', datajs=json_data.values())

if __name__ == '__main__':
    app.run(debug=True)
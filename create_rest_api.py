# simple rest api with two endpoints, serves the current currency rate to the client in json-format
from flask import Flask, jsonify
from scrape_using_beautifulSoup import get_currency

# create an app instance using Flask class
app = Flask(__name__)

# Api has two endpoint: homepage and /api/v1/<in_cur>-<out_cur>. User can change url-end point variables in_cur & out_cur to get exchange rate. 

@app.route('/')
def home():
  return '<h1>Currency Rate API</h1> <p>Example url: api/v1/usd-eur</p>'


@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
  rate = get_currency(in_cur, out_cur)
  result_dictionary = {
    "input_currency": in_cur,
    "output_currency": out_cur,
    "rate": rate
  }
  return jsonify(result_dictionary)

app.run(host="0.0.0.0")
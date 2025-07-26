# 3. Random Quote Generator 
#  Requirements: 
#  Flask serves random quotes from /api/quote 
#  Button on frontend uses Fetch API to get new quote 
#  Style card using Bootstrap 
#  Jinja2 for initial page layout 
#  Loading state shown while fetching 


from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    {"author": "Albert Einstein", "text": "Life is like riding a bicycle. To keep your balance you must keep moving."},
    {"author": "Oscar Wilde", "text": "Be yourself; everyone else is already taken."},
    {"author": "Maya Angelou", "text": "If you don't like something, change it."},
    {"author": "Steve Jobs", "text": "Stay hungry, stay foolish."},
    {"author": "Dr. Seuss", "text": "Don't cry because it's over, smile because it happened."}
]

@app.route('/')
def index():
    initial_quote = random.choice(quotes)
    return render_template('quote.html', quote=initial_quote)

@app.route('/api/quote')
def random_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)

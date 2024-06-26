#!/usr/bin/python3

'''A simple Flask web application demonstrating dynamic content and route ordering.
'''

from flask import Flask, render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False  # Allow trailing slashes in URLs

# Define routes with desired order

@app.route('/greeting/<name>')  # More specific route with a variable
def greet(name):
    return f'Hello, {name}! Welcome to the dynamic page.'

@app.route('/about')  # Route for "About Us" page
def about():
    return render_template('about.html')  # Render an HTML template for richer content

@app.route('/')  # General home page route
def index():
    # Optionally, collect data from user input using request.args or request.form
    if request.args.get('name'):
        return f'Hello, {request.args.get("name")}! (from query string)'
    else:
        return 'Welcome to the HBNB web application!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')


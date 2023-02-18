#from kodland_db import db
from flask import Flask, render_template
from datetime import datetime, timedelta
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prod')
def prod():
    end_date = datetime.now() + timedelta(days=7)
    end_date = end_date.strftime('%d.%m.%Y')
    return render_template('prod.html',end_date=end_date)

@app.route('/builds')
def builds():
    return render_template('builds.html')


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
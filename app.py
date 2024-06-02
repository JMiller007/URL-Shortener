from flask import Flask, request, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

    def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_url = short_url

def create_db():
    with app.app_context():
        db.create_all()

create_db()

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            return jsonify({'short_url': existing_url.short_url})

        short_url = generate_short_url()
        while URL.query.filter_by(short_url=short_url).first() is not None:
            short_url = generate_short_url()

        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()

        return jsonify({'short_url': short_url})
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    app.run(debug=True)

import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, UserRecord

app = Flask(__name__)

db_url = os.getenv('DATABASE_URL', 'sqlite:///local.db')

if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        if name and email:
            new_record = UserRecord(name=name, email=email)
            db.session.add(new_record)
            db.session.commit()
            return redirect(url_for('results'))
            
    return render_template('index.html')

@app.route('/results')
def results():
    records = UserRecord.query.order_by(UserRecord.created_at.desc()).all()
    return render_template('results.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
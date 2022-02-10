from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

### MODELS
class PROJECTS(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column(db.String(50))
    paascode = db.Column(db.String(50))
    approval_status = db.Column(db.Boolean, default=False)
    fund = db.Column(db.String(10))
    pagvalue = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    country = db.Column(db.String(50))
    lead_org_unit = db.Column(db.String(50))
    theme = db.Column(db.String(50))
    donor = db.Column(db.Text)
    total_expenditure = db.Column(db.Integer)
    total_contribution = db.Column(db.Integer)
    total_psc = db.Column(db.Integer)

db.create_all()
### ROUTES

@app.route('/api/projects/all')
def all():
    all_projects = PROJECTS.query.all()
    return jsonify(all_projects)

@app.route('/api/projects/country/<country_name>')
def country(country_name):
    country = PROJECTS.query.filter_by(country=country_name).all()
    return jsonify(country)

@app.route('/api/projects/approval_status/<status>')
def approval_status(status):
    status = PROJECTS.query.filter_by(approval_status=status).all()
    return jsonify(status)


### MAIN

if __name__ == '__main__':
    app.run(debug=True)
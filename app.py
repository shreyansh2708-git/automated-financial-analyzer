from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:yourpassword@localhost/ml_finance'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MLResults(db.Model):
    __tablename__ = 'ml_results'
    company_id = db.Column(db.String(32), primary_key=True)
    company_name = db.Column(db.String(255))         
    logo_url = db.Column(db.String(512))             
    website = db.Column(db.String(512))             
    pros = db.Column(db.Text)
    cons = db.Column(db.Text)
    roe_3y = db.Column(db.Float)
    debt_equity = db.Column(db.Float)
    div_payout = db.Column(db.Float)
    profit_growth_5y = db.Column(db.Float)
    sales_growth_10y = db.Column(db.Float)

@app.route('/')
def index():
    
    return list_companies()

@app.route('/companies')
def list_companies():
    
    companies = MLResults.query.with_entities(
        MLResults.company_id,
        MLResults.company_name,
        MLResults.logo_url,
        MLResults.website
    ).order_by(MLResults.company_name).all()

    return render_template('company_list.html', companies=companies)

@app.route('/company/<company_id>')
def company_detail(company_id):
    result = MLResults.query.filter_by(company_id=company_id).first()
    if not result:
        abort(404, description="Company not found")

    return render_template('company_detail.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


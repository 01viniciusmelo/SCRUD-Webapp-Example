from app import db

class It_companies(db.Model):
    # in flask-sqlalchemy, __tablename__ is automatically set unless overridden
    # http://flask-sqlalchemy.pocoo.org/2.3/models/

    #__tablename__ = 'it_companies'

    company_id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, unique=True, nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    industries = db.Column(db.String(255), nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    fiscal_year = db.Column(db.DateTime, nullable=False)
    employees = db.Column(db.Integer, nullable=False)
    market_cap = db.Column(db.Float, nullable=False)
    headquarters = db.Column(db.String(255), nullable=False)

    # The return value is displayed in tables that reference this class.
    def __str__(self):
        return self.company_name

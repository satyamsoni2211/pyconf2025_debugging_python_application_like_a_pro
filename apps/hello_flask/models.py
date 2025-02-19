from database import db

class Salary(db.Model):
    __tablename__ = "salaries"

    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    month = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "employee_name": self.employee_name,
            "amount": self.amount,
            "month": self.month
        }

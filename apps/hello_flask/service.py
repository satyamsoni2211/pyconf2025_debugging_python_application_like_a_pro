from models import Salary
from database import db

def create_salary(employee_name, amount, month):
    salary = Salary(employee_name=employee_name, amount=amount, month=month)
    db.session.add(salary)
    db.session.commit()
    return salary.to_dict()

def get_all_salaries():
    return [salary.to_dict() for salary in Salary.query.all()]

def get_salary(salary_id):
    salary = Salary.query.get(salary_id)
    return salary.to_dict() if salary else None

def update_salary(salary_id, employee_name, amount, month):
    salary = Salary.query.get(salary_id)
    if not salary:
        return None
    salary.employee_name = employee_name
    salary.amount = amount
    salary.month = month
    db.session.commit()
    return salary.to_dict()

def delete_salary(salary_id):
    salary = Salary.query.get(salary_id)
    if not salary:
        return None
    db.session.delete(salary)
    db.session.commit()
    return {"message": "Salary record deleted"}

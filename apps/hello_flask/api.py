from flask import request
from flask_restx import Api, Resource, fields
from service import create_salary, get_all_salaries, get_salary, update_salary, delete_salary

api = Api(
    title="Salary Management API",
    version="1.0",
    description="An API for managing employee salaries",
)

ns = api.namespace("salaries", description="Salary operations")

salary_model = api.model(
    "Salary",
    {
        "employee_name": fields.String(required=True, description="Employee's name"),
        "amount": fields.Float(required=True, description="Salary amount"),
        "month": fields.String(required=True, description="Salary month"),
    },
)

@ns.route("/")
class SalaryList(Resource):
    @ns.marshal_list_with(salary_model)
    def get(self):
        """Get all salaries"""
        return get_all_salaries()

    @ns.expect(salary_model)
    @ns.marshal_with(salary_model, code=201)
    def post(self):
        """Create a new salary"""
        data = request.json
        return create_salary(data["employee_name"], data["amount"], data["month"]), 201

# 2️⃣ Get, Update, Delete Salary
@ns.route("/<int:salary_id>")
@ns.param("salary_id", "Salary ID")
class SalaryResource(Resource):
    @ns.marshal_with(salary_model)
    def get(self, salary_id):
        """Get a salary by ID"""
        salary = get_salary(salary_id)
        if not salary:
            api.abort(404, "Salary not found")
        return salary

    @ns.expect(salary_model)
    @ns.marshal_with(salary_model)
    def put(self, salary_id):
        """Update a salary by ID"""
        data = request.json
        updated_salary = update_salary(salary_id, data["employee_name"], data["amount"], data["month"])
        if not updated_salary:
            api.abort(404, "Salary not found")
        return updated_salary

    @ns.response(204, "Deleted successfully")
    def delete(self, salary_id):
        """Delete a salary by ID"""
        deleted_salary = delete_salary(salary_id)
        if not deleted_salary:
            api.abort(404, "Salary not found")
        return {}, 204

api.add_namespace(ns)

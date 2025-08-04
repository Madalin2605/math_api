from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from app.schemas.math_schemas import (
    PowerRequest, FibonacciRequest, FactorialRequest
)
from app.controllers.math_controller import (
    handle_power, handle_fibonacci, handle_factorial
)

math_bp = Blueprint('math', __name__, url_prefix='/math')


@math_bp.route('/power', methods=['POST'])
def power_route():
    try:
        req_model = PowerRequest(**request.json)
        res_model = handle_power(req_model)
        return jsonify(res_model.dict()), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422


@math_bp.route('/fibonacci', methods=['POST'])
def fibonacci_route():
    try:
        req_model = FibonacciRequest(**request.json)
        res_model = handle_fibonacci(req_model)
        return jsonify(res_model.dict()), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422


@math_bp.route('/factorial', methods=['POST'])
def factorial_route():
    try:
        req_model = FactorialRequest(**request.json)
        res_model = handle_factorial(req_model)
        return jsonify(res_model.dict()), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422

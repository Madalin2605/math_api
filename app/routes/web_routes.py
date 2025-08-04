from flask import Blueprint, render_template, request
from app.controllers.math_controller import (
    handle_power, handle_fibonacci, handle_factorial
)
from app.schemas.math_schemas import (
    PowerRequest,
    FibonacciRequest,
    FactorialRequest,
)

web_bp = Blueprint('web', __name__, url_prefix='/web')


@web_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@web_bp.route('/power', methods=['POST'])
def web_power():
    data = PowerRequest(base=float(request.form['base']),
                        exponent=float(request.form['exponent']))
    result = handle_power(data).result
    return render_template('index.html', result=result)


@web_bp.route('/fibonacci', methods=['POST'])
def web_fibonacci():
    data = FibonacciRequest(n=int(request.form['n']))
    result = handle_fibonacci(data).result
    return render_template('index.html', result=result)


@web_bp.route('/factorial', methods=['POST'])
def web_factorial():
    data = FactorialRequest(n=int(request.form['n']))
    result = handle_factorial(data).result
    return render_template('index.html', result=result)

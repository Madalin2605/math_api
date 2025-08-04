from app.utils.operations import power, fibonacci, factorial
from app.schemas.math_schemas import (
    PowerRequest, PowerResponse,
    FibonacciRequest, FibonacciResponse,
    FactorialRequest, FactorialResponse
)
# from flask import current_app
from app.models.request_log import RequestLog
from app.models.db import db


def handle_power(request_data: PowerRequest) -> PowerResponse:
    result = power(request_data.base, request_data.exponent)
    response = PowerResponse(result=result)

    # Log to DB
    log = RequestLog(
        operation='power',
        input_data=request_data.json(),
        result=str(response.result)
    )
    db.session.add(log)
    db.session.commit()

    return response


def handle_fibonacci(request_data: FibonacciRequest) -> FibonacciResponse:
    result = fibonacci(request_data.n)
    response = PowerResponse(result=result)

    # Log to DB
    log = RequestLog(
        operation='fibonacci',
        input_data=request_data.json(),
        result=str(response.result)
    )
    db.session.add(log)
    db.session.commit()

    return response


def handle_factorial(request_data: FactorialRequest) -> FactorialResponse:
    result = factorial(request_data.n)
    response = PowerResponse(result=result)

    # Log to DB
    log = RequestLog(
        operation='factorial',
        input_data=request_data.json(),
        result=str(response.result)
    )
    db.session.add(log)
    db.session.commit()

    return response

from app.utils.operations import power, fibonacci, factorial
from app.schemas.math_schemas import (
    PowerRequest, PowerResponse,
    FibonacciRequest, FibonacciResponse,
    FactorialRequest, FactorialResponse
)
from app.models.request_log import RequestLog
from app.models.db import db
from app.kafka.producer import send_log


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

    # Send to Kafka
    send_log(
        operation='power',
        input_data=request_data.dict(),
        result=str(response.result)
    )

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

    # Send to Kafka
    send_log(
        operation='fibonacci',
        input_data=request_data.dict(),
        result=str(response.result)
    )

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

    # Send to Kafka
    send_log(
        operation='factorial',
        input_data=request_data.dict(),
        result=str(response.result)
    )

    return response

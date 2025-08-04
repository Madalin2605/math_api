from pydantic import BaseModel, Field, conint, confloat


# ======== Power ========
class PowerRequest(BaseModel):
    base: confloat(strict=True) = Field(
        ..., description="The base number."
    )
    exponent: confloat(strict=True) = Field(
        ..., description="The exponent to raise the base to."
    )


class PowerResponse(BaseModel):
    result: float


# ======== Fibonacci ========
class FibonacciRequest(BaseModel):
    n: conint(strict=True, ge=0) = Field(
        ..., description="The index of the Fibonacci sequence (must be >= 0)."
    )


class FibonacciResponse(BaseModel):
    result: int


# ======== Factorial ========
class FactorialRequest(BaseModel):
    n: conint(strict=True, ge=0) = Field(
        ..., 
        description="The number to compute the factorial for (must be >= 0)."
    )


class FactorialResponse(BaseModel):
    result: int

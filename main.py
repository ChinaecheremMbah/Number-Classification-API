from fastapi import FastAPI, Query
import httpx

app = FastAPI()

# Simple root route for testing the API
@app.get("/")
def read_root():
    return {"message": "API is working!"}

# Helper function to check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Helper function to check if a number is perfect
def is_perfect(n: int) -> bool:
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

# Helper function to check if a number is an Armstrong number
def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

# Helper function to calculate the sum of digits
def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

# Main API route to classify the number
@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    try:
        # Get a fun fact about the number from the Numbers API
        fun_fact_url = f"http://numbersapi.com/{number}/math"
        async with httpx.AsyncClient() as client:
            response = await client.get(fun_fact_url)
            fun_fact = response.text if response.status_code == 200 else "No fun fact available."

        # List of properties for the number
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        if number % 2 != 0:
            properties.append("odd")
        else:
            properties.append("even")

        # Return the classification data
        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact
        }
    except Exception as e:
        # Return an error response in case of invalid input or any issue
        return {"number": number, "error": True, "message": str(e)}

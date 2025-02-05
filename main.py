from fastapi import FastAPI, Query
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working!"}


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    try:
        fun_fact_url = f"http://numbersapi.com/{number}/math"
        async with httpx.AsyncClient() as client:
            response = await client.get(fun_fact_url)
            fun_fact = response.text if response.status_code == 200 else "No fun fact available."

        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact
        }
    except Exception:
        return {"number": number, "error": True}

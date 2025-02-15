# Number-Classification-API
Create an API that takes a number and returns interesting mathematical properties about it, along with a fun fact.
# Number Classification API

## Overview
This API classifies numbers based on their mathematical properties and fetches a fun fact.

## API Endpoint
**GET** `/api/classify-number?number=<integer>`

Example:

### Example Response:
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Response:
If the input is invalid (like a non-number), the API returns:

{
  "number": "alphabet",
  "error": true
}


How to Run Locally
To run the API on your local machine:

1. Install dependencies

pip install -r requirements.txt

2. Run the app with uvicorn

uvicorn main:app --reload

Deployment

The API is deployed on Render and can be accessed through the following URL:

https://number-classification-api-8emh.onrender.com
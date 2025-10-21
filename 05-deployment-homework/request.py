import requests

response = requests.post(
    "http://localhost:9696/predict",
    json={
        "lead_source": "organic_search",
        "number_of_courses_viewed": 4,
        "annual_income": 80304.0
    }
)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
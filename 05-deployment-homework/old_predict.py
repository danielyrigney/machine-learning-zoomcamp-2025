import pickle

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

datapoint = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

result = pipeline.predict_proba(datapoint)[0, 1]
print(f'Probability of churn: {result:.3f}')
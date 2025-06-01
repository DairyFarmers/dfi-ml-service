# DFI ML Service

A lightweight Flask-based machine learning microservice that predicts:
- How much a person is likely to contribute.
- Whether the company can fulfill a given total contribution request.

## 🚀 Features

- Predict individual contributions based on historical data
- Estimate company's ability to meet a total request
- API endpoint for bulk predictions
- JSON response output
- Simple and clean Flask backend

## 📦 Requirements

- Python 3.10+
- Flask 3.1.0
- pandas 2.2.3
- scikit-learn 1.6.1
- numpy 2.0.2

## Instal docker on running machine

Build docker image:

```bash
docker build -t flask-docker-app .
```

Run docker image:
```bash
docker run -p 5000:5000 flask-docker-app
```

### Note : Before running the docker image configure .env

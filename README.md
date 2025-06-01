# DFI ML Service

A lightweight Flask-based machine learning microservice that predicts:
- How much a person is likely to contribute.
- Whether the company can fulfill a given total contribution request.

## 🚀 Features

- Predict individual contributions based on historical data
- Estimate company's ability to meet a total request
- API endpoint for bulk predictions

## 📦 Requirements

- Python 3.10+
- Docker

## Instal docker on running machine before running following commands

Build docker image:

```bash
docker build -t flask-docker-app .
```

Run docker image:
```bash
docker run -p 5000:5000 flask-docker-app
```

### Note : Before running the docker image configure .env


## Pre-requesties in database

### Note : I'm using postgresql as my database.

Create table which is mandatroy to get the past data
```bash
CREATE TABLE "SuppliersContribution"(
    "SuppliersContributionId" BIGSERIAL,
    "SupplierMailId" VARCHAR(55),
    "CreatedDate" DATE,
    "ItemId" INT,
    "Contribution" BIGINT
)
```


## Request object type
```json
{
"itemId":1,
"requestingAmount":400
}
```


## Response object type

### Sucess
```json
[{"SupplierMailId":"Person5@gmail.com","scaled_prediction":64}, ....]
```
### Failture
```json
{
  "resMsg": "Our suppliers won't be able to do this request"
}
```

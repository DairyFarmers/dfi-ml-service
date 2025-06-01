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

Create table which is mandatroy to sotre and the past data
```bash
CREATE TABLE "SuppliersContribution"(
    "SuppliersContributionId" BIGSERIAL,
    "SupplierMailId" VARCHAR(55),
    "CreatedDate" DATE,
    "ItemId" INT,
    "Contribution" BIGINT
)
```


## To get the result access following end point with the give request body type
```
localhost:5000/bulkRequest
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

To check the ml service working fine whether you don't have any new data hit the following endpoint using post method with a empty body
```
localhost:5000/generateSamples
```
You will be reciving following body
```json
{
  "res": "New samples generated successfully"
}
```

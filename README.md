# passwordless-sandbox

Just an experiment with passwordless authentication. This is a service built with FastAPI, running on AWS Lambda, using DynamoDB for storage, and deployed by Serverless Framework.

## Project structure

The `sandbox` module contains a FastAPI app. Dependencies are managed with Poetry.

The project also uses NPM, but only to manage the Serverless Framework dependency, along with its plugins.

## Prerequisites

* [AWS account](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/#create-an-iam-user-and-access-key) (optional; if you're only running this locally, you don't need an AWS account)
* [Node.js and NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) (for Serverless Framework)
* [Serverless Framework](https://www.serverless.com/framework/docs/getting-started)
* [Poetry](https://python-poetry.org/docs/#installation)

## Setup

### Python

Set up a Python 3.9 virtual environment:

```
python3.9 -m venv venv
source venv/bin/activate
```

### Install dependencies

```
npm install
poetry install
```

### DynamoDB

If running locally, set up a local DynamoDB instance using the Serverless plugin:

```
serverless dynamodb install
```

### Environment

Copy `example.env` to `.env` and customize as needed. All the environment variables listed are required for running locally.

### AWS Parameter Store

This is required if deploying to AWS. If only running locally, this step is not required.

Configure these parameters in [AWS Parameter Store](https://console.aws.amazon.com/systems-manager/parameters/) (link requires being logged in to the AWS account):

* dev-smtp-host (becomes SMTP_HOST environment variable in Lambda)
* dev-smtp-user (becomes SMTP_USER environment variable in Lambda)
* dev-smtp-password (becomes SMTP_PASSWORD environment variable in Lambda)

## Usage

### Running locally

```
serverless dynamodb start --migrate
poetry run server
```

### Deploy to AWS

```
serverless deploy
```

### Undeploy from AWS

```
serverless remove
```

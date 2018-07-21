
This is a very simply project attempting to combine plot.ly and serverless.

However, right now there is an issue where the plotly libraries are too large for AWS Lambda

```
Serverless Error ---------------------------------------

  An error occurred: HelloLambdaFunction - Unzipped size must be smaller than 262144000 bytes (Service: AWSLambda; Status Code: 400; Error Code: InvalidParameterValueException; Request ID: d4ef3b5a-8c8f-11e8-871a-cbe0ff4d6f5e).

  Stack Trace --------------------------------------------

ServerlessError: An error occurred: HelloLambdaFunction - Unzipped size must be smaller than 262144000 bytes (Service: AWSLambda; Status Code: 400; Error Code: InvalidParameterValueException; Request ID: d4ef3b5a-8c8f-11e8-871a-cbe0ff4d6f5e).
    at provider.request.then (/Users/nfeger/.nvm/versions/node/v9.5.0/lib/node_modules/serverless/lib/plugins/aws/lib/monitorStack.js:112:33)
From previous event:
```



Configuring:

one time setup:

1. copy example_config.yaml to config.yaml

Be sure to enter your plot.ly username and api key plot.ly credentials

2. virtualenv example-plotly-metrics --python=python3
2a. pip3 install -r requirements.txt
3. Setup  your aws credentials in .aws/credentials and take note of the credential name if it's not defaul
4. Make sure node and nvm are installed.



Working on the Repo:

```
export AWS_PROFILE=development # or whatever your aws profile is.
nvm use stable  # should use a decent version of node
source example-plotly-metrics/bin/activate
```


When deploying to a local environment besure to use the correct env setting:
```bash
sls -s [username] deploy
```


If you go the AWS console you'll be able to see the CloudFront distribution created by this deploy
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks?filter=active


see: serverless.com for more info

reference: https://serverless.com/blog/serverless-python-packaging/

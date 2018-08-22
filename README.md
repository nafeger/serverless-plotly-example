
This is a very simply project attempting to combine plot.ly and serverless.

If you are using python and serverless pay special attention to the package section of the serverless.yaml file. It makes using large libraries a possibility


Configuring:

one time setup:

1. copy example_config.yaml to config.yaml

Be sure to enter your plot.ly username and api key plot.ly credentials

2. python3 -m venv venv/
2a. pip3 install -r requirements.txt
3. Setup  your aws credentials in .aws/credentials and take note of the credential name if it's not defaul
4. Make sure node and nvm are installed.



Working on the Repo:

```
export AWS_PROFILE=development # or whatever your aws profile is.
nvm use stable  # should use a decent version of node
source venv/bin/activate
```


When deploying to a local environment besure to use the correct env setting:
```bash
sls -s [username] deploy
```


If you go the AWS console you'll be able to see the CloudFront distribution created by this deploy
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks?filter=active


see: serverless.com for more info

reference: https://serverless.com/blog/serverless-python-packaging/

# serverless-framework-demo

Use this guide to install the serverless framework tool:
- https://www.serverless.com/framework/docs/getting-started/

To get yourself logged into AWS, use this guide:

- https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

To deploy this to AWS, use this command:

    sls deploy -s dev


To install python packages to be included in the Lambda layer, use this command:

    pip3 install (package) --system -t packages-layer/python/

See stepFunctions branch for a more complex example with that uses Step Functions.
def section1():
    """
    ## Dataset Binding with AWS

    In this section, we will create an [AWS Lambda](https://www.serverless.com/aws-lambda) that will continuously sync a bucket with Dataloop's Dataset.

    If you want to catch events from the AWS bucket and update the Dataloop Dataset you need to set up a Lambda. The Lambda will catch the AWS bucket events and will reflect them into the Dataloop platform. We have prepared an environment .zip file with our SDK for Python 3.8, so you don't need to create anything else to use dtlpy in Lambda.

    **Note**: For any other custom use (e.g. other Python version or more packages) try creating your own layer (We used [this](https://www.geeksforgeeks.org/how-to-install-python-packages-for-aws-lambda-layers) tutorial and the Python 3.8 docker image).

    ### Create the Lambda
    To create a new AWS Lambda, you need to go through a few steps, listed below:
    
    1. [Create a new Lambda](https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/lambda-tutorial.html).
    
    2. The default timeout is 3[s] so we'll need to change to 1[m] (1 Minute); to do that go to Configuration → General configuration → Edit → Timeout.

    3. Go to the Lambda console -> Select your function -> Configuration -> (Left-side panel) Environment variables -> Edit -> Add environment variable
           * Add the 3 secrets variables `DATASET_ID`, `DTLPY_USERNAME`, `DTLPY_PASSWORD`.
           * To populate the values for the variables: `DTLPY_USERNAME`, `DTLPY_PASSWORD` you'll need to create a **Dataloop Bot** ([read more here](https://developers.dataloop.ai/onboarding/02_login_and_project_and_dataset_creation/) on your Dataloop project using the following code:
    """


def section2():
    """
    4. Copy the following code in your IDE or Console:
    """


def section3():
    """
    ### Add a Layer to the Lambda
    We have created an AWS Layer with the Dataloop's Python SDK. You must now Click [here](https://storage.googleapis.com/dtlpy/aws-python3.8-lambda-layer/layer.zip/) to download the zip file.
    
    Because the layer's size is larger than 50MB you cannot use it directly (due to AWS restrictions), and need to upload it to a bucket first. Once uploaded, create a new layer for the dtlpy environment, using the following steps:
    1. Go to the layers screen and "click Add Layer".
    ![add_layer](../../../../assets/bind_aws/create_layer.png)
    2. Choose a name (e.g. dtlpy-env).
    3. Use the link to the bucket `layer.zip`, the one from above.
    4. Select the environment (x86_64, python3.8).
    5. Click "Create" and the bottom on the page.

    Now you can go back to your Lambda and add the new layer:
    1. Select the "Add Layer".
    ![add_layer](../../../../assets/bind_aws/add_layer.png)
    2. Choose "Custom layer" and select the Layer you've previously added and the version.
    3. Click "Add" at the bottom.

    ### Create the Bucket Events
    To create Bucket Events, you must go to the bucket you are using, and create that event using the following steps:
    1. Go to Properties → Event notifications → Create event notification.
    2. Choose a name for the Event.
    3. For the Event types choose: All object create events, All object delete events.
    4. For the destination choose: Lambda function → Choose from your Lambda functions → choose the function you built → SAVE

    Once you deploy it, you're good to go!
    """

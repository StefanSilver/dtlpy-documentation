def func1():
    """
    ## Offline model training, logging metrics in Dataloop

    Models can be trained offline (i.e. locally, without connecting the model to the platform) with only the model metrics being uploaded to the Dataloop platform for versioning and comparisons.  This tutorial will walk you through how to upload metrics from model training via Dataloop's Python SDK.

    The Dataloop entities required are:
     - Package
     - Codebase reference
     - Model (with a valid Dataset ID)

    ### Create Dataloop entities
    Before starting, you need to create a dummy Package, a dummy Codebase reference, and a model with a valid Dataset ID. The code below shows how to do this, and remember to replace `<project_name>` and `<dataset_id>` with the appropriate strings to reference your Project and Dataset.

    """


def func2():
    """
    ### Metrics
    Now that you’ve created the necessary Dataloop entities, metrics can be uploaded to the platform with `model.add_log_samples()` function.

    In the example below we are uploading some dummy training data:

    """


def func3():
    """
    Metrics plots will appear under the “metrics” tab of your chosen model. The above code example will look like this:

    ![image](https://user-images.githubusercontent.com/58508793/230951041-06544b46-1cce-4f87-9980-10dd7794b1c4.png)

    Once you’ve uploaded multiple model metrics, you can compare them all in the WebUI of the platform.
    """

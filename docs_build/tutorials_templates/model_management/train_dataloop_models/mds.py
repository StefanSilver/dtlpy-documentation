def func1():
    """
    # Using pre-trained Models (AI library)

    Pre-trained models that are ready for use out-of-the-box are available in the Dataloop AI Library. The AI library contains various algorithms and pre-trained models that can be used for inferencing or fine-tuning via additional training on your custom Datasets.

    This tutorial will cover how to use AI library models for:

    - performing prediction using pre-trained models, and
    - fine-tuning the model on a custom Dataset.
    **Note:** Before you do anything using Dataloop's Python SDK, you need to `import dtlpy` and log in into the platform - using the code below.
    ```python
    #importing Dataloop's Python Package and Numpy
    import dtlpy as dl
    
    #Logging in to Dataloop (checks if token expired ~24h expiration time for token)
    if dl.token_expired():
        dl.login()
    #you can also use the simple login: 
    #dl.login()
    ```
    The code below looks for all available packages that are "public", so you can see all models available in the AI library.

    """

def func2():
    """
    The code should print all of the available models on Dataloop, which you can freely use, as they are in the public domain. The output should look similar to below, for each model:
    ```python
    |  0 | 63348723f6a47cc702046af7 | or@dataloop.ai | pretrained-yolo-v5-small | yolo v5 small arch, pretrained on ms-coco | ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',...
    ```
    ## Clone and deploy a model

    As a good practice, you should get the model you want to use and then clone it. To do that, you need to get the model and Package you want and copy it to your Project.

    Only models that are trained (i.e. `model.status = 'trained'`) can be deployed. If the AI library model is pre-trained (i.e. model status is 'trained'), it can be deployed directly. To do that, you can use the script below, where you only need to replace the `<project_id>` and the `model_name`.

    """

def func3():
    """
    ## Train on a custom Dataset

    If you would like to customize the AI library model (for transfer-learning or fine-tuning), you can indicate the new Dataset and Labels you want to use to train the model.

    """

def func4():
    """

    ### Dataset subsets
    Our AI library models require the train/validation split of the Dataset for the training session. To avoid data leakage between training sessions and to make each training reproducible, we will determine the data subsets and save the split type to the Dataset entity (using a DQL). Using DQL ([Dataloop Query Language](https://dataloop.ai/docs/api-dql)) Filters you can split the data however you like.

    For example, if your Dataset is split between folders, you can use the DQL below to add Metadata for all Items in the Dataset. 
    """

def func5():
    """
    This way, when the training starts, the sets will be downloaded using the DQL and any future training session on this Dataset will have the same subsets of data.

    **Note:** In the future, this mechanism will be expanded to use a tagging system on Items. This will allow more flexible data subsets and random data allocation.

    To train the model on your custom data, simply use the `model.train()` function and wait for the training to finish. You can monitor the training progress on the platform or via the Python SDK. To see the updated model status, retrieve the model again from the platform (`get`) and then print its status, as seen in the code below.

    """

def func6():
    """
    ### Deploying the model

    Once the model is trained, it can be deployed as a Service. The `model.deploy()` method automatically creates a Bot and Service for the trained model.

    Once you have a model deployed, you can create a UI slot to inference on individual data Items on the platform, or call the model to inference in a FaaS or Pipelines.
    """

def func7():
    """
    ## Predict on a single item

    Once a model is deployed, you can use it to predict on Items using the `model.predict()` function. The function returns an execution object that can be used to track whether the prediction execution was successful. If successful, the Annotations will be uploaded to the Item directly and can be viewed in the Annotation Studio. You can use `item.open_in_web()` to open the Item in the WebUI.

    **Note:**If you have just deployed the model, `get` the model again to get the updated model Metadata that includes the deployment information.

    """

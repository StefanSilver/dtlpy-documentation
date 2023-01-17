def func1():
    """
    ## Tutorial: Using models from the AI library

    Model algorithms that are ready for use out-of-the-box are available in the Dataloop AI Library. The AI library contains various algorithms and pretrained models that can be used for inferencing or fine-tuning via additional training on your custom datasets.

    This tutorial will cover how to use AI library models for:

    - predicting from pretrained models, and
    - fine-tuning training on a custom dataset.

    To see available public models, filter all available packages to view those with a “public” scope:

    """


def func2():
    """
    ### Clone and deploy a public model

    Download the model and package you want to copy it to your project.

    Only models that are trained (i.e. model.status = 'trained') can be deployed. Since the public model is pre-trained, it can be deployed directly.

    """


def func3():
    """
    ### Train on a custom dataset

    If you want to customize the public model (for transfer-learning or fine-tuning), you can indicate the new dataset and labels you want to use for model training.

    """


def func4():
    """
    Public models can be downloaded to your machine for local training and inference, or they can be trained and deployed on the cloud for integration into the Dataloop platform.

    ### Dataset Subsets
    Our public models use a train/validation split of the dataset for the training session. To avoid data leakage between training sessions and to make each training reproducible,
    we will determine the data subsets and save the split type to the dataset entity (using a DQL). Using DQL filters you can subset the data however you like.

    For example, if your dataset is split between folders, you can use this DQL to add metadata for all items in the dataset
    """


def func5():
    """
    This way, when the training starts, the sets will be downloaded using the DQL and any future training session on this dataset will have the same subsets of data.

    NOTE: In the future, this mechanism will be expanded to use a tagging system on items. This will allow more flexible data subsets and random data allocation.

    ### Deploying a model remotely

    Download the model and package you want to copy it to your project. Since the public model is pretrained, it can be deployed without any further action.

    """

def func6():
    """
    If you want to customize the public model (for transfer-learning or fine-tuning), you can indicate the new dataset and labels for model training.

    A model can be trained with a new dataset with `model.train()`.

    A model can only be deployed after it's been trained. `model.deploy()` automatically creates a bot and service for the trained model.

    """

def func7():
    """
    Once you have a model deployed, you can create a UI slot to inference on individual data items on the platform, or call the model to inference in a FaaS.
    """

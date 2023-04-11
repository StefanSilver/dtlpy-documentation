def func1():
    """
    # Training a Classification Model with ResNet
    In this section we will download a public model from the AI library to inference and train on custom data locally. More specifically, we will use the ResNet50 model.

    Before you can run the code below, you need to install some additional Python packages. Start by installing the following packages if you don't have them installed already. The Model Adapter will use them later:
    - torch
    - torchvision
    - imgaug
    - scikit-image<0.18

    After you make sure everything is installed, import the modules required for the scripts in this tutorial, by copying the code below.
    """


def func2():
    """
    ## Create the Package and pre-trained Model in your Project

    First, we create the Model entity for our project. You can view the public models in [the public Dataloop Github](https://github.com/orgs/dataloop-ai/repositories?type=all). You can view all publicly available models by using a Filter, and then `get` the model you want to use. Here we will use a ResNet50 model pre-trained on the ImageNET dataset.
    """


def func3():
    """
    ### Run a pretrained model
    We will then "build" a model adapter to get the package code locally and create an instance of the ModelAdapter class. Then we will load the pretrained model and weights into the model adapter.
    """


def func4():
    """
    ### Predict on an item
    Now we can get an Item and inference on it with the predict method and upload the Annotations. If you would like to see the Item and predictions, you can view it locally or you can open the Item on the platform(`item.open_in_web()`) and edit it directly there.
    """


def func5():
    """
    ## Train on new dataset
    Here we will use a public dataset of sheep faces. We create a Project and a Dataset and upload the data with 4 Labels of sheep.
    **Note**: You might need to change the location of the Items, which currently points to the root of the documentation repository. If you downloaded the dtlpy documentation repo locally, this should work as it is.
    """


def func6():
    """
    Now we'll run the `prepare_dataset` method. This will clone and freeze the Dataset so that we'll be able to reproduce the training with the same copy of the data. The cloned Dataset will be split into subsets, either filtered using DQL or as percentages. In this example, we'll use the famous 80/20 train/validation split.

    """

def func7():
    """
    After partitioning and cloning the data, we will clone the pretrained model to have a starting point for the fine-tuning. We create an Artifact where we can save the model weights. We will also indicate the model's configuration, which will determine some runtime configurations, such as the number of epochs. In this tutorial we will train for only 2 epochs.
    """

def func8():
    """
    We'll load the new, un-trained model into the adapter and prepare the local Dataset to be used for training.
    """


def func9():
    """
    ## Start the training
    The Package, model, and data are now prepared. We are ready to train our model!
    """


def func10():
    """
    ## Save the Model
    We will save the locally-trained model and upload the trained weights to the Artifact Item. This ensures that everything is on the Dataloop platform and allows other developers to use our trained model.
    """


def func11():
    """
    We can also list all Artifacts associated with this Package, and add more files that are needed to load or run the model.
    """


def func12():
    """
    ## Predict on our newly trained model
    With everything in place, we can now load our model and view an Item's prediction.
    """

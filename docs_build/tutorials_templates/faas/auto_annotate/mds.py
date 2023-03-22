def func1():
    """
    # Example: Model Auto-Annotation Service
    This tutorial demonstrates creating and deploying a Service that pre-annotates a items before manual Annotation work is performed, as part of an active-learning process.

    ## Service Code
    Your code can perform any action you need to execute, as part of pre-annotating Items, for example:
    - Access a remote server/API to retrieve Annotations;
    - Run your algorithm or ML model as a Service in Dataloop FaaS.

    In the example below we use a simple face detection algorithm that uses CV2 and a Caffe model:

    """


def func2():
    """
    ## Define the module
    In this example, we load the model in the `init` method, which runs only once at deployment time, saving us time by not loading on each Execution.
    These initial inputs are attributes that we want the Service to include for its entire lifetime. In this case, it's the model and weights files we want the Service to use and the model confidence (or accuracy) threshold for accepting detections.

    """


def func3():
    """
    ## Model and weights files
    The function uses 2 files containing the model and its weights for inferencing detections. We need to have these files at the same folder as the entry point. To get these files please download them by clicking the following link:
    https://storage.googleapis.com/dtlpy/model_assets/faas-tutorial/model_weights.zip

    ##Package Requirements
    Our Package codebase uses 2 non-standard Python libraries. Therefore, we need to make sure they are pre-installed before running the entry point. One way to do so is to [create and use a custom Docker image](https://dataloop.ai/docs/service-runtime#customimage). The other way is to add a requirements.txt file to the Package codebase. To do so, simply add the following requirements.txt file in the same folder of the entry point (main.py):
    """


def func4():
    """
    ## Push the Package
    Make sure you have the following files in one directory, before attempting to deploy the Package:
    - main.py;
    - requirements.txt;
    - res10_300x300_ssd_iter_140000.caffemodel;
    - deploy.prototxt.txt.

    After you make sure you got everything, use this code to deploy your Package:
    """


def func5():
    """
    ## Deploy The  Service
    The package is now ready to be deployed as a Service and executed in the Dataloop Platform. Whenever executed, your Package will run as a Service on the default instance type. Review the Service configuration and configure it to your particular needs. You could, for example:
    - Change the instance-type to use stronger instances with more memory, CPU and GPU;
    - Increase Autoscaling to handle larger loads;
    - Increase timeouts to allow longer execution times.


    """


def func6():
    """
    ## Trigger the Service
    Once the service is deployed, we can create a trigger to run it automatically when a certain event occurs.
    In our example we trigger the face-detection service whenever an item is uploaded to the platform.
    Consider using other triggers or different ways to run you service:
    - Add the services to a FaaS-node in a pipeline, before annotation tasks
    - Use DQL trigger to run only on specific datasets, or in specific tasks
    - Run the service when an item is updated
    
    In the code below, we create a Trigger for the Service we just created:
    """


def func7():
    """
    ## Uploading Model Weights as Artifacts
    Be aware that large data files such as ML model weights can be too big to include in a Package. [These and other large files can be uploaded as an Artifact](https://github.com/dataloop-ai/dtlpy-documentation/tree/main/functions/using_artifacts_in_faas).

    """

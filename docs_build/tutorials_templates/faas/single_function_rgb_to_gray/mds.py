def func1():
    """
    # Basic Use Case: Single Function
    ## Create and Deploy a Function
    In this section, you will learn how to create and execute a simple function using Dataloop's FaaS system. Below you will find an image manipulation function in Python, which converts an RGB image to a grayscale image. The function receives a single Item, which later can be used as a Trigger to invoke the function:
    """


def func2():
    """
    Once the function is defined, you can deploy the it as a Service using Dataloop's Python SDK. Once the Service is ready, you may execute the available function on any input image you desire. Below, we ```GET``` the Project we want to add the function to, and we then deploy that function:
    """


def func3():
    """
    ## Executing the function
    An Execution means running the function on a Service with specific inputs (arguments). The Execution input will be provided to the function that the Execution runs.

    Now that the Service is up, it can be executed manually (on-demand) or automatically, based on a set Trigger (time/event). In this tutorial, we will demonstrate how to manually run the “RGB to Gray” function. 

    To see the Item we uploaded earlier, run the following code to open the web-version of Dataloop:
    """


def func4():
    """
    We can now convert the Item you've added (and seen on web-view) from RGB to grayscale, using the Service we just created:
    """


def func5():
    """
    We can also execute the the Function on multiple Items using a Filter:
    """


def func6():
    """
    The transformed image will be saved in your Dataset in the specified folder. You may now open the Item in web-view, to see the changes:
    """

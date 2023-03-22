def func1():
    """
    # Multiple Functions and Modules
    ## Multiple Functions
    ### Create and Deploy a Package of Several Functions
    As usual, you must first login to the Dataloop platform (if you haven't already):
    """


def func2():
    """
    You must then define the Project and Dataset you will work with in this tutorial. If you already have a Project and Dataset created, you can use the existing ones.
    Otherwise, you can create a new Project and Dataset using the following code:
    """


def func3():
    """
    If you already have a Project and Dataset available, you can skip the step above, and just use (or `GET`) an existing Project and Dataset:
    """


def func4():
    """
    ### Write your code
    The following code consists of two image-manipulation functions: 
    * RGB to grayscale over an image;
    * CLAHE Histogram Equalization over an image - Contrast Limited Adaptive Histogram Equalization (CLAHE) to equalize images.
    
    To proceed with this tutorial, copy the following code, save it as a main.py file, and place it somewhere so you can find it easily, as we will use it later. 
    """


def func5():
    """
    ### Define the module
    Multiple functions may be defined in a single Package under a “module” entity. This way you will be able to use a single codebase for multiple Services.
    
    Here, we will create a module containing the two functions we discussed. The “main.py” file you downloaded is defined as the module entry point. You will later specify its directory file path.
    """


def func6():
    """
    ### Push the Package
    When you deployed the Service in the previous tutorial (“Single Function”), a module and a Package were automatically generated. 

    Now we will explicitly create and push the module as a Package in the Dataloop FaaS library (application hub). For that, please specify the source path (src_path) of the “main.py” file you downloaded, and then run the following code:
    """


def func7():
    """
    ### Deploy a Service
    Now that the Package is ready, it can be deployed to the Dataloop platform as a service.
    
    To create a Service from a Package, you need to define which module the Service will serve. Notice that a Service can only contain a single module. All the module functions will be automatically added to the Service.

    Multiple Services can be deployed from a single Package. Each service can get its own configuration: a different module and settings (computing resources, Triggers, UI slots, etc.).

    In our example, there is only one module in the Package. Let’s deploy the Service using the code below:
    """


def func8():
    """
    ### Trigger the Service
    Once the Service is deployed, we can configure a Trigger to automatically run the Service functions. When you bind a Trigger to a function, that function will execute when the Trigger fires. The Trigger is defined by a given time pattern or by an event in the Dataloop system.

    An event based Trigger is related to a combination of resource and action. A resource can be any entity in our system (Item, Dataset, Annotation, etc.) and the associated action will define a change in the resource that will prompt the Trigger (update, create, delete). You can only have one resource per Trigger.


    The resource object that triggered the function will be passed as the function's parameter (input). 

    Let’s set a Trigger when a new Item is created, using the code below:
    """


def func9():
    """
    In the Filters we defined above, we specified a Dataset using its ID. Once a new Item is uploaded (created) in this Dataset, the CLAHE function will automatically be executed for this new Item. You can also add Filters to specify the Item type (image, video, JSON, directory, etc.) or a certain format (jpeg, jpg, WebM, etc.).

    A separate Trigger must be set for each function in your Service.
    
    Now, we will define a Trigger for the second function in the module `rgb2gray`. Each time an Item is updated, this Trigger will invoke the rgb2gray function:
    """


def func10():
    """
    To trigger the function only once (only on the first Item update), you can set `TriggerExecutionMode.ONCE` instead of `TriggerExecutionMode.ALWAYS`.

    ### Execute the function
    Now we can upload an image to our Dataset to trigger the Service. Be sure to choose an image you wish, and then change the `local_path` to the exact location of that image, and change the `hamster.jpg` to the name of the image you want to upload.
    To see the Item (image) you just uploaded, you can just run a simple `item.open_in_web()`, which will open the Item in the web-view of Dataloop.
    The function `clahe_equalization` will be invoked when the new Item is uploaded:
    """


def func11():
    """
    Remote path is an optional parameter you can choose if you want the image to be sent toa specific directory; by default, images will go to the main directory.
    
    ### Review the function's logs
    You can review the execution log history to check that your execution succeeded, using the code below:
    """


def func12():
    """
    The transformed image will be saved in the Dataset you chose in the beggining. Once you open the log and see that the Execution succeeded, you may open the Item in web-view to see its transformation:
    """


def func13():
    """
    ### Pause the service:
    We recommend pausing the Service you created for this tutorial so it will not be triggered:
    """


def func14():
    """
    Congratulations! You have successfully created, deployed, and tested Dataloop functions!

    ## Multiple Modules
    You can also define multiple different modules in a Package. A typical use-case for multiple-modules is to have a single code base that can be used by multiple Services (for different applications). For example, having a single YOLOv4 codebase, but creating different modules for training, inference, etc.

    When creating a Service from that Package, you will need to define which module the Service will serve (a Service can only serve a single module with all of its functions). For example, to push a 2-module Package, you will need to have 2 entry points, one for each module. This is how you define the modules:

    """


def func15():
    """
    The code below will push the modules we previously defined to the Package, and then will update the `package` variable:
    """


def func16():
    """
    After doing that, when you deploy the Package, you will need to specify the name of the module you want to use. 
    Remember that a Service can only implement one module.

    """

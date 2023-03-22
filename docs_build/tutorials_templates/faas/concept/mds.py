def func1():
    """
    # FaaS Interactive Tutorial
    ## Concept
    FaaS (Function-as-a-Service), is a cloud computing model where a cloud provider manages and runs individual functions in response to events or triggers. 
    
    In Dataloop, a FaaS Service is a serverless computing Service that allows users to run code without the need to manage servers or other infrastructure. The FaaS Service is a key component of Dataloop's system architecture, providing a platform for executing code and integrating with other Services in the system. 
    
    The FaaS Service in Dataloop is designed to handle the Execution of small, isolated functions that can be triggered by a variety of events, such as data input from sensors or user actions.


    You can use Dataloop FaaS to extend other Dataloop services with custom logic. Altogether, FaaS serves as a super flexible unit that provides you with increased capabilities in the Dataloop platform and allows achieving any need while automating processes.

    With Dataloop FaaS, you simply upload your code and create your functions. Following that, you can define a time interval or specify a resource event for triggering the function. When a trigger event occurs, the FaaS platform launches and manages the compute resources, and executes the function. 

    You can configure the compute settings according to your preferences (machine types, concurrency, timeout, etc.) or use the default settings. 

    ## Components of Dataloop's FaaS
    Dataloop's FaaS has a number of components that you should have basic knowledge of. You can find themost important ones, and their definitions, below.
    
    ### Package
    A Package refers to an entity that is processed using the "Functions-as-a-Service" (FaaS) technology. FaaS Packages are used to automate the processing of data and can be used to perform a wide range of Tasks, such as data cleaning, data transformation, and data enrichment. FaaS Packages in the Dataloop system are created by Project managers or data scientists, who define the specific requirements for each Package, such as the data inputs, the functions to be executed, and the output data format. Once the FaaS Package is defined, it can be executed using the Dataloop FaaS engine, which automatically manages the Execution of the functions within the Package. The Package is a static code with a schema that holds all the Modules, functions, and the code base from which they can be taken.

    A Package could also be thought as a bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point. For now, it can be Python, nodeJS format. The main function of Packages is to deploy a Service and create an executable version of that code. Packages can be public, global, or specific to a particular Project.

    Packages are limited to a maximum of 100MB.
    
    ### Service
    A service can be thought as a deployed Package that serves the code. Given the matching input to a function, it will run it and return the output, e.g. 
    if we have code in our Package for converting RGB images to grayscale, the dl.Service would run the code and upload the grayed image.

    ### Execution
    Execution refers to the process of running a function within the FaaS Service. When a user submits a function for Execution, the FaaS Service creates a container to run the function and provides any necessary inputs. The function is executed within the container, and the results are returned to the user.
    
    ### Trigger
    A Trigger is a rule-based mechanism that initiates an action when a specific event occurs. Triggers are used to automate workflows and streamline data processing. They are created by defining a set of conditions that must be met for the Trigger to be activated. These conditions can be based on a variety of factors, such as the content of data, the time of day, or the occurrence of specific events. Once a Trigger is activated, it can initiate a range of actions, such as sending notifications, generating reports, or Triggering the Execution of a specific Task or workflow. It can be of 2 types:

    EventTrigger - contains a Project on which it monitors events, a Resource type such as Item, Annotation, Task, etc. The action that happened to the Resource such as created, updated, deleted status changed, etc. a DQL (The Data Query Engine) Filter that checks whether or not to invoke the operation based on the Resource JSON, and an operation.
    CRONTrigger - enables you to run functions at specified time patterns with constant input using the Cron syntax. In the Cron Trigger specification, you specify when you want the Trigger to start, when you want it to end, specifying when it should run, and the input that should be sent to the action.
    
    ### Bot
    A Bot is a machine user that has the Developer role and permissions within a Project. In Dataloop, Bots are used to run Services. Once a Service has been deployed, it will log in using the Bot with which the Service was created or the Bot will be created automatically. All of the Dataloop platform's API requests will be made using the Bot’s token.
    
    
    ## Use Cases
    The use cases for Dataloop's FaaS are various, and allows to run a pletora of functions and processes. Some examples of those use cases are:
    
    - **Pre annotation processing**: Resize, video assembler, video dissembler;

    - **Post annotation processing**: Augmentation, crop box-annotations, auto-parenting;

    - **ML models**: Auto-detection;

    - **QA models**: Auto QA, consensus model, majority vote model.

    """

def section1():
    """
    ## Dataset Binding with Azure

    In this section we will create an Azure Function App that will continuously sync a Blob with a Dataloop Dataset.

    If you want to catch events from the Azure Blob and update the Dataloop Dataset you need to set up a Blob function. This function will catch the Blob storage events and will reflect them into the Dataloop Platform.

    If you are familiar with [Azure Function App](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python), you can just use the integration function you will see below.

    We assume you already have an Azure account with resource group and storage account. If you don't, follow the [Azure docs](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create) and create them.

    ### Create the Blob function
    To create a Blob Function, use the steps below:
    
    1. Create a Container in the created Storage account: ***Public access level -> Container OR Blob***.
    **Note:** This container should be used as the external storage for the Dataloop Dataset.
    
    2. Go back to Function App and click ***Create ->*** to create a new function:
       * Choose Subscription.
       * Choose your Resource Group.
       * Choose Function Name.
       * Publish -> Code.
       * Runtime stack -> Python.
       * Version -> 3.10 >= Version >= 3.7.
       **Note:** when choosing python 3.7 please pay attention to the AOL warning.
       * Choose the Region.
       * Use default values for all other options (OS and Plan).
       * Press next and choose your Storage account.
       * Review and create the Blob function.

    ### Deploy your function
    In Visual Studio (VS) code,you must follow the instructions in [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) to configure your environment and deploy the function:
    1. Configure your environment.
    2. Sign in to Azure.
    3. Create your local project:
       * On VS code go to Azure panel -> workspace (bottom left panel)-> create a function.
       * Choose the directory location for your project workspace and choose Select.
        **Note:** You should either create a new folder or choose an empty folder for the project workspace. Don't choose a project folder that is already part of a workspace.
       * In Select a template for your project's first function choose -> Azure Event Grid trigger.
       * Open the code file.
       * In the requirements.txt file -> add ```dtlpy```.
       * Replace the code on \_\_init\_\_.py file with the code snippet below:
       **Note:** Make sure you **save** the file on Vs code - If not it **will not be deployed** to Azure.

    """


def section2():
    """
    4. Deploy the code to the function app you created (for more information take a look at [Azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration#deploy-the-project-to-azure).
    5. In VS code go to ***view tab -> Command Palette -> Azure Functions: Upload Local Settings***.
    6. Go to the Function App -> Select your function -> Configuration (Under Settings section) and:
           * Add the 4 secrets variables: `DATASET_ID`, `DTLPY_USERNAME`, `DTLPY_PASSWORD`, `CONTAINER_NAME` (the container to add a trigger)
           * To populate the values for the variables: `DTLPY_USERNAME`, `DTLPY_PASSWORD` you'll need to create a **Dataloop Bot** on your Dataloop Project using the following code:
    """


def section3():
    """
    7. Now go to ***Function App -> Select your function -> Navigate in the sidebar to the functions tab and select your function ->
    Integration -> Select the trigger -> Create Event Grid subscription***:
        * Event Schema -> Event Grid Schema.
        * Topic Types -> Storage Account (Blob & GPv2).
        * Select your Subscription, Resource Group, Resource.
        * System Topic Name -> your Event Grid Topic (if you do not have one create it).
        * Filter to Event Types -> Create and Delete.
        * Endpoint Type -> Function App (Azure function).
        * Endpoint -> your function.

    **Note:** It will take up to 5 minutes when you deploy using auto upstream.


    **Done! Now your storage Blob will be synced with the Dataset it is linked to in the Dataloop platform!**
    """

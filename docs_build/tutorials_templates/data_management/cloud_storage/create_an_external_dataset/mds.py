def section1():
    """
    # Cloud Storage
    ## External Storage Dataset

    If you already have your data managed and organized on a cloud storage service, such as GCS/S3/Azure, you may want to
    use it in Dataloop without uploading the binaries and creating duplicates. This section will teach you how to integrate your data to Dataloop's Platform, what permissions are required and more.

    ### Cloud Storage Integration

    If you want to create an integration with GCS, S2 or Azure cloud, you need to add a key/secret with the following
    permissions:

    - List (Mandatory) - it allows Dataloop to list all of the Items in the storage.
    - Get (Mandatory) - get the Items and perform pre-process functionalities like thumbnails, Item info etc.
    - Put / Write (Mandatory) - lets you upload your Items directly to the external storage from the Dataloop platform.
    - Delete - lets you delete your Items directly from the external storage using the Dataloop platform.

    ### Create Integration With GCS
    Creating an integration with GCS ([Google Cloud Storage](https://cloud.google.com/storage)) requires having JSON file containing the GCS configuration. If you have that, you can proceed to use the code below to log in to the platform, select your active Organization, select your JSON file containing the settings and then creating the Integration.
    """


def section2():
    """
    ### Create Integration With Amazon S3
    If you want to create an Integration with Amazon S3, the process is much simpler. You only need to log in into the platform, select your active Organization and then directly create the Integration.
    """


def section3():
    """
    ### Create Integration With Azure
    Similarly with Amazon, if you want to create an Azure Integration, you just need to log in, choose your organization and then create the Integration using the `clientId` and `tenantId`.
    """


def section4():
    """
    ### External Storage Driver

    Once you have an Integration, you can set up a driver, which will add a specific bucket (and optionally with a specific path/folder) as a storage resource. The code below shows you how to do that and describes each of the required paramenters of the driver creation function.
    

    ### Create Drivers in the Platform (browser)
    """


def section5():
    """
    Once the Integration and drivers are ready, you can create a Dataloop Dataset and sync all of the data from your cloud to the Dataloop Dataset you just created.
    
    However, if you want to create a Dataset in Dataloop, you must first have a Project created. If you dont have one, you can simply use a `project = dl.projects.create(project_name='project_name')` and then `project = dl.projects.get(project_name='project_name')`.
    [Follow this link if you want to learn more about logging into Dataloop, Dataset and Project creation](https://developers.dataloop.ai/onboarding/02_login_and_project_and_dataset_creation/).
    """


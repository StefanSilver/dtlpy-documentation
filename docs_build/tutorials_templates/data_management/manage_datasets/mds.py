def section1():
    """
    # Manage Datasets

    Datasets are Buckets in the Dataloop system that hold a collection of data Items of any type, regardless of their storage location (be it Dataloop storage or external cloud storage). In this section you will learn how to manage your Datasets in Dataloop.

    ## Create Dataset

    To create a Datasets you need to have already created and selected a Dataloop Project. If you haven't done that, use the code below ([or read more here](https://developers.dataloop.ai/onboarding/02_login_and_project_and_dataset_creation/)):
    ```python
    # Remember to import dtlpy and log in to Dataloop before trying anything
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    # This will create a new Project with the name "My-First-Project". 
    project = dl.projects.create(project_name='My-First-Project')
    # If you already have a Project, you only need to select it using the line of code below:
    project = dl.projects.get(project_name='My-First-Project')
    ```
    
    
    Now that you have created and selected the a Project, you can go on to create a Dataset. There are no limits to the number of Datasets a Project can have. The same is true for data versioning where Datasets can be cloned and merged.
    The code below will create a new Dataset in the Project you selected:
    """


def section2():
    """
    ## Create Dataset With Cloud Storage Driver

    If you’ve created an [Integration and driver to your cloud storage](https://developers.dataloop.ai/tutorials/data_management/cloud_storage/create_an_external_dataset/chapter/), you can create a Dataset connected to that driver. A single integration (for example: AWS S3) can have multiple drivers (per Bucket or even per folder), so you need to specify that.
    Use the code below, and replace the `project_name`, `driver` and `dataset_name` with the ones you have:
    """


def section3():
    """

    ## Retrieve Datasets

    Once you have created one or multiple Datasets, you can all Datasets that exist as part of a particular Project, and then access (get) the Dataset you want to work on, using their ID or name:

    """


def section4():
    """

    ## Create Directory

    A Dataset can have multiple directories, allowing you to manage files by context, such as upload time, working batch, source, etc. You can see an example of creating a new directory in a Dataloop Dataset, below:
    """


def section5():
    """
    ## Deep Copy a Folder to Another Dataset

    Dataloop allows you to turn a clone of a folder into a new Dataset. However, if you want to move a folder stored in the Dataloop system (which contains files) between Datasets, you must first download the files locally and then upload them to the destination Dataset. You can see how that can be done in the following code:

    """

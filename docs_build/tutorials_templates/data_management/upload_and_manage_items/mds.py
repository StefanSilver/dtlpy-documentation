def section1():
    """
    # Upload & Manage Data & Metadata
    Data samples you upload to your Dataset will be stored as something called an Item. Items are Dataloop objects (or entities) belonging to the Dataloop Item class. They are represented as a Dataloop data model object and are stored as a binary object along with a JSON file that contains Metadata about the Item. Item JSON files also contain Metadata from Annotations, for example, that you add to further describe or classify the data sample. Each Item has a stream method to get the data sample along with other attributes, such as the Metadata, from the accompanying JSON file.
    ## Upload Specific Files

    When you have specific files you want to upload, you can upload them all into a Dataset. You can upload (multiple) single Items using the script below:
    **Note:** If you are on Windows, you will have to add an 'r' before the path to the location of the data you want to upload - if you are on Linus or Mac, that 'r' need to be removed.
    
    """


def section2():
    """


    ## Upload All Files in a Folder


    If you want to upload all files from a folder, you can do that in a similar way to uploading single Items. However, here you have to specify the folder name and the `local_path` to that folder, as you can see below:

    """


def section3():
    """

    ## Upload Items From URL Links
    You can also provide Dataloop with the link to an Item, if you choose to upload data from the web:
    """


def section4():
    """

    You can visualize an Item uploaded to Dataloop by opening it in the WebUI version of Dataloop. This will open a new tab in which the Item will be shown. To do that, use the simple line of code below:
    **Note:** The `.open_in_web()` method can be used for all kinds of Dataloop entities, such as Projects (`poject.open_in_web()`)
    """


def section5():
    """
    ## Upload Items with Metadata
    You can upload items as a table using a Pandas DataFrame that will let you upload items with info (annotations, metadata such as confidence, filename, etc.) attached to it.

    """

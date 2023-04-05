def section1():
    """
    # Working with Metadata
    Before we start working with Metadata, we need to log in. To do that, you can use a simple `dl.login()` line of code, to make sure you are logged in. After that, we must `get` the Project and the Dataset we will be working on, using the code below:
    """


def section2():
    """
    ## User Metadata
    The Dataloop's Python SDK is a a powerful tool that can be used for managing data based on your categories and information. You can add any keys and values to the User Metadata sections of Items and Annotations. Then you can use your User Metadata to Filter, Sort, and so on.    
    
    **Note**: When adding Metadata to the same Item, the new Metadata might overwrite existing Metadata. To avoid overwriting a field or the entire Metadata, use the [list](#list) data type.

    ### Metadata Data Types
    Metadata is a dictionary attribute used with Items, Annotations, and other entities of the Dataloop system (Task, Recipe, and more). As such, it can be used with string, number, boolean, list or null types. You can see examples of these types below.
    ### String
    """


def section3():
    """
    ### Number
    """


def section4():
    """
    ### Boolean
    """


def section5():
    """
    ### Null – add metadata with no information
    """


def section6():
    """
    ### List
    """


def section7():
    """
    ## Examples
    The rest of this section will give you some useful code snippets that can be used when working with Metadata.
    
    ### Add new Metadata to a list without losing existing data
    """


def section8():
    """
    ### Add Metadata to an Item's User Metadata
    """


def section9():
    """
    **Note**: An Item in Dataloop's platform should have section 'user' in its Metadata, with the field 'MyKey' and the value 'MyValue'.

    ### Add Metadata to Annotations' User Metadata
    """


def section10():
    """
    An Annotation in Dataloop's platform should have the section 'user' in Metadata with field 'red' and value True.

    ## How to Filter Items by User Metadata
    ### 1. Get your dataset
    """


def section11():
    """
    ### 2. Add Metadata to an Item
    **Note:** You can also <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.md/" target="_blank">add metadata to filtered items</a>.
    """


def section12():
    """
    #### 3. Create a Filter
    """


def section13():
    """
    #### 4. Filter by your written key
    """


def section14():
    """
    #### 5. Get filtered Items
    """


def section15():
    """

    ### Modify an existing user Metadata field 
    """

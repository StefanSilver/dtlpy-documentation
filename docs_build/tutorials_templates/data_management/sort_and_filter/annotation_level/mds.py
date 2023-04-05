def section1():
    """
    # Annotation level Filters
    ## The Dataloop Query Language - DQL
    Using The <a href="https://dataloop.ai/docs/api-dql" target="_blank">Dataloop Query Language</a>, you may navigate through massive amounts of data. The Dataloop platform gives you different capabilities to organize your data in Datasets, folders, and versioning systems, you still need the ability to query your data. This is where our Dataloop Query Language becomes useful. When using the DQL in the SDK, additional fields such as Sort, Page, and pageSize can be defined to sort the data that is returned from the Query. Every DQL query has the following components:
    - Resource - The target Resource for the Query; the Resource can be Items or Annotations.
    - Filter - The Filter includes Attributes and logical operators to filter Items or Annotations.

    
    ## Filters
    Filters are part of the Dataset and Task Browsers, enabling you to Filter Items based on every aspect of your files. When multiple Filters are used, the relationship between them will be the AND logical operator. However, the relationship between multiple values in each Filter will be the OR logical operator.
    By using Filters, you can filter Items and get a generator of the filtered Items. The Filter entity is used to build such Filters.
    To access the filters entity click <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters" target="_blank">here</a>.
    
    ### Filters - Field & Value
    Filter your Items or Annotations using the parameters in the JSON code that represent its data within our system. Access your annotation JSON using `to_json()`.
    A **Filter Field** refers to the attributes you filter by. For example, "dir" would be used if you wish to filter Item Annotations by their folder/directory.
    
    A **Filter Value** refers to the input by which you want to filter. For example, "/new_folder" can be the directory/folder name where the Item Annotations you wish to filter are located.
    
    ### Sort - Field & Value
    A **Sort Field** refers to the field you sort your Annotations list by. For example, if you sort by filename, you will get the Item list sorted in alphabetical order by filename.
    
    You can see the full list of the available fields <a href="https://dataloop.ai/docs/api-dql" target="_blank">here</a>.
    A **Sort Value** refers to the list's order direction, which can be either ascending or descending.
    
    ### Filtering Annotations
    You can filter Annotations by the Annotations' JSON fields.
    
    In the example below, you will get all of the Annotations in the Dataset sorted by the Label.
    """


def section2():
    """
    ### Filter Annotations by the Annotations' Item
    The 'add_join' function can be used to filter Annotations based on the JSON fields of the Annotation's Items. For example, you can Filter only Box Annotations from image Items.
   
    **Note:** See all of the Items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.
    """


def section3():
    """
    ### Filters Method - "OR" and "AND"
    **Note:** For more advanced Filters operators visit the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md" target="_blank">Advanced SDK Filters</a> page.</div>
    
    If you wish to filter Annotations with the "AND" logical operator, you can do so by specifying which Filters will be checked with "AND".
    **Note:** AND is the default value and can be used without specifying the method.
    In the example below, you will get a list of Annotations in the Dataset of the type <b>box</b> and Label <b>car</b>.
    """


def section4():
    """
    ### Or
    If you wish to Filter Annotations with the "OR" logical operator, you can do so by specifying which Filters will be checked with "OR".
    
    In the example below, you will get a list of the Dataset's Annotations that are either a 'box' or a 'point' type.
    """


def section5():
    """
    ### Delete Filtered Items 
    In the example below, you will delete Annotations that were created on 30/8/2020 at 8:17 AM. A Filter will be used that will search for all Annotations that were made at that date and time.
    """


def section6():
    """
    ## Annotation Filtering Fields
    ### More Filter Options
    
    You can use a `.` (dot) to access the parameters within curly brackets. For example you can use `field='metadata.system.status'` to Filter by the Annotation's status.
    """


def section7():
    """
    ### Filter Annotations by their Label
    In the code below, you can see how Annotations can be Filtered using a particular Label. All you have to do is to change `your_label_value` with the Label you want to search for.
    """


def section8():
    """
    ## Advanced Filtering Operators
    If you want to explore advanced filtering options you can do so on <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md" target="_blank">this page</a>.
    """

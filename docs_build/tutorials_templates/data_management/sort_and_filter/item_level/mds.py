def section1():
    """
    # Item Level Filters
    ## Filters
    Using filters, you can filter Items and get a generator of the filtered Items. The Filter entity is used to build such filters.

    ### Filters - Field & Value
    You can filter your annotations using the parameters in the JSON code that represent its data within our system. You can also access your item's JSON using <code>to_json()</code>.

    A **Filter Field** refers to the attributes you filter by. For example, "dir" would be used if you wish to filter Items by their folder/directory.


    A **Filter Value** refers to the input by which you want to filter. For example, "/new_folder" can be the directory or folder name where the Items you wish to filter are located.
    ### Sort - Field & Value

    A **Sort Field** refers to the field you sort your Items/Annotations list by. For example, if you sort by filename, you will get the Item list sorted in alphabetical order by filename.
    **Note:** See the full list of the available fields <a href="https://dataloop.ai/docs/api-dql" target="_blank">here</a>.

    A **Sort Value** refers to the list's order direction, which cane be either ascending or descending.

    ### Filtering Items
    You can Filter Items by the Item's JSON fields. In the example below, you will get all Annotated Items from a Dataset sorted by the filename.

    **Note:** See all of the Items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.

    """


def section2():
    """
    ### Filter Items using their Annotations
    The `add_join` can be used to filter Items by the JSON fields of the Items' Annotation. For example, it could Filter only Items with 'box' Annotations.

    **Note:** See all of the Items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.

    """


def section3():
    """
    ### Filters Method - "Or" and "And"

    **Note:** For more advanced Filter Operators visit the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md" target="_blank">Advanced Python SDK Filters</a> page.</div>
    

    If you wish to filter Annotations with the "AND" logical operator, you can do so by specifying which filters will be checked with "AND".
    
    **Note:** The 'AND' is the default value and can be used without specifying the method.
    In the example below, you will get a list of Annotated Items with <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/working_with_metadata/chapter.md" target="_blank">user Metadata</a> of the field `is_automated` and the value `True`.

    """


def section4():
    """

    If you wish to filter annotations with the "OR" logical operator, you can do so by specifying which filters will be checked with "OR".
    In the example below, you will get a list of Items that are either on "folder1" or "folder2" directories.

    """


def section5():
    """
    ### Update The User Metadata of Filtered Items
    To update filtered Items - The `update_value` must be a dictionary. The dictionary will only update User Metadata. To understand more about user Metadata <a href=https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/working_with_metadata/chapter.md/" target="_blank">click this link</a>.
    
    In the example below, you will update/add user Metadata (with the field "BlackDogs" and value True), to Items in a specific folder 'dogs' with an attribute 'black'.

    """


def section6():
    """
    ### Delete Filtered Items 
    Sometimes, you may want to remove the items that were updated in a specific time-frame. In the example below, you will delete all Items that were created on 30/8/2020 at 8:17 AM.

    """


def section7():
    """
    ### More Filter Options
    You can Use a `.` (dot) to access parameters within curly brackets. For example, you could use `field='metadata.system.originalname'` to filter by the Item's original name.</div>

    """


def section8():
    """
    ### More Examples
    The example below shows you how to filter Items by their Annotations Label.

    """


def section9():
    """
    The example below shows you how to filter Items by the `completed` and `approved` status.
    """


def section10():
    """
    The example below shows you how to filter Items by the `completed` status (with Items That are approved as well).
    """


def section11():
    """
    The example below shows you how to filter Items only by completed status.
    """


def section12():
    """
    The example below shows you how to filter unassigned Items.
    """


def section13():
    """
    The example below shows you how to filter Items by a specific folder.
    """


def section14():
    """
    The example below shows you how to Get all Items named `foo.bar`.
    """


def section15():
    """
    The example below shows you how to Sort files of size 0-5 MB by name, in ascending order.
    """


def section16():
    """
    The example below shows you how to Sort with multiple fields - Sort Items by Labels in ascending order and by `createdAt` in descending order.
    """


def section17():
    """
    ### Advanced Filtering Operators
    You can explore more advanced filtering options on <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md/" target="_blank">this page</a>.

    ### Response to DQL Query
    A typical response to a DQL query will look like the following:
    """

def section18():
    """
    ### Using Custom DQL Filter
    If you have a DQL JSON copied from the platform you can create an Filter directly in the SDK with it, using the "custom_filter" attribute:
    """

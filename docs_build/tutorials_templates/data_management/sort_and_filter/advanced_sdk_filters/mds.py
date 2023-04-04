def section1():
    """
    # Advanced Filters in the Python SDK
    Filters are part of the Dataset and Task Browsers, enabling you to Filter Items based on every aspect of your files. When multiple Filters are used, the relationship between them will be the AND logical operator. However, the relationship between multiple values in each Filter will be the OR logical operator. For example, entering "dog" and "cat" in the Labels Filter will result in all Items that have a "dog" Label OR a "cat" Label.
    Here are some resources that will help you learn more about Filters:
    - [Beginner Filter Onboarding](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/04_metadata_querying_and_filtering.md).
    - [Dataloop's Query Language Documentation](https://dataloop.ai/docs/api-dql).
    - [General Filters Documenation](https://dataloop.ai/docs/sort-filter).
    - [DQL Tutorial](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/)
    
    ## Filter Operators

    When adding a Filter, There are several operators you could use. In this section, we will explore the most important ones and provide what you can

    The **Equal** or `eq` Operator (dl.FiltersOperation.EQUAL) filters for items that are equal to the parameter you filter by.
    

    In the example below, we Filter Items from a specific folder directory.
    """


def section2():
    """
    The ***Not Equal*** or `ne` Operator (dl.FiltersOperation.NOT_EQUAL)
    ne -> not equal
    

    In the example below, you will get all Items that do have ONLY a 'cat' Label.
    **Note:** This Operator is a better fit for filters of a single value.
    """


def section3():
    """
    The ***Greater Than*** Operator or `gt` (dl.FiltersOperation.GREATER_THAN) searches for Items that are above the given threshold you set.


    In the example below, the script gets all Items with a greater height (in pixels) than the given threshold value.
    """


def section4():
    """
    The ***Less Than*** Operator or `lt` (dl.FiltersOperation.LESS_THAN) is the oposite of the Greater Than Operator, meaning that it will search for Items that are below a given threshold value.


   In the example below, the script gets all Items with a width (in pixels) that isless than the given threshold value.
    """


def section5():
    """
    The ***In a List*** Operator or `in`(dl.FiltersOperation.IN), is a `list` type, where you can provide multiple Labels or other parameters that the Filter will look for.

    In the example below, the script will get all Items with the dog OR cat Labels.
    """


def section6():
    """
    ### SDK defaults
    Filters ignore SDK defaults like hidden Items and directories or note Annotations as issues. If you wish to change this behavior, you can use the following script:
    """


def section7():
    """
    ### Hidden Items and Directories
    If you wish to only show hidden Items & directories in your Filters use this code:
    """


def section8():
    """
    ### Delete a Filter
    Sometimes you may wish to delete a Filter that is stored in Dataloop. To do that, use the script below.
    """


def section9():
    """
    ## Other Examples
    ### Filter forItems that were created between specific dates
    In this example, you will get all of the Items that were created in 2018. You can adapt it to your needs, so you can Filter for Items created between any dates you wish.
    """


def section10():
    """
    ### Filter for Items that don't have a specific Label
    In this example, you will get all Items that **do not have** a 'cat' Label attached to them.
    """

def section11():
    """
    #### Exist
    The filter param FILTERS_OPERATIONS_EXISTS checks if an attribute exists. The following example checks if there is an Item with user Metadata:
    """

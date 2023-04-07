def section1():
    """
    # Advanced Tutorials
    This section will provide more advanced scripts that can be used in Dataloop to perform different processes on image Annotations.
    ## Copy Annotations Between Items
    We can copy Annotations between Items by setting the Annotations entity from one Item and uploading it to another. Running a Filter through all Items allows us to copy from one Item into multiple Items, such as video snapshots with the same object.
    """


def section2():
    """
    ## Show Images & Annotations
    This code downloads an image and its Annotations from a Dataset, displays the Annotations and the image separately, and then displays the Annotated image with the Annotations pasted onto it.
    **Note:** This script uses  Pillow and CV2, please make sure they are installed (`pip install opencv-python` and `pip install --upgrade Pillow`).

    """


def section3():
    """
    ## Show Annotations from JSON file (Dataloop format)
    This code reads Annotation data from a JSON file in Dataloop format, generates an image mask for each Annotation, and displays the mask image for visualization purposes.
    **Note:** Directory paths look different in MacOS and Linux when compared to Windows. MacOS and Linux don'trequire "r" at the beginning of the filepath.


    """


def section4():
    """
    ## Count total number of annotations
    The following script counts the number of Annotations with a Filter. The Filter can be set to any context - Dataset, folder or other criteria. In the following example, it is set to a Dataset.
    """


def section5():
    """
    ## Parenting Annotations

    Parenting establishes a relation between 2 annotations, executed by setting the parent_id parameter. The Dataloop system will reject an attempt to set circular parenting.
    The following script demonstrate setting parenting relation while uploading/creating annotations


    """


def section6():
    """

    The following script demonstrate setting parenting relation on existing annotations:
    """


def section7():
    """

    ## Change Annotations’ Label
    The following example creates a new label in the recipe (an optional step, you can also use an existing label), then applies it to all annotations in a certain filter.

    """

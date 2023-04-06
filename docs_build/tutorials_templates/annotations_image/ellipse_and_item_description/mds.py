def section1():
    """
    # Ellipse and Item Description
    Ellipse and Item Description are both concepts related to computer vision and image processing.

    An Ellipse is a geometric shape that is characterized by its center point, two radii (major and minor), and an orientation angle. In computer vision and image processing, ellipses can be used to represent objects in an image or to define regions of interest.

    Ellipse Annotations can be used to annotate objects that have an elliptical shape, such as eyes, wheels, or plates. In computer vision applications, ellipse Annotations can be used for object detection, tracking, and segmentation.

    Item description, on the other hand, refers to the Metadata or information associated with an Item. For example, in the case of image or video, Item description can include Metadata information such as the date the image was taken, the location, the camera settings, and any additional details or context that may be relevant. Item descriptions can be used to organize and categorize Items, and can also provide useful information for machine learning and computer vision algorithms.
    
    This section will teach you how to create Elipse Annotations and how to add Item Descriptions in Dataloop, using the Python SDK.
    
    ## Create Ellipse Annotation
    This code uploads an Ellipse Annotation to an image Item. First, the code retrieves the image to which the Annotation will be added. Then, it creates an instance of an Annotation builder, which is used to construct the Annotation object.

    Next, the code adds an Ellipse Annotation to the builder instance. The Ellipse Annotation is defined by specifying the center coordinates (x and y), radii (rx and ry), and the rotation angle. The Label is also added to the Annotation.

    Finally, the code uploads the Ellipse Annotation on to the image Item, on the platform, using the `item.annotations.upload` method.

    """


def section2():
    """
    ## Item Description

    The Item Description is added as a “system Annotation”, and serves as a way to save information about the Item, that can be seen by anyone accessing it.
    
    The code below retrieves an Item from a Dataset on a platform and then adds the description of the Item. If the text provided is an empty string, it will remove the existing description from the Item.

    """

def section1():
    """
    # Bounding Box and Cuboid
    Bounding Box and Cuboid are both geometric shapes that are commonly used in computer graphics, computer vision, and machine learning.

    A bounding box is a rectangular shape that is used to enclose an object or a region of interest in an image or a video frame. The bounding box is defined by its top-left corner coordinates (x, y) and its width and height (w, h). The bounding box is often used to represent the location and size of an object in an image, and it is a common input format for object detection and object tracking algorithms.

    A cuboid, on the other hand, is a three-dimensional shape that is similar to a box, but with rectangular faces on all six sides. A cuboid is defined by its length, width, and height, and it is used to represent the shape and size of three-dimensional objects. Cuboids are often used in computer graphics to represent 3D models of objects and scenes.

    In computer vision and machine learning, both bounding boxes and cuboids are used to represent objects and regions of interest in images and videos. Bounding boxes are used more frequently for 2D object detection and tracking, while cuboids are used for 3D object detection and tracking in 3D space.
    
    This section will teach you how to use Bounding Boxes and Cuboids in Dataloop's Python SDK.
    
    ## Create Box Annotation
    This code example retrieves an image from a Dataset, creates a Bounding Box Annotation with a specified Label, and uploads the Annotation to the retrieved image Item.

    """


def section2():
    """
    ## Create a Rotated Bounding Box Annotation
    The Rotated Bounding Box Annotation is a way to represent objects in images using boxes that are oriented at an angle relative to the image's horizontal axis. This is useful for irregular or angled objects. It involves specifying four corner points and the angle of rotation, and can improve the accuracy of computer vision models in object detection and recognition Tasks.
    
    A rotated box is created in the code below, by setting its top-left and bottom-right coordinates, and providing its rotation angle.


    """


def section3():
    """
    ## Convert Semantic Segmentation to Bounding Box
    Converting Semantic Segmentation to Bounding Boxes typically involves identifying the pixels that belong to each object class and then determining the smallest possible bounding box that encloses all those pixels. This approach can help to localize objects within the image and provide a compact representation of their spatial extent. 
    
    The code below shows you how to convert all Semantic Segmentation Annotations in an Item into a Box Annotation in Dataloop.

    """


def section4():
    """
    ## Create Cuboid (3D Box) Annotation
    Cuboid (3D Box) Annotation is a way to annotate objects in 3D space, commonly used in computer vision and autonomous driving. A 3D cuboid, which is a box-like structure with length, width, and height dimensions, is used to represent the object. This technique requires determining the position, orientation, and size of the object using 3D sensing technologies and drawing the cuboid around the object. This approach provides more detailed information for computer vision models to better understand the environment. 
    
    The code below shows you how to create a cuboid Annotation in two different ways.

    """

def section1():
    """
    # Polygon and Polyline
    Polygon and Polyline are two types of geometric shapes used in computer vision and image processing.

    A polygon is a closed shape defined by a set of vertices or points connected by straight line segments. It is commonly used to represent the boundary or outline of an object in an image. In image annotation, a polygon is often used to define the region of interest (ROI) or the shape of an object that needs to be detected, segmented or classified.

    A Polyline is a sequence of connected line segments defined by a set of vertices or points. It is commonly used to represent a curve or a path in an image or a video. In image annotation, a polyline is often used to define the trajectory or movement of an object, such as a vehicle or a pedestrian.

    Both Polygon and Polyline annotations provide more detailed information about the shape and location of objects in an image than simple bounding boxes. They are useful for applications such as object detection, tracking, and segmentation in computer vision and image analysis. However, annotating polygons and polylines can be a more challenging task compared to other annotation techniques due to the need for accurate point placement and the complexity of the shapes.
    
    This section will teach you how to use both of the in Dataloop's Python SDK.
    
    ## Create Single Polygon/Polyline Annotation
    The code below demonstrates how to create and upload Polygon and Polyline Annotations for an image on the Dataloop platform.
    """


def section2():
    """
    ## Create Multiple Polygons from Mask
    The code below retrieves the Annotations of an image from the platform, selects the first annotation in the list, and creates a new Annotation builder object. 
    
    Then, it uses the `dl.Polygon.from_segmentation` method to convert the segmentation points of the first Annotation to a Polygon Annotation from a mask, with a maximum of 2 instances and the same Label as the original Annotation. Finally, it uploads the new Polygon Annotation to the image Item in Dataloop's platform.
    """


def section3():
    """
    ## Convert Mask Annotations to Polygon
    Converting Mask Annotations to Polygon is a computer vision technique that transforms binary mask annotations of an object into polygon annotations. Binary mask annotations indicate which pixels in an image belong to the object, creating a binary image of its shape and location.
    Find out more about the `from_segmentation()` function [at this link](https://console.dataloop.ai/sdk-docs/dtlpy.entities.annotation_definitions.html#dtlpy.entities.annotation_definitions.polygon.Polygon.from_segmentation).
    """


def section4():
    """
    ## Convert Polygon Annotation to Mask
    onverting Polygon Annotation to Mask is the opposite of Converting Mask Annotation to Polygon. It's a technique in computer vision that converts the Polygon Annotations of an object into binary mask Annotations. To create a binary mask annotation, the interior of the polygon is filled with a specific color, while the rest of the image is assigned a different color. This can be automated using algorithms like rasterization or winding number, or done manually by an Annotator. The resulting binary mask Annotations can be used for object segmentation and classification in computer vision models.
    Find out more about `from_polygon()` function [at this link](https://console.dataloop.ai/sdk-docs/dtlpy.entities.annotation_definitions.html#dtlpy.entities.annotation_definitions.segmentation.Segmentation.from_polygon).
    
    The script below uses the CV2 module to convert from Polygon to Mask Annotation, please use [this page to install CV2](https://pypi.org/project/opencv-python/).

    """

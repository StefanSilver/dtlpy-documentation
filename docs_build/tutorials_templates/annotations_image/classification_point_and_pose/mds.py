def section1():
    """
    # Classification Point and Pose
    Classification point and pose are two related concepts in computer vision and image processing, specifically in the area of human pose estimation.

    A classification point, also known as a key point or landmark, is a specific point on a person's body, such as the shoulder or elbow, that can be identified and located using computer vision algorithms. These points are often used as reference points to estimate the position and orientation of the human body.

    Pose, on the other hand, refers to the overall configuration of the body, including the position and orientation of the limbs and the torso. In human pose estimation, the goal is to determine the pose of a person from a given image or video sequence. This can involve detecting the location of the key points on the body and using this information to infer the overall pose.

    Classification points and pose estimation are important in a variety of applications, such as motion capture for animation and gaming, human-robot interaction, and action recognition in video surveillance. They are also used in medical imaging to analyze human movement and diagnose musculoskeletal disorders.
    
    In this section of the tutorial, you will learn how to use Classification Point and Pose in Dataloop's Python SDK.
    ## Classification

    To classify a single Item, you must first get the items you want to classify and use a builder. You can see that below.

    """


def section2():
    """
    ## Classify Multiple Items

    Classifying multiple Items requires using an Items entity with a Filter.
    """


def section3():
    """
    ## Create a Point Annotation
    Once the Items that need to be Point Classified are selected, you can create a Point Annotation, as seen below.
    """


def section4():
    """
    ## Pose Annotation
    Pose Annotations are a collection of points that follows a certain template, for example a 'skeleton' for tracking key-point on the people that are present in image or video Items. Templates are created in the Dataloop platform, at the instructions settings of a Recipe. The code below shows how you can create Pose Annotations in Dataloop's Python SDK.
    """

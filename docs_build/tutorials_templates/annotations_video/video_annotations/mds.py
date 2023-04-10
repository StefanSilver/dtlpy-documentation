def section1():
    """
    # Video Annotations
    or annotating video data with metadata that can be used to train and improve deep learning models. Video annotations are critical for many applications of deep learning, such as object detection, action recognition, and scene understanding.

    One common method of video annotation in deep learning is to use bounding boxes to identify objects within the video frames. For example, if the goal is to train a deep learning model to recognize cars in video footage, annotators would manually draw bounding boxes around the cars in each frame of the video. These annotations can then be used to train a deep learning model to recognize cars and classify them correctly.

    Other types of video annotations used in deep learning include segmentation, where each pixel in a video frame is labeled with a corresponding object or region, and keypoint annotation, where specific points on an object or person within the video are labeled.

    The accuracy and quality of video annotations are critical to the success of deep learning models trained on video data. In recent years, there has been a growing interest in developing automated video annotation techniques that can reduce the need for manual annotation and improve the efficiency and scalability of deep learning applications.
    
    In this tutorial we will create and upload Annotations into a video Item. Video Annotations differ from image Annotations since they span over multiple frames.
    **Note:** The scripts in this tutorial use the CV2 module, please <a href="https://pypi.org/project/opencv-python/" target="_blank">usethis page to install it</a>.

    ## Setup
    Before you start doing anything using the Dataloop Python SDK, please make sure to have the `dylpy` package installed, to log in into the Dataloop platform and import your Project and Dataset. Then you will need to import a video file on which you can use the scripts below.
    """


def section2():
    """
    ## Create A Single annotation
    This code creates a single neewnnotation object for a video item, spans the annotation over 100 frames, and adds a box to each frame with specific coordinates and a label. Finally, it uploads the annotation to a platform.
    Create a  Annotation for a video Item and upload it

    """


def section3():
    """
    ## Adding Multiple Annotations Using Annotation Builder

    The following scripts demonstrate adding 10 annotations into each frame

    """


def section4():
    """
    ## Read Frames of an Annotation
    The following example reads all the frames an annotation exist in, e.g. the frame range an annotation spans over.

    """


def section5():
    """
    ## Create Frame Snapshots from Video

    One of Dataloop video utilities enables creating a frame snapshot from a video item every X frames (frame_interval).
    You will need FFmpeg needs to be installed on your system using <a href="https://ffmpeg.org/download.html" target="_blank">this official website</a>.

    """


def section6():
    """

    ## Play An Item In Video Player
    Play a video item with its annotations and labels with a video player

    """


def section7():
    """

    ## Show Annotations in a Specified Frame

    """

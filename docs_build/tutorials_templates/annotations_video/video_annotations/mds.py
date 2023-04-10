def section1():
    """
    # Video Annotations
    In the context of deep learning, video annotations refer to the process of manually labeling or annotating video data with metadata that can be used to train and improve deep learning models. Video annotations are critical for many applications of deep learning, such as object detection, action recognition, and scene understanding.

    One common method of video annotation in deep learning is to use bounding boxes to identify objects within the video frames. For example, if the goal is to train a deep learning model to recognize cars in video footage, annotators would manually draw bounding boxes around the cars in each frame of the video. These annotations can then be used to train a deep learning model to recognize cars and classify them correctly.

    Other types of video annotations used in deep learning include segmentation, where each pixel in a video frame is labeled with a corresponding object or region, and keypoint annotation, where specific points on an object or person within the video are labeled.

    The accuracy and quality of video annotations are critical to the success of deep learning models trained on video data, so Dataloop also offers the tools necessary to annotate video data. 
    
    In this tutorial we will create and upload Annotations into a video Item. Video Annotations differ from image Annotations since they span over multiple frames.
    **Note:** The scripts in this tutorial use the CV2 module, please <a href="https://pypi.org/project/opencv-python/" target="_blank">usethis page to install it</a>.

    ## Setup
    Before you start doing anything using the Dataloop Python SDK, please make sure to have the `dylpy` package installed, to log in into the Dataloop platform and import your Project and Dataset. Then you will need to import a video file on which you can use the scripts below.
    """


def section2():
    """
    ## Create A Single annotation
    This code creates a single new Annotation object for the video Item, spans the Annotation over 100 frames, and adds a box to each frame with specific coordinates and an attached Label. Finally, it uploads the Annotation to the Dataloop platform.


    """


def section3():
    """
    ## Adding Multiple Annotations Using Annotation Builder
    This code creates a new Annotation builder for a video Item, and spans the Annotation over 100 frames, and adds 10 box Annotations to each frame with specific coordinates and a Label. The `object_id` parameter is used to connect the Annotations of each object in different frames. Finally, it uploads the Annotations to the platform on the spicific video Item it was used on.
    The following scripts demonstrate adding 10 annotations into each frame

    """


def section4():
    """
    ## Read Frames of an Annotation
    The code below reads all the frames an Annotation exist in, e.g. the frame range an Annotation spans over. It also prints the bounding box coordinates of the Annotation in each frame.
    """


def section5():
    """
    ## Create Frame Snapshots from Video

    One of Dataloop's video utilities enables creating a frame snapshot from a video Item every `x` frames (`frame_interval`). You need [FFmpeg](https://ffmpeg.org/) to be installed on your system.

    """


def section6():
    """

    ## Play An Item In Video Player
    Using the code below, you can play a video Item with its attached Annotations and Labels in a video player.

    """


def section7():
    """

    ## Show Annotations in a Specified Frame
    This code imports the `matplotlib` Python library for plotting and visualization purposes. It then retrieves a list of Annotations for the video Item from the platform and selects the Annotations for a specific frame (number 55). It plots the bounding boxes of the Annotations on top of the corresponding frame using the `imshow()` method from matplotlib. Finally, it uses the `video_player()` method from the Dataloop platform to play the video.
    """

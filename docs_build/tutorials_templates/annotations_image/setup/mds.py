def section1():
    """
    # Setup
    
    This tutorial will guide you through the process using the Dataloop Python SDK to create and upload Annotations into Items. It includes chapters that teaches you how to use different tools. The last chapter includes various more advanced scripts.
    
    Here is the list of all that's encompassed in this tutorial section:
    - [Classification Point & Pose](../classification_point_and_pose/chapter.md)
    - [Bounding Box & Cuboid](../bounding_box_and_cuboid/chapter.md)
    - [Polygon & Polyline](../polygon_and_polyline/chapter.md)
    - [Ellipse & Item-Description](../ellipse_and_item_description/chapter.md)
    - [Advanced Tutorials](../advance_tutorials/chapter.md)
        - [Copy Annotations Between Items](../advance_tutorials/chapter.md#copy-annotations-between-items)
        - [Show Images & Annotations](../advance_tutorials/chapter.md#show-images--annotations)
        - [Show Annotations from JSON file](../advance_tutorials/chapter.md#show-annotations-from-json-file-dataloop-format)
        - [Count the Total Number of Annotations in a Dataset](../advance_tutorials/chapter.md#count-total-number-of-annotations)
        - [Parenting Annotations](../advance_tutorials/chapter.md#parenting-annotations)
        - [Change Annotation's Label to a New Label](../advance_tutorials/chapter.md#change-annotations-label)

    Before trying to run any of the scripts in this tutorial, remember that you must Log In to Dataloop, and select the Project and Dataset you will be working on. If you don't have a Project and Dataset created, [find out how to do that here](https://developers.dataloop.ai/onboarding/02_login_and_project_and_dataset_creation/). The code below shows you how to import Dataloop's Python SDK package (`dtlpy`), and how to `get` the Project and Dataset you will be working on, if you already have them created.
    

    """


def section2():
    """
    ## Initiation
    Using the Annotation definition classes you can create, edit, view and upload platform Annotations. Each Annotation's `init` receives the coordinates for the specific type, Label, and other optional attributes.

    ## Optional Plotting
    Before updating Items with Annotations, you can optionally plot the Annotation you created and review it before uploading it. This applies to all Annotations described in the next section.

    """

def section1():
    """
    # Upload & Manage Annotations
    Dataset Items are annotated using Labels. A Label is composed of various Label Settings and Instructions that are defined by a Dataset’s Recipe. For example, an Item can contain 1 Label defined as a Classification, to categorize the entire data sample. It can also contain multiple Annotation Labels covering only parts of your data sample to identify specific sections of that Item. For example, if the Item contains cats and dogs, you might find a label for Cat and a label for Dog in the Recipe.
    
    If you want to read more about Annotations, [consult our Annotation Documentation](https://dataloop.ai/docs/classify-item).
    
    Classification is used to categorize an entire data sample. For example, a Classification label can be used to classify product images under categories, subcategories, and characteristics, such as men’s clothes, polo shirts, hand cremes, etc.

    The Python SDK can add Classification Labels to an item using 2 steps:
    - Firstly, you need to add a Classification Label to be a part of the Dataset's Recipe (create Label).
    - Then, add that Label to the Item you wish to classify.
    
    In the code example below, you can see how you can get an Item from the platform in a variable, and then get the Annotations of that Item. Using the `annotation_id='<id>' gets only 1 specific Annotation; deleting that parameter will get all of the Annotations of that Item.
    
    """


def section2():
    """
    ## Upload User Metadata
    To upload Annotations from JSON and also include the user Metadata, you can add the parameter local_annotation_path to the dataset.items.upload function, like in the code below: 
    """


def section3():
    """
    ## Convert Annotations To COCO Format
    The [COCO dataset](https://cocodataset.org/#home) uses a JSON format that contains information about each dataset and all of the images contained within it, such as image licenses, categories used to classify objects in the images, raw image data such as pixel size, and the all-important annotations of objects in the images.
    
    If you want to convert your Annotations to COCO format, you can use the code below:
    """


def section4():
    """
    ## Upload  Directory  Annotations
    Sometimes you may want to upload an entire Directory and the Corresponding Dataloop JSON Annotations of the Items into the platform. To do that, simply adapt the code below to your needs:
    
    """


def section5():
    """
    ## Upload Annotations To Video Item
    Uploading Annotations to video Items needs to consider the spanning between frames, and toggling the visibility (occlusion). In this example, we will use a CSV file. In this file there is a single 'person' Box Annotation that begins on frame number 20, disappears on frame number 41, reappears on frame number 51 and ends on frame number 90.

    [Click here to Download the video_annotations_example.CSV file](https://cdn.document360.io/53f32fe9-1937-4652-8526-90c1bc78d3f8/Images/Documentation/video_annotation_example.csv). 
    If you want to upload your own Annotation to video Items, you can use the code below, and adapt it to your needs:
    """


def section5a():
    """
    ## Upload Annotations In VTT Format
    The Dataloop builder also supports [VTT files](https://fileinfo.com/extension/vtt), for uploading Web Text Tracks for video transcription. Using the code below you can upload Annotations in having the VTT format to Dataloop:

    """


def section5b():
    """
    ## Upload Audio Annotation to an Audio File
    Dataloop offers an Audio Studio that supports both Classification and text transcription operations. These operations enable Annotators to annotate audio files quickly on one hand and for various needs on the other. [Read more about Audio Studio here](https://dataloop.ai/docs/audio-guide).
    To upload Audio Annotations to an Audio File, you can use the code below:
    
    """


def section6():
    """
    ## Set Attributes On Annotations
    
    You can set attributes on Annotations in the platform using Dataloop's Python SDK. Since Dataloop deprecated a legacy attributes mechanism, attributes are refered to as version '2.0' and need to be set as such first (you can see this in the first line of code, below). In this code snippet, you can see how you can set the attribute of an Annotation, using the Annotation's ID:
    
    
    ## Free Text Attribute
    """


def section7():
    """
    Here are some other types of attributes you can set on your Annotations:
    #### Range Attributes (Slider in UI)

    """


def section8():
    """
    #### CheckBox Attribute (Multiple choice)
    """


def section9():
    """
    #### Radio Button Attribute (Single Choice)
    """


def section10():
    """
    #### Yes/No Attribute
    """


def section11():
    """
    ## Show Annotations Over Image
    After uploading Items and Annotations with their Metadata, you might want to see some of them so you can perform visual validation. 
    
    To see only the Annotations, use the Annotation type `show` option.

    """


def section12():
    """

    To see the Item itself with all of its Annotations, use the Annotation option.

    """


def section13():
    """

    ## Download Data, Annotations & Metadata
    The Item ID for a specific file can be found in the platform's Web UI. Click BROWSE for a Dataset, double click the Dataset you want, then click on the selected Item you want to see the details for. The file information will be displayed in the right-side panel. The Item ID is detailed, and can be copied in a single click.
    
    ## Download Items and Annotations
    You can download a Dataset's Items and Annotations to your computer, in two separate folders. To do that, list the download Annotation option using `dl.ViewAnnotationOptions`:
    1. JSON: Download json files with the Dataloop Annotation format.
    2. MASK: Save a PNG Image file with the RGB Annotation drawn.
    3. INSTANCE: Saves a PNG with the Annotation Label ID as the pixel value.
    4. ANNOTATION_ON_IMAGE: Saves a PNG with the Annotation drawn on top of the image.
    5. VTT: Save `subtitle` Annotation type in a VTT format.
    6. OBJECT_ID: Save a PNG with the object ID as the pixel value.

    """


def section14():
    """
    **Note**: The Annotation option can also be a list to download multiple options, as seen below:

    """


def section15():
    """

    ## Filter by Item and/or Annotation
    * **Items Filter** - allows you to download filtered Items based on various parameters (e.g. their directory). You can also download Items based on multiple different Filters. Learn more [about Item Filters here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.md/).
    * **Annotation Filter** - download filtered Annotations based on multiple parameters (e.g. their Label). You can also download Items Annotations based on different Filters, learn all [about Annotation Filters here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/). 
    
    **Note: **The example below will download Items and JSONS from a dog folder of the Label 'dog'.


    """


def section16():
    """

    ## Filter by Annotations
    * **Annotation filter** - download filtered Annotations based on multiple parameters like their Label. You can also download Items Annotations based on different Filters, learn all about Annotation Filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/).


    """


def section17():
    """

    ## Download Annotations in COCO/YOLO/VOC Format

    The example  below will show you how to download Annotations in COCO format, from the dog items folder using the Label Filter 'dog'. If you want to download in the other formats, simply uncomment the format you want in the script (while commenting the others), to change between YOLO/VOC/COCO formats.


    """


def section18():
    """

    ## Exporting Files with File Extension as Part of the Filename

    Files can be exported from a dataset with their file extension as part of the exported filename. The `export_version` parameter in `dataset.download` can be set to `ExportVersion.V1` or `ExportVersion.V2` to avoid duplication of files with different extensions. This allows Items with the same filename and different extensions in the Dataset to be saved as different Items.
    * **Old functionality (V1)** – `abc.jpg` → Annotations are saved as `abc.png` and the JSON is saved as an `abc.json`  file.
    * **New functionality (V2)** – `abc.jpg` → Annotations are saved as `abc.jpg.png` and JSON is saved as an `abc.jpg.json` file.

    """


def section19():
    """

    ## Download NdArray with Numpy

    - Only Images that have `.jpg` or `.png` formats are supported.
    - `save_localy=False` means it returns a buffer.
    - `to_arraymeans` it returns the buffer as an array.

    """

def func1():
    """
    # Dataloop dataloader
    For the purpose of training and visualizing data Items, a generator for images and Annotations in the form of `dl.Dataset` can be employed. Data visualization can be carried out with the aid of augmentation techniques to facilitate debugging and exploration. Once this has been accomplished, the data generator can be used as an input to the training functions.
    """


def func2():
    """
    ## Object detection examples
    Using the simple code below, we can visualize a random Item from the Dataset.
    """


def func3():
    """
    We can also get the same Item using its index.
    """


def func4():
    """
    The code below defines a data augmentation Pipeline using the imgaug library, which includes image resizing, flipping, and Gaussian blurring techniques. The DatasetGenerator class is then used to apply these augmentations to the data in the specified directory, using Bounding Box Annotations. Finally, the visualize method is called to display the augmented images, with an option to display a specific number of images.
    """


def func5():
    """
    All of the Data Generator options (from the function docstring) can be seen below:

    - :param dataset_entity: dl.Dataset entity.
    - :param annotation_type: dl.AnnotationType - type of Annotation to load from the annotated Dataset.
    - :param filters: dl.Filters - filtering entity to filter the Dataset Items.
    - :param data_path: Path to Dataloop Annotations (root to "item" and "json").
    - :param overwrite:.
    - :param label_to_id_map: dict - {label_string: id} dictionary.
    - :param transforms: Optional transform to be applied on a sample. list or torchvision.Transform.
    - :param num_workers:
    - :param shuffle: Whether to shuffle the data (default: True) If set to False, sorts the data in alphanumeric order.
    - :param seed: Optional random seed for shuffling and transformations.
    - :param to_categorical: convert Label id to categorical format.
    - :param class_balancing: if True - performing random over-sample with class ids as the target to balance training data.
    - :param return_originals: bool - If True, return ALSO images and Annotations before transformations (for debug).
    - :param ignore_empty: bool - If True, generator will NOT collect Items without Annotations.


    The output of a single element is a dictionary holding all the relevant information. The keys for the DataGen above are: ['image_filepath', 'item_id', 'box', 'class', 'labels', 'annotation_filepath', 'image', 'annotations', 'orig_image', 'orig_annotations']. You can print them using the line of code below.
    """


def func6():
    """
    The code below imports the Matplotlib plotting library and creates a dataset generator object using a specified data path, Annotation type, and set of image transformations. It then creates a 2x2 subplot and displays a random image from the Dataset on each subplot, with the left column showing the image after applying the specified transformations and the right column showing the original, unmodified image. Using this code, we'll add the flag to return the original Items, so we can better understand how the augmentations look like, compared to the original.
    """


def func7():
    """
    ## Segmentation examples
    This section will describe Semantic Segmentation examples. First we'll load a semantic Dataset and view some images and the output structure. 
    The code below loads a Dataset using its ID and generates images using a data generator. The data generator applies a series of transformations specified by the "tfs" variable to the Dataset images, and returns the original images along with the transformed versions. The transformed images are of the type "SEGMENTATION", which refers to images that have been annotated with Labels for object Segmentation. The "visualize" function is called five times in a loop to display the original and transformed images in a graphical user interface (GUI) for visualization purposes.
    """


def func8():
    """
    We can use the code below to visualize the original vs the augmented images and Annotations mask:
    """


def func9():
    """
    The code below is converting to 3D one-hot-encoding to visualize the binary mask per label. We will plot only 8 Labels (there might be more on the Item):
    """


def func10():
    """
    ## Setting a label map
    One of the inputs to the `DatasetGenerator` is the `label_to_id_map`. This variable can be used to change the Label mapping for the Annotations and allows using the Dataset Ontology in a greater variety of cases. For example, you can map multiple Labels so a single id or add a default value for all the unlabeled pixels in Segmentation Annotations. This is what the Annotation looks like without any mapping:
    """


def func11():
    """
    Now, we'll map both the 'eye' Label and the background to 2 and the 'fur' to 1:
    """


def func12():
    """
    ## Batch size and batch_size and collate_fn
    If `batch_size` is not `None`, the returned structure will be a list with `batch_size` data Items. Setting a collate function will convert the returned structure to a tensor of any kind. The default collate will convert everything to ndarrays. We also have Tensorflow and Torch collate to convert to the corresponding tensors.
    """

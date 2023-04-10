def section1():
    """
    # Ontology
    
    In this section, we will learn how to create an Ontology and populate it with Labels.

    ## Preparing - Entities setup
    Before we get started, we need to import the "dtlpy" library and use it to login to Dataloop. Then, we need to `get` a Project and Dataset from the Dataloop platform, and then get the Recipe and Ontology from the Dataset. Finally, we print the Recipe and Ontology entities.
    
    If you don't know exactly how to do all of that, or don't have the `dtlpy` Python package installed, [please consult the beginner onboarding](https://developers.dataloop.ai/onboarding/onboarding/).
    
    **Note:** If you want to print all of your Recipes, from a Dataset, just use `dataset.recipes.list()`. You should get an output similar to the one below:
    ```python
    Recipe(id='63e6283b8c01ead480810b66', creator='email@gmail.com', title='Creatures Default Recipe', project_ids=['4c74c1b5-e9cb-4294-b9d5-cbfa13eda242'], description='', metadata={'system': {'collectionTemplates': [], 'validationFile': {'itemId': '64133bff0fd0ee79187768cc', 'datasetId': '63e6280e6a656962930ec4b9', 'name': 'one_anno.js'}, 'script': {'entryPoints': {'main': {'_instructions': []}}}}}, ui_settings={'fastClassificationBar': True, 'requireObjectId': True, 'requireParenting': True, 'ocrMode': False, 'showText': False, 'freeText': True, 'interpulationActiveOnLoad': True, 'allowInterpulationChange': True, 'allowAutomation': True, 'nextItemOnClassification': True, 'enablePixelSmoothing': True, 'allowCuboidRotation': True, 'allowAsymmetricCuboids': False, 'studioV2App': True, 'allowMinimumZoom': False, 'allowObjectIdAutoAssign': False, 'polylineArrowHead': False, 'polylineTolerance': False, 'forcePolylineTolerance': False, 'forcePolylineToleranceValue': 0.8, 'keepZoomAndPositionBetweenItems': False, 'paragraphDelimiter': '', 'semanticEnforcing': False, 'autoActivateTool': False, 'lockNavWithoutDone': False, 'enableTimeMeasurement': False, 'timeMeasurementSettings': {'limit': 0, 'bonus': 0, 'value': 0}, 'showInSceneHelperArrowsFor3DEditor': False, 'allowBoxRotation': False, 'textPreWraped': True, 'ignoreVideoWarning': False, 'allowLabelSuggestion': False, 'enableItemDescriptionInCardsView': True, 'defaultAssignmentView': False, 'warnNoAnnotationsBeforeStatusUpdate': True, 'labelSubjects': False, 'requireConfirmationBeforeStatusUpdate': False, 'editAnnotationDefinitionToEntireAnnotation': False, 'enableBrowserValidation': False, 'defaultStudioOpacity': 0.2})
    ```
    
    **Note:** If you want to print all Ontologies from a Recipe, you can use `recipe.ontologies.list()', after you `get`  a specific Recipe in a variable (for example, using `recipe = dataset.recipes.list()[0]`). The output will be similar to this:
    ```python
    [Ontology(id='63e6283ba93464a0e0fcd102', creator='email@gmail.com', title='Creatures-ontology', attributes=None)]
    ```
    """


def section2():
    """
    ## Create an Ontology
    The lines of code below retrieve a Dataloop Project by name and then creates a new Ontology within it with a specified title and a red (255, 0, 0) colored "Chameleon" Label.
    """


def section3():
    """
    ## Labels

    Ontology uses the ‘Labels’  entity, which is a Python list object, meaning that you can use Python list methods such as `sort()`. Be sure to use `ontology.update()` after each Python list action, so that the Ontology can update on the platform.

    """


def section4():
    """
    Labels can be added with branched hierarchy to facilitate sub-labels at a maximum of 5 levels. Labels hierarchy is created by adding ‘.’ between parent and child Labels. In this example, the script will get the Donkey Label (from the `label_list` above):
    """


def section5():
    """
    ## Attributes
    An Attribute describes a Label, without having to add more Labels. For example “Car” is a Label, but its color is an Attribute. You can add multiple Attributes to the Ontology, and map it to Labels. For example you can create the “color” Attribute once, but have multiple Labels use it.
    
    Attributes can be multiple-selection (e.g checkbox), single selection (radio button), value over slider, a yes/no question and free-text. An Attribute can be set as a mandatory one, so Annotators have to answer it before they can complete the Item.

    ## Add attributes to the ontology
    The following example adds 1 attribute of every type, and all are set as mandatory Attributes:
    * Multiple-choice attribute
    * Single-choice attributes
    * Slider attribute
    * Yes/no question attribute
    * Free text attribute
    """


def section6():
    """
    ## Read Ontology Attributes
    The code below can be used to read & print the all the Ontology Attributes.

    """


def section7():
    """
    ## Printing all labels
    The code below will print all of the Labels in an Ontology, including child labels
    """


def section8():
    """
    And listing the keys will get:

    """

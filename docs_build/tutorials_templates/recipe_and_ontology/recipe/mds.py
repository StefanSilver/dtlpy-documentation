def section1():
    """
    
    Because a Recipe is linked to an Ontology, changes to Labels and Attributes are possible. When a Recipe is set as the default one for a Dataset, the Dataset entity can be used to make changes to the Labels and Attributes, that are ultimately linked to it via the Recipe and its Ontology.
    ## Working With Recipes

    """


def section2():
    """
    ## Cloning Recipes
    When you want to create a new Recipe that’s only slightly different from an existing Recipe, it can be easier to start by cloning the original Recipe and then making changes on its clone.
    **Note:** If the 'shallow' parameter is set to 'True', the link will be set to an existing ontology. If it's set to `False`, it will clone all Ontologies that are linked to the Recipe as well.


    """


def section3():
    """
    ## View Dataset Labels
    The lines of code below retrieve Labels from a Dataset, either as a list of objects or as a map of instances.
    """


def section4():
    """
    ## Add Labels by Dataset
    **Note:** Working with Dataset Labels can be done one-by-one or as a list. The Dataset entity documentation details all Label options - <a href="https://console.dataloop.ai/sdk-docs/dtlpy.entities.html#dtlpy.entities.dataset.Dataset.add_label" target="_blank">read it here</a>.
    
    The lines of code below add Labels to a Dataset, either multiple Labels at once or individual Labels with specific Attributes.
    """


def section5():
    """
    ## Add Labels Using Label Object
    The lines of code below create a list of Labels using a Label object, adds them to a Dataset, and creates a Recipe from the Label list, for future use.
    """


def section6():
    """
    ## Add a Label and Sub-Labels
    This code creates a parent Label "Fish" with two child labels "Shark" and "Salmon" using the Label object, adds them to a Dataset, and creates a Recipe from the Label list, for future use.
    """


def section7():
    """
    ## Add Hierarchy Labels using Nested Labels
    This code adds labels to a dataset in three different ways: 
    - Option A - adds Labels one by one. 
    - Option B - automatically generates parent and grandparent Labels if they don't exist.
    - Option C - adds Labels using a nested dictionary structure. 
    
    **Note:** Labels can have attributes like name, color, and children (sub-labels).

    """


def section8():
    """
    ## Delete Labels by Dataset
    This code deletes the Labels named "Cat" and "Dog" from the Dataset.
    """


def section9():
    """
    ## Update Label Features
    These lines of code update the color attribute of a Label named "Cat" in a Dataset. The first line updates an existing Label and will fail if the Label doesn't exist, while the second line adds the Label if it doesn't exist (`upsert`) and updates it.
    """

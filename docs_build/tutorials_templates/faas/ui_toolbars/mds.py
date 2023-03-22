def func1():
    """
    # UI Toolbars
    ## Define a UI Slot in Dataloop
    UI Slots can be created for any function, making it possible to invoke the function through a button click, in the web version of Dataloop.
    Binding functions to UI Slots will enable you to manually trigger them on selected Items, Annotations, or Tasks.

    Dataloop currently supports the following UI slots:
    1. Item as a resource, which can be of two types:
        - Dataset Browser;
        - Annotation Studio.
    2. Annotation as a resource, in the Annotation Studio;
    3. Task as a resource, in the Tasks browser.

    Let’s start by defining a UI button for the “RGB to Gray” function. To do that, we should create a slot entity in the Python SDK, that can be later activated from the UI to quickly invoke functions.
    In this case, the input for the RGB function is an Item, so the slot resource should be an Item as well (i.e. SlotDisplayScopeResource.ITEM). As a result, the function will be accessible in the Annotations Studio under "Applications" dropdown:

    """


def func2():
    """
    Once the function finishes executing, you can decide what the function outputs. Currently, 3 Post-Action outputs are available for UI slots:
    1. `SlotPostActionType.DOWNLOAD` - Download the output, available only for Item output;
    2. `SlotPostActionType.DRAW_ANNOTATION` - Available only for Annotation output. Draw the annotation on the Item;
    3. `SlotPostActionType.NO_ACTION` - Take no further actions.

    Additionally, you can use filters to specify which items in are eligible to be used in app (e.g. filtered by item type, item format, etc.).

    ## Update the Package and Service with the Slot

    Now you can update your Package and Service with the new Slot you added:

    """


def func3():
    """
    ## Activate the UI Slot

    To make the UI Slot visible to Users in the platform, you need to activate the Slots:

    """


def func4():
    """
    Notice that clicking on the UI Slot button will trigger the Service only if it is active.

    
    Important: We highly recommend **pausing** the service you created for this tutorial so it will not be triggered when you don't want it to. You can activate it when you want to use it.

    """


def func5():
    """
    Congratulations! You have successfully created, deployed, and tested Dataloop functions!
    """


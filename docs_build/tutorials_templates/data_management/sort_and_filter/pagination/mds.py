def section1():
    """
    # Pagination
    ## Pages
    We can use pages instead of a list when we have an object that contains a lot of information. The page object divides a large list into pages (with a default of 1000 Items) in order to save time when going over the Items. It's the same as we display it in the Annotation platform, in the WebUI of Dataloop (see example <a href="https://dataloop.ai/docs/organize-dataset#datastructuredisplay" target="_blank">here</a>).

    You can redefine the number of Items on a page by modifying the `page_size` attribute. When we go over the Items, we use nested loops to first go to the pages, and then go over the Items for each page. [Read more here](https://dataloop.ai/docs/en/data-browser)

    ## Iterator of Items
    The example below shows you how you can create a generator of Items with different Filters:

    """


def section2():
    """
    A Page entity iterator also allows the reverse iteration, in case you want to change Items during the iteration, as you can see in the code below:

    """


def section3():
    """
    If you want to iterate through all of the Items within your Filter, you can also do so without going through them page by page:

    """


def section4():
    """
    If you are planning to do a process on each Item, it's faster to use multi-threads (or multi-process) for parallel computation. The code below uses `ThreadPoolExecutor` with 32 workers to process parallel batches of 32 Items:

    """


def section5():
    """
    Using the code below can be used to show you how to compare the runtime, to see that the process is faster due to parallel computing:

    """


def section6():
    """
    You can also visualize the progress, using the `tqdm` progress bar, as seen below:
    """

def section7():
    """
    ### Set page_size
    To change the `page_size`, which determines how many Items are shown on a page, you can use the code examplebelow, which sets the `page_size` to 50:
    """

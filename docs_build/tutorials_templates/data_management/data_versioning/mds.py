def section1():
    """
    # Data Versioning
    Dataloop's powerful **data versioning** provides you with unique tools for data management - clone, merge, slice & dice your files, to create multiple versions for various applications. Sample use cases include:
    - Golden training sets management.
    - Reproducibility (Dataset training snapshot).
    - Experimentation (creating subsets of different kinds).
    - Task and Assignment management.
    - Data Version "Snapshot" - Use our versioning feature as a way to save data (Items, Annotations, Metadata) before any major process. For example, a Snapshot can serve as a roll-back mechanism to the original Datasets, without losing the data, in case an error breaks your Dataset.

    ## Clone Datasets
    Cloning a Dataset creates a new Dataset with the same files as the original. Files are actually a reference to the original binary and not a new copy of the original, so your cloud data remains safe and protected. When cloning a Dataset, you can add a destination Dataset, the remote file path, and more. You can see how the cloning of a dataset can be done, below:
    """


def section2():
    """
    ## Merge Datasets
    To merge Datasets, they need to be similar to each other when it comes to their Recipes and Ontology. The outcome of Dataset merging depends on how similar or different the Datasets are. Here is some important points you need to know, before merging different types of Datasets:
    * For Cloned Datasets - Items, Annotations, and Metadata will be merged. This means that you will see the Annotations from different Datasets on the same Item.
    * Different Datasets (not clones) with similar Recipes - Items will be "summed up", which will cause the duplication of similar Items.
    * Datasets with different recipes - Datasets with different default Recipes **cannot be merged**. Use the 'Switch Recipe' option on the Dataset level in the Dataloop WebUI (3-dots action button) to match Recipes between Datasets and be able to merge them.
    
    You can see how the merging of 2 Datasets (having similar Recipes) can be done using Dataloop's Python SDK:
    """

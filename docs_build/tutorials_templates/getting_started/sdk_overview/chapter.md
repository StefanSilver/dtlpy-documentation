# Dataloop Python SDK Quick-Start Guide


Dataloop provides an end-to-end platform that supports the entire AI lifecycle, from development to production. 
By leveraging both a data management and annotation platform, deep learning data generation is streamlined, resulting in
accelerated automated pipeline production and reduced engineering time and costs.

The Dataloop platform is built upon an extensive Python SDK that provides full control over your projects and code. It
allows you to automate CRUD (Create, Read, Update, Delete) operations within the platform for:

* Projects
* Datasets
* Items
* Annotations
* Metadata


## About this guide

This Quick Start guide will provide you, as a developer, with an efficient Python SDK on-boarding experience that covers the following:

1. [Installing the prerequisite software](#installing-prerequisite-software)
2. [Login to the platform through SDK](#sdk-login)
3. [Create a project](#to-create-a-new-project)
4. [Get existing project](#to-select-the-new-project)
5. [Create Dataset](#to-create-a-new-dataset)
6. [Get Dataset](#to-select-the-dataset)
7. [Upload items](#uploading-items)
8. [Get items](#getting-items)
9. [Annotate item (labels and classification)](#annotating-items)
10. [Upload annotation](#classification)
11. [Filter items](#creating-filters)
12. [Working with Item Metadata](#working-with-item-metadata)
13. [Create Task](#creating-tasks)
14. [Logout](#logging-out)

## Installing Prerequisite Software

The **Dataloop SDK** requires several prerequisite software packages to be installed on your system before it can be
used.

> :information_source: The scope of this guide does not cover detailed external software installation issues. Please use the provided software vendor website links for further installation information and troubleshooting related to your OS.

### **Python**

Python **3.6 or later** must be installed in order to use Dataloop's Python SDK.

#### To download Python:

1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. From the **Downloads** page, **select** your desired OS and proceed with the download.
3. Once the download is complete, you can proceed to **install** the software.

**Note**: You can also use packages like [Anaconda](https://www.anaconda.com/), which come with Python pre-installed. Just make sure that the version of Python is at least 3.6 for our dtlpy package to work properly.

### Dataloop's Python SDK Package

### pip

The Python SDK package requires **pip** to be installed on your system, which is the package installer for **Python**. If
Python was installed from [python.org](https://www.python.org/) as described above, or if you are using [Anaconda](https://www.anaconda.com/), **pip** should already be installed.

You can also check if **pip** is installed on your system.

To do that, just **run** the following from the Command Line or Terminal:

```
pip --version
```
If pip is installed, that command will return the version of pip on scree. Otherwise, it will return a "command not found" error.


If **pip** isn’t already installed, you can [bootstrap pip from the standard library](https://docs.python.org/3/library/ensurepip.html).

#### To bootstrap pip:
**Run** the following from the Command Line:

```
python3 -m ensurepip --default-pip
```

### DTLPY Package

Once you have verified that **pip** is installed, the **Dataloop SDK Package** can be installed.

To install the Dataloop SDK Package execute the following from the Command Line or Terminal:

```
pip install dtlpy
```

This will install dtlpy, which is Dataloop's Python SDK package, along with all of its requirements. Once the dtlpy package is successfully installed, a **confirmation message** is displayed:

```
Successfully installed dtlpy-1.64.9
```

## SDK Login

Once the **Dataloop SDK Package** is installed, you can login using the Python SDK.

To log in to the Dataloop SDK:

1. **Open** a Python Shell.
2. **Run** the following Python command:

```python
import dtlpy as dl
dl.login()
```

You can also use the command below, which checks if the login token expired. Login tokens **expire** after **24hours**, therefore the following expression can be added at the start of the command:

```python
if dl.token_expired():
    dl.login()
```
This command is also useful because it will execute only once every 24 hours.

A web browser login screen will be displayed after execution, where you will need to use your Dataloop credentials to log in to the platform:

![alt_text](../../../assets/log_in/login.png "image_tooltip")

3. **Enter** your credentials, or alternatively login using a Google account.

Once your credentials have been verified a **confirmation message** will be displayed:

![alt_text](../../../assets/log_in/login_successful.png "image_tooltip")
  
## Machine-to-Machine Login  
Long-running SDK jobs require API authentication.  The M2M flow allows machines to obtain valid, signed JWT (authentication token) and automatically refresh it, without the need for a web browser login.  
  
M2M Login is recommended when you want to:  
    - run commands on the platform without an ongoing internet connection.  
    - run API commands directly from an external system to Dataloop.   

> :information_source: This can be done with your email and password (signup with a password), or using project bots (which is NOT is the scope of this tutorial).  

```python
dl.login_m2m(email=email, password=password)
```
## Datasets

In Dataloop, a Dataset entity is a collection of **Items** (files), their respective **Metadata**, and **Annotations**. Datasets have a file system structure and are organized into folders and subfolders at multiple levels.

There are **3 types** of datasets:

1. **Master** - The original dataset which manages the actual binaries.
2. **Clone** - Contains pointers to original files, which enables management of virtual Items that do not replicate the
   binaries of the underlying storage once cloned or copied. When cloning a Dataset, users can decide if the new copy
   will overwrite the original Metadata and Annotations.
3. **Merge** - Several Datasets can be merged into one, allowing multiple Annotations to be combined into the same
   Dataset.





### Creating a new Project
Before a new Dataset can be created, at least one Project must exist. **Run** the following command to create a new project named: **My-First-Project**:

```python
project = dl.projects.create(project_name='My-First-Project')
`````

The new Project is **created**. The new Project must then be selected prior to creating a new associated Dataset. **To select the new Project** run the following command, using the name of the Project you just created:

```python
project = dl.projects.get(project_name='My-First-Project')
```

The new Project is now **selected**. A Project can also be referenced in the above command via its unique `project_id`. You can find the ID of your projects by going into the Web UI version of Dataloop, clicking the Project you want to use and check the URL:
![image](https://user-images.githubusercontent.com/58508793/229094587-598ec96a-5cf9-4474-84f0-a09ea495df49.png)

Otherwise, if you want to do it in the SDK, you can simply run this command, which will list all of the Projects you have:
```python
dl.projects.list()
```
After running this command, you should get something like this:

```python
Project(created_at=1674492313392, creator='myfuncont@gmail.com', id='764803e6-af9b-4dde-8141-fea54231fb54', name='My-First-Project', feature_constraints=[{'name': 'downloadJsons', 'quota': 0, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 0, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 0, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 0, 'title': 'Create Driver'}])
```

### To select the new Project using a project_id:

**Run** The following command to select the new Project by referencing the **project_id**:

```python
project = dl.projects.get(project_id='e4a5e5b3-a22a-4b59-9b76-30417a0859d9')
```

The new Project is now **selected** using the Project's ID.



### Create a new dataset
Now that we have created and selected a Project, a new Dataset can be created. **Run** the following command to create a new Dataset named My-First-Dataset associated with the Project you just created:

```python
project.datasets.create(dataset_name='My-First-Dataset')
```

Confirmation of the successfully created dataset should be **displayed** if everything went well:

```python
Dataset(id='632c24ae3444a86f029acb47', url='https://gate.dataloop.ai/api/v1/datasets/632c1194120a7571664d0de3', name='My-First-Dataset', creator='JohnDoe@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2022-09-22T07:41:08.324Z')
```

**Note**: Your Dataset's ID will differ from the example above.

## Uploading items

Items (files) can be **uploaded to Datasets** in a file system structure, and are organized into folders and subfolders. Individual Items or entire folders can be uploaded.

Before Items can be uploaded, the Dataset to which the Items will be uploaded must be selected.

To select the dataset: **Run** the following command to initialize a new instance **(dataset)** of the new dataset **(My-First-Dataset)** in order to upload items:

```python
dataset = project.datasets.get(dataset_name='My-First-Dataset')
```

Confirmation of the new instance of the selected dataset should be **displayed** if all went well:

```
Dataset(id='632c24ae3444a86f029acb47', url='https://gate.dataloop.ai/api/v1/datasets/632c1194120a7571664d0de3', name='My-First-Dataset', creator='JohnDoe@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2022-09-22T07:41:08.324Z')
```

**Note**: Your Dataset's ID will differ from the example above.
If the selected dataset does not exist the following error message is **displayed**:

```
dtlpy.exceptions.NotFound: ('404', "Dataset not found. Name: 'My-First-Dataset')
```

Once the Dataset instance has been successfully initialized, Items can be uploaded.

The structure of the **Upload Item Command** is:

```
dataset.items.upload(local_path='/path/to/file.extension')
```

**Note**: Directory paths look different in Windows and in Linux; Windows require an "r" at the beginning.

### To upload an Item to a Dataset:

1. **Create** a local directory in your file explorer. For this example, **C:\UploadDemo** is used.
2. **Run** The following command to upload an Image file from a local directory:

```python
dataset.items.upload(local_path=r'C:\UploadDemo\test1.jpg')
```

**Note**: Ensure the path and file exists before running the command.


Confirmation of the completed upload should be **displayed** if all went well:

```
Upload Items: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.54it/s]
Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/'632c24ae3444a86f029acb47', created_at='2022-09-22T10:18:03.000Z', dataset_id='632c24ae3444a86f029acb47', filename='/test1.jpg', name='test.jpg', type='file', id='632dadf7b28a0c0da317dfc8', spec=None, creator='JohnDoe@gmail.com', _description=None, annotations_count=0)
```

The **Item ID** of the uploaded file is 632dadf7b28a0c0da317dfc8. This ID is used when **Listing/Getting** items (
See [Getting Items](#getting-items)).

**Note**: Your Item ID will differ from the example above.

If the item to upload is not found, the following **error message** is **displayed**:

```
dtlpy.exceptions.NotFound: ('404', 'Unknown local path: C:\\UploadDemo\\test1.jpg')
```

**Note**: By default, files are uploaded to the root directory. Items can be uploaded to an existing folder within a Dataset using the `remote_path` argument (Not in the scope of this guide).

### <span style="text-decoration:underline;">Exercise 1</span>

1. Write the commands to **Upload** a 2nd image (**test2.jpg**) file item to **My-First-Dataset.**

## Getting Items

Items can be retrieved from a dataset individually using the **item ID**. Alternatively, all Items can be retrieved
using a loop.

### Getting a Single Item

The command structure of **Getting a Single Item** is:

```python
item = dataset.items.get(item_id='my_item_id')
item.print()
```

#### To get a single item:

1. **Run** the following command to set an instance of a single Item object (**item_1**) from the dataset (**My-First-Dataset**) by specifying an **item ID**:

```python
item_1 = dataset.items.get(item_id='632c365b6002b1266e007830')
```

**Note**: Your Item ID will differ from the example above.

2. **Run** the following command to print the specified Item:

```python
item_1.print()
```

The item details are **displayed** including the following:

* Filename
* Creator of the Item
* Created timestamp
* Dataset ID of the Item

### <span style="text-decoration:underline;">Exercise 2</span>

1. Write the commands to **print** the details of the 2nd uploaded Item (**Test2**). Name the Item object **item_2**.

**Note**: The ID of the Item (Test2) must be identified first.

### Getting All Items

All item details in a Dataset can be printed using a loop.

#### To get all items:
Run the following command to loop through the Dataset and print all Item details:

```python
pages = dataset.items.list()
for item in pages.all():
    item.print()
```

or:

```python
pages = dataset.items.list()
for page in pages:
    for item in page:
        item.print()
```

All dataset Item details should be **displayed**.

## Annotating Items

Dataset Items are annotated using **Labels**. A **Label** is composed of various **Label Settings** and **Instructions**
that are defined by a Dataset’s **Recipe**. For example, an image or video file Item can contain 1 Label defined as
a [Classification](#classification) to categorize the entire image and multiple other labels defined
as [Point Markers](#point-markers) to identify specific objects in an image/video file item.

### Classification

**Classifications** are used to categorize an entire image or scene (in the case of a video file). For example, a
**Classification** label can be used to classify product images under categories, subcategories, and characteristics,
such as men’s clothes, polo shirts, etc.

In the Python SDK you can add **Classification** Labels to an **Item** using 2 steps.

1. **Adding** a Label to a Dataset’s **Recipe**.
2. **Adding** the Label to an Item as a **Classification**.

#### To Add a Classification Label to a Dataset Recipe:

1. Run the following command to add a **Label** (**Person**) to the **My-First-Dataset** Dataset Recipe.

```python
dataset.add_label(label_name='Person')
```

The Label is created and its **Properties** are displayed, if everything went well.

```
[Label(tag='Person', display_data={}, color='#0214a7', display_label='Person', attributes=[], children=[])]
```

2. **Run** the following commands to **Annotate** and **Upload** the Label (**Person**) as a **Classification** to the Item (**item_1**):

```python
builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='Person'))
item_1.annotations.upload(builder)
```

The Label is now Annotated as a **Classification** to **item_1**.

## Point Markers

A **Point Marker** is used to identify specific objects in an image or video item. For example, an image of a person's
face can contain multiple **Point Marker** Labels specifying the person’s eyes, mouth, ears, etc.

**Point Marker** commands accept 2 coordinate input parameters (x,y) which specify where the Label is plotted on the
image.

The Python SDK can add **Point Marker** Labels to an **Item** using 2 steps.

1. **Adding** a Label to a Dataset’s **Recipe**.
2. **Adding** the Label to an Item as a **Point Marker**.

### To Add/Upload a Point Marker Label to a Dataset Recipe:

1. **Run** the following command to add a Label (**Ear**) to the **My-First-Dataset** Dataset Recipe.

```python
dataset.add_label(label_name='Ear')
```

The Label is created and its **properties** are displayed.

```
[Label(tag='Ear', display_data={}, color='#0214a7', display_label='Person', attributes=[], children=[])]
```

2. **Run** the following commands to **Annotate** and **Upload** the Label (**Ear**) as 2 **Point Markers** to the
   Item (**item_1**):

```python
builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Point(x=80, y=80, label='Ear'))
builder.add(annotation_definition=dl.Point(x=120, y=120, label='Ear'))
item_1.annotations.upload(builder)
```

The Label is Annotated as 2 **Point Markers** to **item_1**.

**Note**:  Other Label Types include Box, Cube, Polygon etc.

### <span style="text-decoration:underline;">Exercise 3</span>

1. **Annotate** 3 Items (use **item_2** from [Exercise 2](#span-styletext-decorationunderlineexercise-2span)) with the **Classification** Label of '**Face**'.
2. **Annotate** 2 random **Point Marker** Annotations with the Label '**Eye**' to an Item (use **item_2** from [Exercise 2](#span-styletext-decorationunderlineexercise-2span)).

**Note**: Remember that the Label must first be added to the Recipe of the Dataset.

## Working with Filters

Dataloop's Python SDK supports the filtering of Item data. You can filter Items by creating **Filter Queries** that define the
**Parameters** of the Filter. For example, you can create a **Filter Query** that filters Item data on a specific field
name, or by an Item’s Annotation Label.

Multiple **Parameters** can be added to a **Filter Query**, for example, you can include a parameter that filters for
all Items that include **Point Marker Annotation** types that are **Labelled** as ’**Ear**’.

### Creating Filters

1. The first step is to create a **Filter Query**. You can **Run** the following command to create a **Filter Query** named **my_filter**:

```python
my_filter = dl.Filters()
```

Once the **Filter Query** is created, **Filter Parameters** can be added.


2. **Run** the following command to add a **Filter Parameter** to **my_filter** that filters for all Items that include **Point Marker Annotation** types:

```python
my_filter.add_join(field='type', values='point')
```

The **Filter Parameter** should be created.

**Note**: Other Fields can be used as Filter Parameters including id, dataset_id, etc.

Additional **Filter Parameter**s can be added to the **Filter Query.**

To add additional Filter parameters:

3. **Run** the following command to add **Additional Filter Parameter** to **my_filter** that filters for all Items that
   include a **Label** value of **‘Ear’**.

```python
my_filter.add_join(field='label', values='Ear')
```

The **Additional Filter Parameter** is added.

#### To Apply the Filter Query:

4. **Run** the following commands to **Apply** the **Filter Query** to the **Dataset** and **display** the filtered
   Item(s):

```python
pages = dataset.items.list(filters=my_filter)
for item in pages.all():
    item.print()
```

The **Filter Query** is **applied** to the **Dataset** and the filtered Item details are **displayed**:

```
Iterate Pages:   0%|                                                                                                                                                                        | 0/1 [00:00<?, ?it/s]Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/632c24ae3444a86f029acb47', created_at='2022-09-23T13:00:39.000Z', dataset_id='632c24ae3444a86f029acb47', filename='/test1.jpg', name='test1.jpg', type='file', id='632dadf7b28a0c0da317dfc8', spec=None, creator='JohnDoe@gmail.com', _description=None, annotations_count=7)
Iterate Pages: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 169.70it/s]
>>>
```

## Using Filters to Replace Data

Filters can also be used to **Replace** existing Item data. For example, you can **Create** and **Apply** a **Filter Query**
that returns a **subset** of Item data that includes a particular **Classification** such as ‘Person’ and **Replace** it
with another value, such as ‘Adult’, across the entire **subset**.

The first step is to **Create** a new **Filter Query** with a **Filter Parameter** that filters for all Items that include a **Label** value of **‘Person’**.

### To Create the Replacement Filter Query:

1. **Run** the following commands to **create** the Replacement **Filter Query** and **Filter Parameter**:

```python
person_filter = dl.Filters(resource=dl.FILTERS_RESOURCE_ITEM)
person_filter.add_join(field='label', values='Person')
```

The Replacement **Filter Query** and **Filter Parameter** are **created**.

The **new label** can be added with the value ‘Adult’.

2. **Run** the following commands to **create** the **new label**:

```python
dataset.add_label(label_name='Adult')
pages = dataset.items.list(filters=person_filter)
```

The **new Label** is **created**.

The existing Label can be deleted and replaced with the **new label**.

3. **Run** the following commands to **delete** the **existing label** and **Add** the **new label**:

```python
import dtlpy as dl

person_ann_filter = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
person_ann_filter.add(field='label', values='Person')

for item in pages.all():
    item.annotations.delete(filters=person_ann_filter)
    annotations = item.annotations.builder()
    annotations.add(annotation_definition=dl.Classification(label='Adult'))
    item.annotations.upload(annotations)
```

All instances of the old label are replaced in each Item with the **new Label**.

### <span style="text-decoration:underline;">Exercise 4</span>

1. **Create** and **Apply** a **Filter Query** (use **item_2** from [Exercise 3](#span-styletext-decorationunderlineexercise-3span)) that filters items and returns all items that include **Point Marker Annotations** that are labeled **‘Eye’**.
2. **Create** and **Apply** a **Filter Query** (use **item_2** from [Exercise 3](#span-styletext-decorationunderlineexercise-3span)) that filters the items with the **‘Face’** classification, deletes the label, and replaces it with the label **‘Person’**.

## Working with Item Metadata

**Metadata** is a dictionary attribute used with Items, Annotations, and other entities of the Dataloop system, for
example, **Recipes**. You can add any keys and values to both Item and Annotation **user metadata** sections using the Python SDK. This **User Metadata** can be used for data filtering, sorting, etc.

### Adding a New User Metadata Field to an Item

The following example will demonstrate adding a new user **metadata field** named **Date&Time** to the Item named
**test1**, which in this case has an **item ID** = `632dadf7b28a0c0da317dfc8`. 

**Note** Your Item ID will differ from the example above.

The first step is to **import** the **datetime** module. **Run** the following commands to import the **datetime module**:

```python
import datetime
```

The **datetime** module is now imported.

An instance of Item **test1** can be **created**.

**Create** an [instance](#to-get-a-single-item)of Item **test1** named **item_1**.

```python
item_1 = dataset.items.get(item_id='632dadf7b28a0c0da317dfc8')
```

An instance of Item **test1** named **item_1** is created. The current date can be **assigned** to a new field in the Item’s Metadata named **Date&Time** and the Item can be **updated**.

**Run** the following commands to assign the date to a new **metadata field** and **update** the item:

```python
now = datetime.datetime.now().isoformat()
# modify metadata for the item
item_1.metadata['user'] = dict()
# add it to the item's metadata
item_1.metadata['user']['dateTime'] = now
# update the item
item_1 = item_1.update()
```

The date is **assigned** to the new **metadata field** and the Item is **updated**.

**Metadata fields** can also be created for a subset of Items at once using **Filters**.

**Run** the following commands to **create Metadata fields** for **a subset** of **Items** that include the label **‘Person’** using a **Filter**:

```python
filters = dl.Filters()
filters.add_join(field='label', values='Person')
now = datetime.datetime.now().isoformat()
dataset.items.update(filters=filters, update_values={'user': {'dateTime': now}})
```

The date is **assigned** to the new **Metadata field** and **all Items** that include the Label **‘Person’** are **updated**.

### <span style="text-decoration:underline;">Exercise 5</span>

1. For the filtered Items with the **classification  Label ‘Adult’** from [Exercise 4](#span-styletext-decorationunderlineexercise-4span), add a new field called ‘date’ In the Item’s **User Metadata** and assign it the current date.

## Creating Tasks

A **Task** can used to initiate the annotation of Items. A **Task** requires defining the included data Items, the assignee(s), and other options such as due date, etc.

### To Create a Task

**Run** the following commands to **create** a **Task** containing Items with the Label **‘Person’** (from the previous example).

```python
task = dataset.tasks.create(task_name='test',
                            due_date=datetime.datetime(day=15, month=7, year=2022).timestamp(),
                            assignee_ids=['JohnDoe@gmail.com'],
                            filters=filters)
```

The Task is **created**.

### <span style="text-decoration:underline;">Exercise 6</span>

1. Create a **Task** that contains those Items from [Exercise 5](#span-styletext-decorationunderlineexercise-5span), ie all the Items **filtered** for the classification **‘Adult’**.

## Logging out

To Logout **Run** the following command to **Logout** of the SDK:

```python
dl.logout()
```


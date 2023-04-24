# Chapter 5 - Tasks

In the Dataloop platform, Tasks are created to initiate Annotation or Quality Assurance (QA) workflows. It requires defining the data items to be included, the Task assignees, and various options such as work-load, custom-status, and more. The Tasks can be of 2 types, which were mentioned above - Annotation Tasks or QA Tasks. You will now find out how to create and assign people to both types of Tasks.

To create a task, you will need to know the Dataset and Project you want to use. To find the Project you want to use, you can list all of the Projects you currently have in your Organization:
```python
dl.projects.list()
```
To which you will get an output similar to this:
```python
[Project(created_at=1676027918381, creator='email@gmail.com', id='4c74c1b5-e9cb-4294-b9d5-cbfa13eda242', name='CreatureHunt', feature_constraints=[{'name': 'downloadJsons', 'quota': 1, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 1, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 1, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 1, 'title': 'Create Driver'}])]
```
Then you can use the following command to `Get` the Project by `name`:
```python
project = dl.projects.get(project_name='CreatureHunt')
```
Once you got the Project you want, you can also list all of the Datasets that are part of the specific Project you selected:
```python
project.datasets.list()
```
With an output similar to this one:
```python
[Dataset(id='63e6280e6a656962930ec4b9', url='https://gate.dataloop.ai/api/v1/datasets/63e6280e6a656962930ec4b9', name='Binaries', creator='email@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2023-02-10T11:18:38.717Z'),
 Dataset(id='63e6283b4a03c631b54725ec', url='https://gate.dataloop.ai/api/v1/datasets/63e6283b4a03c631b54725ec', name='Creatures', creator='email@gmail.com', items_count=1132, expiration_options=None, index_driver='v1', created_at='2023-02-10T11:19:23.239Z')]
```
And then, you can get the Dataset you want to use in a variable, like this:

```python
dataset = project.datasets.get(dataset_name='Creatures')
```
The basic example that can be seen below, walks you through how to create a simple Task using the Python SDK.  Your first step is to name the Task then you set a due date for when the Task should be completed.  Next you'll add one or more Annotators (Assignees below) to work the Task.  If you don't want to assign all the objects in the Dataset to the Task, add a Filter. Simply run the following code with the desired parameters and your first Task will get created complete with a due date, Assignee(s), and a Filter:

```python
task = dataset.tasks.create(
    task_name='test_task1',
    due_date=datetime.datetime(day=11, month=3, year=2025).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignees
    filters=filters  # (optional) filter by folder directory or use other filters
)
```

To create a QA Task, the process is quite similar. See the code below:

```python
qa_task = dataset.tasks.create_qa_task(
    task=task,
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    filters=filters  # this filter is for "completed items"
)
```

If you simply want to create a Task out of an entire Dataset, you can simply remove the `filters` parameter, and a Task will be created and use the entire Dataset you identified:

```python
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
    # The items will be divided equally between assignments
)
```



The example below exemplifies the creation of a basic Annotation Task and then create a QA (Quality Assurance) Task, for the initial Task. The code below also creates a Filter, that looks for all unannotated Items in the Dataset you provided. It includes all the code you need, including imports, login, etc. - you need only to  change the names to fit your Project, Dataset, email accounts, etc. 
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='CreatureHunt')
dataset = project.datasets.get(dataset_name='Creatures')
# filter items without annotations
filters = dl.Filters(field='<annotated>', values=False)
# Create annotation task with filters
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignments
    filters=filters  # filter by folder directory or use other filters
)
# Create QA task with filters
qa_task = dataset.tasks.create_qa_task(task=task,
                                       due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
                                       assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
                                       filters=filters  # this filter is for "completed items"
                                       )
```
If everything goes right, 2 commands progress bars should execute (one for Task and one for QA), as seen below:
```python
Command Progress: 100%|██████████████████████████████████████████████████████████████| 100/100 [00:01<00:00, 62.61it/s]
Command Progress: 100%|██████████████████████████████████████████████████████████████| 100/100 [00:01<00:00, 93.34it/s]
```
Sometimes you may also want to add new Items to a specific Task - so you don't have to create another Task. To do that, you can use the code below to add a single Item, or a list of Items to an existing Task:
```python

item_to_upload_1 = dl.items.get(item_id='<item-id>')
item_to_upload_2 = dl.items.get(item_id='<item-id>')
task.add_items(items=[item_to_upload1, item_to_upload_2],
               assignee_ids=['<annotator1@dataloop.ai>'])

```
**Note:** The same code can be used to add an item to a QA Task.

You can also use a Filter, if you want to upload a high ammount of Items to the task, using the code snippet below. The Filter in this code looks for all Items that are not assigned to any Task:
```python

filters = dl.Filters(field='<metadata.system.refs>', values=[])  # filters for Items unassigned to any task
# Create annotation task
task.add_items(
    filters=filters,  # filter by folder directory or use other filters
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'])

```

If you want to see more code snippets about Tasks, [check out this page](https://developers.dataloop.ai/tutorials/task_workflows/create_a_task/chapter/).
Now you know the basics of Tasks. In the next chapter, you will learn how you can use data versioning tools to manage your data.

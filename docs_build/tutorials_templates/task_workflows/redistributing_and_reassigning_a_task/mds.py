def func1():
    """
    # Managing Tasks & Assignments
    While setting up Tasks and Assignments is important, it's also critical to have a good system in place to manage and modify them. Dataloop has this system, which makes it easy for you to manage the Tasks and Assignments you give to your workers. This section will show some examples of code that will help you manage your Tasks and Assignments.
    
    ## Get Task
    The first example will teach you how to `get` the Task you want to work on. As you can see in the code below, there are multiples ways in which you can `get` a Task, and also how you can list the Tasks of either a Project or a Dataset.
    **Note:** Remember to Log In to Dataloop before trying any of the code, using `dl.login()`.
    """


def func2():
    """
    ## Get Assignments
    This example shows you how you can get the asignments in multiple ways, both by ID and by Assignment name. It also shows you how you can list the Assignments you have in a Project, Dataset or even in a particular Task.
    """


def func3():
    """
    ### Get Assignment Items
    If you want to get all of the Items from a particular Assginment in a variable, you can use the line of code below.
    """


def func4():
    """
    ## Redistribute and Reassign Assignments
    Sometimes, circumstances may lead to having to redistribute or to reasign Assignments, due to factors like a worker leaving the Project, taking Personal Time Off, or other factors. If that is the case, this section shows you how you can reasign and redistribute an Assignment, when needed. 
    **Note:** The code below shows you how to log in, and then `get` the Project, Dataset, Task and Assignment you want to modify.
    """


def func5():
    """
    ### Redistribute
    Redistributing an Assignment means to distribute the Items to multiple assignees. This process is identical to both Annotation and QA tasks. You can see how it's done, below.
    """


def func6():
    """
    ### Reassign
    Reassigning an Assignment changes the assignee from its original one to another one that you specify. Use the simple line of code below, to reasign an Assignment.
    """


def func7():
    """
    ### Delete Task and Assignments
    Sometimes you may wish to delete a Task or an Assignment for various reasons. 

    Before you delete a Task, keep in mind that when a Task is deleted, all of its Assignments will be deleted as well. To delete a Task you must first get that task in a variable, using `task = dl.tasks.get(task_id='<my-task-id>')`. After doing that you can use the line of code below to delete it. 
    """


def func8():
    """
    If you want to delete only a particular Assignment of a Task, you must first get that Assginment by ID or by name, using `assignment = task.assignments.get(assignment_name='<my-assignment-name>')`, and then execute the line of code below.
    """

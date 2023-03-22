def func1():
    """
    # Advanced Configurations
    ## Service Runtime
    Services are configured with a runtime driver and runtime configuration, which defines how the Service should be deployed. Currently, the only supported driver is the Kubernetes driver.
    When a Service is deployed with the Kubernetes driver, a Kubernetes deployment is created. A Kubernetes deployment basically tells Kubernetes how many replicas of the Service should be up at any point in time, and how many resources should be allocated to it.
    """
def func2():
    """
    ## Autoscaler
    When we have varying loads of work, we want the number of service replicas to scale up when there are a lot of executions coming in and scale down otherwise.
    To do so, we need to create an Autoscaler, as using the code below:
    """

def func3():
    """
    ## Using Secrets in a Function
    You can use Organization integration Secrets (key-value) as environment variable inside the function's environment.
    First you'll need to add the integrations (possible only in UI mode), then simply add the integrations' IDs when deploying the Service:
    """


def func4():
    """
    Inside the Service you can access the values using an OS Package, as seen below:
    """

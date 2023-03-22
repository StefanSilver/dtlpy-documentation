def func1():
    """
    # Executions Control
    ## Execution Termination
    Sometimes when we need to run long Executions of various Services, such as model training. That's why we need to have the option to terminate an Execution. This is facilitated using the Terminate at Checkpoint.
   
    To stop an Execution set the code checkpoints to check if this Execution received a termination; if it did, raise the Termination Exception.
    This allows you to save the processing that was already done before terminating the execution. Here is an example:
    """


def func2():
    """
    Each time there is a "kill_event" the Service runner checks to see if this Execution received a termination request. To kill such Execution we use the following command:
    """


def func3():
    """
    ## Execution Timeout
    You can tell an Execution to stop after a given number of seconds with the timeout parameter (the default time is 1 hour).
    In case a Service reset, such as in timeout or Service update, if there are running Executions the service will wait for the Execution timeout before resetting. The value needs to be a natural number (int):
    """


def func4():
    """
    You can also decide what to do to Executions that have experienced a timeout. There are 2 options of timeout handling:
    1. Mark Execution as failed;
    2. Retry (rerun) Execution.
    """


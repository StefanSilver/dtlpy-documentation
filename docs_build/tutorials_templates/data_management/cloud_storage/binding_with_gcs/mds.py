def section1():
    """
    ## Dataset Binding with Google Cloud Storage (GCS)

    In this section, we will create a GCP cloud function to continuously sync a Bucket with a Dataloop Dataset.

    If you want to catch events from the GCS Bucket and update the Dataloop Dataset you need to set up a Cloud function. This function will catch the GCS Bucket events and will reflect them into the Dataloop Platform.

    If you are familiar with [GCP Cloud Functions](https://cloud.google.com/functions), you can just use our integration function  you will see below, after step 6.

    **Note:** We assume you already have a GCP account. If you don't, follow the [GCP docs](https://cloud.google.com/docs/get-started) and create it.

    ### Create the Cloud Function
    To bind you GCS with Dataloop, you need to follow the steps below:
    
    1. Create a GCS Bucket.

        **Note:** This Bucket should be used as the external storage for the Dataloop Dataset.

    2. Go to Cloud Functions and click ***Create Function*** to create a new function.
    3. Basic:
       * Environment -> 1st gen Subscription.
       * Choose the Function Name.
       * Choose the Function Region.
    4. Trigger:
       * Trigger type -> Cloud Storage.
       * Event type ->  On (finalizing/creating) file in the selected Bucket.
       * Bucket -> Choose the Bucket for which you would like to allow auto-sync with Dataloop.
       * Click Save.
    5. Runtime, build, connections and security settings:
       * Choose the Runtime tab.
       * Runtime environment variable -> Add variable.
       * Add the 3 environment variables: `DATASET_ID`, `DTLPY_USERNAME` and `DTLPY_PASSWORD`.
         **Note:** To populate the values for the variables: `DTLPY_USERNAME`, `DTLPY_PASSWORD` you'll need to create a **DataLoop Bot** on your Dataloop Project using the following code:
        * The output:
          * username -> `DTLPY_USERNAME`
          * password -> `DTLPY_PASSWORD`
        * After adding all environment variables click **Next**.
    """


def section2():
    """
    6. Code:
       * Runtimes: => python 3.7.
       * Entry point: Your function name from the code snippet (default `create_gcs`).
       * In the requirements.txt file -> add `dtlpy`.
       * Copy the following code to the main.py file:
    """


def section3():
    """
    * Click -> Deploy.


    7. Add another function for delete actions:
       * Repeat the process above.
       * Create another function for `delete` with `delete event` with the code below and the same settings.
       * Trigger -> Event type ->  On (deleting) file in the selected Bucket.
       * Entry point: Your function name from the code snippet (default `delete_gcs`).
    """


def section4():
    """
    ** If you followed the guide, you should now have your GCS bound to the Dataloop Dataset, which will synch automatically!



    ### Here are some graphical examples of this process:

    ![add_layer](../../../../assets/bind_gcs/create_function.png)
    ![add_layer](../../../../assets/bind_gcs/settings.png)
    """

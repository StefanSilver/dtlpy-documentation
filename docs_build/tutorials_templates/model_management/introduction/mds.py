def func1():
    """
    # Model Management

    
    Dataloop's model management system offers machine learning engineers a unified platform for handling both research and production workflows. This centralized approach simplifies the management of the model lifecycle, enabling data scientists to optimize their models, train them more effectively, and deploy them faster.

    The system employs a combination of Packages, Datasets, and Artifacts that are used to run models. Packages are collections of code that contain the necessary codebase to execute a model. Model architectures are pushed to the cloud through Packages, allowing for seamless integration with the rest of the Dataloop ecosystem. Datasets, on the other hand, include images (or other types of data) used for training or inference, and they identify which images belong to different subsets (e.g., train/validation/test). This enables users to perform tasks such as dividing the Dataset in different ways to achieve specific training objectives.

    Dataloop offers a variety of pre-built models, including popular open-source algorithms like ResNet and Yolo. In addition, users can create models from pre-trained models for fine-tuning or transfer learning. They can also upload their own models and view training metrics to compare model performance.

    All models can be easily integrated into the Dataloop platform, connected to the UI via buttons or slots, or added to pipelines. This allows for maximum flexibility and efficiency, making it easier for data scientists to collaborate and deploy models more quickly. Overall, Dataloop's model management system offers a robust, end-to-end solution for machine learning workflows, from model creation to deployment.

    In this tutorial we will cover the required Dataloop entities to create, compare, restore, manage, and deploy model training sessions and trained models. In the image below, you can see the components of a model in Dataloop.
    
    ![image](https://user-images.githubusercontent.com/58508793/230947969-460fcd1d-6fdc-41c6-9289-c689005e3eea.png)

    ## Package and Model Entities

    ### Package

    Dataloop uses the Package entity to save the architecture of the model (e.g Yolov5, Inception, SVM, etc.) and the model algorithm code.

    - In “online” mode (see “Model Comparison” below), Packages should include a Model Adapter to create the Dataloop API.

    Model algorithms that are ready as-is to use can be found in the AI Library. All public packages listed in the AI Library are pretrained and include the model algorithm code and default configurations. Users can download the codebase of any Packages pushed to the cloud.

    ### Model

    To create a model in Dataloop, we need a few components: a Package of code, a Dataset, an Ontology (which provides Labels for the data), and a configuration in the form of a dictionary. These elements work together to produce a functional machine learning model.

    Once the model has been trained using the Dataset and Ontology, it will contain various weights and other important artifacts that are needed to load and use the model for inference. This means that the model can take in new data and produce predictions or other outputs based on what it has learned from the training data.

    One advantage of machine learning models is that they can be cloned, meaning that the model and all of its associated weights and artifacts can be saved and used as a starting point for a new model. This is particularly useful for fine-tuning or transfer learning, where we want to build a new model that is based on the knowledge and experience gained from a previous model.

    ## Additional Package components

    Some users may want to further customize their models, such as uploading their own model weights or creating their own custom model. This can be achieved with Artifacts and a Model Adapter.

    ### Artifacts and Codebase

    Artifacts are any additional files that are necessary for a given model to run on the cloud. For example, if a user wanted to upload their own weights to create a pre-trained model, the weights file would be included as an Artifact. These artifacts can be uploaded via one of the following:

    1. local directory or path
    2. dl.Item
    3. Git repository
    4. other link

    ### The Model adapter

    The model adapter is a Python class that creates a single API between Dataloop's platform and your model. The `ModelAdapter` class contains standardized methods that make it possible to integrate models into other parts of the Dataloop platform. Model adapters allow the following model functions:
    1. train
    2. predict
    3. load/save model weights
    4. annotation conversion (if needed)

    ## Model comparison

    All Dataloop models can be viewed in one place, and different model versions can be compared and evaluated with user-selected metrics. This way the data scientist can keep track of their models easily, experiment without worries, and pick the best models.

    ### Offline vs online mode

    Model management can be used in two modes: offline (for local model training) or online (for integration into the Dataloop platform).

    In "offline" mode, users can run and train models on their local machine using local data, and can compare model configurations and metrics on the platform. “Offline” requires minimal platform integration, and can be used after dl.Package and dl.Model entities are created. This mode allows only visualizing metrics exported from the (local) model training session. In “offline” mode, code and weights are not saved anywhere in the Dataloop platform. Only model metrics are saved and viewable at a later time.

    ![image](https://user-images.githubusercontent.com/58508793/230951041-06544b46-1cce-4f87-9980-10dd7794b1c4.png)

    In "online" mode, models can be trained to be deployed anywhere on the platform. For example, you can easily create a button interface to use your model to inference on a new data Item and view it on the platform. To do this, you need to create a `ModelAdapter` class and implement the required functions to build the Dataloop API.

    **Note:** The “Online” mode also includes all the platform features mentioned above in the “offline” mode.
    """

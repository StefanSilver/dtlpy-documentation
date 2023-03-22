def func1():
    """
    # FaaS Docker Image

    Dataloop enables you to deploy a custom Docker image in the FaaS module , to enrich your application with literally anything required for your Project. Deploying a Docker image is as easy as providing the Docker image path when deploying the Service:
    """


def func2():
    """
    In some cases, you may only want to  update an existing Service. To do that, you can use the code below:
    """


def func3():
    """

    ## Our Docker Image

    We have our list of Docker images publicly available in [Dockerhub](https://hub.docker.com/repository/registry-1.docker.io/dataloopai/dtlpy-agent/tags).

    ## Public Docker Images

    You can use any public Docker image, and the Dataloop agent will install the following at runtime:

    1. Package requirements;
    2. dtlpy Package (version as defined on the Service);
    3. dtlpy-agent (same version as the SDK).

    For example, using `docker.io/python:3.9.13` will run the function with Python 3.9.

    ## Build Your Own Docker Image

    If you want another environment or need to add some apt-get installation, you can create any Docker image and use it directly.
    You will need to set the HOME directory to `/tmp` and install the python packages with `--user` (or as USER 1000). For example:
    ```
    FROM dockerhub.io/dataloopai/dtlpy-agent:latest.gpu.cuda11.5.py3.8.opencv

    RUN apt update && apt install -y zip ffmpeg

    USER 1000
    ENV HOME=/tmp
    RUN pip3 install --user \
        dtlpy==1.54.10 \
        dtlpy-agent==1.54.10 \
        torch \
        torchvision \
        imgaug \
        scikit-image==0.17.2
    ```

    ## Using Private Docker Registry

    To connect a private registry, you'll need to add the Docker container registry credentials as an Organization Secret (ONLY in the UI version) and just use the runner image.

    """

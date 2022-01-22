# Containers, Docker and Kubernetes Workshop

As a Software Developer, my day to day job includes building Applications, APIs, etc. I use some of the popular frameworks such as Python Flask, NodeJs to build the applications or APIs. I could Code an Application and running it in my machine, excellent! Thats what I learn't in my college. And if a friend of mine asks for the Application, sure here is a github link to it just make sure you download it and then run pip install dependencies or npm install dependencies. As Naive as I sounded, I realised that is not how you distribute an application, there are certain best practices such as Containerizing the Application and deploying it on a Kubernetes cluster. Hence I started to learn about Containers, Docker and Kubernetes. I used to face challenges quite often. Challenges such as not knowing how to write a dockerfile, dockerfile failed to build, even if it built successfully the image size would be large, not knowing to write deployment scripts, unable to access the deployed app from kubernetes cluster and the list goes on. Hence I decided to create a simple workshop that covers the following:

In this workshop, You will learn to build a basic python flask app or a basic NodeJs Express app, containarize it, store it in container registry, write a deployment script and deploy it on a kubernetes cluster.

## Pre-requisite

1. [Python 3.x](https://www.python.org/downloads/)
1. [Docker Account](https://hub.docker.com/)
1. [Docker CLI](https://docs.docker.com/get-docker/)
1. [Kubernetes Cluster]()
1. [Kubectl CLI](https://kubernetes.io/docs/tasks/tools/)

# Steps

1. [Developing a basic Flask or NodeJs Application](#developing-a-basic-flask-or-nodejs-application)
1. [Containerizing the Application](#containerizing-the-application)
1. [Storing the Container Image in a Container Registry](#storing-the-container-image-in-a-container-registry)
1. [Writing the deployment scripts](#writing-the-deployment-scripts)
1. [Deploying the Application on a Kubernetes Cluster](#deploying-the-application-on-a-kubernetes-cluster)

## Developing a basic Flask or NodeJs Application

<details><summary><b>Python Flask App</b></summary>

- As a best practice create a Virtual Environment to get started. In terminal, run the following command:

    ```bash
    virtualenv venv
    ```

- Once the virtualenv is created, source into the venv by running the following command:

    ```bash
    source venv/bin/activate
    ```

- You will see the prompt change to `(venv)`.

    ```
    (venv)$
    ```

- Create an `app.py` file by running the following command:

    ```bash
    touch app.py
    ```

- Since we are building a flask app make sure to install the flask library, by running the following command:

    ```bash
    pip install flask
    ```

- Open the `app.py` in your favourite code editor.
  - Import the flask module

    ```python
    from flask import Flask
    ```

  - Set app context

    ```python
    app = Flask(__name__)
    ```

  - Define a route for `/`

    ```python
    @app.route('/')
    def index():
        return "<h1 align='center'>Hello World from Python Flask!</h1>"
    ```

  - Finally set the flask run

    ```python
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
    ```

- Your `app.py` file should look something like this:

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return "<h1 align='center'>Hello World from Python Flask!</h1>"

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=True)
    ```

- Save the file. Back to terminal, run the following command to start the application and check whether it works

    ```bash
    python app.py
    ```

    ```
    * Serving Flask app "app" (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 812-299-939
    ```

- Visit `http://0.0.0.0:8080/` on your browser or run the following command:

    ```bash
    curl http://0.0.0.0:8080
    ```

    ```
    <h1 align='center'>Hello World from Python Flask!</h1>
    ```

- If you see `Hello World` message, congrats you have successfully built the basic flask application.

</details>

<details><summary><b>NodeJs Express App</b></summary>

</details>

## Containerizing the Application

<details><summary><b>Python Flask App</b></summary>

- Create a `Dockerfile`. In terminal, run the following command:

    ```bash
    touch Dockerfile 
    ```

- Create a python library requirements file by running the following command:

    ```bash
    pip freeze > requirements.txt 
    ```

- This will create a `requirements.txt` file in the same directory which will contain all the dependencies for the project.

- Open the `Dockerfile` in your favourite code editor.
  - Define a base image

    ```dockerfile
    FROM python:3.9-slim
     ```

  - Create a working directory

    ```dockerfile
    WORKDIR /app
    ```

  - Add the `app.py` and `requirements.txt` file to the working directory

    ```dockerfile
    ADD . /app
    ```

  - Install the python dependencies

    ```dockerfile
    RUN pip install --trusted-host pypi.python.org -r requirements.txt
    ```

  - Expose the flask access port

    ```dockerfile
    EXPOSE 8080
    ```

  - run the python run command

    ```dockerfile
    CMD ["python", "-u", "app.py"]
    ```

- Your Dockerfile should look something like this:

    ```dockerfile
    FROM python:3.9-slim

    WORKDIR /app

    ADD . /app

    RUN pip install --trusted-host pypi.python.org -r requirements.txt

    EXPOSE 8080

    CMD ["python", "-u", "app.py"]
    ```
</details>

<details><summary><b>NodeJs Express App</b></summary>

</details>

- Save the file. Back to terminal, run the following command to build a container image for the application.

    ```bash
    docker build -t sample-app:1.0 .
    ```
    <details><summary><i>Python Output</i></summary>
    ```
    => [internal] load build definition from Dockerfile                            0.0s
    => => transferring dockerfile: 203B                                            0.0s
    => [internal] load .dockerignore                                               0.0s
    => => transferring context: 2B                                                 0.0s
    => [internal] load metadata for docker.io/library/python:3.9-slim              4.1s
    => [auth] library/python:pull token for registry-1.docker.io                   0.0s
    => [internal] load build context                                               0.3s
    => => transferring context: 15.34MB                                            0.3s
    => [1/4] FROM docker.io/library/python:3.9-slim@sha256:7783d80eca13fb9f8cfd8b  5.7s
    => => resolve docker.io/library/python:3.9-slim@sha256:7783d80eca13fb9f8cfd8b  0.0s
    => => sha256:7783d80eca13fb9f8cfd8b84b27ac09ecc28f52bafdd9b94 1.86kB / 1.86kB  0.0s
    => => sha256:9fa920a5e22c494e2c879fee24f72ba0bb842b8e8e7376ac 1.37kB / 1.37kB  0.0s
    => => sha256:afaa64e7c7fe503b643b460295b8621f4709ebd058c55c2b 7.63kB / 7.63kB  0.0s
    => => sha256:69692152171afee1fd341febc390747cfca2ff302f2881 27.15MB / 27.15MB  3.3s
    => => sha256:59773387c0e7ec4b901649cd3530cde9a32e6a76fccaf0b0 2.77MB / 2.77MB  3.0s
    => => sha256:3fc84e535e87f5dfd4ab5a3086531224f67051d7f7853c 10.93MB / 10.93MB  4.2s
    => => sha256:68ebeebdab6f71c7a8dc8532e56ed6d69171502240306980ae78 234B / 234B  4.2s
    => => extracting sha256:69692152171afee1fd341febc390747cfca2ff302f2881d8b394e  1.2s
    => => sha256:ada7ec54b5b23c775e12472f8975b1af576ca949c63a7957 2.60MB / 2.60MB  4.2s
    => => extracting sha256:59773387c0e7ec4b901649cd3530cde9a32e6a76fccaf0b015119  0.2s
    => => extracting sha256:3fc84e535e87f5dfd4ab5a3086531224f67051d7f7853c659d3dd  0.5s
    => => extracting sha256:68ebeebdab6f71c7a8dc8532e56ed6d69171502240306980ae78e  0.0s
    => => extracting sha256:ada7ec54b5b23c775e12472f8975b1af576ca949c63a795703bcf  0.2s
    => [2/4] WORKDIR /app                                                          0.1s
    => [3/4] ADD . /app                                                            0.2s
    => [4/4] RUN pip install --trusted-host pypi.python.org -r requirements.txt    5.7s
    => exporting to image                                                          0.2s
    => => exporting layers                                                         0.2s
    => => writing image sha256:c6e96d921302343506b1c228c5840e4f2ffe20a85c60c2d832  0.0s
    => => naming to docker.io/library/sample-app:v1.0
    ```
    </details>

    <details><summary><i>NodeJs Output</i></summary>
    ```
    ```
    </details>

- If you see no errors, congrats you have successfully containerized the application.

- You can check if the application runs inside the container by running the following command:

    ```bash
    docker run -p 8080:8080 sample-app:v1.0
    ```

- Visit `http://0.0.0.0:8080/` on your browser or run the following command:

    ```bash
    curl http://0.0.0.0:8080
    ```

    ```
    <h1 align='center'>Hello World from Python Flask!</h1
    ```

- If you see `Hello World` message, congrats your containerized application works as expected.

## Storing the Container Image in a Container Registry

Now that you have your application containerized, you can store it in a container registry such as dockerhub. Storing static container images in container registry is required to deploy application on a remote kubernetes cluster.

- Login to docker by running the following command:

    ```bash
    docker login
    ```

    ```
    Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
    Username: manojjahgirdar
    Password:
    Login Succeeded
    ```

- Rename the container image in the format `username/imagename:tag` by running the following command:

    ```bash
    docker tag sample-app:1.0 manojjahgirdar/sample-app:1.0
    ```

- Push the image to docker hub by running the following command:

    ```bash
    docker push manojjahgirdar/sample-app:1.0
    ```
    <details><summary><i>Python Output</i></summary>
    ```
    The push refers to repository [docker.io/manojjahgirdar/sample-app]
    c51c5d086047: Pushed
    c37b64c6b724: Pushed
    af602c0dc044: Pushed
    a765872192e3: Mounted from library/python
    a6dfc8291750: Mounted from library/python
    7e46f0272529: Mounted from library/python
    5359ff267161: Mounted from library/python
    2edcec3590a4: Mounted from library/python
    1.0: digest: sha256:db6ad330c4d5e5df3728b4b3123129e9a0449f0becba21a7b681f8f773d7ba38 size: 1999
    ```
    </details>

    <details><summary><i>NodeJs Output</i></summary>
    ```
    ```
    </details>

- You can check the image in <https://hub.docker.com>

## Writing the deployment scripts

## Deploying the Application on a Kubernetes Cluster
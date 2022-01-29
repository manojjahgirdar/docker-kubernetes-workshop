=== "Python Flask Application"
    ### Containerize Python Flask App
    #### 2.1. Create a Dockerfile

    * Create a `Dockerfile`. In terminal, run the following command:
    ```bash
    touch Dockerfile 
    ```

    * Create a python library requirements file by running the following command:
    ```bash
    pip freeze > requirements.txt 
    ```

    * This will create a `requirements.txt` file in the same directory which will contain all the dependencies for the project.

    * Open the `Dockerfile` in your favourite code editor.
        * Define a base image
        ```dockerfile
        FROM python:3.9-slim
        ```

        * Create a working directory
        ```dockerfile
        WORKDIR /app
        ```

        * Add the `app.py` and `requirements.txt` file to the working directory
        ```dockerfile
        ADD . /app
        ```

        * Install the python dependencies
        ```dockerfile
        RUN pip install --trusted-host pypi.python.org -r requirements.txt
        ```

        * Expose the flask access port
        ```dockerfile
        EXPOSE 8080
        ```

        * Run the python run command
        ```dockerfile
        CMD ["python", "-u", "app.py"]
        ```

    * Your Dockerfile should look something like this:
    ```dockerfile title="Dockerfile" linenums="1"
    FROM python:3.9-slim

    WORKDIR /app

    ADD . /app

    RUN pip install --trusted-host pypi.python.org -r requirements.txt

    EXPOSE 8080

    CMD ["python", "-u", "app.py"]
    ```

    * Save the file.

    #### 2.2. Build Container Image

    * Back to terminal, run the following command to build a container image for the application.
    ```bash
    docker build -t sample-app:v1.0 .
    ```

    * You will see output similar to the following:
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

    * If you see no errors, congrats you have successfully containerized the application.

    * You can check if the application runs inside the container by running the following command:
    ```bash
    docker run -p 8080:8080 sample-app:v1.0
    ```

    * Visit `http://0.0.0.0:8080/` on your browser or run the following command:
    ```bash
    curl http://0.0.0.0:8080
    ```

    * You will see output similar to the following:
    ```
    <h1 align='center'>Hello World from Python Flask!</h1>
    ```

    * If you see `Hello World` message, congrats your containerized application works as expected.

=== "NodeJs Express Application"
    ### Containerize NodeJs Express App
    #### 2.1. Create a Dockerfile

    * Create a `Dockerfile`. In terminal, run the following command:
    ```bash
    touch Dockerfile 
    ```

    * Open the `Dockerfile` in your favourite code editor.
        * Define a base image
        ```dockerfile
        FROM node:16
        ```

        * Create a working directory
        ```dockerfile
        WORKDIR /app
        ```

        * Add the application source code to the working directory
        ```dockerfile
        ADD . /app
        ```

        * Install dependencies
        ```dockerfile
        RUN npm install
        ```

        * Expose the flask access port
        ```dockerfile
        EXPOSE 3000
        ```

        * Run the npm run command
        ```dockerfile
        CMD [ "npm", "start" ]
        ```

    * Your Dockerfile should look something like this:
    ```dockerfile title="Dockerfile" linenums="1"
    FROM node:16

    WORKDIR /app

    ADD . /app

    RUN npm install

    EXPOSE 3000

    CMD [ "npm", "start" ]
    ```

    * Save the file.

    #### 2.2. Build Container Image

    * Back to terminal, run the following command to build a container image for the application.
    ```bash
    docker build -t sample-app:v1.0 .
    ```

    * You will see output similar to the following:
    ```
    => [internal] load build definition from Dockerfile                                        0.0s
    => => transferring dockerfile: 134B                                                        0.0s
    => [internal] load .dockerignore                                                           0.0s
    => => transferring context: 2B                                                             0.0s
    => [internal] load metadata for docker.io/library/node:16                                  5.3s
    => [internal] load build context                                                           0.1s
    => => transferring context: 1.77MB                                                         0.1s
    => [1/4] FROM docker.io/library/node:16@sha256:d3d1a02bab20f7956                          39.3s
    => => resolve docker.io/library/node:16@sha256:d3d1a02bab20f7956                           0.0s
    => => sha256:d3d1a02bab20f7956676ff17e901f7c5054114a902a152cbebd 1.21kB / 1.21kB           0.0s
    => => sha256:842962c4b3a745b6cfc84acf07688a392bcb90af27adb28a6b6 7.60kB / 7.60kB           0.0s
    => => sha256:b6013b3e77fe6fd3dcf46a05f8e5b3afa9fbca7ba0161c62e56 7.83MB / 7.83MB           4.6s
    => => sha256:d87a1f3e0b5b2a684aa101fb7259913a13372626aa1de17398d 2.21kB / 2.21kB           0.0s
    => => sha256:9b99af5931b39ce167150ad668cfa57ddf7664697be9996cb7e 50.44MB / 50.44MB         6.8s
    => => sha256:bbced17b6899896c8e4016d62c885d737fe667acace2733e17c 10.00MB / 10.00MB         3.5s
    => => sha256:8b609dabefa83fae157bcd42123a8ed45199bb6c301e09a1126 51.84MB / 51.84MB        16.2s
    => => sha256:50544bfef33d1d653b7bc10316e20bd84889fd56dd2b7e2f742 192.43MB / 192.43MB      30.2s
    => => extracting sha256:9b99af5931b39ce167150ad668cfa57ddf766469                           2.1s
    => => sha256:fea3f8b8e0752b4518bab41fb3fa31db44fceb625894b117f3e 4.20kB / 4.20kB           7.1s
    => => sha256:9e4e229021eebc9d3673e52ada928bc35ba736634fd90c021c5 33.36MB / 33.36MB        16.7s
    => => extracting sha256:b6013b3e77fe6fd3dcf46a05f8e5b3afa9fbca7b                           0.3s
    => => extracting sha256:bbced17b6899896c8e4016d62c885d737fe667ac                           0.3s
    => => sha256:971c8efc250bdf861d7751378b93dd39d0143f59583b44ce152 2.27MB / 2.27MB          17.6s
    => => extracting sha256:8b609dabefa83fae157bcd42123a8ed45199bb6c                           2.4s
    => => sha256:3e9d4bc41c274ff79bb76a3ae8553a7932ff87e2401e7ea6c61 449B / 449B              17.4s
    => => extracting sha256:50544bfef33d1d653b7bc10316e20bd84889fd56                           7.0s
    => => extracting sha256:fea3f8b8e0752b4518bab41fb3fa31db44fceb62                           0.1s
    => => extracting sha256:9e4e229021eebc9d3673e52ada928bc35ba73663                           1.3s
    => => extracting sha256:971c8efc250bdf861d7751378b93dd39d0143f59                           0.1s
    => => extracting sha256:3e9d4bc41c274ff79bb76a3ae8553a7932ff87e2                           0.0s
    => [2/4] WORKDIR /app                                                                      0.1s
    => [3/4] ADD . /app                                                                        0.1s
    => [4/4] RUN npm install                                                                   2.3s
    => exporting to image                                                                      0.1s
    => => exporting layers                                                                     0.1s
    => => writing image sha256:9d26c44d4e20a81041771d79d6af41b348504                           0.0s
    => => naming to docker.io/library/sample-app:1.0                                           0.0s
    ```

    * If you see no errors, congrats you have successfully containerized the application.

    * You can check if the application runs inside the container by running the following command:
    ```bash
    docker run -p 3000:3000 sample-app:v1.0
    ```

    * Visit `http://0.0.0.0:3000/` on your browser or run the following command:
    ```bash
    curl http://0.0.0.0:3000
    ```

    * You will see output similar to the following:
    ```
    <h1 align='center'>Hello World from NodeJs Express!</h1>
    ```

    * If you see `Hello World` message, congrats your containerized application works as expected.
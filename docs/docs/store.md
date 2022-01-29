### 3.1. Push the container image to DockerHub

Now that you have your application containerized, you can store it in a container registry such as dockerhub. Storing static container images in container registry is required to deploy application on a remote kubernetes cluster.

* Login to docker by running the following command:

```bash
docker login
```

* You will see output similar to the following:

```
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: manojjahgirdar
Password:
Login Succeeded
```

* Rename the container image in the format `username/imagename:tag` by running the following command:

```bash
docker tag sample-app:v1.0 <username>/sample-app:v1.0
```

* Push the image to docker hub by running the following command:

```bash
docker push <username>/sample-app:v1.0
```

* You will see output similar to the following:
    ```text title="Python Flask Output"
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

    ```text title="NodeJs Express Output"
    The push refers to repository [docker.io/manojjahgirdar/sample-app]
    166293c07cb0: Pushed
    c01bf11fccb2: Pushed
    56034ba0dab4: Pushed
    70b4fdd67645: Mounted from library/node
    b77fe0f00494: Mounted from library/node
    9b5ca33009b8: Mounted from library/node
    75b4edf780e2: Mounted from library/node
    126712f9d0fb: Mounted from library/node
    330a6fb3364f: Mounted from library/node
    b20560b6a21c: Mounted from library/node
    a1215953fc64: Mounted from library/node
    b14cb48b3aeb: Mounted from library/node
    v1.0: digest: sha256:e15a8a285030922451616efb88bb2362a302fcbd4f9032e080534f464fde343b size: 2841
    ```

- You can check the image in <https://hub.docker.com>

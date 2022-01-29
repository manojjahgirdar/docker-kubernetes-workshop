=== "Python Flask Application"
    ### Python Flask App Deployment Script
    #### 4.1. Create a Deployment

    * Create a `deploy.yaml` file. In terminal, run the following command:
    ```bash
    touch deploy.yaml
    ```

    * Open the `deploy.yaml` file in your favourite code editor.
        * Set the API version to `v1` and the kind to `Deployment`.
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        ```

        * Define the metadata for the deployment.
        ```yaml
        metadata:
          name: sample-app
          labels:
            app: flask
        ```

        * Define the spec for the deployment. Add the container image name as a value for the `image:` key.
        ```yaml hl_lines="13"
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: flask
          template:
            metadata:
              labels:
                app: flask
            spec:
              containers:
              - name: sample-app
                image: <username>/sample-app:v1.0
                ports:
                - containerPort: 8080
        ```

    * Your `deploy.yaml` file should look something like this:
    ```yaml title="deploy.yaml" linenums="1"
    apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
    kind: Deployment
    metadata:
      name: sample-app
      labels:
        app: flask
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: flask
      template:
        metadata:
          labels:
            app: flask
        spec:
          containers:
          - name: sample-app
            image: <username>/sample-app:v1.0
            ports:
            - containerPort: 8080
    ```

    * Save the file.

    #### 4.2. Create a Service

    * Create a `service.yaml` file. In terminal, run the following command:
    ```bash
    touch service.yaml
    ```

    * Open the `service.yaml` file in your favourite code editor.
        * Set the API version to `v1` and the kind to `Service`.
        ```yaml
        apiVersion: v1
        kind: Service
        ```

        * Define the metadata for the deployment.
        ```yaml
        metadata:
          name: my-flask-app-service
        ```

        * Define the spec for the deployment.
        ```yaml
        spec:
          selector:
            app: flask
          ports:
          - protocol: TCP
            port: 8080
            targetPort: 8080
            nodePort: 32200
          type: NodePort
        ```

    * Your `service.yaml` file should look something like this:
    ```yaml title="service.yaml" linenums="1"
    apiVersion: v1
    kind: Service
    metadata:
      name: my-flask-app-service
    spec:
      selector:
        app: flask
      ports:
      - protocol: TCP
        port: 8080
        targetPort: 8080
        nodePort: 32200
      type: NodePort
    ```

    * Save the file.

=== "NodeJs Express Application"
    ### NodeJs Express App Deployment Script
    #### 4.1. Create a Deployment

    * Create a `deploy.yaml` file. In terminal, run the following command:
    ```bash
    touch deploy.yaml
    ```

    * Open the `deploy.yaml` file in your favourite code editor.
        * Set the API version to `v1` and the kind to `Deployment`.
        ```yaml
        apiVersion: apps/v1
        kind: Deployment
        ```

        * Define the metadata for the deployment.
        ```yaml
        metadata:
          name: sample-app
          labels:
            app: express
        ```

        * Define the spec for the deployment. Add the container image name as a value for the `image:` key.
        ```yaml hl_lines="13"
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: express
          template:
            metadata:
              labels:
                app: express
            spec:
              containers:
              - name: sample-app
                image: <username>/sample-app:v1.0
                ports:
                - containerPort: 3000
        ```

    * Your `deploy.yaml` file should look something like this:
    ```yaml title="deploy.yaml" linenums="1"
    apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
    kind: Deployment
    metadata:
      name: sample-app
      labels:
        app: express
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: express
      template:
        metadata:
          labels:
            app: express
        spec:
          containers:
          - name: sample-app
            image: <username>/sample-app:v1.0
            ports:
            - containerPort: 3000
    ```

    * Save the file.

    #### 4.2. Create a Service

    * Create a `service.yaml` file. In terminal, run the following command:
    ```bash
    touch service.yaml
    ```

    * Open the `service.yaml` file in your favourite code editor.
        * Set the API version to `v1` and the kind to `Service`.
        ```yaml
        apiVersion: v1
        kind: Service
        ```

        * Define the metadata for the deployment.
        ```yaml
        metadata:
          name: my-express-app-service
        ```

        * Define the spec for the deployment.
        ```yaml
        spec:
          selector:
            app: express
          ports:
          - protocol: TCP
            port: 80
            targetPort: 3000
            nodePort: 32201
          type: NodePort
        ```

    * Your `service.yaml` file should look something like this:
    ```yaml title="service.yaml" linenums="1"
    apiVersion: v1
    kind: Service
    metadata:
      name: my-express-app-service
    spec:
      selector:
        app: express
      ports:
      - protocol: TCP
        port: 80
        targetPort: 3000
        nodePort: 32201
      type: NodePort
    ```

    * Save the file.

!!! info "Learning Materials"
    - [Yaml Checker](https://yamlchecker.com) provides a quick and easy way to validate YAML
    - Learn more about [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
    - Learn more about [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/)
    - Learn more about [Kubernetes Pods](https://kubernetes.io/docs/concepts/workloads/pods/)

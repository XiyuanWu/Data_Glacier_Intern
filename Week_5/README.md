# Week 5 - Deployment on Cloud

This week's material is about deploying a model on cloud. 

Presentation mode [here](https://gamma.app/public/ML-Model-Deployment-Cloud-upg2quwrfl1h5sg).


# Note

Please note to deploy in the cloud, we also need a `.dockerignore` file, but Github blocked this file. After you download the file, you need to create a new file exactly named `.dockerignore` (note there is a dot in front of it), and paste the following code in:
```
Dockerfile
README.md
*.pyc
*.pyo
*.pyd
__pycache__
.pytest_cache
```
For mode information, check google [site](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?hl).

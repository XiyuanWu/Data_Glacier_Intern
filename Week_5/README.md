# Week 5 - Deployment on Cloud

This week's material is about deploying a model on the cloud.


# Note

Please note, in order to deploy in cloud, we also need `.dockerignore` file, but this file was block by Github. After you download file, you need create a new file exactly name `.dockerignore` (note there are a dot in front of it), and paste following code in:
`
Dockerfile
README.md
*.pyc
*.pyo
*.pyd
__pycache__
.pytest_cache
`
For mode information, check google [site](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?hl).
# Week 5 - Deployment on Cloud

This week's material is about deploying a model on cloud. 

Presentation mode [here](https://gamma.app/public/ML-Model-Deployment-Cloud-upg2quwrfl1h5sg).

1. Select any toy data (simple data) (You are allowed to use data set of week 4)
2. Save the model (You are allowed to use model of week 4)
3. Deploy the model on any cloud eg: Heroku,AWS,GCP,Azure (Deployment should be API based as well as web app)
4. Create pdf document (Name, Batch code, Submission date, Submitted to ) which should contain snapshot of each step of deployment
5. Upload the document and code to Github
6. Submit the URL of the uploaded document


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

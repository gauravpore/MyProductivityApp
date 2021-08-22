# 🔹MyProductivityApp
### 📌Click [here](https://drive.google.com/file/d/1NkTVstCDgjh42h6_RkSA0aYnZOIQudFL/view?usp=sharing) to watch the demo of the project.
## 🔸Overview:
A to-do list app lets you write, organize, and prioritize your tasks more efficiently. They also let you to manage, priortize and set deadlines for your tasks, hence resulting in more productivity. This repository contains all neccesary files for the MyProductivity App which is basically a Django Application built with APIs (Class-based views), to enable CRUD operations and basic HTML/CSS for client-side (frontend) User interface. Additionaly this application has User-Authencation system to save user-specific tasks. Go through the whole read.md (documentation) to undersatnd the working architecture and other features more clearly.

## 🔸**Concepts:**
- Back-end Development
- API Development
- Djang Development
- CRUD Operations
- SDLC

## 🔸**Tools & Technologies:**
- Python 3
- [Django](https://www.djangoproject.com/start/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Postman API Platform](https://learning.postman.com/docs/getting-started/introduction/)
- HTML/CSS
- Sqlite3
- Git Bash
- PyCharm
- [Anaconda Environment](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#:~:text=A%20conda%20environment%20is%20a,NumPy%201.6%20for%20legacy%20testing.)

## 🔹Working:

- This is a To Do list application that allows user to manage his/her tasks more efficiently.
- The App uses Django for back-end support and sqlite3 database to store the models data. 
- The app is developed using Class-based views, that allows a convenient and faster way to produce the application.
- MyProductivityApp can store multiple users and secured authentication functionality
- Its a complete application with an attractive user-interface which allows user to interact with the application in a better way.

### 🔸**Features:**
```
1. User can login/logout to his/her account using email/password auth and can also register new account, if the user does not exist.
2. User can perform basic CRUD operations , i.e Create | Update | Delete the ToDo list.
3. Users can add new tasks & also delete existing tasks from their respective list.
4. The Application provides a convenient way to priortize the tasks accorrding to user's need, just by dragging and shuffling the task within the list.
5. User can set deadlines for each specific tasks, using DateTimeZone functionality, which can result in good productivity.
6. User can comment on task, i.e add a good neat description for each task.
7. User can mark the task as DONE, once completed, just by selecting done button.
8. User can edit the description as well.
9. The Application has a good responsive SEARCH functionality to search the existing tasks by prefixing the starting letter.
10. Lastly, the application offers an attractive interface to interact.
```
> **🔸Installation Guide:**
- To install django:
```
pip install django
```
- T0 install Django REST Framework:
```
pip install djangorestframework
```
- To run the application on local Port 8000:
```
py manage.py runserver
```

- Refer [this](https://docs.djangoproject.com/en/3.2/) to know more about important commands.

## 🔹Application Back-end:
- I have developed the APIs to perform CRUD operations using Django REST Framework. You can find the source files on ['initial']() branch. Refer [this](https://www.section.io/engineering-education/django-crud-api/) article to get started with same.
- The postman collections can be found [here](). Refer [this](https://learning.postman.com/docs/getting-started/introduction/) to get started with Postman.
- The final application uses Class-based Views as it offers execellent default views like Login/Logout view, redirect view, etc, which results in faster development process & more importantly saves time. Refer [this](https://docs.djangoproject.com/en/3.1/ref/class-based-views/) for more understanding.
- Django provides in-built functionality for User-Authentication and User-Registration form. Refer [this](https://docs.djangoproject.com/en/3.2/topics/auth/) to implement User Auth.

## 🔹Deployment Guide:
### ☁️ PythonAnywhere:
[Pythonanywhere](https://www.pythonanywhere.com/) is a cloud platform, that offers free web-hosting for Python-Django Apps. Follow [this](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/) article to host the application with just few steps.
### <em> 📌NOTE: MyProductivityApp will be deployed soon on PythonAnywhere platform. </em>
### ☁️ AWS:
We can use following [Amazon Web Services](https://aws.amazon.com/) to deploy our application rapidly:
- [Elastic BeanStalk](https://aws.amazon.com/elasticbeanstalk/) || Follow [this](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) steps
- [Amazon Lightsail](https://aws.amazon.com/lightsail/)  || Follow [this](https://aws.amazon.com/getting-started/hands-on/deploy-python-application) steps 

## 🔹References | Articles | Documentation:
-  [Django docs](https://www.djangoproject.com/start/)
-  [Django REST Framework docs](https://www.django-rest-framework.org/)
-  [Anaconda Environment docs](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#:~:text=A%20conda%20environment%20is%20a,NumPy%201.6%20for%20legacy%20testing.)
-  [CRUD operation article](https://www.section.io/engineering-education/django-crud-api/)
- [Postman API Platform docs](https://learning.postman.com/docs/getting-started/introduction/)
- [User-Authentication django docs](https://docs.djangoproject.com/en/3.2/topics/auth/)
- [Deployment steps article](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)

## 🔹Screenshots:
 #### Login page:
![alt tag](https://github.com/gauravpore/MyProductivityApp/blob/finalApp/Snips/login.png "login page")

#### 🔸Applucation UI:
![alt tag](https://github.com/gauravpore/MyProductivityApp/blob/finalApp/Snips/AppUI.png "App UI")

#### 🔸Description:
![alt tag](https://github.com/gauravpore/MyProductivityApp/blob/finalApp/Snips/description.png "description")

#### 🔸API:
![alt tag](https://github.com/gauravpore/MyProductivityApp/blob/finalApp/Snips/REST.png  "REST API")

        



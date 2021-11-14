# Tech Dive Blog

A web application blog built using Django Web Framework.

My aim was to keep it as simple as possible while also making it similar to a real blog.

# Features
  * User authentication
  * postgresql database 
  * blog system - creating and deleting blog posts
  * a comment functionality so authenticated users can comment on posts
  * markdown html text formatting
  
Boostrap cdn was used for the styling, although I paid  less attention to the frontend part of 
the project as my focus was on Django.

For the views, I utilized the power of Class Based Views and the flexibility of Function Based Views

# If you are interested in improving this project

Just fork the project and clone into your local machine.

Create  a virtual environment
I used: <addr> python -m virtualenv virtualenv<addr> 

Activate the virtual environment
``` 
cd virualenv/scripts

activate 
```

For clarity, the apps are placed in a dedicated 'apps' folder to ease workflow. 
The following code snipet allows the project to work just fine like nothing changed:
```
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR,'apps'))
```
All imports should be done like normal. Example:

 ```
INSTALLED_APPS = [
    ...
    'the_blog.apps.TheBlogConfig',
    'account.apps.AccountConfig',

    ...
]
```

# If i had more time, I would:
  * add javascript funtionalities to the frontend
  * add email verification for users upon signup
  * add a password change and password reset functionality
  


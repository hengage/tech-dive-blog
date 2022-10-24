# Tech Dive Blog

A web application blog built using Django Web Framework.
[https://techdive.herokuapp.com/](https://techdive.herokuapp.com/)

# Features
  * user authentication
  * postgresql database 
  * blog system - creating and deleting blog posts
  * a comment functionality so authenticated users can comment on posts
  * markdown html text formatting
  * search for posts by post title 
  * password change and reset
  
Boostrap was used for the styling.

For the views, I utilized the power of Class Based Views and the flexibility of Function Based Views


Fork the project and clone into your local machine.

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
 
Situated at the top part of the settings file.
All imports should be done like normal. Example:

 ```
INSTALLED_APPS = [
    ...
    'the_blog.apps.TheBlogConfig',
    'account.apps.AccountConfig',

    ...
]
```
  


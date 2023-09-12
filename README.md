
# **Monthesorri Inspired**

Montessori Inspired is a website created for parents who are interested in raising their children with a Montessori method of education.
After logging in, all visitors can write reviews and comment on other users' content.
All comments and posts require approval by the administrator, who is responsible for ensuring that everyone feels safe from abuse, inappropriate language, etc. Approvals are made from the administration panel. The site has a clean design that makes it easy for users to navigate.

[Live Project Here](https:/)

(photo of the website)

README Table Content

* [**Montessori Inspired - Introduction**](<#montessori-inspired--introduction>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
    * [Agile Methodology](<#agile-methodology>)
    * [Main Site Goals](<#main-site-goals>)

* [**User Experience (UX)**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)
      - [Colours](#colours)
      - [Typography](#typography)
      - [Imagery](#imagery)
      - [Database Diagram](#database-diagram)

* [**Existing Features**](<#existing-features>)
    * [Home Page](#home-page)
    * [Navbar](<#navigation>)
    * [About](<#about>)
    * [Blog Page](#blog-page)
    * [Post Detail Page](#post-detail-page)
    * [Delete/Edit Comment](#deleteedit-comment)
    * [Categories Page](#categories-page)
    * [Search Box](#search-box)
    * [Search Results Page](#search-results-page)
    * [Signup Page](#signup-page)
    * [Login Page](#login-page)
    * [Logout Page](#logout-page)
    * [User Profile Page](#user-profile-page)
    * [Footer](<#footer>)
    * [Like Post](#like-post)
    * [Unlike Post](#unlike-post)
    * [Comment Post](#comment-post)
   

* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks & Software](<#frameworks--software>)
    * [Libraries](<#libraries>)
    *  [Django Packages](#django-packages)


* [**Testing**](<#testing>)
    * [Testing User Stories](<#testing-user-stories>)
    * [Code Validation](<#code-validation>)
    * [Additional Testing](<#additional-testing>)
    * [Known Bugs](<#known-bugs>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

## Montessori-inspired-introduction

Project milestone 4 for Code Institute Full-stack development program.
This project is a Full Stack website built using the Django framework.
Montessori Inspired is a website created for parents who are interested in raising their children with a Montessori method of education.
They can find here practical tips and information about this method for everyday life.
When the user is logged in they can also like/unlike a post and comment on a post.
Parents can also share their information by adding a post and uploading or updating their user image and details.


[Back to top](<#contents>)

## Site-users-goal
The Monessori Inspired user is interested in the Montessori philosophy and wants to implement this method in his home, in raising his children. The blog is a place where she can learn more about Montessori, interact with other parents, and share her knowledge with like-minded parents.


## Site-owners-goal
The website owner's goal is to provide a website where users will be able to read about Montessori-related topics and add their own posts and comments in an easy and accessible way.


[Back to top](<#contents>)

## Agile-methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/…)

## Main Site Goals

* Give users a good experience while using the website.
* Give users an intuitive to use and easy to navigate website.
*  Give users a website pleasant to look at and with valuable content.
* Give users a website with a clear purpose.
* Give role-based permissions that allows user to interact with the website.


[Back to top](<#contents>)

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User |  I can immediately understand the purpose of the site so that I can decide if it meets my needs. | &check; |
| As a Site User |  I can intuitively navigate around the site so that I can find content and understand where I am on the site | &check; |
| As a Site User | I can see a list of posts so that I can select the one that I want to read. | &check; |
| As a Site User | I can click on a post and read the full content. | &check; |
| As a Site User | I can see the number of likes on every post so that I can see which is the most popular or viral | &check; |
| As a Site User | I can navigate easy on the site through paginated list of posts so that I feel comfortable using the site | &check; |
| As a Site User | I can view comments on a specific post so that I can read the conversations between different users on the site | &check; |

### After loggin-in to the website:
|  | | |
|:-------:|:--------|:--------|
| As a Site User | I can sign up an account so that I can like and comment on posts, create a profile page, create own posts and edit / remove my posts | &check; |
| As a Site User | I can edit my comment so that I can change the content if I want to | &check; |
| As a Site User | I can remove my comment so that I have full control of my comments| &check; 
| As a Site User | I can choose to see my own posts so that I can find them easily | &check; |
| As a Site User | I can log out from the site so that I can feel safe that nobody can access my information | &check; |
| As a Site User | I can edit my profile, so that I can keep the information up to datee | &check; |
| As a Site User | I can  see my login status so that I know if I'm logged in or out | &check; |
| As a Site User | I can delete my account so that I can remove my details and posts if needed | &check; |
| As a Site User | I can like/unlike posts that I enjoyed/I didn’t enjoy so that I can interact with the content| &check; |
| As a Site User | I can log out from the website| &check; |

### As a website Admin:
|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can log out from the site so that I can feel safe that nobody can access my information | &check; |
| As a Site Admin | I can create, read, update, and delete posts so that I can manage my blog content | &check; |
| As a Site Admin | I can approve posts so that I can secure good quality of the content | &check; |
| As a Site Admin | I can approve and disapprove comments so that I can secure a safe environment for the Site Users | &check; |
| As a Site Admin | I can create drafts of my posts that they can be reviewed and finalized later | &check; |
| As a Site Admin | I can access an admin area so that I can get a general understanding of logged in users, number of likes and number of posts | &check; |


[Back to top](<#contents>)


### User Experience (UX)

## Wireframes

TThe Wireframes were created by me by hand. Drawing gives me more flexibility and is for me more comfortable to make a chanages during the process.


## Site-structure

The Montessori Inspired site gives different options, depending if a user is logged in or logged out.
Depending on login status different pages are available for the user. When the user is logged out the pages: *home page*, *about*, *blog*, *search page* are available.
When the user is logged in, he can use the above-mentioned websites but has additional new options: *my posts* and *add post* and *profile page* are available.
As I mentioned before the site is a minimalistic, clean, and intuitive design that makes the site easy to navigate for the user.


[Back to top](<#contents>)

## Design


The site has a very simple and minimalistic design which was chosen by me on purpose. Users can move on the page very intuitively and easily find the content that they are searching for. I wanted to bring a sense of calm when the user is visiting the website.

## Colours
Colour palette from Coolors

![Colour Palette](<static/images/ImgReadMeFile/page colors.png>)


The selected colors are warm and natural, which is related to the Montessori philosophy, where users mainly use natural wooden materials as toys, tools, or interior decoration. The colors are supposed to refer to this.
 
The colors of the website are mainly cream, light pink, light gray and brown. The colors chosen are quite neutral and calming.


I also wanted to ensure there was good contrast between the background colors and text at all times to ensure the user felt comfortable while navigating the site.


[Back to top](<#contents>)


## Typography

The fonts used for the site are 'Roboto' and 'Lato'.

* 'Roboto' is a very clean font that works really well, it's easy to read and matches the minimalistic style that I wanted the site to 'breath'.

* 'Lato' has a nice design and works really well for longer paragraphs of text.

* 'Font-Monospace' -to change a selection of particular text.

## Imagery

All the images are related to Montessori Philosophy and the website design.
All other images will be uploaded by the authors to the database.

## Database-diagram

I used Canva to create a database schema to visualize the types of custom models needed for the project.
I used it as a guide to what needed to be added to each model.
The relationship between Post, Author, Category, User Profile, and Comment are shown in this diagram.

* **Category** - Handles categories.
* **Post** - Handles all the reviews.
* **Comment** - Handles all the comments.
***Author**- Handel's info about the author.
* **UserProfile** - Handles the user profile information (first name, last name, presentation, and featured image for the specific user/reviewer).

![[ER Diagram]](<static/images/ImgReadMeFile/date diagram.png>)

[Back to top](<#contents>)

# Features

## Home Page

* The home page gives a short message explaining what the website is about and what the Montessori philosophy is.
The hero section contains scrolling imagees,wich are related to Montessori education. Changin photos add dynamics and encourage the user to learn more about the blog's topic. There is a button in the photo that takes the user to the blog page.

[Back to top](<#contents>)

## Navbar

* The navigation bar is very clean and straight forward and easy to use. Iis present at the top of every page and navigates all links to the respective pages.
The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

*Links that are visible to not loged-in user:*

* About - Includes information about Monessori Inspired.
* Blog - Lists of all posts.
* Login / Sign Up - Gives the user the opportunity to log in or sign up if not ready a registered user at Review | Alliance.
* Search Box - allowes the user to search of particular content.

*Links that are visible to loged-in user:*

* My space- after collapsing will allows user to got to: the users profile, users posts or add a new post.

[Back to top](<#contents>)

## About

* The About Page gives, users information about the author and and it makes an introduction to the Montessori Inspired. It explains as well the main purpose of the blog.<br>

![About]()

## Blog Page

* On the Blog Page, users have access to all posts available on the website. The user can choose which post to read by clicking on the post card.
The blog posts is paginated in a way that 9 posts are displayed. Further post can be accessed by clicking next button. Each blog post shows the image related to the post content. The user can see the post title with specific fields and sliced post content along with the name of author, submitted date and shows the number of likes and comment icon.

![Blog Page]()

## Post-detail-page

* On the top of the Post Detail Page, users can see the post's main image and they can also have access to information about the post like category,  author name, posted date, and the option to like/unlike the post. It will also show how many likes and comments the post has received.<br>
The author of posts/ comments will have the option to edit or delete them.

![Post Detail Page - Top]()

## Delete/Edit Comment

![Edit Comments Page](./assets/readme/features/tasty_blog_edit_comments_page.jpg)

* On this page, users are allowed to edit their own comments. The website superuser can delete or update any comments on the blog without having to access the admin panel.

## Search Results Page

* After entering the word that the user is looking for, the person will be redirected to the search results page.
On the Search Results Page, users can see the posts found by their search.  When their post is found, the user can go to the
  Post Details Page by clicking on the card result.
* If there are No Results Found, users will see the message informing them about this

![Seach page](<static/images/ImgReadMeFile/search page.png>)


## Signup Page

* If the site visitor has no registered yet, they can sign upThe user is asked to enter a username and password to sign up.
If the username exists or the password is too small the user will be guided by validation messages which were created by modifying Django inbuilt templates.

## Login Page

* On the Login Page, the users can log in to the website by placing the username and password. After that, they have access
  to website services registered  for a user.

## Logout Page

* On this page, the users can confirm that they wish to exit the website.

## User Profile Page

* On the Profile Page, users have access to their own information and can update their user name, email and profile image.

## New Post Page



## Footer

* The footer is simple and estetic. In this section user can find links to Facebook, Instagram and Youtube.
  Clicking the links in the footer opens a separate browser.

## Like Post

* When users are logged in to the website they can like a post.<br>

## Unlike Post

*When users are logged in to the website they can unlike a post.


## Comment Post



* On Edit Page, loged-in users have an option to leave their comment, delete and edit them. The website superuser can 
  delete or update any comments on the blog.

# Technologies Used

## Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)- Used to structure all the templates on the site
* [CSS 3](https://en.wikipedia.org/wiki/CSS)- to provide extra styling to the site
* [JavaScript](https://www.javascript.com/)- Minimum javascript was used to fade out alerts after a few seconds.
* [Python](https://www.python.org/)- To provide the functionality to the site. Packages used in the project can be found in requirements.txt

## Django Packages

* [Gunicorn](https://gunicorn.org/)- As the server for Heroku.
* [Cloudinary](https://cloudinary.com/)- Was used to host the static files and media for the site.
* [Dj_database_url](https://pypi.org/project/dj-database-url/)- To parse the database URL from the environment variables in Heroku.
* [Summernote](https://summernote.org/)- As a text editor.
* [Psycopg2](https://pypi.org/project/psycopg2/)- As an adaptor for Python and PostgreSQL databases.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- To style the forms.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- For authentication, registration, account management.

## Frameworks - Libraries - Programs Used


* [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
* [GitHub](https://github.com/)- Used to store the project's code after being pushed from Git.
* [Heroku](https://id.heroku.com)- Used to deploy the live project.
* [Bootstrap](https://getbootstrap.com/)- Used to style the website, add responsiveness and interactivity.
* [Git](https://git-scm.com/)- Used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
* [PostgreSQL](https://www.postgresql.org/)- Database used through heroku.
* [Google Fonts:](https://fonts.google.com/) used for the Roboto font
* [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) was used to inspect page elements, debug, troubleshoot and test features and adjust property values. Using the Lighthouse extension installed in Chrome Browser, the performance report was generated.


## Testing


### Validation
I used the following validation tools to validate HTML, CSS, PYTHON codes. Below the link of TESTING.md file, which includes all validation results.  
- HTML using [W3C HTML validator](https://validator.w3.org/)
- CSS using [Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/)
- Python via [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/)


### Manual Testing

Testing has taken place continuously throughout the development of the project. Each view was tested regularly.

    * Testing User Stories
    * Code Validation
    * Additional Testing
    * Known Bugs


[Back to top](<#contents>)


## Deployment


### 1. Creating the Django Project
* Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click on `Use This Template` button, then create new repository.
* Name our repository and click on `Create repository from template` button.
* Once the template is available in your repository click on `Gitpod` button.
* When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App.
* Install Django and gunicorn: `pip3 install 'django<4' gunicorn`.
* Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url==0.5.0 psycopg2`.
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`.
* Create file for requirements: `pip freeze --local > requirements.txt`.
* Create project:`django-admin startproject project_name .`.
* Create app: `python manage.py startapp app_name`.
* Add app to list of `installed apps` in settings.py file: `'app_name'`.
* Migrate changes: `python manage.py migrate`.
* Test server works locally: `python manage.py runserver`.
* If the app has been installed correctly the window will display- The install worked successfully! Congratulations!


### 2. Create your Heroku app
* Navigate to [Heroku](https://id.heroku.com).
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account.
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app.
* Click Reveal Config Vars and add a new record with `DATABASE_URL`.
* Click Reveal Config Vars and add a new record with `PORT`.
* Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`(note: this must be either removed or set to 0 for final deployment).
* Next, scroll down to the Buildpack section, click `Add Buildpack` select python and click Save Changes.


### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory.
* Add env.py to the .gitignore file.
* In env.py import the os library.
* In env.py add `os.environ["DATABASE_URL"]` = "Paste the link copied from Heroku DATABASE_URL".
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`.
* In Heroku Settings tab Config Vars enter the same `SECRET_KEY` created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.


### 4. Setting up settings.py
* In your Django 'settings.py' file type:


 ```
 from pathlib import Path
 import os
 import dj_database_url


 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default':
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku, click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS:
```ALLOWED_HOSTS = ['<Heroku_app_name>.herokuapp.com', 'localhost']```
* Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```


* Commit and push the code to the GitHub Repository.


### 5. Heroku Deployment:
* Click Deploy tab in Heroku.
* Select Github as the deployment method.
* Confirm you want to connect to GitHub.
* Search for the repository name and click the connect button to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.
* Scroll to the bottom of the deploy page and select the preferred deployment type.
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github or To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.


### 6. Final Deployment
In the IDE:
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py`
* In Heroku settings config vars change the `DISABLE_COLLECTSTATIC` value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku.
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

[Back to top](<#contents>)


## Acknowledgements

The website was completed as a Portfolio Project 14 made for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/).
I would like to thank my mentor who did his best to guide me, and all at the Code Institute for their help and support.



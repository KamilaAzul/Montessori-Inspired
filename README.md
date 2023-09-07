
# **Monthesorri Inspired**

Montessori Inspired is a website created for parents who are interested in raising their children with a Montessori method of education.
After logging in, all visitors can write reviews and comment on other users' content.
All comments and posts require approval by the administrator, who is responsible for ensuring that everyone feels safe from abuse, inappropriate language, etc. Approvals are made from the administration panel. The site has a clean design that makes it easy for users to navigate.

[Live Project Here](https:/)

(photo of the website)

README Table Content

* [**Montessori Inspired - Introduction**](<#montessori-inspired--introductiont>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
    * [Agile Methodology](#agile-methodology)
    * [Main Site Goals](#main-site-goals)

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
    * [Content Page](<#navigation>)
    * [About](<#about>)
    * [Blog Page](#blog-page)
    * [Post Detail Page](#post-detail-page)
    * [Edit Comments Page](#edit-comments-page)
    * [Categories Page](#categories-page)
    * [Search Box](#search-box)
    * [Search Results Page](#search-results-page)
    * [Search Results - No Results Found](#search-results---no-results-found)
    * [Signup Page](#signup-page)
    * [Login Page](#login-page)
    * [Logout Page](#logout-page)
    * [User Profile Page](#user-profile-page)
    * [Profile Update](#profile-update)
    * [Navbar](#navbar)
    * [Footer](<#footer>)
    * [Like Post](#like-post)
    * [Unlike Post](#unlike-post)
    * [Comment Post](#comment-post)
    - [Delete/Edit Comment](#deleteedit-comment)
    - [Delete Comment - 1](#delete-comment)
    - [Edit Comment](#edit-comment)
    - [No Search Found](#no-search-found)

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

#montessori-inspired--introduction

Project milestone 4 for Code Institute Full-stack development program.
This project is a Full Stack website built using the Django framework.
Montessori Inspired is a website created for parents who are interested in raising their children with a Montessori method of education.
They can find here practical tips and information about this method for everyday life.
When the user is logged in they can also like/unlike a post and comment on a post.
Parents can also share their information by adding a post and uploading or updating their user image and details.

[Back to top](<#table-of-content>)

  #site-users-goal
The Monessori Inspired user is interested in the Montessori philosophy and wants to implement this method in his home, in raising his children. The blog is a place where she can learn more about Montessori, interact with other parents, and share her knowledge with like-minded parents.


    #site-owners-goal
The website owner's goal is to provide a website where users will be able to read about Montessori-related topics and add their own posts and comments in an easy and accessible way.

[Back to top](<#table-of-content>)

    #agile-methodology
All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/…)

# Main Site Goals

* Give users a good experience while using the website.
* Give users an intuitive to use and easy to navigate website.
*  Give users a website pleasant to look at and with valuable content.
* Give users a website with a clear purpose.
* Give role-based permissions that allows user to interact with the website.

[Back to top](<#table-of-content>)

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User |  I can immediately understand the purpose of the site so that I can decide if it meets my  
    needs. | &check; |
| As a Site User |  I can intuitively navigate around the site so that I can find content and 
    understand where I am on the site | &check; |
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

[Back to top](<#table-of-content>)

#site-structure

#design-choices

#colours

![Colours Palete](./assets/readme/extras/tasty_blog_colors_palete.png)<br>

- The color scheme is kept simple by opting for a combination of white text set against the image background and black text against the white background. For the navbar was set as a white background color that changes when the user scrolls. For a linear gradient, 3 colours were used dark blue, orange, and purple. This gradient is also used as a search box background. To highlight the icons an interactive color set of light blue was used.

#typography

- The Lato font is used as the main font for the whole project and the Kaushan font is used to
display the word enjoy in the Post Details and About pages.

#imagery

- All the images are related to Montessori philosophy and the website design.
Only 7 images are static.
All other images will be uploaded by the authors to the database.

#database-diagram

## Features
#existing-features

### **Home Page**
#home-page

![Home Page](photo to upload)

- The hero image related to Montessori education should welcome the user and gives a short message explaining what the website is about.

### **Navigation**
The navigation bar is very clean and straight forward and easy to use.

*Links that are visible to the user: *

* About - Includes information about Monessori Inspired.
* Categories - Shows all categories of posts.
* Blog - Lists of all posts.
* Login / Sign Up - Gives the user the opportunity to log in or sign up if not ready a registered user at Review | Alliance.
* Search Box - allowes the user to search of particular content.

### **About**

The About Page gives, users information about the author and and it makes an introduction  to the website. It explains as well the main purpose of the blog.<br>

<details><summary><b>About Section</b></summary>

![About](readme/assets/images/about.png)
</details><br/>


### **Blog Page**


![Blog Page]

- On the Blog Page, users have access to all posts available on the website.
The user can choose which post to read by clicking on the post card.<br>

### **Post-detail-page**

### **Categories Page**

* On the Categories Page, users can see the categories available in the blog and filter the posts by category.

### **Categories Results**

* On the Categories Results Page, users can access the post filtered by the chosen category.

### **Search Results Page**

* On the Search Results Page, users can see the posts found by their search.  When their post is found, the user can go to the 
  Post Details Page by clicking on the card result.

    ###Search Results - No Results Found

* On the Search Results Page - No Results Found, users will see this message if there is nothing found for the search.

### **Signup Page](#signup-page)
### **Login Page](#login-page)
### **Logout Page](#logout-page)
### **User Profile Page](#user-profile-page)
### **Profile Update](#profile-update)
### **Navbar](#navbar)
### **Footer](<#footer>)
### **Like Post](#like-post)
### **Unlike Post](#unlike-post)
### **Comment Post](#comment-post)
### **Delete/Edit Comment](#deleteedit-comment)
### **Delete Comment - 1](#delete-comment---1)
### **Delete Comment - 2](#delete-comment---2)
### **Edit Comment](#edit-comment)
 

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


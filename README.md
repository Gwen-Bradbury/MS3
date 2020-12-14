# UK Walks

(*Markdown Toc)
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Introduction

(*![Apple Devices Picture](./wireframes/responsive.png))

This is my third milestone project; Designed to exhibit my capabilities and skills in javascript, as a student
of Code Institute. (https://codeinstitute.net/)
The goal was to showcase my skills to potential employers/recruiters, on a topic that I'm deeply interested in.
My project allows users to discover new walks within the UK, inspiring them to get outside and enjoy the beautiful UK countryside.
My app contains a landing page, complete with headline image and images of the UK's National Parks, followed by a list of all the walks in the DB.
There's a login and register page containing required form fields that give you access to the rest of the app, where users can add and delete walks that they've added. There's also a 'My Walks' page that lists all the 
walks that they've added.
The last link is a 'Log Out' button that logs users out of the app by removing thier session cookies.
The app is colourful and engaging, drawing the user in with bright, bold images and standout text, which I hope entices them
to get planning thier next walking route.

A link to my website can be found [here](https://gwen-bradbury.github.io/MS3/) or [here](https://ms3-walkapp.herokuapp.com/)

## UX

### Goals -

The purpose of the app is to provide a simple, straightforward format presenting information about some of the UK's best National Park walks.
My app is designed for people interested in walking in the UK, and I'm hopeful my app
will give them the motivation towards getting out into the countryside more often and visiting somewhere new.
The app is fully functional and interactive giving the user a positive experience as they move throught the pages.
I focused on a design that would be engaging and easy to navigate so users will continue to repeatedly visit and make use of the
features implimented within the app.

### Wireframes-

I have produced a mock up of all of my app's pages.

![Wireframe picture](./wireframes/MS3.png)

### Design

#### Design Process-

1. _Strategy Plane_ - From the onset I knew that my primary aim was to encourage people who enjoy walking to explore different UK National Parks in a way that was engaging and simple, 
therefore stimulating them to get back outdoors and into the countryside. My main focus thoughout this project has been to excute this aim. I started the UX process by making a list of user stories, which allowed me to visualise what would be necessary to satisy them.
2. _Scope Plane_ - Having decided the main aim for the project, I began outlining the key features that I wanted my app to have.
To do so, I focused on the Python and Javascript I would need to implement, as I knew this would be crucial to the aim of making the app interactive. This led me to decide that I wanted to focus on two key features: a registration form and login page, and a page for users to add walks to a list, with the added option to delete walks they've added if needed.
3. _Structure Plane_ - Once I had narrowed down the features I wanted to include, I formulated the structure of my design into 7 seperate pages: The landing or 'Home' page, 'Login', 'Register', 'My Walks', 'Add Walk' and 'Add Park'.
The 'Home' page is the first page you see when visiting the app. It lists the National Parks and Walks within them. It also has links to the 'Login' and 'Register' pages. Both the previously mentioned pages contain forms with fields requiring a username and password in order to gain access to the rest of the site. Upon registering or logging in you get taken to the 'My Walks' page. 
This page lists all the walks that that user has added into it. The navbar links also navigate the user back to the 'Home' page, the 'Add A Walk' and, for the admin, the 'Add A Park' pages.
Both the 'Add A Walk' page allow users to add Walks, to the database using a simple form. The admin also has access to the 'Manage Parks' page which allows them to Edt, Add and Delete parks. These added parks and walks are then listed on the 'Home' page with the walks also listed on the 'My Walks' page. 
The last link in the navbar allows users to exit or 'Log Out' of the app.
I made navigation through the website easy with a navbar and search box located on the 'Home' page.
4. _Skeleton Plane_ - As mentioned in the Structure Plane, I decided to use a navbar and search bar as the main source of navigation through the app. This allows the user to move thoughout the app at a pace that suits them, in the easiest way possible. Returning users can find the page they're looking for, using the navbar, without having to scroll through lots of information they've already seen on previous visits, 
and can use the search bar to search for the walks and parks that they're most interested in. The 'My Walks' page link in the navbar will also allow the user to locate all the parks and walks they've added to it, without scrolling through the database on the 'Home' page.
5. _Surface Plane_ - 

- For my design to work, I knew that it would be important to create a theme that would keep the user interested. My first design decision was therefore to make the app as bright and colourful with images from the three National Parks I'm focusing on, to gain and keep thier attention.
- With this in mind, I began experimenting with my wireframes. I found it useful to generate a color scheme using coolors, which provided me with contrasting colours for my website and found images that complemented that colour scheme. I used figma to make mock ups of my websites pages.
- With the wireframes complete I began experimenting with the libraries and technologies I would use for the features within my app. I used a different workspace for the different technologies needed for each feature.

> Note: Throughout the design process, I kept referring back to my original 'Main Aims' and 'User Stories' to make sure that my project was developing as intended.

#### Colour Pallette-

I used coolors to generate my colour scheme-

https://coolors.co/8e9aaf-cbc0d3-f0d1d4-dee2ff

And matched this as best I could to the CCS colors on Materialize, which I used throughout my project.

I used ![#37474f](https://placehold.it/15/14213D/000000?text=+) #37474f (Materialize shade: blue-grey darken-3) for the background color of my pages as it's dark and contrasts with my images.
I used ![#fff](https://placehold.it/15/14213D/000000?text=+) #fff (white) as my text color as it stood out clearly against the dark background.
![#eceff1](https://placehold.it/15/14213D/000000?text=+) #eceff1 (Materialize shade: blue-grey lighten-5) as a background color to the flash messages, with ![#37474f](https://placehold.it/15/14213D/000000?text=+) #37474f (Materialize shade: blue-grey darken-3)
as the flash message text color.
![#fff](https://placehold.it/15/14213D/000000?text=+) #fff (white) is also used as the background to my burger menu on mobile devices with the ![#37474f](https://placehold.it/15/14213D/000000?text=+) #37474f (Materialize shade: blue-grey darken-3) text color
to give it some separation from the main page.

All my colors were chosen for thier relaxing and calming shades, in keeping with the tone of the app. The National Parks are nature at it's most beautiful and being within them and finding peace within them, allows you the time
to relax and rejuvenate, with the added benefit of exercising by walking. 

#### Font-

I used a line height of 3 on my flash messages to make them stand out more and grab the users attention.

## User Stories

### As a Site User - 

- As a user, I want to be able to add, edit and delete my input easily.

- As a user, I want to find what I'm looking for quickly and easily.

- As a user, I want to know how the app works and have easy to follow instructions.

- As a user, I want to know when I take the wrong action or when something doesn't work.

- As a user, I want the app to be interactive with real time feedback.

- As a user, I want the the app to be easy to use and navigate.

### As a Designer-

- As a web designer and developer, I want to track the user behaviour so that I can improve the user experience. I want to track the user behaviour so that I can identify the possible user confusion over navigating the app.
I want feed back from the users on what features are being used most frequently and ideas on other interesting walks.

- As a web designer and developer, I want the app to be interactive and give real time feedback when a user executes an action.

### As an Employer-

- As an employer/recruiter, I need to see and review the skills and work capabilities, and analyze if you have the skills we require. In this website I've used many user-friendly features to showcase my skills as a developer.
From the layout and colour scheme to the interactivity, every implemented piece of code has been built to make the site as appealing and easy to use for customers as possible.
Possible employers will be able to see from the app and the features implemented that my standard of work is very high, and my capabilities reflect my current skillset, which will improve as I gain more knowledge moving through
the Code Institute Full Stack Developer course.

- On our Human Resources team, we look for the information that pertains to the specific needs of the company, and does this individual have those skill sets. My skill sets are evidenced in the app produced. I've used a wide range of HTML, CSS, JavaScript and Jinja to
develop this app, as well as technologies such as Materialize for responsiveness.

## Features

### Exsisting Features-

#### Features on the Home Page -

- _Navbar_ - 

-_Headline Image_-

-_List of Parks_-

-_List of Walks_-

-_Add to My Walks button_-

Navbar is repeated across all pages to provide consistant navigation throughout the app.

Headline Image is repeated across all pages to provide consistancy within app.

#### Features on the Login Page-

-_Login Form_-

-_Link to Register Account page_-

#### Features on the Register Page-

-_Register Account form_-

-_Link to Login page_-

#### Features on the Add a Walk Page-

-_Form to Add Walks to DB_-

#### Features on the Manage Parks Page-

-_List of Parks_-

-_Edit button_-

-_Delete button_-

#### Features on the Users Walks Page-

-_List of added Walks_-

-_Edit button_-

-_Delete button_-

### Features left to Implement -

-_More Parks_-

-_More Walks_-

-_Language button_-

### Bugs and Fixes Implemented after Testing -

- _Images_ - Changed headline image as the origional one looked pixelated and streched.

## Technologies Used

### Languages-

1. **HTML, or Hyper Text Markup Language:** Used to construct the page withn this app. For further info on this language, see this link;  
https://developer.mozilla.org/en-US/docs/Web/HTML

2. **CSS, or Cascading Style Sheets:** Used to style the various elements on the app's pages via coloring, fonts, spacing, etc. For further info, see this link;
https://www.w3.org/Style/CSS/Overview.en.html

3. **Javascript:** A programming language used 

4. **JQuery:**

5. **Python:**

6. **Jinja:**

### Libraries-

1. **Materialize:** A CSS framework that assists the programmer in creating responsive, mobile first front-end web sites. https://materializecss.com/ 
                               - navbar
                               - cards - 'My Walks' page/ 'Home' page/ 'Manage Parks' page
                               - forms  
### API's-

### Tools-

1. **Gitpod:** An online IDE also used for creating & saving code that runs in a browser, it does not have to be installed on your PC.
   https://www.gitpod.io/

2. **Git:** A version control system for tracking changes in source code during software development. https://git-scm.com/

3. **Github:** A company that provides hosting for software development version control using Git. It is a subsidiary of Microsoft. https://github.

4. **Heroku:**

5. **Chrome DevTools:** A set of web developer tools built directly into the Google Chrome browser. I used these tools constantly thoughout the development cycle.
   https://developers.google.com/web/tools/chrome-devtools

6. **W3C Markup Validation Service:** Used to run all html and css code through a validation process looking for errors; https://validator.w3.org/
   https://jigsaw.w3.org/css-validator/validator


## Testing

### Validation of Code Testing-

## Deployment

This website was developed in Gitpod and pushed to the remote repositories, GitHub and Heroku.

### Heroku

In order to successfully deploy the app, the following steps were taken:

1. Visit GitPod workspace.

2. Create the Flask App.

3. Use the CLI to tell Heroku which applications and dependencies are required to run the application via the, pip3 freeze --local > requirements.txt command.

4. Create the Procfile via echo web: python walkapp.py > Procfile.

5. Create env.py file to store the following information:
- IP
- PORT
- MONGO_URI
- SECRET_KEY
- MONGO_DBNAME

6. Visit Heroku.

7. Click, 'Create a New App'
- Create an application on Heroku with a unique name ('ms3-walkapp') to satisfy Heroku requirements.
- Create the Heroku application.

8. Add the following configuration vars to Heroku application (taken from the env.py file in GitPod workspace):
- IP
- PORT
- MONGO_URI
- SECRET_KEY
- MONGO_DBNAME

9. Visit workspace

10. Push newly created requirements.txt and Procfile to Git.

11. Navigate back to Heroku and enable automatic deployment.

12. Connect Heroku to deploy from the master branch of Dash's repository.

Successfully deploy the application.

### GitHub

1. Visit GitPod workspace.

2. Create the Flask App.

3. Use the CLI to tell Heroku which applications and dependencies are required to run the application via the, pip3 freeze --local > requirements.txt command.

4. Create the Procfile via echo web: python walkapp.py > Procfile.

5. Create env.py file to store the following information:
- IP
- PORT
- MONGO_URI
- SECRET_KEY
- MONGO_DBNAME

6. Use -

* git add . - To add files to staging area.

* git commit -m "message here" - To commit the files.

* git push - To push the committed files to the origin master branch on github.

#### Used Commands during Deployment -

1. git add . - To add files to staging area.

2. git commit -m "message here" - To commit the files.

3. git push - To push the committed files to the origin master branch on github.

4. git status - To see the current state of the files.

### Running this Project Locally-

You will need to install the following to run this locally:

- An IDE 
- Python3 to run the application
- PIP to install all app requirements
- MongoDB to develop your own database either locally or remotely on MongoDB Atlas.
- GIT for cloning and version control

1.  To run this code on your local machine, you would go to my respository at
    https://github.com/Gwen-Bradbury/MS3 and on the home page on the right hand side just above all the files, you will see a green button that says,
    "Clone or download", this button will give you options to clone with HTTPS, open in desktop or download as a zip file.
    To continue with cloning, you would;

    - Open Git Bash
    - Change the current working directory to the location where you want the cloned directory to be made.
    - Type git clone, and then paste this URL; https://github.com/Gwen-Bradbury/MS3.git Press Enter. Your local clone will be created.

For more information about the above process; https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

## Credits

### Content-

1. https://www.peakdistrict.gov.uk/

2. https://www.lakedistrict.gov.uk/

3. https://www.snowdonia.gov.wales/

4. https://www.visitdartmoor.co.uk/

### Media-

1. unsplash.com

2. https://www.lakedistrict.gov.uk/

3. https://www.snowdonia.gov.wales/

4. https://www.visitdartmoor.co.uk/

5. https://www.peakdistrict.gov.uk/


### Acknowledgements-

## Disclaimer

#### This website was made for educational purposes only

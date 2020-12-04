# UK Walks

(*Markdown Toc)
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Introduction

(*![Apple Devices Picture](./wireframes/responsive.png))

This is my third milestone project; Designed to exhibit my capabilities and skills in javascript, as a student
of Code Institute. (https://codeinstitute.net/)
The goal was to showcase my skills to potential employers/recruiters, on a topic that I'm deeply interested in.
My project allows users to discover new walks within the UK, inspiring them to get outside and enjoy the beautiful English countryside.
My app contains a landing page, complete with headline image and linked images of the UK's National Parks.
There's a login and register page containing required form fields that give you access to the rest of the site, where users can add and delete parks and walks that they've added. There's also a 'My Walks' page that lists all the 
walks that they've added.
The last link is a 'Log Out' button that logs users out of the app by removing thier session cookies.
The website is colourful and engaging, drawing the user in with bright, bold images and standout text, which I hope entices them
to get planning thier next walking route.

A link to my website can be found [here](https://gwen-bradbury.github.io/MS3/) or [here](https://ms3-walkapp.herokuapp.com/)

## UX

### Goals -

The purpose of the site is to provide a simple, straightforward format presenting information about some of the UK's best National Park walks.
My website is designed for people interested in walking in the UK, and im hopeful my website
will give them the motivation towards getting out into the countryside more often and visiting somewhere new.
The website is fully functional and interactive giving the user a positive experience as they move throught the pages.
I focused on a design that would be engaging and easy to navigate so users will continue to repeatedly visit and make use of the
features implimented within the app.

### Wireframes-

I have produced a mock up of all of my app's pages.

![Wireframe picture](./wireframes/MS3.png)

### Design

#### Design Process-

1. _Strategy Plane_ - From the onset I knew that my primary aim was to encourage people who enjoy walking to explore different UK National Parks in a way that was engaging and simple, therefore stimulating them to get back outdoors and into the countryside. My main focus thoughout this project has been to excute this aim. I started the UX process by making a list of user stories, which allowed me to visualise what would be necessary to satisy them.
2. _Scope Plane_ - Having decided the main aim for the project, I began outlining the key features that I wanted my app to have.
To do so, I focused on the Python and Javascript I would need to implement, as I knew this would be crucial to the aim of making the app interactive. This led me to decide that I wanted to focus on two key features: a registration form and login page, and a page for users to add walks to a list, with the added option to delete walks they've added if needed.
3. _Structure Plane_ - Once I had narrowed down the features I wanted to include, I formulated the structure of my design into 7 seperate pages: The landing or 'Home' page, 'Login', 'Register', 'My Walks', 'Add Walk' and 'Add Park'.
The 'Home' page is the first page you see when visiting the app. It lists the National Parks and Walks within them. It also has links to the 'Login' and 'Register' pages. Both the previously mentioned pages contain forms with fields requiring a username and password in order to gain access to the rest of the site. Upon registering or logging in you get taken to the 'My Walks' page. This page lists all the walks that that user has added. The navbar links also navigate the user back to the 'Home' page, the 'Add A Walk' and the 'Add A Park' pages.
Both the 'Add A Walk' and 'Add A Park' pages allow users to add National Parks, and Walks within them, to the database using a simple form. These added parks and walks are then listed on the 'Home' and 'My Walks' pages. 
The last link in the navbar allows users to exit or 'Log Out' of the app.
I made navigation through the website easy with a navbar and search box located on the 'Home' page.
4. _Skeleton Plane_ - As mentioned in the Structure Plane, I decided to use a navbar and search bar as the main source of navigation through the app. This allows the user to move thoughout the app at a pace that suits them, in the easiest way possible. Returning users can find the page they're looking for, using the navbar, without having to scroll through lots of information they've already seen on previous visits, and use the search bar to search for the walks and parks that they're most interested in. The 'My Walks' page link in the navbar will also allow the user to locate all the parks and walks they've added without scrolling through the database on the 'Home' page.
5. _Surface Plane_ - 

- For my design to work, I knew that it would be important to create a theme that would keep the user interested. My first design decision was therefore to make the website as bright and colourful with images from the three National Parks I'm focusing on, to gain and keep thier attention.
- With this in mind, I began experimenting with my wireframes. I found it useful to generate a color scheme using coolors, which provided me with contrasting colours for my website and found images that complemented that colour scheme. I used figma to make mock ups of my websites pages.
- With the wireframes complete I began experimenting with the libraries and technologies I would use for the features within my app. I used a different workspace for the different technologies needed for each feature.

> Note: Throughout the design process, I kept referring back to my original 'Main Aims' and 'User Stories' to make sure that my project was developing as intended.

#### Colour Pallette-

I used coolors to generate my colour scheme-

https://coolors.co/8e9aaf-cbc0d3-f0d1d4-dee2ff

And matched this as best I could to the CCS colors on Materialize, which I used throughout my project.

I used ![#37474f](https://placehold.it/15/14213D/000000?text=+) #37474f (Materialize shade: blue-grey darken-3) for the background color of my pages as it's dark and contrasts with my images.
I used ![#fff](https://placehold.it/15/14213D/000000?text=+) #fff (white) as my text color as it stood out clearly against the dark background.
![#fce4ec](https://placehold.it/15/14213D/000000?text=+) #fce4ec (Materialize shade: pink lighten-5) as a background color to the flash messages, with ![#37474f](https://placehold.it/15/14213D/000000?text=+) #37474f (Materialize shade: blue-grey darken-3)
as the flash message text color.
![#fff](https://placehold.it/15/14213D/000000?text=+) #fff (white) is also used as the background to my burger menu on mobile devices with the ![#37474f](https://placehold.it/15/14213D/000000?text=+) #37474f (Materialize shade: blue-grey darken-3) text color
to give it some separation from the main page.

All my colors were chosen for thier relaxing and calming shades, in keeping with the tone of the app. The National Parks are nature at it's most beautiful and being within them and finding peace within them, allows you the time
to relax and rejuvenate, with the added benefit of exercising by walking. 

#### Font-

## User Stories

### As a Site User - 

- As a user, I want to know how the website works and have easy to follow instructions.

- As a user, I want to know when I take the wrong action or when something doesn't work.

- As a user, I want the website to be interactive with real time feedback.

- As a user, I want the the website to be easy to use and navigate.

### As a Designer-

- As a web designer and developer, I want to track the user behaviour so that I can improve the user experience. I want to track the user behaviour so that I can identify the possible user confusion over navigating the website.
I want feed back from the users on what features are being used most frequently and ideas on other interesting walks.

- As a web designer and developer, I want the website to be interactive and give real time feedback when a user executes an action.

### As an Employer-

- As an employer/recruiter, I need to see and review the skills and work capabilities, and analyze if you have the skills we require. In this website I've used many user-friendly features to showcase my skills as a developer.
From the layout and colour scheme to the interactivity, every implemented piece of code has been built to make the site as appealing and easy to use for customers as possible.
Possible employers will be able to see from the website and the features implemented that my standard of work is very high, and my capabilities reflect my current skillset, which will improve as I gain more knowledge moving through
the Code Institute Full Stack Developer course.

- On our Human Resources team, we look for the information that pertains to the specific needs of the company, and does this individual have those skill sets. My skill sets are evidenced in the website produced. I've used a wide range of HTML, CSS, JavaScript and Jinja to
develop this site, as well as technologies such as Materialize for responsiveness.

## Features

### Exsisting Features-

#### Features on the Home Page -

- _Navbar_ - 

#### Features on the Login Page-

#### Features on the Register Page-

#### Features on the Add a Walk Page-

#### Features on the Manage Parks Page-

#### Features on the Users Walks Page-

### Features left to Implement -

### Bugs and Fixes Implemented after Testing -

- _Images_ - Changed headline image as the origional one looked pixelated and streched.

## Technologies Used

### Languages-

1. **HTML, or Hyper Text Markup Language:** Used to construct the page withn this app. For further info on this language, see this link;  
https://developer.mozilla.org/en-US/docs/Web/HTML

2. **CSS, or Cascading Style Sheets:** Used to style the various elements on the app's pages via coloring, fonts, spacing, etc. For further info, see this link;
https://www.w3.org/Style/CSS/Overview.en.html

### Libraries-

1. https://materializecss.com/ - navbar

### API's-

### Tools-

## Testing

### Validation of Code Testing-

## Deployment

#### Used Commands during Deployment -

### Hosting on GitHub Pages-

### Running this Project Locally-

## Credits

### Content-

### Media-

1. unsplash.com

### Acknowledgements-

## Disclaimer

#### This website was made for educational purposes only

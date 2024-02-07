# FragTube

## Introduction

Welcome to FragTube, a video sharing platform for gamers to showcase frag movies and compilations. Users can share and discuss content with one another, follow other users to keep up to date with their posts and like posts to quickly find content they enjoy.

## Table of Contents

## UX

### User Stories

#### Navigating the Site
* As a user I can view a navbar so that I can easily navigate the site

#### Authentication
* As a user I can create an account so that I can access all the features for signed up users.
* As a user I can sign in so that I can access functionality for logged in users.
* As a user I can tell if I am logged in so that I can logged in if need be.
* As a user I can maintain my logged-in status until I choose to log out so that user experience is not compromised.
* As a user I can view user's avatars so that I can easily identify users of the application

#### Adding & Liking Posts
* As a logged in user I can create posts so that I can share frag movies with other users.
* As a user I can view details of a single post so that I can get all the information on it.
* As a logged in user I can like posts so that I can show appreciation of good content.

#### The Posts Page
* As a user I can view all the most recent posts, ordered by most recent so that I can keep up to date with new content.
* As a user I can search keywords so that I can easily find content or profiles that would be of interest to me.
* As a logged in user I can view my liked posts so that I can easily view posts I most enjoy.
* As a logged in user I can view posts from profiles I follow so that I can filter the posts I see by profiles I follow.
* As a user I can keep scrolling through posts on the site, that are loaded for me automatically so that I do not have to click on a link to the next page.

#### The Post Page
* As a logged in user I can edit my posts so that I can make corrections or update my post after creation.
* As a user I can view comments on a post page so that I can read what others think about the content.
* As a logged in user I can delete comments I have made on a post so that I can control the removal of my comment from the application.
* As a logged in user I can edit my comment so that I can update it if necessary.

#### The Profile Page
* As a user I can view other users profiles so that I can see their posts and learn more about them.
* As a user I can view statistics about a specific user so that I can leanr more about them.
* As a logged in user I can follow or unfollow other users so that I can see and remove posts by a specific user in my posts feed.
* As a logged in user I can edit my profile so that I can update my profile picture and bio.
* As a logged in user I can update my username and password so that I can change my display name and keep my profile secure.

### Admin Stories
* As an admin I can delete user's comments so that I can remove any comments which are offensive or harmful.

### Website Goals

The goals of this website are to allow users to share gaming clips and videos that they have either created themselves or find interesting. Users will have the ability to follow other users, like posts from other users and comment on posts to discuss the content. The website should allow users to share and discuss content.

### Requirements
* Home page.
* User sign up.
* User sign in.
* Create post feature for logged in users.
* Functionality for logged in users to edit their posts.
* Functionality for logged in users to like other user's posts.
* Liked posts page to allow user to filter posts to those they have liked.
* Functionality for logged in users to follow other users.
* Personal feed for users to only view posts from users they have followed.
* Profile page for users to view other users profiles and showcase their own profile.
* Functionality for logged in users to edit their profile.
* Functionality for logged in users to comment on posts.
* Functionality for logged in users to edit or delete their comments.
* Functionality for logged in users to update their username and password.

## Design Choices

### Fonts

[Google Fonts](https://fonts.google.com/ "Google Fonts") has been used to select the fonts for the website. The font selected for the logo was [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) as it perfectly fits the gaming theme of the website. The font [Play](https://fonts.google.com/specimen/Play) has been selected for headers and main body text as it fits the overall theme of the website and feels like it has been pulled directly from a game.

### Colours
Colours for the website where selected using [Coolors](http://coolors.co "Coolors").

* #808C8C - Battleship grey is used for the background and body of contents.
* #FF0000 - Red is used for the main logo and header.
* #FFFFFF - White is used for main body text.

### Icons

The icons used for the site were sourced from [Font Awesome](https://fontawesome.com/ "Font Awesome").

## Structure

The structure of the site will be split into frontend and backend. The frontend of the site will be comprised using [React](https://react.dev/) components with custom [CSS](https://en.wikipedia.org/wiki/CSS) and [React Bootstrap](https://react-bootstrap.netlify.app/) for the design. The backend will be built using [Django Rest Framework](https://www.django-rest-framework.org/) which will hold all necessary data and pass it to the frontend where necessary.

### Database Models

#### Post Model

| Object     | Field         |
|------------|---------------|
| owner      | ForeignKey    |
| created_at | DateTimeField |
| updated_at | DateTimeField |
| category   | CharField     |
| title      | CharField     |
| content    | TextField     |
| embedid    | CharField     |

#### Profile Model

| Object     | Field         |
|------------|---------------|
| owner      | OneToOneField |
| created_at | DateTimeField |
| updated_at | DateTimeField |
| name       | CharField     |
| content    | TextField     |
| image      | ImageField    |

#### Like Model

| Object     | Field         |
|------------|---------------|
| owner      | ForeignKey    |
| post       | ForeignKey    |
| created_at | DateTimeField |

#### Follower Model

| Object     | Field         |
|------------|---------------|
| owner      | ForeignKey    |
| followed   | ForeignKey    |
| created_at | DateTimeField |

#### Comment Model

| Object     | Field         |
|------------|---------------|
| owner      | ForeignKey    |
| post       | ForeignKey    |
| created_at | DateTimeField |
| updated_at | DateTimeField |
| content    | TextField     |


### Wireframes

Wireframes have been created using [Balsamic](https://balsamiq.com "Balsamic"). These wireframes gave a basic view of how the site will be laid out. The layout may have changed slightly in the finished product.

## Features

### Home Page

The home page will feature the most recent posts on the site and a list of popular profiles for the user to explore. 

### Navbar

The navbar will change dependent on whether the user is logged in or not. If the user is not logged in, they will see links to log in or sign up and one for home. If the user is logged in, they will see links for add post, home, feed, liked, sign out and profile. The navbar will be present on all pages of the site.

### Sign Up Page

The sign up page will display a form for new users to create a profile of their own. The form will contain a username field, a password field and a secondary confirmation password field. There will be a submit button which will pass the details filled in to the database and create a new profile instance.

### Sign In Page

The sign in page will contain a form for the user to input their username and password. When submitted it will be checked, log in the user if information is correct and redirect to the home page on successful submission.

### Avatar

The avatar component will be used to display the profile image of user profiles. It will work as a clickable link to the specific user's profile page. Users can upload their profile image and edit it at their convenience.

### Add a Post

If the user is logged in, they will be able to access the add post page from a link on the navbar. The page will contain a form for the user to create a new post and on successful submission, a new post will be created.

### Search Bar

The search bar will be present on the home page, feed page and liked page to allow users to filter their post responses with keywords. The search function will check titles, profile names and categories that correspond to the user inputted keywords.

### Liking a Post

Logged in users will be able to like posts in which they enjoy so that they can easily find posts which they find interesting. 

### Following Users

Logged in users will be able to follow other users so that they can filter posts to those created by users which they have followed.

### Posts

Posts will be rendered on the home page, personal feed, liked page, user profile page and the individual post page. The posts will show an embedded youtube video, the title, the user who uploaded, the date on which it was uploaded, the content description, the number of likes and number of comments. On the individual post page the user will be able to view the comments on the post and add their own if they are logged in.

### Post Page

The post page will be of individual posts. The page will display the specific post and comments for that post. If the current user is the owner of the post, there will be functionality to edit the post.

### Feed Page

The feed page is for logged in users to filter posts to those from users they have followed.

### Liked Page

The liked page is for logged in users to filter posts to those of which they have liked.

### Profile Page

The profile page will display a profile image, profile bio, post count, followers count, following count and a list of the user's posts. There will be a button to follow or unfollow visible to logged in users. If the current user is the owner of the profile page, there will be functionality to edit their profile.

### Popular Profiles Component

The popular profile componet will be displayed on the home page, feed page, liked page and profile page. It will contain a list of the most followed profiles, ordered from most followers to least with a maximum length of 10 profiles. The profiles will show up as the profile avatar and the profile name. Additionally, if the user is logged in, there will be an additional button to follow/unfollow the user.

### Comments

Comments will be displayed on the individual post page for users to discuss the content. Users will only be able to post comments if they are logged in. Logged in users can edit and delete their own comments. If a user is an admin, they will be able to delete other user's comments where necessary.





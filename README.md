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
*  As a user I can search keywords so that I can easily find content or profiles that would be of interest to me.
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






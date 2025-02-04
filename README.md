# CookBook API

<img src="docs\images\CookBook-Logo.png" width=300>


## Table of Contents
* [CookBook API](#cookbook-api)
  * [Objective](#objective)
    * [React Frontend](#react-frontend)
  * [Live API](#live-page)
* [Planning](#planning)
  * [Data Models](#data-models)
    * [ERD Diagram](#erd-diagram)
    * [Profile Model Fields](#profile-model-fields)
    * [Recipe Model Fields](#recipe-model-fields)
    * [Favorite Model Fields](#favorite-model-fields)
    * [Review Model Field](#review-model-field)
    * [Comment Model Fields](#comment-model-fields)
    * [Barker Notation](#barker-notation)
* [Manual Testing](#manual-testing)
  * [Validation](#validation)
  * [Frameworks, libraries and dependencies](#frameworks-libraries-and-dependencies)
* [Development and Deployment](#development-and-deployment)
  * [Heroku](#heroku)
  * [Forking](#forking)
  * [Other Utils](#other-utils)
* [Credits](#credits)
  * [Media](#media)
* [Acknowledgements](#acknowledgements)

## Objective
This is the API for the CookBook front end a vibrant online platform designed to bridge the gap between seasoned culinary enthusiasts and novice cooks. Our mission is to create an inclusive environment where experienced chefs can showcase their culinary creations, share innovative recipes, and impart valuable cooking knowledge. Simultaneously, CookBook provides budding cooks with a safe haven that includes detailed instructions and a community of support to help them feel inspired and confident in the kitchen.

- Here the backend structure and information is stored.
    - Profile Data
    - Recipe Data
    - Favorite Recipe Data
    - Review Data
    - Comment Data

### React Frontend
The repository for the frontend of the application can be found here:<br>[CookBook React](https://github.com/JuanModzelewski/cookbook-react)

## Live API
[CookBook API](https://cookbook-drf-api-d322c7998986.herokuapp.com/)

# Planning
User stories, which described the objectives and specifications from the viewpoint of the users, were created to start the planning phase. By acting as a fundamental blueprint, these user stories made sure that end users' requirements and expectations were taken into account throughout the process.

Following the creation of user stories, wireframes were designed to visually structure the various components and functionalities of the site. These wireframes provided a clear and tangible representation of the user interface.

Based on the identified features and functionalities from the wireframes, the necessary data models could be developed. These data models were crucial in outlining the structure and relationships of the data that would be used throughout the application, ensuring a coherent and efficient data flow.

## Data Models:
By employing an entity relationship diagram, the data model schema was planned concurrently with the API endpoints.

### ERD Diagram
<img src="docs\images\erd-diagram.jpg">

### Profile Model Fields:
- owner: A one-to-one relationship with the User model. This ensures that each user has one profile and each profile is associated with one user.
- created_at: A datetime field that automatically records when the profile was created 
- updated_at: A datetime field that automatically updates whenever the profile is saved 
- name: A character field that can store up to 255 characters.
- content: A text field for additional content or description.
- image: An image field for storing the user's profile picture. Cloudinary Media storage was used and a default image set.

### Recipe Model Fields:
- title: A character field for the title of the recipe.
- description: A text field for a detailed description of the recipe.
- ingredients: A JSON field to store the list of ingredients. This allows for a flexible format to include quantities.
- cooking_instructions: A text field for detailed cooking instructions.
- recipe_image: An image field for uploading a picture of the recipe.  Cloudinary Media storage was used and a default image set.
- owner: A foreign key linking to the User model. This represents the user who created the recipe. If the user is deleted, their recipes are also deleted.
- created_at: A datetime field that automatically records when the recipe was created 
- updated_at: A datetime field that automatically updates whenever the recipe is saved 

### Favorite Model Fields:
- owner: A foreign key linking to the User model. This represents the user who marked the recipe as a favorite. If the user is deleted, all their favorite records are also deleted 
- recipe: A foreign key linking to the Recipe model. This represents the recipe that has been marked as a favorite. If the recipe is deleted, the associated favorite records are also deleted. The related_name='favorites' allows accessing favorite records from the Recipe model via recipe.favorites.
created_at: A datetime field that automatically records when the favorite record was created 

### Review Model Field:
- owner: A foreign key linking to the User model. This represents the user who created the review.
- recipe: A foreign key linking to the Recipe model. This represents the recipe being reviewed. The related_name='reviews' allows accessing reviews from the Recipe model via recipe.reviews.
- rating: An integer field with choices ranging from 1 to 5 stars (STAR_CHOICES), representing the user's rating of the recipe.
- comment: A text field for optional comments about the recipe.
- created_at: A datetime field that automatically records when the review was created
- updated_at: A datetime field that automatically records when the review was last updated

### Comment Model Fields:
- owner: A foreign key linking to the User model. This represents the user who wrote the comment. If the user is deleted, all their comments are also deleted.
- review: A foreign key linking to the Review model. This indicates which review the comment is associated with. If the review is deleted, the associated comments are also deleted. The related_name='comments' allows accessing comments from the Review model via review.comments.
- parent: A self-referential foreign key that allows a comment to be a reply to another comment. This field can be null or blank. If specified, it links to another comment, allowing nested comments (related_name='replies'). If the parent comment is deleted, all its replies are also deleted
- comment: A text field to store the content of the comment.
- created_at: A datetime field that automatically records when the comment was created 
- updated_at: A datetime field that automatically updates whenever the comment is saved 

### Barker Notation
- User and Profile:
  - One-to-One relationship: Each user has one profile, and each profile is associated with one user (owner in Profile).

- User and Recipe:
  - One-to-Many relationship: Each user can create many recipes, but each recipe has one owner (owner in Recipe).

- User and Review:
  - One-to-Many relationship: Each user can write multiple reviews, but each review has one owner (owner in Review).

- Recipe and Review:
  - One-to-Many relationship: Each recipe can have multiple reviews, but each review is associated with one recipe (recipe in Review).

- User and Favorite:
  - One-to-Many relationship: Each user can have multiple favorites, but each favorite is associated with one user (owner in Favorite).

- Recipe and Favorite:
  - One-to-Many relationship: Each recipe can be marked as a favorite by multiple users, but each favorite record is associated with one recipe (recipe in Favorite).

- User and Comment:
  - One-to-Many relationship: Each user can write multiple comments, but each comment has one owner (owner in Comment).

- Review and Comment:
  - One-to-Many relationship: Each review can have multiple comments, but each comment is associated with one review (review in Comment).

- Comment and Comment (Self-Referential):
  - One-to-Many relationship: Each comment can have multiple replies, but each reply is associated with one parent comment (parent in Comment).

# Manual Testing

Manual Testing for the overall functionality of the API was performed by entering dummy data in the backend both via Backend-and Front-end.
All data is CRUDed accordingly.<br>
<b>[Detailed manual testing is located here](./docs/testing/TESTING.md)</b>

## Validation
[Code Institutes Python Linter](https://pep8ci.herokuapp.com/) was used to check all ``.py`` files.

- List App and files with their current status.
- Reviews
  - ``views.py`` : no error found
  - ``serializers.py`` : no error found
  - ``models.py`` : no error found
  - ``urls.p`` : no error found

- Recipes
  - ``views.py`` : no error found
  - ``serializers.py`` : no error found
  - ``models.py`` : no error found
  - ``urls.p`` : no error found

- Profiles
  - ``views.py`` : no error found
  - ``serializers.py`` : no error found
  - ``models.py`` : no error found
  - ``urls.p`` : no error found

- Favorites
  - ``views.py`` : no error found
  - ``serializers.py`` : no error found
  - ``models.py`` : no error found
  - ``urls.p`` : no error found

- Comments
  - ``views.py`` : no error found
  - ``serializers.py`` : no error found
  - ``models.py`` : no error found
  - ``urls.p`` : no error found

- Cookbook_drf
  - ``urls.p`` : no error found
  - ``serializers.py`` : no error found
  - ``permissions.py`` : no error found

## Frameworks, libraries and dependencies
The following packages were installed using ``pip install``
<br>

``cloudinary``: Python client for Cloudinary, used for managing and optimizing media assets.

``dj-database-url``: Allows using Database URLs in Django for database configuration.

``dj-rest-auth``: Provides a set of REST API endpoints for user authentication.

``Django``: High-level Python web framework that encourages rapid development and clean, pragmatic design.

``django-allauth``: Integrated set of Django applications addressing authentication, registration, account management, and third-party (social) account authentication.

``django-cloudinary-storage``: Cloudinary integration for Django, for media files storage.

``django-cors-headers``: Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

``django-filter``: Used for filtering querysets dynamically.

``djangorestframework``: Powerful and flexible toolkit for building Web APIs.

``djangorestframework_simplejwt``: Provides JSON Web Token authentication support for Django REST framework.

``gunicorn``: Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model.

``oauthlib``: Implementation of OAuth1 or OAuth2.

``pillow``: Python Imaging Library (PIL) fork.

``psycopg2``: PostgreSQL database adapter for Python.


# Development and Deployment
The project was developed using GitHub and GitPod platforms...
- Navigate to: "Repositories" and create "New".
- Mark the following field: ✓ Public
- Select template: "Code-Institute-Org/react-ci-template".
- Add a Repository name: "your_repository".
- ...and create Repository.


For Commits on this project, the following commands ran:
- ``git add .`` <- Stages before commiting.
- ``git commit -m "written imperative declaration"`` <- Declares changes and updates.
- ``git push`` <- Push all updates to the GitHub Repository.

To run the server locally (Debug = True), the following command ran:
- ``python manage.py runserver`` <- Loads the website on the in-built Terminal.

During development migrations to the database were made.
To make migrations the following commands ran:
- ``python manage.py makemigrations`` <- Creates a new database migration
- ``python manage.py migrate`` <- Applies pending migrations

To create or update Requirements.txt file the following commands ran:
- ``pip3 freeze --local > requirements.txt``  <-Runs the req.
- ``pip install -r requirements.txt`` <- Install req.

To create a Superuser the following command ran (from Heroku terminal): 
- ``python manage.py createsuperuser`` (username->email->password1->password2) <- Creates a Superuser

To create a new Django project, in the currenct directory, the followig command ran:
- ``django-admin startproject NAMEOFTHEPROJECT .`` <- Starts the project

To create the app the following command ran:
- ``python3 manage.py startapp NAMOFTHEAPP`` <- Creates a folder for the app withing the project
- 

## Heroku
The website is being hosted and deployed on Heroku:
- Navigate to: "Create new app" add a unique name "djangorestframework-api" and select your region. Click "Create App"
- Head over to "Settings" tab and apply the respective config VARs
- Move to "Deploy" section and select "Github" method"
- From here search for the repository name "connect", from the GitHub account.
- Hit "Connect" and "Enable Automatic Deploys" to keep the the repository in parallel to Heroku.
- Manually "Deploy Main Branch".
- Upon successful deployment, retrieve the link for the mock terminal.
- The live app can be found [here](https://cookbook-drf-api-d322c7998986.herokuapp.com/).

## Forking
Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to 
  fork.

- On the top right of the page under the header, 
  click the fork button.

- This will create a duplicate of the full 
  project in your GitHub Repository.

## Other utils
- [dbdiagram.io](https://dbdiagram.io/home/) - ERD Diagram creation
- [Github Desktop](https://github.com/apps/desktop) - Provide an easy and effective way to manage commits and version control


# Credits
- CI Moments Project walkthrough provided me with a good understanding and technical knowledge on how to develop this api
- Extensive use of documentation provided by
  - [Django documentation](https://www.djangoproject.com)
  - [Django Rest Framework documentation](https://www.django-rest-framework.org)
  - [django-filter documentation](https://django-filter.readthedocs.io/en/stable/)
  - [django-recurrence documentation](https://django-recurrence.readthedocs.io/en/latest/)

# Acknowledgements
- The awesome slack for provide info and guides on how to display readme documentation 

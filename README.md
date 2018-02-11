# The Gram
## This is a web app that keeps residents of a place on the know about their neighbourhood. It is created using Django., 9/21/2018


## By **[Kepha Okari](https://github.com/kepha-okari)**

## Description
[This](https://kepha-the-watch.herokuapp.com/) is a neighbourhood information portal. A user with an account can:
* post image/message on the board
* view information regarding his/her neighbourhood
* move to new hood when need be
* has a profile
* comment on a post


## User Stories
As a user I would like:
* to sign in to use the application
* to upload photos/messages
* to see my profile update it
* see messeges relevant to my neighbourhood
* comment on a post

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.


## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display sign up for | N/A | Display sign up form when a user visits the site |
| Create an account | Fill the sign up form and **click submit** | Create an account and profile for the user and log the user into the site |
| Display current user's profile | **Click** the user icon | Display the current user's profile page with their posts |
| Upload a post | **Click** create post | Direct the user to a page with a form where the user can create and submit a post |
| Follow a neighborhood | **Click** follow link | Direct user to their timeline where they see the posts by neighbourhood he/she is following |
| Comment on post | **Click** comment link | Direct user to a page with a form for writing a comment |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Django 1.11
* Virtual environment
* Postgres Database
* Internet


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd hood
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE hoodwatch
```
9. Change the database information in `watch/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hoodwatch',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
```
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application


## Known Bugs

No known bugs


## Technologies Used
- Python3.6
- Django
- Bootstrap
- Postgres Database
- CSS
- HTML
- Heroku

### License

**[MIT](./LICENSE)** (c) 2018 **[Kepha Okari](https://github.com/kepha-okari)**

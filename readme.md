# WEB50X FINAL PROJECT: LOGISTIC SOLUTIONS WEBSITE

## Main idea
I created a website for a shipment company. The admin of the website can edit the content through the admin dashboard. The admin dashboard has been created using django jazzmin library. The main pages are:

* Home page
* Services page
* Contact page
* About page


## Distinctiveness and Complexity
The home page is not similar to anything we have already created. It's not a social media app nor an e-commerce. It's not similar to other years projects either. 

In terms of complexity, I used Django with more than one model (explained below) and several javascript files to the frontend. 
Moreover, all of the website is responsive to the different screen sizes (mainly mobile phones and computers).
The webite has been designed with figma, and the design then has been implemented with html, css, js, and bootstrap.
The admin dashboard has been implemented with django-jazzmin library.

## Files information

* In views.py there is all of the backend code. The main functions are:
    * home with all the dynamic data obtained from the database 
    * contact for contact page
    * about for about page with dynamic data 
    * services for services page with dynamic data 
    * create_quote for creating new quote request, which then the admin will use the info to make shipment to the customer.
    * create_contact for creating new contact request, it is similar to quote request but with less information (only a sufficient info for contact).

* Models.py. The different models are:
    * A Frieght_Type model
    * A Service model
    * A Why_choose_us model
    * A Contact_us model
    * A About_us model
    * A Quote model
    * A Contact model

* home.js:
    * handle click event of the request quote button and scroll smoothly to the request quote form
    * handle the click event of the dropdown items of freightType field of the request quote form, and change the innerText of the dropdown button to the clicked item and the value of the freightType hidden input field
    * handle click event of submit button of request quote and obtain the values of the input fields of the quote form and send an async request to create new quote
    * show loading spinner while waiting for the response of create new quote
    * handle the response of create new quote and show a "success" toast message if the quote has been create successfully

* services.js: scroll smoothly to the clicked service

* contact.js:
    * handle click event of submit button of contact form and obtain the values of the input fields of the form and send an async request to create new quote
    * show loading spinner while waiting for the response of create new contact
    * handle the response of create new contact and show a "success" toast message if the quote has been create successfully

* env.js: contain the server url

* Templates for all of the different html pages

* A main css file for the theme and common clases. 

* A css file for each html page

* A context_processors file for data used across all pages

* Other files like urls, admin, settings...

## How to run the application
* Install project dependencies by running pip install -r requirements.txt
* Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
* Run the server by running python manage.py runserver
* Make sure to change the serverUrl in env.js file to your host server url
* Make sure to create a new superuser and fill the website content through admin dashboard
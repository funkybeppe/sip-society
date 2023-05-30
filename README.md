# SipSociety - Online Wine Shop
<img width="1342" alt="Screenshot 2023-05-29 at 12 34 48" src="https://github.com/funkybeppe/sip-society/assets/105980082/7238c822-7a48-4836-baa9-363ae68f0c27">

# Overview
SipSociety is an e-commerce website created for a fictive wine shop located in London, UK. The main purpose of the project was to implement a fully functional online store that will make the process of selecting and purchasing wine products much easier for customers.
The users are given the possibility to see every product's details, create a wishlist, add items to the shopping bag, purchase with an online payment and access orders' history. Also, the staff members have permission for controlling the data using specially designed features.
The website was developed using Python(Django), HTML, CSS and JavaScript. The data was stored in a PostgreSQL database using ElephantSql for manipulation.

The fully deployed project can be accessed at [this link](https://sip-society-wine-shop.herokuapp.com/).

# UX
This site was created respecting the Five Planes Of Website Design:

### Strategy

### User Stories:

 ### VIEWING AND NAVIGATION
   * PURPOSE: As a user, I want to understand the purpose of the website from the first interaction with it content.
   * RESPONSIVENESS: As a user, I want to be able to easily use the site functionalities on all viewports, so I can shop the products from any device.
   * FOOTER: As a user, I want to see a footer with relevant information and documents.
   * ACCESSIBLE MENU: As a user, I want to be able to access a navigation menu at any time, so I can easily navigate through the website content.
   * PRODUCT SEARCH BAR: As a user, I want to be able search through site products by entering a key word.
  
 ### REGISTRATION AND USER ACCOUNTS
   * REGISTRATION: As a user, I want to be able to register on the website.
   * CONFIRMATION EMAIL: As a user, I want to be able to confirm my account with an email.
   * AUTHENTICATION: As a user/admin, I want to be able to authenticate using only email and password.
   * PASSWORD RESET: As a user, I want to be able to reset my password in case I lose it.
   * EASY LOGOUT: As a user/admin, I want to be able to easily logout at any time.
 
 ### PRODUCTS
   * PRODUCT LIST: As a user, I want to see a catalog with all the products sorted in categories.
   * PRODUCT DETAILS: As a user, I want to see a page with full specifications for every product, so I can easily decide which one I would want to buy.
   * SORTING: As a user, I want to be able to sort the listed products, so I can easily find the ones I am interested to buy.
   * AVAILABILITY: As a user, I want to be able to see the stock availability for low stock products.
   * SHOPPING BAG: As a user, I want to be able to add any product to the shopping bag in a selected quantity.
   * ADMIN: As an admin, I want to be able to add, edit or delete any product to the website.
 
 ### PRODUCT REVIEWS
   * UNREGISTERED USER: As a user, I want to be able to see all the reviews added for any product, so I can easily valuate its quality.
   * REGISTERED USER: As a logged in user, I want to be able to add my reviews for any product I want.

 ### WISHLIST
   * PRODUCT ADD: As a logged-in user, I want to be able to add/remove any product from the Wishlist.
   * PRODUCT LIST: As a logged-in user, I want to see all the products added to Wishlist.
   * SORTING: As a logged-in user, I want to be able to sort the products in the Wishlist.

 ### SHOPPING BAG
   * BAG REVIEW: As a user, I want to see all the products I added to the shopping bag.
   * PRODUCT DETAILS: As a user, I want to see all the details about the price for the order.
   * PRODUCT REMOVE: As a user, I want to be able to remove a product from the shopping bag.
   * QUANTITY EDIT: As a user, I want to be able to edit the quantity of the products.
   * DELIVERY: As a user, I want that all the delivery charges to be applied properly.

 ### PURCHASING AND CHECKOUT
   * ORDER DETAILS: As a logged-in user, I want to be able to see and edit my default delivery details for the order.
   * ORDER SUMMARY: As a user, I want to see the order summary with all the price details and quantity to ensure the order is correct.
   * PAYMENT DETAILS: As a user I want to be able to introduce my card details for payment.
   
 ### USER PROFILE
   * DETAILS: As a logged in user, I want to be able to see and edit my personal and delivery details.
   * ORDER HISTORY: As a logged-in user, I want to be able to see my orders history.

 ### NEWSLETTER
   * MARKETING EMAILS SUBSCRIPTION: As a user, I want to be able to subscribe to a newsletter, so I can always be up to date with the latest promotions.

#### Project Goal:
Create an e-commerce application for SipSociety wine shop that is useful for clients and staff members as well.
#### Project Objectives:
   * To create a website with a simple and intuitive User Experience;
   * To add content that is relevant and helps create a better image of the shop;
   * To differentiate between client and staff member accounts;
   * To make the website available and functional on every device.

### Scope

#### Simple and intuitive User Experience
* Ensure the navigation menu is visible and functional at every step;
* Ensure every page has a suggestive name that fits its content;
* Ensure the users will get visual feedback when navigating through pages;
* Create a design that matches the requirements of an e-commerce website.

#### Relevant content
* Add a representative cover image;
* Add the website title and details about its purpose;
* Add a section that includes information about the shop's name, location and contact data;
* Make a clear and beautiful designed presentation of the menu elements;

#### Features for upgraded experience
* Create a list with all the products and group them by category;
* Create a Bag feature that allows the user to add, update and remove products from the shopping bag;
* Create a Wishlist feature that gives the user the possibility to add and remove items from the wishlist;
* Create a Review feature that displays all the reviews added for a product and allows the user to add a review;
* Create a Checkout feature for giving the user the possibility to complete an order on the website;
* Create a Profile page for the user to add/update his delivery details and see his orders' history;
* Create a Newsletter feature that allows the user to subscribe with his email;
* Create a feature for the staff members to add/edit products on the website;

#### Responsiveness
* Create a responsive design for desktop, tablet and mobile devices.

### Structure
The structure of the website is divided into multiple pages and the content is displayed depending on authentication and client/admin type of user.

* Register/Login pages give the user the possibility to create an account and authenticate for accessing different features.
* Logout feature is a modal that helps user exit their current account;
* The Home page is visible for both types of users and includes relevant information about the websites' purpose and details a bout the wine shop, location and contact;
-The All products page displays a list with all the products available for selling;
* The Wines navigation link gives the user the possibility to access the list of products grouped by category, Red, White, Rose and Sparkling;
* The Product details page displays full specifications for a product and gives access to the Review feature. It also includes a feature for updating the shopping bag for users. Staff members have access to the feature for editing/removing current product;
* The Profile page is available for authenticated users and gives access to personal delivery details and orders' history;
* The Profile order details page gives access to the user to full specifications only for orders placed by him.
* The Wishlist page contains a list with all the products added by the user and cannot be accessed by guest;
* The Bag page displays all the items added in the shopping bag with associated features;
* The Checkout page includes an order summary and a form for personal, delivery and payment details;
* The Checkout success page displays full specification for the successful order;

### Skeleton 

#### Wireframes
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool.
<img width="554" alt="Screenshot 2023-05-29 at 20 16 24" src="https://github.com/funkybeppe/sip-society/assets/105980082/aedd1728-d609-4868-857b-203a4603a5af">
<img width="550" alt="Screenshot 2023-05-29 at 20 16 33" src="https://github.com/funkybeppe/sip-society/assets/105980082/1aa62a95-9a6c-462c-8ff6-3542e1818071">
<img width="547" alt="Screenshot 2023-05-29 at 20 16 47" src="https://github.com/funkybeppe/sip-society/assets/105980082/7492b625-611d-4425-a2f5-cbe13aae2032">
<img width="525" alt="Screenshot 2023-05-29 at 20 17 03" src="https://github.com/funkybeppe/sip-society/assets/105980082/dadf68f8-9af3-4932-91fe-5ac4c8c29aaf">
<img width="434" alt="Screenshot 2023-05-29 at 20 17 20" src="https://github.com/funkybeppe/sip-society/assets/105980082/160d1907-eb73-4122-9744-e4c40b97b416">




#### Database
The project uses the PostgreSQL relational database for storing the data.
![Screenshot 2023-05-29 at 18 14 16](https://github.com/funkybeppe/sip-society/assets/105980082/544a0ff0-e971-4361-a0d3-8f104750927e)


### Surface

#### Color Scheme
All the colours were selected with the eyedropper plugin from the website cover, to maintain chromatic harmony.

* The primary colour scheme was used for the most of the existent text on the website, in either dark or bright colours for creating a good contrast. The bottle green color has been used repetedly as a main colour, inspired by the color of the wine bottles.
 ••![Screenshot 2023-05-29 at 16 59 29](https://github.com/funkybeppe/sip-society/assets/105980082/0874520d-5fe3-4057-8f34-9d00bf6369a0)

* The secondary colour scheme was used for buttons, warnings, errors or for highlighting important information.
 ••![Screenshot 2023-05-29 at 17 04 27](https://github.com/funkybeppe/sip-society/assets/105980082/9cd80b5f-ab29-4a5a-a9ee-2e128ae40c19)


#### Fonts
* The font I used for this site was imported from [Google Fonts](https://fonts.google.com/):
  Body and Logo: Playfair Display, serif
  
#### Visual Effects
* A loading spinner is present when user submits payment for an order and waits for confirmation.
* Hover effect on navbar icons and underline for the footer.

## Business Model
* The business model chosen for this project is Businesgit stas to Customer, as the main purpose of the website is to deliver final products to customers. This model was implemented using an interactive, attractive and intuitive interface that gives the clients an upgraded experience for shopping.

![Screenshot 2023-05-29 at 17 15 02](https://github.com/funkybeppe/sip-society/assets/105980082/8ba5a088-3a6c-49ac-86d1-1237df844edf)


* The store offers a diverse selections of wines categorised as Red, Rose, White and Sparkling. Customers can order any quantity of the products within the limit of available stock.

## Marketing
* The marketing strategy includes a Facebook business page that is intended to create a good image of the shop by posting news and promotions available. By highly promoting the products and always adding new content, the page will increase its popularity and attract more and more customers to buy from the online store.
<img width="1308" alt="Screenshot 2023-05-30 at 07 44 38" src="https://github.com/funkybeppe/sip-society/assets/105980082/b9f8bf50-6a99-4eaf-a52d-d831fadaeb4a">
<img width="1236" alt="Screenshot 2023-05-30 at 07 45 01" src="https://github.com/funkybeppe/sip-society/assets/105980082/14602f2e-929c-41f3-a31e-73336e5671db">

## Agile Methodology
This project was developed using the Agile methodology.
All epics and user stories implementation progress was registered using GitHub Projects. As the user stories were accomplished, they were moved in the Project board from To Do, to In Progress, and Done lists.

## Features
### Existing Features

#### Products

Every user can access the page with the product catalogue. The items are listed attractively and their design is adapted to all devices.

* On every page with a catalogue of products, there is a section for filtering and sorting.
* The sorting feature is available for the user by selecting a value from the available options that will update the products' list   accordingly.
 <img width="464" alt="Screenshot 2023-05-29 at 18 17 08" src="https://github.com/funkybeppe/sip-society/assets/105980082/149370f6-cbda-42bc-a81b-7e22cc45de0f">

* All the products are listed including relevant information for the users.
 <img width="1133" alt="Screenshot 2023-05-29 at 18 17 46" src="https://github.com/funkybeppe/sip-society/assets/105980082/dfd28812-8171-4493-9393-6bda548ee2f2">

* Every products has a details page that includes full specifications.
 <img width="925" alt="Screenshot 2023-05-29 at 18 18 27" src="https://github.com/funkybeppe/sip-society/assets/105980082/2a255eb2-d184-4d7e-9be2-cbb59ae4189b">


#### Product Reviews

* On the Product Details page there is a list with all the reviews posted on the website and it is visible to all types of users. All the reviews have the same design and type of content. Important details are displayed such as Username, Date and time, Rating number and the Message posted.
 <img width="683" alt="Screenshot 2023-05-29 at 18 19 04" src="https://github.com/funkybeppe/sip-society/assets/105980082/10634e36-e96e-4088-b0e0-f668c67ec5c0">

* When a user is authenticated and he never posted a review, a form is provided for leaving a message and a star rating.
 <img width="320" alt="Screenshot 2023-05-29 at 18 19 29" src="https://github.com/funkybeppe/sip-society/assets/105980082/3d0ac870-674d-4544-b158-7bc64d0fda96">

* Only one review per person each item
* For authenticated users that already posted a review, they can submit another one which will update the review with new message and new rating number. This is to prevent a user to submit too many and compromise the rating.

#### Wishlist

* On the Product Details page there is an interactive feature that is only available for logged-in users. A user has the possibility to add a product to the wishlist through a form that uses a heart icon as a button. The heart shape defines the state of the product in the wishlist database.
<img width="179" alt="Screenshot 2023-05-29 at 18 19 46" src="https://github.com/funkybeppe/sip-society/assets/105980082/3fa09d35-8247-4cc3-a2a5-d786169a14ce">
<img width="202" alt="Screenshot 2023-05-29 at 18 19 52" src="https://github.com/funkybeppe/sip-society/assets/105980082/8c62f126-7aaa-4e64-8013-0d06f7999099">


* In the Wishlist page there are listed all the favourite items of the user with a design similar to the one created for the Products pages. Sorting section is also available and every element is linked to a Product Details page.
<img width="254" alt="Screenshot 2023-05-29 at 18 20 14" src="https://github.com/funkybeppe/sip-society/assets/105980082/c8f347a9-3c8c-4a89-8c24-883dc68dcd58">


#### Bag
* A feature for adding a product to the shopping bag has been created and included in the Products, Product Details and Wishlist pages. This is a form for updating the products existing in the shopping bag and also their quantity.
* In the Bag page there are listed the added items with details about quantity and price. Any item can be removed by clicking on the remove link and also the quantity can be updated.
<img width="1127" alt="Screenshot 2023-05-29 at 18 20 37" src="https://github.com/funkybeppe/sip-society/assets/105980082/da3f880f-0689-4912-a455-83f439908d3e">

#### Checkout
* The Checkout page represents the final step in completing the order.
A form for personal, delivery and payment details is displayed for the user to fill in with valid data. The payment input has its own Stripe-implemented validation.
<img width="572" alt="Screenshot 2023-05-29 at 18 21 39" src="https://github.com/funkybeppe/sip-society/assets/105980082/a6431ee6-beae-457f-b904-dbc15d20c7b9">
<img width="582" alt="Screenshot 2023-05-29 at 18 21 54" src="https://github.com/funkybeppe/sip-society/assets/105980082/81403308-11a8-4ea4-a315-5b933087db30">

* An order summary is displayed with details about the products and cost.
* After the order is completed, the user is sent to a *Checkout Success * page with full specifications and details.

#### User Profile
The User Profile page gives the user access to individual and private features.

* The page includes a form for adding or updating the delivery details. These details are saved in the database and whenever the user is logged in and wants to make an order, the values will be automatically set in the checkout form.
<img width="610" alt="Screenshot 2023-05-29 at 18 22 45" src="https://github.com/funkybeppe/sip-society/assets/105980082/905fa348-75f3-409c-b179-46719cda2e8a">

* Another important feature is the Orders history which is represented by a table with all the orders created by the user. Any order element has a details page that can be accessed by clicking on the order number value.
<img width="619" alt="Screenshot 2023-05-29 at 18 22 55" src="https://github.com/funkybeppe/sip-society/assets/105980082/82130fb7-6188-4bac-be8d-cd25bb03e68b">

#### Admin
The admin account was created as a superuser account from the terminal and also has access to the admin panel.
* An admin user have access to features for adding a new product, edit a product's details and delete product. The last two implementations are available on the Products and Product Details page and only for staff accounts.
* <img width="241" alt="Screenshot 2023-05-29 at 18 23 11" src="https://github.com/funkybeppe/sip-society/assets/105980082/09d7077a-8d5b-46f5-8ec1-df0e604ddb7a">

* <img width="599" alt="Screenshot 2023-05-29 at 18 23 28" src="https://github.com/funkybeppe/sip-society/assets/105980082/c2e17d60-6532-4a7f-bcc5-1180637d235c">

* <img width="599" alt="Screenshot 2023-05-29 at 18 23 41" src="https://github.com/funkybeppe/sip-society/assets/105980082/769a3340-a4d6-41fd-93a6-2c12ccbbb946">

### Future Feature Considerations
* Implementing a chat feature for communication between customers and staff members. This would be useful for any client that has an issue on the website and also will create a better and faster way of finding solutions. 
* Creating a feature for easily sending advertising emails to all the customers. This would be a default template form to be filled and the email will be automatically sent to the clients.
* Create a better platform for Admin, so that some content and features available for users are not for admins. A page to display all the orders without accessing Django Admin.

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, custom breakpoints were used.

#### Breakpoints:
- max-width:360px(extra small devices)
- max-width:500px(small devices)
- max-width:991px(medium devices)
- min-width:992px(medium devices)
- min-width:1200px(large devices)
#### Tested devices:
- Moto G4 
- iPhone SE 
- iPhone XR 
- iPhone 11 
- iPhone 13
- iPhone 5/SE 
- iPhone 6/7/8 
- Ipad
- Ipad Air 
- Ipad Mini
- Ipad Pro 
- Pixel 5 
- Surface Duo 
- Surface Pro 7 
- Nest Hub 
- Nest Hub Max
- Samsung Galaxy S20 Ultra 
- Samsung Galaxy S8 
- Galaxy Note 2 
- Galaxy Tab S4
- Macbook Pro 14"
- Samsung Odyssey G9 49"

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program
[Visual Studio](https://code.visualstudio.com/) - for writing and testing the code
[Heroku](https://heroku.com/) - used for deploying the project
[Balsamiq](https://balsamiq.com/) - for creating the wireframes
[DrawSQL](https://drawsql.app/) - used for creating the Database relational schema
[Favicon.io](https://favicon.io/) - used for generating the website favicon
[Image Resizer](https://imageresizer.com/) - for compressing the images
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons
[Bootstrap4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - for adding predifined styled elements and creating responsiveness
[Google Fonts](https://fonts.google.com/) - for typography
[JsHint](https://jshint.com/) - used for validating the javascript code
[pycodestyle](https://pypi.org/project/pycodestyle/) - used for validating the python code
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri)- used for validating the CSS
[Chrome Dev tools](https://developer.chrome.com/docs/devtools/) - for debugging the project
[AWS](https://aws.amazon.com/) - for storing media and static data
[Stripe](https://stripe.com/gb) - for payments
[ElephantSql](https://www.elephantsql.com/) - for hosting the PostgresSql database migrated from Heroku LightHouse - for testing performance
Gmail - for sending emails using the SMTP server

### Python packages
* django
* django-allauth
* dj-database-url
* psycopg2-binary
* gunicorn
* heroku
* django-heroku
* boto3
* django-storages
* pillow
* django-countries
* stripe
* django-phonenumber-field

## Testing
The testing documentation can be found at [TESTING.MD](https://github.com/funkybeppe/sip-society/edit/main/TESTING.md)

## Deployment
### Deploy on Heroku
1. Create Pipfile
In the terminal enter the command  pip3 freeze > requirements.txt, and a file with all the requirements will be created.

2. Setting up Heroku
* Go to the Heroku website (https://www.heroku.com/)
* Login to Heroku and choose Create App
* Click New and Create a new app
* Choose a name and select your location
* Go to the Resources tab
* From the Resources list select Heroku Postgres
* Navigate to the Deploy tab
* Click on Connect to Github and search for your repository
* Navigate to the Settings tab
* Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.

3. Deployment on Heroku
* Go to the Deploy tab.
* Choose the main branch for deploying and enable automatic deployment
* Select manual deploy for building the App

### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, useFork directly from GitHub:

* On [My Repository Page](https://github.com/funkybeppe/sip-society/), press Fork in the top right of the page
* A forked version of my project will appear in your repository

### Clone the repository
For creating a clone of the repository on your local machine, use Clone:

* On [My Repository Page](https://github.com/funkybeppe/sip-society/), click the Code green button, right above the code window
* Chose from HTTPS, SSH and GitClub CLI format and copy (preferably HTTPS)
* In your IDE open Git Bash
* Enter the command git clone followed by the copied URL
* Your clone was created

## Credits
### Content
* The content of the website is fictive.

### Media
* All products images used on the site were taken from [Google](https://www.google.com/)

### Code 
* Templates were taken and adapted from [Code Institute](https://learn.codeinstitute.net/) project Boutique Ado
* The Review code was taken and adapted from [Stackoverflow](https://stackoverflow.com/)
* The loading spinner was taken and adapted from [Code Institute](https://learn.codeinstitute.net/) project Boutique Ado
* The email subscription form was taken and adapted from [Mailchimp](https://mailchimp.com/)

## Acknowledgements
Code Institute for all the material and support offered
Slack community for great involvement in helping each other
My partner Jess for everyday support and patience

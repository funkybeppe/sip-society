# Testing

Back to README.MD

## User Story and Feature Testing
All the user stories were tested manually, including all the representative features, and were described below with a summary of the steps made for demonstrating the validation of the tests:

## VIEWING AND NAVIGATION

#### PURPOSE
As a user, I want to understand the purpose of the website from the first interaction with it
Acceptance Criteria: A site user should see information about the promoted wine shop and its products.

Summary:

When a user first opens the site, he is redirected to the home page where the role of the site is described;
The home page contains a cover with an image that suggests what the products that are being sold;
The title that exists on the cover clarifies that the website is made for selling fine wines and sparkling drinks;
A button attracts the user to click on it for being redirected to the products page;
There is a section with privacy documents, terms & conditions and contact details.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### RESPONSIVENESS
As a user, I want to be able to easily use the site functionalities on all viewports, so I can shop the products from any device
Acceptance Criteria: A user should be able to see a nice design adapted for all devices.

Summary:

The website's features are functional on all types of devices;
The headers have been adapted to fit the smaller devices' screens;
The forms' inputs have been adapted to fit the smaller devices' screens.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### FOOTER
As a user, I want to see a footer with relevant information and documents
Acceptance Criteria: A user should see relevant information and important documents that clarify privacy aspects.

Summary:

The footer contains link to All products page;
The footer contains link to Privacy And Policy document for the website;
The footer contains link to Terms & Conditions document for the website;
The footer contains links to social media pages.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### ACCESSIBLE MENU
As a user, I want to be able to access a navigation menu at any time, so I can easily navigate through the website content
Acceptance Criteria: A site user should always have access to the navigation menu so he can easily switch between pages at any time.

Summary:

When a user visits the website he can easily see the navigation menu at the top of the page;
Even if switching the pages, the menu is always present and indicates what page is active at the moment;
The navigation menu is set to sticky so it is always fixed on the top of the page;
For logged-in clients, the menu contains an additional page, My Profile, and Logout link replaces Register and Login pages;
For logged-in staff members, the navigation includes Product Management link to add a new product.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### PRODUCT SEARCH BAR
As a user, I want to be able to search through site products by entering a keyword
Acceptance Criteria: A site user should be able to use the search feature for filtering through site products.

Summary:

A search bar is present at any time on the top navigation header;
The user can enter and submit any keyword;
The websites display only the products that contain in their description the keyword entered by the user, or an informative text if no product matches the search query;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

## REGISTRATION AND USER ACCOUNTS
#### REGISTRATION
As a user, I want to be able to register on the website
Acceptance Criteria: A site user should be able to create an account by filling in a form on the website.

Summary:

There is a Register page that provides a form with email, first name, last name and password for the user to fill in;
When the user submits the form he is redirected to a page that informs him that he needs to verify his email to finalize the signup process;
A info alert is displayed with the message "Confirmation e-mail sent to..." that suggests the user verify his email.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### CONFIRMATION EMAIL
As a user, I want to be able to confirm my account with an email
Acceptance Criteria: A site user should be able to confirm his account using his email.

Summary:

An email is sent to the user when he tries to register on the page;
The email includes a link that will redirect him to a page from the shop website where he can confirm the email by clicking on a button.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### AUTHENTICATION
As a user/admin, I want to be able to authenticate using only email/username and password
Acceptance Criteria: A site user should be able to authenticate at any time with email/username and password.

Summary:

There is a Login page that provides a form with email/username and password to be filled;
The authentication form has a "Remember me" checkbox that will keep the user logged in;
A success alert is displayed with the message "Logged in as..." that confirms to the user that he has been logged in successfully.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### PASSWORD RESET
As a user, I want to be able to reset my password in case I forgot it
Acceptance Criteria: A site user should be able to reset his password with his email.

Summary:

On the Login page there is a clickable link with the text Forgot password?;
The link redirects the user to a page where he can enter the email address where he wants to receive the email for resetting the password;
An email is sent to the specified address with a link;
The link redirects the user to a page on the shop website where he can enter and submit the new password;
The user can now authenticate with the updated password.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### EASY LOGOUT
As a user/admin, I want to be able to log out at any time
Acceptance Criteria: A site user should be able to exit the current account at any time.

Summary:

There is a Logout link when clicking on the hyperlink in the navbar which redirects to a logout page.
The logout page asks the user again if he wishes to log out of the current account;
A success alert is displayed with the message "Logged out" that confirms to the user that he has been successfully logged out.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

## PRODUCTS

#### PRODUCT LIST
As a user, I want to see a catalogue with all the products and also grouped by categories
Acceptance Criteria: A user should be able to access a page with all the products, and other pages for every category.

Summary:

In the navigation menu there are separate links that redirect the user to the products' catalogue. These links are classified as: All products, White Wines, Red Wines, Rose Wines and Sparkling Wines;

By testing this feature, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### SORTING
As a user, I want to be able to sort the listed products, so I can easily find the ones I am interested to buy
Acceptance Criteria: A user should be able to sort products in the order specified and products

Summary:

On the pages that contain a list of products, there is a sorting section on the top of the page;
All sorting options work properly;
By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### AVAILABILITY
As a user, I want to be able to see the stock availability for low-stock products
Acceptance Criteria: A user should see a banner with text that informs him about the product's availability.

Summary:

Every product that is in low stock contains a banner element with information about its value;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### PRODUCT DETAILS
As a user, I want to see a page with full specifications for every product, so I can easily decide which one I would want to buy
Acceptance Criteria: A user should have access to every product's full description

Summary:

Every element listed on products' pages is clickable and it redirects to the selected product's details page;
The details page includes the product's name, price, information about the wine's origins, code and food pairing;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### SHOPPING BAG
As a user, I want to be able to add any product to the shopping bag in a selected quantity
Acceptance Criteria: A user should be able to select the quantity value and add any product to the shopping bag.

Summary:

There is a container with input for quantity and an Add to bag button on every element listed in products pages;
There is a container with input for quantity and an Add to bag button on every product detail page;
The quantity input has validation that doesn't allow the user to insert and submit a value greater than the stock value or smaller than 1;
When a product is added to the shopping bag an alert is triggered with the success message "Added ... to your bag"
When the same product is added to the shopping bag, only the quantity value is updated and an alert is triggered with the success message "Updated ... quantity to ...".

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### ADMIN
As an admin, I want to be able to add, edit or delete any product on the website
Acceptance Criteria: An admin user should have access to a form to add product. An admin user should have access to a form to update specifications for any product. An admin user should have a delete button to delete any product.

Summary:

When a user is logged in as admin, the navigation panel includes a link for Add a new product;
When the link is clicked, a page opens and contains a form with fields for every detail of the product;
The form has validation that prevents the user to add a product with invalid information.
After the form is submitted, the element is added to the products' list.
When a user is logged in as admin, the page for product details adds a button for Edit product and one for Delete product;
When the edit button is clicked, a page opens and contains a form for editing every detail of the product;
The form is prefilled with existing data;
The form has validation that prevents the user to update a product with invalid information;
Any update is reflected in the product's details page;
When the delete button is clicked, the product is deleted from the website;

By testing all these features, it can be affirmed that the user story is accomplished.


Outcome: Pass

## PRODUCT REVIEWS

#### UNREGISTERED USER
As a user, I want to be able to see all the reviews added for any product, so I can easily make an opinion about its quality
Acceptance Criteria: A user should have access to a way of seeing all the reviews for any product.

Summary:

All the reviews registered for a product are listed on the Product details page;
Every review element contains relevant details such as User name, Review text, rating number and Date and Time of posting;
The reviews are ordered by time in a reverse way so that the last added review is the first on the list.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### REGISTERED USER
As a logged-in user, I want to be able to add a review for any product I want
Acceptance Criteria: A logged-in user should be provided with a way of adding a review for any product.

Summary:

On the Product details page there is a section for "Add a review" only visible for authenticated users;
For a user that hasn't already added a review to the list, there is a form to fill in for creating one;
The form only contains an input for the review message to be posted, and rating number from 1 to 5 with 3 as default;
There is no implementation for approval of the review because a shop has to have real and transparent reviews of products;
When the review is posted, an alert is triggered confirming that the review was successfully added to the list;
The response is immediate and the review appears as the first on the list;
Every user can only post 1 review for each item, this is to prevent the compromisation of the rating;
Submitting the form again with another review will update the existing one;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

## WISHLIST

#### PRODUCT ADD
As a logged-in user, I want to be able to add/remove any product from the Wishlist
Acceptance Criteria: A logged-in user should be able to add a product to the wishlist through an implemented feature.

Summary:

On every product's details page there is a wishlist feature visible only to users that are authenticated;
To add a product object to the wishlist, a form is displayed with an empty heart icon that acts like a button, and a suggestive message, "Add to wishlist", that indicates to the user what is its purpose;
When the user clicks on the button, the change is visible immediately, as the heart icon changes its shape into a filled heart, and the message is now "Remove from Wishlist";
The change is also reflected in the Wishlist page where the list of products includes only the ones that are currently in the wishlist database;
By clicking on the filled heart, the form comes back to its initial state, and the wine is removed from the list.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### PRODUCT LIST
As a logged-in user, I want to see all the products added to the wishlist
Acceptance Criteria: A logged-in user should be able to access a page with all the favourite products.

Summary:

For an authenticated user the content of the Wishlist page is available with all the products added to the wishlist;
The page content is not accessible to guest users;
Every product element is clickable and redirects to the details page.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### SORTING
As a logged-in user, I want to be able to sort the products in the wishlist
Acceptance Criteria: A logged-in user should be able to sort the products on the Wishlist page.

Summary:

On the wishlist page, there is a select input for sorting the products section on the top of the page;
All sorting options work properly;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

## SHOPPING BAG

#### BAG REVIEW
As a user, I want to see all the products I added to the shopping bag
Acceptance Criteria: A user should be able to access a page with all the products added to the shopping bag.

Summary:

There is a Shopping bag page with a table that contains every product added to the bag in the selected quantity;
The table list reflects the actual state of the added products.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### PRODUCT ADD 

#### PRODUCT DETAILS
As a user, I want to see all the details about the price for the order
Acceptance Criteria: A user should be able to see a section with price details for the items added to the shopping bag.

Summary:

On the Shopping bag page, for every product in the table, the price per item and the total price is displayed;
There is also an Order Summary section with full specifications about the total and grand total price, and also the part of it calculated for delivery;
The value from Order Summary section updates according to the shopping bag list of products and quantity update.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### PRODUCT REMOVE
As a user, I want to be able to remove a product from the shopping bag
Acceptance Criteria: A user should be able to delete any product from the shopping bag through an implemented feature.

Summary:

On the Shopping bag page, for every product in the table there is a link for deleting the product;
When the users click on the link, the product is removed from the bag.
After the deletion, the bag is updated.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### QUANTITY EDIT
As a user, I want to be able to edit the quantity of the products
Acceptance Criteria: A user should be able to update the quantity for any product from the shopping bag through an implemented feature.

Summary:

On the Shopping bag page, for every product in the table there is a feature for updating the quantity;
The feature includes an input with addition and subtraction buttons that can be used to set the value for the quantity;
The Update quantity button submit action sets the input value as the quantity value and also updates the price details.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### DELIVERY
As a user, I want that all the delivery charges to be applied properly.
Acceptance Criteria: The delivery should be calculated correctly on the bag total, no delivery changes applied after reaching £60.

Summary:
On the shopping bag page there is a section next to the total where it shows if delivery charges occurs;
If the total is less than £60, 10% delivery charge on the bag total;
If the total is more than £60, no delivery charges;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

## PURCHASING AND CHECKOUT

#### ORDER DETAILS
As a logged-in user, I want to be able to see and edit my default delivery details for the order
Acceptance Criteria: A logged-in user should be able to see and update his delivery details if they were registered before.

Summary:

On the Checkout page there is a form section with fields for delivery information;
The form section for delivery details is prefilled with data corresponding to the authenticated user if it exists;
If the checkbox with the text Save delivery details to my profile is checked, the profile will be updated with the delivery data from the form on submit;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### ORDER SUMMARY
As a user, I want to see the order summary with all the price details
Acceptance Criteria: A logged-in user should be able to see a section with price details for the items added to the checkout.

Summary:

On the Checkout page, there is a table with every product added to checkout;
On the Checkout page, for every product in the table, the price per item is displayed;
There is also an Order Summary section with full specifications about the total price, grand total price, discount and also delivery cost;

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### PAYMENT DETAILS
As a user, I want to be able to introduce my card details for payment
Acceptance Criteria: A user should be able to add his payment details in order to complete the order

Summary:

On the Checkout page there is a form section with fields for payment information;
The form can be filled by the user with the card details;
The card input has validation that doesn't accept invalid card details.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

## USER PROFILE

#### DETAILS
As a logged-in user, I want to be able to see and edit my delivery details
Acceptance Criteria: A logged-in user should be able to add his delivery details to the profile page.

Summary:

On the Profile page, there is a form with fields for delivery details;
When the user adds or updates the delivery values in the Profile page, the form from the Checkout page is prefilled with the updated data.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

#### ORDER HISTORY
As a logged-in user, I want to be able to see my orders history
Acceptance Criteria: A logged-in user should be able to see a list of the orders he has made.

Summary:

On the Profile page, there is a table that includes a list of all the orders made by the authenticated user;
Every order element displayed in the table contains information about the order number, date, quantity and total price.
By clicking the link on the order the user can find the full order details;

By testing all these features, it can be affirmed that the user story is accomplished.
Outcome: Pass

## NEWSLETTER

#### MARKETING AND EMAIL SUBSCRIPTION
As a user, I want to be able to subscribe to a newsletter, so I can always be up to date with the latest promotions
Acceptance Criteria: A user should be able to register his email to newsletter for getting informed about the latest promotions

Summary:

There is a form available in the footer of every page where the user can register his email;
The form has validation that doesn't let the user register the same email twice.

By testing all these features, it can be affirmed that the user story is accomplished.

Outcome: Pass

## ADDITIONAL MANUAL TESTING

#### Error Handling

Ensure that 404 HTTP errors display the custom 404.html.
Stress Test: Input a random route in the URL that can't be found in the declared paths of the project

#### Interface Interaction
Ensure all interactive elements respond appropriately:
Desktop:
All navbar elements correctly respond to hovering.
All buttons correctly respond to hovering.
All authentication links correctly respond to hovering
Mobile:
All navbar elements correctly respond to touch.
All buttons correctly respond to touch.
All authentication links correctly respond to touch

#### Links
Ensure the external links to social media present in the footer open up in new tabs.

### Browser Testing
The website was tested on different browser for assuring the features work accordingly.

* Chrome
* Edge
* Safari
* Opera
* Firefox

### Code Validation

#### HTML
The html code of the website was validated using W3 Markup Validator.
At the time of deployment the validation have the following outcome:

#### CSS
The CSS code was validated using W3 Jigsaw Validator
At the time of deployment the validation for base.css has the following outcome:

#### JAVASCRIPT
The Javascript code was validated using using JsHint

#### PYTHON
The python code was tested using pycodestyle online validator.
At the time of deployment the python code validation has the following outcome:

### Accessibility
The accessibility of the website was tested with Wave

### Performance
The performance of the website was tested with Google Lighthouse

### Bugs
Form reloads page
The bug here is the fact that when a user submits any kind of form, the page is reloaded and the user is brought to the top of the page. This results in a decrease in the user experience's quality because sometimes the user has to scroll back to the element where the action has been performed.

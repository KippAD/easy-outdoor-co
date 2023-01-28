# **The Easy Outdoor Co.**


## **Brief**
The Easy Outdoor Co. is an e-commerce site for a fictional store that sells clothing and equipment for outdoor activities. The application takes payments using Stripe and logs orders. Features for the site owner include adding and updating products, deleting stock, and sending newsletters to a mailing list attached to the database. Users are able to create an account, review products, and make orders. 

This project was undertaken as my Milestone 5 E-commerce project for my Full Stack Software Engineering diploma with Code Institute. The project was planned using Agile methodology and built using the Django framework alongside various other technologies.

## **Planning**

### **Objectives**

Planning this project required considering the ideal goals of the user, the site owner, and the necessary steps to achieve them as the developer of the project. At the highest level of abstraction these goals are:

- **User**: The user wants to be able to browse for products and buy them easily.
- **Owner**: The owner wants to be able to profit off the business and manage the store.

#### **To achieve these goals:**

**User**:
- Create an interface that the user can move through intuitively.
- Site actions are clear and the user can achieve their objectives without hassle.
- The site is aesthetically attractive and users enjoy using it.
- Content is organized in a hierarchy of importance so that users can get where they need to be quickly.

**Owner:**
- SEO will improve the websites traffic and therefore increase the amount of orders made.
- Marketing such as a newsletter and social media will ensure that users return to the site and increase the amount of sales.
- A custom admin UI will improve the owners User Experience by making CRUD on the database more intuitive.
- Managing discounted prices, products, sending newsletters are all easily achieved from within the UI.

## **User Stories**
By considering the requirements for the User and Owner, as well as the intended marketing techniques, I could then break the requirements of a successful development into epics. From there I broke the epics down into User Stories which were used to decide on the project’s required features.

###  **User Stories**

**Epic: Site Navigation**

A clear, well designed, and simple UI that allows both staff and customers to use navigate the site easily.

- As a **user** I can **easily navigate the site** so that **I can access the different areas of the shop and complete user actions intuitively**
- As a **user** I can **view products** so that **I can browse the products for sale on the site**
- As a **user** I can **filter products by category** so that **narrow down shopping searches to items relevant to my interests**
- As a **user** I can **search for products** so that **query for specific items of interest faster**
- As a **user** I can **sort product search results** so that **I can filter through products by various attributes intuitively**
- As a **user** I can **view a list of frequently asked questions** so that **I can have my queries answered without contacting the site admin**

**User Epic: Buying Products**

Buying products is simple and quick and all of the relevant information to make an order is clear to a shopper.

- As a **user** I can **select the sizes of items** so that **I can choose specific clothing sizes when I buy items**
- As a **user** I can **add products to a basket** so that **I can store items in a list of products to purchase as I navigate through the site**
- As a **user** I can **clearly see what items are currently in stock** so that **I am aware which items can be ordered immediately**
- As a **user** I can **see the total cost of my order** so that **I am aware exactly how much I am required to pay**
- As a **user** I can **view delivery costs** so that **I am aware of any surplus charges to my order**
- As a **user** I can **see discounted products** so that **I am aware of opportunities to save money on purchases**
- As a **user** I can **update the quantity of items in the basket** so that **I can easily manage the items I wish to order**
- As a **user** I can **remove items from the basket** so that **I can delete any unwanted items from my order**
- As a **user** I can **make secure payments** so that **I can safely order items with my card**
- As a **user** I can **update the quantity of items in the basket** so that **I can easily manage the items I wish to orderr**
- As a **user** I can **join a newsletter** so that **I can be made aware of any news or promotions running in the store**

**Epic: Account Management**

Users can create a profile, manage their own information and speed up the checkout process with saved personal data.

- As a **user** I can **create an account** so that **I can manage my personal details and view order history if I am a regular shopper**
- As a **user** I can **save my personal details when checking out** so that **placing orders is faster in future**
- As a **user** I can **manually add my personal information to a profile** so that **I can checkout faster when ordering**
- As a **user** I can **update my profile information** so that **I can keep my personal details up to date**
- As a **user** I can **view my order history** so that **I can access information about unfulfilled and past orders**
- As a **user** I can **change my password** so that **I can keep my account safe and access my profile if I lose my password**
- As a **user** I can **delete my account** so that **I can maintain control over my personal information**
- As a **user** I can **rate products** so that **I can give feedback to the store and other prospective buyers on items that I have purchased**
- As a **user** I can **contact the store** so that **I can have any queries answered by the site admin**
- As a **user** I can **create a wish list of items so that I can save products to buy at a future date**

**Epic: Site Management**

Site staff can manage products, update stock, send newsletters and complete other actions of managing the database.

- As an **admin** I can **add products to the store** so that **I can keep the product list up to date with new arrivals**
- As an **admin** I can **update existing products** so that **I can manage the information of currently listed products**
- As an **admin** I can **delete existing products** so that **I can remove products from the product database**
- As an **admin** I can **hide products from the store** so that **I can remove out of stock or faulty items from being displayed**
- As an **admin** I can **manage stock** so that **I can maintain that items for sale are available to be bought and shipped**
- As an **admin** I can **add a discount to items** so that **I can create a list of items on sale**
- As an **admin** I can **change my password** so that **I can keep my account safe and access my profile if I lose my password**
- As an **admin** I can **delete my account** so that **I can maintain control over my personal information**
- As an **admin** I can **rate products** so that **I can give feedback to the store and other prospective buyers on items that I have purchased**
- As an **admin** I can **send a newsletter so that I can keep users up to date with the latest deals or promotions**

The four epics are ranked in terms of priority. In order for the site to function in its most basic state the user needs to be able to navigate the site and buy products. To greatly improve the UX of the user the account management epic can be added next. Finally Django has a built in admin panel so the site management epic is of lowest priority.

### **Marketing Techniques**

An integral part of developing a successful online store is how you can achieve a higher traffic of users.

- **Newsletter:** Using a newsletter subscription allows users to easily opt in to an email that notifies them of the promotions that the store is offering.
- **Social Media:** An active social media presence would offer similar advantages to that of a newsletter. It would also allow the running of ads through the social media website, which would reach a much wider audience than that of just the users that have subscribed to the newsletter.
- **Sales:** Sales and promotions in general are an important aspect of bringing customers in. Using discounted products in emails and social media posts will entice users onto the site.
- **SEO:** Search engine optimisation will increase the likelihood of users finding the site when searching, therefore increasing the amount of users on the site.


## **Project Management**
These user stories were added to a project board on this repository's project board so that development could be managed.

[**Project Board**](https://github.com/users/KippAD/projects/6/views/1)

## **Design**

### **Design Objective**
- The site is aesthetically appealing and users enjoy being on the site.
- Users are able to complete site actions and navigate intuitively.
- The user rarely encounters errors but is redirected appropriately when doing so.
- Site information is presented in a heirachy of importance.

### **Wireframes**

The wireframes on the site were created with Figma. The design itself was intended to be fairly simple to keep the entire experience for the user as neat and uncomplex as possible and to avoid creating a visual overload.


## **Features**

### **Navbar**
The navbar allows easy and intuitive navigation throughout the site. Built from bootstraps responsive navbar template, the navigation bar minimizes into a burger menu on smaller screens and features dropdowns to contain all of the necessary links.

- **Burger Menu** - The navbar transforms into a burger menu so that the page isn’t crowded with links on smaller devices.
- **Search Bar** - The search bar allows the user to quickly search for products from anywhere on the site; they will be transported to a list of products matching their query upon submitting.
- **Profile Icon** - The profile icon features a dropdown menu that allows the user to view their profile and order history. The icon is dynamic so that it only displays if a user is logged in, otherwise it shows a login link. It also displays a link to the admin panel if the user is a staff member.
- **Basket Icon** - The basket icon in the navbar will display the total amount of different items in the basket. It also allows the user to access their shopping basket from anywhere on the site.

### **Home**
Most of the site is quite simple in its design, usually using black and white colors with an orange color to signify user actions. This is not to overload the user when they are trying to use the site's functionality. The home page however is the first place that the user lands, so there is an impetus on aesthetic design in order to entice the user to stay, as well as concise information that explains the site's purpose.

- **Hero Image** - The hero image is the first thing the user sees. The idea is that they are drawn in by an impressive image, and a catchy overlay text - they then can surmise what the purpose of the store is.
- **Shopping Panels** - The panels link to the three main sections of the shop; the sale, clothing, and equipment. These images draw the user in more to the necessary actions to view products more so than the smaller links in the navbar.
- **About Us** - This describes the purpose of the store in much more detail than the hero overlay, allowing the user to unravel information about the site as they move through it rather than overloading them with content all at once.
- **Product Carousel** - The product carousel is a scrollable assortment of random items from the store. If a first time user is seeing this feature, they have potentially not seen a product yet. This feature brings the product section to them, showing them the sort of items that are sold without them having to navigate to a different area.
- **Footer** - The footer contains mosts of the navigation that has already been shown in the navbar and the home page. It also includes a newsletter subscription form and a link to the sites instagram page.

### **Products**
The products section displays all of the products for sale on the store, and also allows the user to sort or filter them by different categories to help them narrow items down to those that are relevant to them.

- **Discounted Items** - Items with a discounted price display both the original price and the sale price. This shows the user the amount of money they can save on an item during its promotion period. The sale tab also limits all products to those that are discounted, meaning the user can browse all discounted items at once.
- **Sorting Dropdown** - The user can quickly sort items by their name, price, category and rating. This improves their user experience by streamlining their search.
- **Reviews** - The user is able to see the star rating of the product, and can also see the amount of reviews left on a specific item. From there they can view the reviews and comments left by users on items of interest.
- **Product Detail** - Upon clicking a product in the main product page, the user is brought to the product detail page. This page displays the product information, as well as a quantity selector and a size selector that the user can use to add the product to the basket.
- **Related Products** - The product detail page also contains a related products carousel which contains products of the same category as that of the product the user is viewing. This allows them to continue their search easily with relevant items if they are not interested in purchasing the item in the product detail.

### **Basket**
The basket is accessed by the shopping cart icon in the navbar. It contains every item added to the basket by the user, their size, quantity, price, and total price. The user is able to manage the products from there by increasing or decreasing their quantity, or removing them entirely.

- **Quantity Input** - The user can update the total quantity of their items from the basket. This allows them to control their shopping basket easily, and manage the total cost of the order.
- **Remove From Basket** - The user can remove items from the basket by setting the quantity to 0 or by selecting the x icon on the item’s panel.

### **Stock**
The site features stock management. Stock can be managed by staff and is automatically adjusted when orders are completed.

- **Dynamic Stock** - Stock is automatically decremented when sales are completed. Out of stock items remove the ability to add the product to the basket.
- **Basket Validation** - Stock value is used to validate the quantity of items added to the basket. This prevents users from setting a quantity greater than the remaining stock and putting the business in a position where they cannot fulfill their orders.

### **Account & Profile**
The user can manage their account and view order history by accessing the user icon in the navigation bar. They are able to manage their personal details and keep track of their orders. Allauth is used to manage the users login, password and confirmation emails.

- **Profile** - The user profile section is where the user can add and update their personal details and delivery information. Their information is then used to speed up the checkout process by preloading the checkout form to improve their user experience.
- **Order History** - The user is also able to view details about previous orders. They are also able to rate items if they have purchase them, and are shown the ratings that they have given items when reviewing them.
- **AllAuth** - AllAuth allows the user to easily access and administer their account, with the templates being customized to fit the design of the website.

### **Reviews**
The user is able to give a star rating and leave a comment review of products that they have previously bought. Giving feedback gives a way for the user to interact with the site and also informs prospective buyers on products of interest.

- **Star Rating Selector** - The review form contains a radio selector styled into a five star input. The value is parsed into a float value which is added to the database. The rating displayed on the product is the average value of all combined ratings.
- **Comment** - The user can also use the comment box to leave a description of the production which will be fed back to the site owner and displayed on the site for other users.

### **Custom Admin**
To improve the experience of site staff, a custom admin UI was built to complete site actions such as product and stock management. From this panel staff members can complete CRUD on products, view orders, manage stock, manage the mailing list, and send newsletters.

- **Sorting Tables** - The information on the database is displayed in a sorting table that includes pagination and a search bar. This means that staff can move through large amounts of data easily, and in a friendlier way than the default django admin.
- **Product CRUD** - Staff can create, update, and delete products from the database from within the UI.
- **Stock Management** - Staff can keep a products stock corresponding stock up to date from within the UI. This allows them to easily maintain items that are available for sale on the store.
- **Order List** - Staff can see a list of all orders and view them in detail in another page. This means that sales can be tracked easily and the site owner can see how well the store is doing, and that specific orders can be found without hassle.
- **Mailing List** - Staff can remove users from the mailing list and update their details if necessary.
- **Newsletter** - Staff can also send newsletters from within the admin panel, which builds off of a base newsletter template and adds the subject and content from the input of the user. A summernote editor means that the message can be formatted well and promotional emails can be well styled.

### **Secure Checkout**
The checkout process features a delivery form and a stripe payment form, as well as a final summary of the order before the user decides to purchase. There is also a confirmation page that displays upon completion of the order.

- **Checkout Form** - The checkout form takes the users personal and delivery information, validating it before completing the process. There is also a final summary of the items in the order, and an option to save the users information to their profile upon completion. A spinner displays to prevent the user from submitting multiple payments whilst the order is being processed.
- **Order Summary** - Upon a successful order, the details of the order are displayed on a new page with a notification stating that the order has been completed, and that a confirmation email has been sent.

### **Newsletter, Contact Form & Emails**
Custom html email templates were built for allauth and django emails which are triggered for events such as an order being completed or the newsletter being subscribed to.

- **Newsletter** - Users can subscribe to a mailing list and receive emails sent by site staff. These emails feature a custom template and can be sent by staff from the admin panel. Users receive an email upon subscribing successfully to the newsletter.
- **Order Confirmation Email** - Users receive a confirmation email upon completing an order successfully. The email contains all of the relevant information about the order.
- **Allauth Emails** - The default allauth emails for resetting a password and for verification of a new account have been customized to be consistent with other site emails.
- **Contact Form**  - There is a contact form that is linked to the main email address of the site owner where users can query with any questions or issues that they are facing when using the site. The message is validated and sent to the owner along with the email that the user wishes to be contacted with.

### **FAQ’s**
The user can see a list of frequently asked questions to answer any questions that they might have.

- **Accordion** - The FAQ’s are formatted in a Bootstrap accordion to present the large amount of text in bitesize quantities so that the user can navigate to helpful answers easily.

## **Future Features**

- **Stock Anayltics** - A future feature would be an interface that informs the admin on sales so that they can make decisions on how much stock to order, or which items are the most popular and which are not performing as well.

- **Wishlist** - A feature that was intended to be included in this iteration of development was a product wishlist. This would allow users to make a list of products that they can return to later on if they wish to buy them. Unfortunately this feature did not make it in due to time constraints, but would be a useful thing to add in future.

- **Stock Notification** - Another intended feature was an email sent to the user of when stock comes back into the store of a specific item. The user would be able to opt in to this from the product detail. This feature was not added as others were prioritized to meet the deadline.

## **Future**
Here are some future features that were outside of the project scope on the current iteration of development, but could be included to improve the user experience and site in general.

- **Form Submission Email:** User receives an email when an account is created or when a booking is made.
- **Waiting List:** Users will have the option to join a waiting list for full events and receive an email if there is availability.
- **Prefilled Booking Form:** Booking form is prefilled with the event and can be replaced with a select form if the user chooses.
- **Repeating/Self Deleting Event:** Events can be set to repeating so that they automatically appear on the schedule each week, and events in the past self-delete.
- **Messaging In Browser:** User and admin can message within the website from the account and admin panels respectively.
- **Menu:** Admin has access to CRUD functionality for a menu.
- **Admin Interface for User:** Whilst the admin can see users in the admin panel, it redirects the admin to the default django admin dashboard, so CRUD functionality for the user within the custom UI would provide a better experience for the site owner.

## **Testing**

### **Testing User Stories**

#### **Epic: Site Navigation**

<details>
  
**As a user I can easily navigate the site so that I can access the different areas of the shop and complete user actions intuitively**
- **COMPLETE:** The navigation bar and footer mean that the user is able to move through the site easily to get to their desired area. Buttons and links are consistently designed throughout the site so that the user can build familiarity with navigation elements.

**As a user I can view products so that I can browse the products for sale on the site**
- **COMPLETE:** The products section is clearly accessible from the navbar and footer so that viewing products can be achieved from anywhere on the site.

**As a user I can filter products by category so that narrow down shopping searches to items relevant to my interests**
- **COMPLETE:** Products are categorized and can be filtered by selecting the chosen category in the top navbar.

**As a user I can search for products so that query for specific items of interest faster**
- **COMPLETE:** There is a search input in the navigation bar which allows the user to query specific products from anywhere in the site.

**As a user I can sort product search results so that I can filter through products by various attributes intuitively**
- **COMPLETE:** The products page includes a sorting dropdown that allows the user to filter items by attributes such as price, rating, and name.

**As a user I can view a list of frequently asked questions so that I can have my queries answered without contacting the site admin**
- **COMPLETE:** There is a FAQ page that contains information in the site in much more detail so that the user can resolve any issues they might have.

**As a user I can contact the store so that I can have any queries answered by the site admin**
- **COMPLETE:** There is a contact form the allows the user to send an email directly to the main site email, the user is forced to include their email address so that the site owner knows who to send the response to.
  
</details>

#### **Epic: Buying Products**

<details>

**As a user I can select the sizes of items so that I can choose specific clothing sizes when I buy items**
- **COMPLETE:** On the product detail there is a size selector which will show the user if the item has sizes, and allows them to select one before adding the item to the basket.

**As a user I can add products to a basket so that I can store items in a list of products to purchase as I navigate through the site**
- **COMPLETE:** There is add to product functionality from the product detail pages. Users can select the quantity and size of the item before adding it to the basket. There is validation to prevent users from adding more quantity than available stock.

**As a user I can clearly see what items are currently in stock so that I am aware which items can be ordered immediately**
- **INCOMPLETE:** The product detail displays whether an item is in stock or not. Sized items also display if a particular size is low on stock. However there is no functionality to filter out of stock items from the product list.

**As a user I can see the total cost of my order so that I am aware exactly how much I am required to pay**
- **COMPLETE:** Total order cost is displayed in the basket and checkout. It also appears in the success toast of adding a product to the basket.

**As a user I can view delivery costs so that I am aware of any surplus charges to my order**
- **COMPLETE:** Delivery cost is displayed in the basket and checkout. It also appears in the success toast of adding a product to the basket.

**As a user I can see discounted products so that I am aware of opportunities to save money on purchases**
- **COMPLETE:** Discounted prices can be easily seen in the product list and detail as a new value with the old price crossed out. There is also a sale tab to filter all discounted items into one search.

**As a user I can update the quantity of items in the basket so that I can easily manage the items I wish to order**
- **COMPLETE:** Total order cost is displayed in the basket and checkout. It also appears in the success toast of adding a product to the basket.

**As a user I can remove items from the basket so that I can delete any unwanted items from my order**
- **COMPLETE:** Users are able to remove individual items from the basket with the x icon. They can also set the quantity to 0 or to a negative number and the same outcome is achieved.

**As a user I can make secure payments so that I can safely order items with my card**
- **COMPLETE:** Stripe functionality securely takes payments for orders and appears in the dashboard. A spinner overlay hides the form and prevents the user from accidentally making double payments.

**As a user I can update the quantity of items in the basket so that I can easily manage the items I wish to order**
- **COMPLETE:** Users are able to increment and decrement their quantity from within the basket. These inputs are validated to prevent quantity from being greater to the remaining stock.

**As a user I can join a newsletter so that I can be made aware of any news or promotions running in the store**
- **COMPLETE:** Users can sign up to a mailing list from the form in the footer. They receive a confirmation email upon submitting the form, and then receive any newsletters the admin might send.

</details>

#### **Epic: Account Management**

<details>

**As a user I can create an account so that I can manage my personal details and view order history if I am a regular shopper**
- **COMPLETE:** Users are able to sign up easily and receive an email verification in order to complete the registration process.

**As a user I can save my personal details when checking out so that placing orders is faster in future**
- **COMPLETE:** There is a checkbox on the checkout form that allows a user to take the personal information entered and add it to their profile. If a user is not logged in it gives them the option so register an account or sign in.
  
**As a user I can manually add my personal information to a profile so that I can checkout faster when ordering**
- **COMPLETE:** There is a profile page that contains a form for the user to manually add their personal and delivery information to their profile.
  
**As a user I can update my profile information so that I can keep my personal details up to date**
- **COMPLETE:** Users can use the profile form on their profile page to update existing information on their profile and keep their data up to date.

**As a user I can view my order history so that I can access information about unfulfilled and past orders**
- **COMPLETE:** Order history is displayed in the order history page accessed from the profile dropdown menu. There they can see orders they have made and the items they have purchased. A confirmation email sends upon order completion.

**As a user I can change my password so that I can keep my account safe and access my profile if I lose my password**
- **COMPLETE:** Logged in users are able to change their password through a change password button located on the profile form; they are redirected to a change password form where they can complete the action. Users are also able to request a password reset email from the login page if they forget it, where they will be sent an email with a link to change it.

**As a user I can delete my account so that I can maintain control over my personal information**
- **INCOMPLETE:** Users are unable to delete or request a deletion for their account automatically. Instead they have to send an email to the site owner to delete the user manually. This is below-par UX so this User Story is considered incomplete.

**As a user I can rate products so that I can give feedback to the store and other prospective buyers on items that I have purchased**
- **COMPLETE:** Users are able to review products that they have purchased from the order history tab. They are automatically presented with a link to rate the product once they have made a purchase, and will be shown a message if they have already rated it. From there they can submit a star rating and leave a comment, which will be displayed on the products reviews section.

**As a user I can contact the store so that I can have any queries answered by the site admin**
- **COMPLETE:** There is a contact form accessed through various areas of the site, but most easily from the footer. In this form they are able to send an email directly to the site owner.

**As a user I can create a wish list of items so that I can save products to buy at a future date**
- **INCOMPLETE:** This user story was not completed. During development it was put on a lower priority due to expected time constraints, so didn’t make the final deployment. This feature is one that should be implemented in future.

</details>

#### **Epic: Site Management**

<details>

**As an admin I can add products to the store so that I can keep the product list up to date with new arrivals**
- **COMPLETE:** The admin is able to add products by accessing the add product button in the custom admin UI.

**As an admin I can update existing products so that I can manage the information of currently listed products****
- **COMPLETE:** The admin can update existing products from the update products form in the admin UI.

**As an admin I can delete existing products so that I can remove products from the product database
- **COMPLETE:** The admin can delete existing products from the database in the custom admin UI by selecting the delete product button and confirming the action****

**As an admin I can hide products from the store so that I can remove out of stock or faulty items from being displayed**
- **COMPLETE:** Incomplete user story. This user story was ultimately not completed. Out of stock items simply display that they are out of stock. For an admin to hide a product they would have to delete the model.

**As an admin I can manage stock so that I can maintain that items for sale are available to be bought and shipped**
- **COMPLETE:** The admin is able to manage stock values in the custom admin UI for both sized and regular item stock.

**As an admin I can add a discount to items so that I can create a list of items on sale**
- **COMPLETE:** The admin can add a discounted price to the product model. These products display their discounted value in the products list, and can be grouped by accessing the sale link.

**As an admin I can send a newsletter so that I can keep users up to date with the latest deals or promotions.**
- **COMPLETE:** The admin is able to send a newsletter to all emails on the mailing list from the custom admin UI. The message input is a summernote field, meaning that content can be meaningfully formatted.

</details>

### **Python**

### **HTML**

### **CSS**

### **Responsiveness**

### **Browser Testing**

Easy Outdoor Co has been tested on the following browsers:

- **Chrome**
- **Mozilla Firefox**
- **Safari**
- **Opera**

### **Lighthouse Testing**

## **Bugs**

### Resolved

### Unresolved

## **Technologies**
The George Orwell Pub was built with the following technologies:

1.  [**Django**](https://www.djangoproject.com/) - Full stack framework to build database and backend.
2.  [**Bootstrap**](https://getbootstrap.com/) - Front end framework used to build features quickly.
2.  [**Python**](https://www.python.org/) - Application logic and functionality.
3.  [**HTML**](https://en.wikipedia.org/wiki/HTML5) - Templates content and email design.
4.  [**CSS**](https://en.wikipedia.org/wiki/CSS) - Styling content on the site.
5.  [**JQuery**](https://jquery.com/) - Javascript library used for form validation and interactivity.
6.  [**Gitpod**](https://gitpod.io) - The IDE used for the project development.
7.  [**Heroku**](https://dashboard.heroku.com/apps) - Hosting deployed project.
9.  [**Figma**](https://figma.com/) - Wireframe design.
10. [**Real Favicon Generator**](https://realfavicongenerator.net/) - Generating favicon from logo image.

## **Deployment**

### **To deploy the project**
The Easy Outdoor Co. was used to host the deployed application:

## Cloning Project
The project files are hosted on GitHub and can be cloned for further development:

## Credits

[**Bootstrap**](https://getbootstrap.com/) - Bootstrap makes up the core of the site structure and design.

[**Data Tables**](https://datatables.net/examples/basic_init/index.html) - The admin panel data tables were taken from here.

I want to thank Precious Ijege and my fellow students at Code Institute for their guidance and support in development of this project. I wouldn't have managed to complete the diploma without the help I recieved throughout!

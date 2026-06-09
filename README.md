# manaVault

## Overview
ManaVault is a Django-based e-commerce web application for browsing and purchasing Magic: The Gathering cards from a curated personal collection. Users can register for an account, browse available cards, manage a shopping cart, securely complete purchases using Stripe test payments, view their order history, and create wishlist requests for cards they would like ManaVault to stock in future. The project was intentionally scoped as a single-seller storefront to deliver core e-commerce functionality to a high standard, while allowing for future expansion into a wider card trading marketplace.

## 🚀 Live Project

👉 https://manavault-03c0788c9056.herokuapp.com/

---

## 🎯 UX Design

### Target Audience
- Trading card collectors  
- Hobbyists and gamers  
- Users looking for a simple online card store  

### User Goals
- Browse available cards  
- View detailed card information  
- Add items to a cart  
- Complete purchases securely  
- View previous orders  
- Create wishlist requests
- Manage wishlist items

### Design Decisions
- Clean Bootstrap layout for clarity and usability  
- Card-based UI for product browsing  
- Fully clickable product cards  
- Responsive design for mobile and desktop  
- Minimal friction checkout flow  

---

## ✨ Features

### 🏠 Homepage

- Hero section with featured imagery
- Call-to-action buttons
- Featured cards display
- Responsive design

![Homepage](documentation/hero-section.png)

### 🔐 Authentication
Registered accounts allow users to:

- View previous orders
- Save delivery information
- Create and manage wishlist requests
- Access personalised profile features
- User registration 
![Registration](documentation/register.png)
- Login and logout (secure POST logout)
![Login](documentation/login.png)  
- Profile page displaying order history
![Profile](documentation/profile.png)  

### 🃏 Cards
- View all cards 
![Cards](documentation/cards.png) 
- Card detail pages  
![Card-detail](documentation/card-detail.png)
- Stock tracking  
![Stock](documentation/stock-control.png)
- Rarity and condition display
![Condition](documentation/condition.png)  

### 🛒 Cart
- Add to cart (AJAX + POST fallback) 
![Add-to-cart](documentation/added-to-cart.png) 
- Update quantities  
- Remove items  
![Remove](documentation/cart-remove.png)
- Dynamic total calculation  

### 💳 Checkout (Stripe)
- Stripe Checkout integration  
![Stripe](documentation/stripe-pay.png)
- Secure payment handling  
- Order creation after successful payment 
![Order-success](documentation/order-success.png) 
- Automatic stock updates  
![Stock](documentation/stock-control.png)

### 📦 Orders
- Orders stored with delivery details  
![Order](documentation/order-history.png)
- OrderLineItems track purchased cards  
- Profile shows order history  
![Profile](documentation/profile.png)

### 📩 Contact
- Contact form for user communication
- Messages are stored in the database
- Contact messages are visible through the Django admin panel
![Contact](documentation/contact.png)

### ⭐ Wishlist
The Wishlist feature was introduced to provide full frontend CRUD functionality.

Users can create, view, edit, and delete wishlist requests without requiring access to the admin panel.
Users can also add existing cards directly to their wishlist from the card detail page with a single click.

- Create wishlist requests 
![wishlist](documentation/wishlist-form.png)
- View wishlist items
![wishlist-items](documentation/my-wishlist.png)
- Edit wishlist requests
![wishlist-edit](documentation/wishlist-edit.png)
- Delete wishlist requests
![wishlist-delete](documentation/wishlist_delete.png)
- Add existing cards directly to wishlist from card detail pages
![wishlist-quick-add](documentation/wishlist-quick-add.png)

---
## 📖 User Stories

### As a visitor:
- I want to browse cards so I can see what is available  
- I want to view card details so I can make informed decisions  

### As a shopper:
- I want to add items to a cart so I can purchase multiple cards  
- I want to update quantities so I can control my order  
- I want to securely checkout so I can complete my purchase  

### As a registered user:
- I want to create an account so I can track my orders  
- I want to log in and out securely  
- I want to view my order history 
- I want to create wishlist requests and save cards I am interested in
- I want to see, edit, and delete items in my wishlist 

### As a site owner:
- I want to manage card stock via admin  
- I want to track orders placed  
- I want to view contact messages
- I want to view wishlist requests

---

## 🗃️ Database Schema

### Models

#### Card
- name  
- set_name  
- card_type  
- rarity  
- condition  
- mana_cost  
- color_identity  
- description  
- price  
- stock_quantity  
- image  
- is_active

#### Order
- user  
- full_name  
- email  
- phone_number  
- country  
- postcode  
- town_or_city  
- street_address1  
- street_address2  
- county  
- order_total  
- date  

#### OrderLineItem
- order (ForeignKey)  
- card (ForeignKey)  
- quantity  
- lineitem_total  

#### UserProfile
- user (OneToOne)  
- default delivery information  

---

#### WishlistItem

- user
- card_name
- set_name
- desired_condition
- max_price
- notes
- created_at

#### ContactMessage

- name
- email
- message
- created_at
- is_read

---

## 🔗 Relationships

- One User → One UserProfile  
- One User → Many Orders  
- One Order → Many OrderLineItems  
- One Card → Many OrderLineItems
- One User → Many WishlistItems
- ContactMessages are stored independently

---

## 📊 Entity Relationship Diagram

![ERD](documentation/erd.png)

---

## 🔐 Data Validation

- Users cannot exceed available stock  
- Quantity inputs are restricted by stock limits  
- Checkout requires valid input fields  
- Stripe handles secure payment validation  
- Orders are only created after successful payment 
- Wishlist forms require valid input
- Contact form validates required fields
- Users can only edit or delete their own wishlist items 

---

## 🎨 Design Rationale

ManaVault balances a trading card aesthetic with a clean e-commerce layout.

### Homepage Improvements

Following assessment feedback, the homepage was redesigned to improve visual appeal and user engagement.

Enhancements include:

- Hero image
- Stronger call-to-action buttons
- Featured cards section
- Wishlist promotion
- Improved spacing and typography

### UI Decisions
- Grid layout improves browsing  
- Fully clickable cards enhance usability  
- AJAX interactions reduce page reloads  
- Consistent navigation improves UX  

### Styling
- Bootstrap is used for consistency  
- Colour scheme inspired by trading card themes  
- Focus on readability and clarity  

---

## 🧩 Agile Planning

The project was developed iteratively:

1. Project setup and app structure  
2. Card model and display  
3. Cart functionality  
4. Checkout and Stripe integration  
5. User authentication and profiles  
6. Deployment to Heroku  
7. UI improvements and debugging 
8. Contact form database integration
9. Wishlist CRUD implementation
10. Defensive design improvements
11. Homepage redesign and UX enhancements 


## Testing 

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## ☁️ Media Storage (Cloudinary)

Images are stored using Cloudinary to ensure reliable media handling in production.

### Why Cloudinary?
- Heroku filesystem is temporary  
- Uploaded files are not persistent  
- Cloudinary provides cloud-based hosting  

### Implementation
- django-cloudinary-storage used  
- Environment variables for credentials  
- Images re-uploaded via admin  

---

## 🔐 Security

- No secrets stored in code  
- Environment variables used  
- CSRF protection enabled  
- Secure POST logout  
- Stripe handles payment security  

---

## 🛡️ Defensive Design

Defensive design has been implemented throughout the project.

Examples include:

- Login required for wishlist functionality
- Ownership checks on wishlist edit and delete views
- Users cannot access another user's wishlist items
- 404 responses returned for unauthorized access attempts
- Protected profile and order history pages
- Secure POST logout implementation

---

## 🎨 Future Improvements

- Advanced search and filtering
- Wishlist email notifications
- Card availability alerts
- Order confirmation emails
- Expanded inventory management
- Community marketplace functionality

---

## Tools & Technologies Used

---

### Databases
- SQLite (development)
- [PostgreSQL](https://www.postgresql.org) used as the production relational database.

---

### Languages used
- [HTML](https://en.wikipedia.org/wiki/HTML) - Used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) -Used for styling and colours
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Used minimally for Bootstrap components and client-side interactions.
- [Google Dev Tools](https://developer.chrome.com/docs/devtools) - Used for troubleshooting, testing responsiveness, and styling.
- [GitHub](https://github.com/) - Used to save and store the project files.
- [Gitpod](https://www.gitpod.io/) - Cloud-based IDE for development
- [Git](https://git-scm.com/) - Used for version control. (git add, git commit, git push)
- [Heroku](https://dashboard.heroku.com/) - Live deployment of the site was hosted here
- [Django](https://www.djangoproject.com/) - Framework that helped build the site. 
- Django Admin enabled for secure backend management of users and bookings
- [Gunicorn](https://gunicorn.org/) used for WSGI server
- [Cloudinary](https://cloudinary.com/) used for hosting images on the cloud server


---

## 📂 Project Structure

manavault/  
├── home/  
├── cards/  
├── cart/  
├── checkout/  
├── profiles/ 
├── wishlist/ 
├── templates/  
├── static/  
├── media/  
├── requirements.txt  
├── Procfile  
├── .python-version  
└── manage.py  

## 🖥️ Admin Functionality

The Django admin panel allows site administrators to manage:

- Cards
- Orders
- Order Line Items
- User Profiles
- Wishlist Items
- Contact Messages

The admin panel allows assessors and site administrators to verify orders, wishlist requests, contact messages, and customer activity.

![Admin Panel](documentation/admin-panel.png)

## Deployment

### Heroku Deployment

The project was deployed to Heroku using the following steps:

1. Create Heroku app
2. Add PostgreSQL add-on
3. Configure environment variables:
   - SECRET_KEY
   - DATABASE_URL
4. Configure settings for production:
   - DEBUG = False
   - ALLOWED_HOSTS
   - CSRF and session security
5. Collect static files
6. Run migrations
7. Scale web dyno

The live application can be found here:  
https://manavault-03c0788c9056.herokuapp.com/

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- pip3 install -r requirements.txt

If you have your own packages that have been installed, then the requirements file needs updated using:
- pip3 freeze --local > requirements.txt

The **Procfile** can be created with the following command:
- echo web: gunicorn app_name.wsgi > Procfile
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: heroku login -i
- Set the remote for Heroku: heroku git:remote -a app_name (replace *app_name* with your app name)
- After performing the standard Git add, commit, and push to GitHub, you can now type:
	- git push heroku main

The project should now be connected and deployed to Heroku!

---

## Local Deployment

### Cloning the Repository

1. Go to the [GitHub repository.](https://github.com/Dmolloy/manaVault.git).
2. Locate the Code button above the list of files and click it.
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard.
4. Open Git Bash or Terminal.
5. Change the current working directory to the one where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone my repository:
- git clone https://github.com/Dmolloy/manaVault.git
7. Press Enter to create your local clone.

### Forking 
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Dmolloy/manaVault.git).
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits
- [Stack Overflow](https://stackoverflow.com/)- For help with learning proper syntax and troubleshooting tips
- [Code Institute](https://codeinstitute.net/) - Tutorials and engaging course work.
- [youtube](https://www.youtube.com/watch?v=PBcqGxrr9g8) - For helping with understanding live deployment using Heroku
- [favicon.io](https://favicon.io/emoji-favicons/books/) - For providing the favicon
-[Cardmarket](https://www.cardmarket.com/) - Where I sourced all of my images for this project.

## Acknowledgements
I would like to thank [Code Institute](https://codeinstitute.net/) for the lessons and guidance in working on this project. The [Discord Community](https://discord.com/) for the support to help continue moving with the project. 
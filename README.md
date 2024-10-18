# Django Classifieds Portal

This Django application provides a user-friendly platform for posting and browsing classified ads. Users can create accounts, search for ads based on various criteria, and contact sellers directly.

## Key Features:
- User Authentication: Secure login and registration for users.
- Ad Posting: Users can create detailed ad listings with photos, descriptions, and categories.
- Ad Searching: Users can filter ads by category, location, price range, and keywords.
- Messaging System: Users can send private messages to sellers to inquire about ads.
- Admin Panel: (Optional) For managing categories, users, and reviewing reported ads.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django.

## Clone the Repository

```bash
git clone https://github.com/devla-d/ads.git
```
## Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
## Install Dependencies:
```bash
pip install -r requirements.txt
 ```
## Database Setup:
- Create a database (e.g., using MySQL, PostgreSQL, or SQLite)
- Configure database settings in settings.py
## Run Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
## Collect Static Files: (If using static assets)
```bash
python manage.py collectstatic
```
## Start Development Server:
```bash
python manage.py runserver
```
## Usage:
1. Access the application: Visit http://127.0.0.1:8000/ in your web browser.
2. Register or Login: Create an account or log in using existing credentials.
3. Post an Ad: Navigate to the "Post Ad" section and fill in the details.
4. Search for Ads: Use the search bar and filters to find relevant ads.
5. Contact Seller: If interested in an ad, send a message to the seller.
6. Admin Panel (Optional): If available, access the admin panel to manage categories, users, and ads.


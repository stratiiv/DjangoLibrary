# Django Library
Django Library is a web application built using the Django framework for managing a library system. It provides functionalities for managing books, authors, and library members.

## Features
* User authentication and authorization for administrators and library members.
* CRUD operations for books, authors, and library members.
* Ability to track borrowed books and due dates.
Search functionality to find books by title, author, or category.
* Admin panel for managing the library database and configurations.
* Responsive design for optimal user experience on different devices.

## Demo
The application is hosted on Railway and can be accessed at https://stratiiv.up.railway.app/
## Installation
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Set up the database by running the migrations:
```
python manage.py migrate
```
5. Create a superuser to access the admin panel:

```
python manage.py createsuperuser
```
6. Start the development server:
```
python manage.py runserver
```
Access the application at http://localhost:8000 in your web browser.

## Usage 
* Log in with your superuser credentials to access the admin panel at http://localhost:8000/admin.
* Use the admin panel to manage books, authors, library members, and borrowed books.
* Library members can sign up and log in to browse and borrow books.
* Use the search functionality on the home page to find books by title, author, or category.
* Update the due date of borrowed books in the admin panel or mark them as returned.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

DjangoLibrary is open source and released under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for more details.

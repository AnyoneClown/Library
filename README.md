# Django Project

## Setup

The first thing to do is to clone the repository:

```sh
 git clone https://github.com/AnyoneClown/Library.git
 cd library
```

Create a virtual environment to install dependencies in and activate it:

```sh
 python -m venv env
 env\Scirpts\activate
```

Then install the dependencies:

```sh
(env) pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env) cd library
(env) python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.



# Library Management System

This is a library management system that allows users to register as either a regular visitor or a librarian.

## Book

In this system, librarians have the following capabilities:
- View all books and their information
- Create new books
- Filter books based on criteria

Regular visitors have the capability to:
- Browse and view books in the library

## Order

In the Order section, librarians have the following capabilities:
- Check all orders and their details
- Delete unnecessary orders
- Mark orders as delivered to the customer

Users have the following capabilities:
- Place orders for books
- Check their own orders and their details

## Authors

In the Authors section, librarians have the following capabilities:
- View information about all available authors
- Create new authors
- Remove unnecessary authors

## Users

In the Users section, librarians have the following capabilities:
- View information about all users
- Update user profile data

Users have the following capabilities:
- Check their own profile information
- Update their profile data

## API Endpoints

### User Endpoint: `/api/v1/user/{id}`
- **GET:** Retrieve user information for the specified `{id}`.
- **PUT:** Update user information for the specified `{id}`.
- **DELETE:** Delete the user with the specified `{id}`.

### User Order Endpoint: `/api/v1/user/{id}/order/{id}`
- **GET:** Retrieve order information for the specified user `{id}` and order `{id}`.
- **PUT:** Update order information for the specified user `{id}` and order `{id}`.
- **DELETE:** Delete the order for the specified user `{id}` and order `{id}`.

### Order Endpoint: `/api/v1/order/{id}`
- **GET:** Retrieve order information for the specified `{id}`.
- **PUT:** Update order information for the specified `{id}`.
- **DELETE:** Delete the order with the specified `{id}`.

### Book Endpoint: `/api/v1/book/{id}`
- **GET:** Retrieve book information for the specified `{id}`.
- **PUT:** Update book information for the specified `{id}`.
- **DELETE:** Delete the book with the specified `{id}`.

### Author Endpoint: `/api/v1/author/{id}`
- **GET:** Retrieve author information for the specified `{id}`.
- **PUT:** Update author information for the specified `{id}`.
- **DELETE:** Delete the author with the specified `{id}`.

Feel free to customize and enhance the API endpoints based on your specific requirements and implementation details.
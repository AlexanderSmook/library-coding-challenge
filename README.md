# RSAWEB Book Library Pair Coding Challenge

## Introduction
This Book Library challenge involves building a simple but functional application with a front-end interface and a supporting API layer. The task is designed to assess the your technical skills, planning abilities, and collaboration with another developer.

You have two hours to complete this task, including any planning or research. Following the two hours there will be a brief review of the code and functionality, discussing any challenges faced and how they were addressed.

## Functional requirements

The **primary requirement** for this app is for users to be able to check-out and check-in books.


### User Interface
- Allow users to add new books to the library through a form with at least the title and author.
- Display a list of all books with details such as title, author, and status (available or checked out).
- Enable users to search for books by title or author.
- Provide functionality to check out and return books.

### API Endpoints
- `PUT /books/:id/checkout`: Check out a book.
- `PUT /books/:id/return`: Return a book.
- `GET /books`: Retrieve all books.
- `POST /books`: Add a new book.
- `GET /books/search?query={query}`: Search for books by title or author.

### Data Storage
- Use a simple in-memory data structure (e.g., a dictionary or list) to store book details, with an option to use a persistent database if time permits.

### Technology Stack
The front-end and API layer must use different tech stacks but can be chosen from any of the following, based on your assessment of the most suitable technology:

- NodeJS + Express
- NodeJS + Fastify
- NodeJS + VueJS
- Python + Flask
- Python + Django
- PHP + Laravel
- PHP + Slim

You can use any suitable component library to assist you in delivering features.

### Database
You can use any of the following systems for persisting your data:

- MySQL
- MongoDB
- In-memory storage
- Memcached
- Flat file

If you spin up either the MySQL or MongoDB containers they have defaults of:
| Database | User     | Password |
|----------|----------|----------|
| `rsaweb` | `rsaweb` | `rsaweb` |

### Docker

##### A shared network

All the containers need to be on the same network, some OSes have issues sharing the default network so we first build a network that all the containers can share.

`docker network create rsaweb`

To check if the network was successfully created, run:

`docker network ls`

##### Individual environments

This repository contains several individual environments all running on the same ports for the type of service:
* Frontends run on 3000;
* Backends run on 4000;
* Datbases use their default ports: 3306, 27021 ans 11211.

1. `/frontend` for your frontend work exposed on `http://localhost:3000` (`http://frontend:3000` internally)
2. `/backend` for your backend work exposed on `http://localhost:4000` (`http://backend:4000` internally)
3. `/database` for your database work exposed on `http://localhost:{{port}}` (`http://database:{{port}}` internally)

We haven't exposed a single, common port in the database layer, rather all three default ports for the relevant database type are available: `mysql:3306`, `mongodb:27021` and `memcached:11211`.

#### Dockerfiles

Each environment is in a folder prefixed by its purpose (frontend_, backend_ and database_). Spin up one of each type you need. It should create a working bare-bones environment.

#### Package management
We have assumed the default package manager for each language. If you plan on using a different one you may need to change the `Dockerfle` to build it correctly.

We run the package manager from the `Dockerfile` but we don't build any of the package files for you, you'll need to do that yourself before you build the containers.

You can get defaults for these files from `/_default package manager files`.

| Language | Manager  | File             |
|----------|----------|------------------|
| PHP      | Composer | composer.json    |
| Python   | pip      | requirements.txt |
| Node     | npm      | package.json     |

#### Known issues

1. You will need to modify the final `CMD` command in your `Dockerfile`s to suit your particular solution.
2. Vue/Vite: If http://localhost:3000/ is not accessible ensure your `vite.config.mjs` has:

    ```JS
    server: {
        port: 3000,
        host: true,
        strictPort: true,
    },
    ```
    **NB:** Depending on whether you are in the frontend or api layer, port will be **3000** or **4000**.
3. `django-admin startproject api|frontend` creates a `api/api/*.py` or `frontend/frontend/*.py` folder structure.<br>
    Use those to replace the provided `api` or `frontend` folders.
4. `composer create-project --prefer-dist laravel/laravel api|frontend` creates the full `api|frontend` project folder structure.
    Use those to replace the provided `api` or `frontend` folders.
5. If you run a database server on your localhost you may need to disable it, or change gthe exposed ports for the database in your Docker container so they can run simultaneously.

#### Running the containers
To run the containers, navigate to the root of this repo and run `docker compose up`.

## User Stories
1. As a user, I want to add a new book to the library:
    - When I visit the add book page, I can input the book's title, author, and initial status (available).
    - After submitting the form, the book appears in the library list.
2. As a user, I want to view a list of all books in the library:
    - When I visit the library page, I see a list of all books with their titles, authors, and status (available or checked out).
3. As a user, I want to search for books by title or author:
    - When I enter a search query on the library page, I see a list of books that match the query.
4. As a user, I want to check out a book:
    - When I view the details of an available book, I see an option to check out the book.
    - After checking out the book, its status changes to checked out, and this is reflected in the library list.
5. As a user, I want to return a book:
    - When I view the details of a checked-out book, I see an option to return the book.
    - After returning the book, its status changes to available, and this is reflected in the library list.

## Success Criteria
### User Interaction and Experience
- The user interface is intuitive and easy to navigate.
- Users can successfully add, view, search, check out, and return books.
- The application is responsive and works well on both desktop and mobile devices.

### API Functionality
- All endpoints are implemented and functional.
- The API correctly handles requests and returns appropriate responses.

### Collaboration and Communication
- The developers must chose one of the systems each on which to drive the keyboard.
- Both developers contribute meaningfully to the project.

### Technical Proficiency
- The code is clean, well-structured, and follows best practices.

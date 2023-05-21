# Blogscribe

Blogscribe is a clone of the popular blogging platform Medium. This repository contains the API for Blogscribe

## Features

- User registration and authentication
- Creating, editing, and deleting blog posts
- Liking and commenting on blog posts
- Following other users and receiving notifications
- Categorizing blog posts using tags
- Searching for blog posts by keywords or tags
- Pagination and sorting of blog posts
- User profiles with bio and profile picture
- User activity feed
- Email notifications using MailHog
- Asynchronous task processing using Celery and Redis
- Monitoring and management of Celery tasks using Flower
- Containerized deployment using Docker and Docker Compose
- Reverse proxy and load balancing using Nginx

## Technologies

- [Python](https://www.python.org/) - Programming language
- [Django](https://www.djangoproject.com/) - Web framework
- [Django REST framework](https://www.django-rest-framework.org/) - Toolkit for building APIs
- [PostgreSQL](https://www.postgresql.org/) - Relational database management system
- [Redis](https://redis.io/) - In-memory data structure store
- [Celery](http://www.celeryproject.org/) - Distributed task queue
- [Flower](https://flower.readthedocs.io/) - Monitoring and management tool for Celery
- [Docker](https://www.docker.com/) - Containerization platform
- [Docker Compose](https://docs.docker.com/compose/) - Tool for defining and running multi-container Docker applications
- [Nginx](https://www.nginx.com/) - Web server and reverse proxy
- [Elasticsearch](https://www.elastic.co/elasticsearch/) - Distributed search and analytics engine
- [MailHog](https://github.com/mailhog/MailHog) - Email testing tool

## Prerequisites

Make sure you have the following technologies installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

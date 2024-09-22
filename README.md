# Flask Python API

## Overview
This project is a scalable, efficient Flask-based API designed to manage customers, products, and orders. The application utilizes a layered architecture, leveraging Flask blueprints for organized route management and structured service layers for business logic. The API supports full CRUD operations for customers, products, and orders, and includes a health check endpoint to ensure the service remains operational.

## Features
- **Customers**: Create, update, retrieve, and delete customer records.
- **Products**: Add, modify, fetch, and delete products.
- **Orders**: Place and fetch customer orders, with transaction management.
- **Health Check**: Ensure API uptime and service availability.
- **Layered Architecture**: Separation of concerns through services and route handlers.
- **Flask Blueprints**: Modular routing for scalable API design.

## Technologies Used
- **Flask**: Web framework for building the API.
- **MySQL**: Database for persisting customer, product, and order information.
- **SQLAlchemy**: ORM for database interaction (if applicable).
- **Postman**: API documentation and testing.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/gayanukabulegoda/Flask-Python-API.git

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set Up the Database**
   - Create a MySQL database and configure the database URI in the `config.py` file.

4. **Run the Application**
   ```bash
   flask run

5. **Access the API** 
   - The API will be accessible at `http://127.0.0.1:5001/`.

## API Documentation
The full API documentation is available on Postman. It provides a detailed overview of all available endpoints, request formats, and response examples.

- **Postman Documentation**: [Flask Python API Documentation](https://documenter.getpostman.com/view/36681432/2sAXqqchr4)

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

##
<div align="center">
<a href="https://github.com/gayanukabulegoda" target="_blank"><img src = "https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
<a href="https://git-scm.com/" target="_blank"><img src = "https://img.shields.io/badge/Git-100000?style=for-the-badge&logo=git&logoColor=white"></a>
<a href="https://www.python.org/" target="_blank"><img src = "https://img.shields.io/badge/Python-100000?style=for-the-badge&logo=python&logoColor=white"></a>
<a href="https://flask.palletsprojects.com/en/3.0.x/" target="_blank"><img src = "https://img.shields.io/badge/Flask-100000?style=for-the-badge&logo=flask&logoColor=white"></a>
<a href="https://www.mysql.com/downloads/" target="blank"><img src = "https://img.shields.io/badge/Mysql-100000?style=for-the-badge&logo=mysql&logoColor=white"></a>
<a href="https://www.postman.com/downloads/" target="blank"><img src = "https://img.shields.io/badge/Postman-100000?style=for-the-badge&logo=Postman&logoColor=white"></a>
</div> <br>
<p align="center">
  &copy; 2024 Gayanuka Bulegoda
</p>

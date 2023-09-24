# E-commerce Application with FastAPI and MongoDB

This is a sample backend application built with FastAPI and MongoDB. It simulates an e-commerce platform like Flipkart or Amazon.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [API Endpoints](#api-endpoints)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Database Models](#database-schema)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)


## Overview

The E-commerce Application is designed to provide a set of APIs for managing products, orders, and user data. It allows users to view available products, create orders, retrieve order details, update product quantities, and more.

## Features

- List available products with details.
- Create new orders with items and user address.
- Fetch all orders with pagination support.
- Retrieve a single order by Order ID.
- Update product quantities as needed.
- Store product data, order data, and user information in MongoDB.

## Tech Stack

- Python 3.10+
- FastAPI: A modern web framework for building APIs with Python.
- MongoDB: A NoSQL database for storing product and order data.
- PyMongo: A Python driver for MongoDB to interact with the database.

## API Endpoints

The application provides the following API endpoints:

1. **List Available Products**
   - Endpoint: /products (GET)
   - Description: Get a list of all available products in the system.
   - Query Parameters:
          - skip (Optional): Skip N products (default: 0, minimum: 0).
          - limit (Optional): Limit the number of products returned (default: 10, maximum: 100).
   - Example
          -   GET /products?skip=0&limit=20

2. **Create a New Order**
   - Endpoint: `/orders` (POST)
   - Description: Create a new order with timestamp, items, and user address.

3. **Fetch All Orders**
   - Endpoint: `/orders` (GET)
   - Description: Fetch all orders with pagination support (using `limit` and `offset`).
   - 

4. **Fetch a Single Order**
   - Endpoint: `/orders/{order_id}` (GET)
   - Description: Get details of a specific order by Order ID.

5. **Update Product Quantity**
   - Endpoint: `/api/products/{product_name}` (PUT)
   - Description: Update the available quantity for a product.

6. **Fetch a Single Product**
   - Endpoint: `/products/{product_name}` (GET)
   - Description: Get details of a specific product by Product name.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/ecommerce-app-fastapi.git
   cd ecommerce-application
   
2. Create a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install the project dependencies:
4. Set up environment variables:
    Create a .env file in the project root directory with the following content:
    MONGODB_URI=mongodb://localhost:27017/ecommerce

Initialize the database:

python database/connection.py
Run the FastAPI server:

uvicorn main:app --reload
The application should now be accessible at http://localhost:8000.

## Project Structure
The project follows a structured layout with key directories:

api: Contains FastAPI router files for defining API endpoints.
models: Defines Pydantic models for request and response objects.
utils: Includes Python scripts other utilities.
database: Include Python scripts for initializing the database.
main.py: The main application file where FastAPI is configured.

## Database Models
MongoDB is used to store product and order data. The data models include:

Product: Represents a product with attributes such as name, price, and available quantity.
Order: Represents an order with properties like timestamp, items purchased, and user address details.

## Running the Application
After following the installation steps, the application can be accessed at http://localhost:8000. You can use the API endpoints mentioned in the API Endpoints section to interact with the application.

## API Documentation
API documentation is available at http://localhost:8000/docs. You can explore and test the API using the Swagger UI.

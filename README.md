# Python MongoDB Integration Project

This project demonstrates how to use MongoDB with Python via the pymongo library. It covers core MongoDB operations, including database creation, CRUD operations (Create, Read, Update, Delete), data insertion, querying, sorting, and more.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Structure](#project-structure)
3. [MongoDB Concepts](#mongodb-concepts)
4. [Setting Up MongoDB Connection](#setting-up-mongodb-connection)
5. [Basic MongoDB Operations](#basic-mongodb-operations)
   - [Check if Database Exists](#check-if-database-exists)
   - [Check if Collection Exists](#check-if-collection-exists)
   - [Insert Data (Single & Multiple Documents)](#insert-data-single--multiple-documents)
   - [Find Data (Simple Query)](#find-data-simple-query)
   - [Find Data with Sorting](#find-data-with-sorting)
   - [Update Data](#update-data)
   - [Delete Data](#delete-data)
   - [Limit Results](#limit-results)
6. [Running the Project](#running-the-project)
7. [MongoDB vs SQL](#mongodb-vs-sql)
8. [Advanced MongoDB Features](#advanced-mongodb-features)
9. [Conclusion](#conclusion)

## 1. Prerequisites

Before you begin, ensure you have the following installed:

- **MongoDB**: Running locally or using a cloud provider like MongoDB Atlas. You can download it from the [MongoDB Download Center](https://www.mongodb.com/try/download/community).
- **Python**: Ensure Python 3.x is installed. You can download it from [python.org](https://www.python.org/downloads/).
- **pymongo**: The Python driver for MongoDB. Install it using pip:

  ```bash
  pip install pymongo
  ```

## 2. Project Structure

```plaintext
/project-root
    ├── main_app.py                 # Main Python script for MongoDB operations
    ├── connection.py           # MongoDB connection setup (used in main.py)
    ├── README.md               # This detailed README
```

### connection.py

This file contains the logic for connecting to MongoDB using pymongo. MongoDB creates databases and collections dynamically when you insert data.

```python
import pymongo

# MongoDB Connection Setup
mongodb_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongodb_database = mongodb_client["my_first_database"]  # Select/Create a database
mongodb_collection = mongodb_database["my_first_collection"]  # Select/Create a collection
```

- `pymongo.MongoClient("mongodb://localhost:27017/")`: Connects to the MongoDB server running locally on the default port 27017.
- `mongodb_client["my_first_database"]`: References a database named `my_first_database`. If it doesn't exist, MongoDB will create it when we insert data.
- `mongodb_database["my_first_collection"]`: References a collection named `my_first_collection`. If it doesn't exist, MongoDB will create it as well.

## 3. MongoDB Concepts

- **Database**: A container for collections. MongoDB does not create the database until it contains data.
- **Collection**: A group of documents (similar to a table in SQL).
- **Document**: A record, represented in BSON (Binary JSON). A document is analogous to a row in SQL.

## 4. Basic MongoDB Operations

### 4.1. Check if Database Exists

MongoDB databases are created only when you insert data. You can check if the database exists by listing all databases:

```python
# Check if database exists
database_list = mongodb_client.list_database_names()
if "my_first_database" in database_list:
    print("The database exists.")
else:
    print("The database does not exist.")
```

### 4.2. Check if Collection Exists

Similar to databases, collections are created on the fly when you insert data. Here's how you can check if a collection exists:

```python
# Check if collection exists
collections = mongodb_database.list_collection_names()
if "my_first_collection" in collections:
    print("The collection exists.")
else:
    print("The collection does not exist.")
```

### 4.3. Insert Data (Single & Multiple Documents)

To insert documents into a MongoDB collection, use `insert_one()` for a single document and `insert_many()` for multiple documents.

**Inserting a Single Document:**

```python
data = {"name": "John", "address": "Highway 37"}
result = mongodb_collection.insert_one(data)
print(f"Inserted document with ID: {result.inserted_id}")
```

**Inserting Multiple Documents:**

```python
data_list = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blue 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky red 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central road 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Side way 1633"},
]
result = mongodb_collection.insert_many(data_list)
print(f"Inserted documents with IDs: {result.inserted_ids}")
```

### 4.4. Find Data (Simple Query)

To read data from MongoDB, use the `find_one()` method for a single document or `find()` for multiple documents.

**Find One Document:**

```python
result = mongodb_collection.find_one({"name": "John"})
print(result)
```

**Find All Documents:**

```python
for document in mongodb_collection.find():
    print(document)
```

**Find Documents with a Condition:**

```python
query = {"address": "Highway 37"}
documents = mongodb_collection.find(query)
for document in documents:
    print(document)
```

### 4.5. Find Data with Sorting

MongoDB supports sorting using the `.sort()` method. You can sort by any field in ascending (1) or descending (-1) order.

```python
# Sort by 'name' in ascending order
for document in mongodb_collection.find().sort("name", 1):
    print(document)

# Sort by 'address' in descending order
for document in mongodb_collection.find().sort("address", -1):
    print(document)
```

### 4.6. Update Data

MongoDB allows you to update documents using the `update_one()` method. Use the `$set` operator to update fields.

```python
# Update the address of the document where name is 'John'
query = {"name": "John"}
new_values = {"$set": {"address": "Canyon 123"}}
result = mongodb_collection.update_one(query, new_values)
print(f"Documents updated: {result.modified_count}")
```

### 4.7. Delete Data

You can delete a document by specifying a condition using `delete_one()` or `delete_many()` for multiple documents.

```python
# Delete a document where name is 'John'
query = {"name": "John"}
result = mongodb_collection.delete_one(query)
print(f"Documents deleted: {result.deleted_count}")
```

### 4.8. Limit Results

MongoDB allows you to limit the number of documents returned using the `.limit()` method.

```python
# Get the first 5 documents
for document in mongodb_collection.find().limit(5):
    print(document)
```

## 5. Running the Project

1. **Start MongoDB**: Ensure MongoDB is running. You can start MongoDB on your local machine by using the command:

   ```bash
   mongod
   ```

2. **Create a Virtual Environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**: Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**: Execute the following command to run the script:

   ```bash
   python main_app.py
   ```

## 6. MongoDB vs SQL

While MongoDB and SQL databases like MySQL or PostgreSQL share the concept of storing data, they differ in structure and capabilities.

- **Schema**:
  - SQL: Fixed schema (tables, rows, columns) with predefined data types.
  - MongoDB: Schema-less (collections and documents with flexible structure).

- **Transactions**:
  - SQL: Strong ACID (Atomicity, Consistency, Isolation, Durability) guarantees.
  - MongoDB: Supports multi-document transactions but typically used for single-document operations.

- **Joins**:
  - SQL: Supports complex JOIN operations.
  - MongoDB: No native support for joins, but you can embed documents or use the `$lookup` operator.

- **Scaling**:
  - SQL: Vertical scaling (more powerful machines).
  - MongoDB: Horizontal scaling (sharding across multiple machines).

## 7. Advanced MongoDB Features

- **Aggregation Pipeline**: MongoDB provides a powerful aggregation framework to perform complex data processing, including filtering, grouping, and transformation of documents.

- **Indexes**: MongoDB allows you to create indexes to improve query performance, similar to SQL databases.

- **Replication**: MongoDB supports replication for high availability and data redundancy.

## 8. Conclusion

This project demonstrates the basics of using MongoDB with Python. MongoDB’s flexible schema and scalability make it a great choice for high-volume applications, big data analytics, or applications that require quick and easy data access.

Explore further by leveraging aggregation pipelines, sharding, and indexing for large datasets. Happy coding!
from typing import Dict, List, Any, Optional

from connection import mongodb_collection


# 1. Check if Database Exists
def check_database_exists(db_name: str) -> None:
    """Check if the specified database exists.

    Args:
        db_name (str): The name of the database to check.

    Returns:
        None
    """
    database_list = mongodb_collection.database.client.list_database_names()
    if db_name in database_list:
        print("The database exists.")
    else:
        print("The database does not exist.")


# 2. Check if Collection Exists
def check_collection_exists(collection_name: str) -> None:
    """Check if the specified collection exists in the database.

    Args:
        collection_name (str): The name of the collection to check.

    Returns:
        None
    """
    collections = mongodb_collection.database.list_collection_names()
    if collection_name in collections:
        print("The collection exists.")
    else:
        print("The collection does not exist.")


# 3. Insert Data (Single Document)
def insert_single_document(data: Dict[str, Any]) -> None:
    """Insert a single document into the collection.

    Args:
        data (Dict[str, Any]): The document to insert.

    Returns:
        None
    """
    result = mongodb_collection.insert_one(data)
    print(f"Inserted document with ID: {result.inserted_id}")


# 4. Insert Multiple Documents
def insert_multiple_documents(data_list: List[Dict[str, Any]]) -> None:
    """Insert multiple documents into the collection.

    Args:
        data_list (List[Dict[str, Any]]): A list of documents to insert.

    Returns:
        None
    """
    result = mongodb_collection.insert_many(data_list)
    print(f"Inserted documents with IDs: {result.inserted_ids}")


# 5. Find One Document
def find_one_document(query: Dict[str, Any]) -> None:
    """Find and print a single document based on the query.

    Args:
        query (Dict[str, Any]): The query to find the document.

    Returns:
        Optional[Dict[str, Any]]: The found document or None if not found.
    """
    result = mongodb_collection.find_one(query)
    print("Find One:", result)


# 6. Find All Documents
def find_all_documents() -> None:
    """Retrieve and print all documents in the collection.

    Returns:
        None
    """
    print("All Documents:")
    for document in mongodb_collection.find():
        print(document)


# 7. Find Documents with a Condition
def find_documents_with_condition(query: Dict[str, Any]) -> None:
    """Find and print documents that match the specified condition.

    Args:
        query (Dict[str, Any]): The query to filter documents.

    Returns:
        None
    """
    documents = mongodb_collection.find(query)
    print(f"Documents with condition {query}:")
    for document in documents:
        print(document)


# 8. Sort Data
def sort_documents_by_field(field_name: str, order: int = 1) -> None:
    """Sort documents by a specified field and print them.

    Args:
        field_name (str): The field to sort by.
        order (int): The order of sorting, 1 for ascending and -1 for descending.

    Returns:
        None
    """
    print(f"Sorted by {field_name}:")
    for document in mongodb_collection.find().sort(field_name, order):
        print(document)


# 9. Update Data

def update_document(query: Dict[str, Any], new_values: Dict[str, Any]) -> None:
    """Update a document based on the query with new values.

    Args:
        query (Dict[str, Any]): The query to find the document to update.
        new_values (Dict[str, Any]): The new values to update the document with.

    Returns:
        None
    """
    result = mongodb_collection.update_one(query, new_values)
    print(f"Documents updated: {result.modified_count}")


# 10. Delete Data
def delete_document(query: Dict[str, Any]) -> None:
    """Delete a document based on the specified query.

    Args:
        query (Dict[str, Any]): The query to find the document to delete.

    Returns:
        None
    """
    result = mongodb_collection.delete_one(query)
    print(f"Documents deleted: {result.deleted_count}")


# 11. Limit Results
def limit_results(limit: int) -> None:
    """Limit the results to a specified number of documents and print them.

    Args:
        limit (int): The number of documents to limit the results to.

    Returns:
        None
    """
    print(f"Limiting to first {limit} documents:")
    for document in mongodb_collection.find().limit(limit):
        print(document)


def main() -> None:
    """Main function to execute all database operations.

    This function orchestrates checking the existence of the database
    and collection, inserting documents, finding documents, updating,
    deleting, and limiting results.

    Returns:
        None
    """
    check_database_exists("my_first_database")
    check_collection_exists("my_first_collection")

    # Insert a single document
    insert_single_document({"name": "John", "address": "Highway 37"})

    # Insert multiple documents
    insert_multiple_documents([
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
    ])

    # Find a specific document
    find_one_document({"name": "John"})

    # Retrieve all documents
    find_all_documents()

    # Find documents with a specific condition
    find_documents_with_condition({"address": "Highway 37"})

    # Sort documents by name
    sort_documents_by_field("name")

    # Update a document
    update_document({"name": "John"}, {"$set": {"address": "Canyon 123"}})

    # Delete a document
    delete_document({"name": "John"})

    # Limit results to the first 5 documents
    limit_results(5)

    # Recheck the database and collection
    check_database_exists("my_first_database")
    check_collection_exists("my_first_collection")


if __name__ == '__main__':
    main()

def create_document(client, database, collection, document):
    """Create a document in the specified collection."""
    db = client[database]
    col = db[collection]
    col.insert_one(document)


def read_document(client, database, collection, username):
    """Read a document from the specified collection by ID."""
    db = client[database]
    col = db[collection]
    document = col.find_one({"username": username})
    return document


def update_document(client, database, collection, id, update):
    """Update a document in the specified collection by ID."""
    db = client[database]
    col = db[collection]
    col.update_one({"_id": id}, {"$set": update})


def delete_document(client, database, collection, id):
    """Delete a document from the specified collection by ID."""
    db = client[database]
    col = db[collection]
    col.delete_one({"_id": id})
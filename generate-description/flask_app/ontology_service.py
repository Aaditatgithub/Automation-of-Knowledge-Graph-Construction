from neo4j_connection import neo4j_conn

def create_ontology_node(category, subcategory, item_data):
    """
    Inserts Category, Subcategory, and Item nodes in Neo4j with relationships.
    Args:
        category (str): Main category (e.g., "Apparel", "Footwear").
        subcategory (str): Subcategory (e.g., "T-Shirts", "Sneakers").
        item_data (dict): Item attributes (converted from class object).
    """
    
    try:
        # Step 1: Ensure Domain Node (Fashion) Exists
        query_domain = """
        MERGE (d:Domain {name: "Fashion"})
        RETURN d
        """
        neo4j_conn.execute_query(query_domain)

        # Step 2: Ensure Category Node Exists
        query_category = """
        MERGE (c:Category {name: $category})
        MERGE (d:Domain {name: "Fashion"})-[:CONTAINS]->(c)
        RETURN c
        """
        neo4j_conn.execute_query(query_category, {"category": category})

        # Step 3: Ensure Subcategory Node Exists
        query_subcategory = """
        MERGE (s:Subcategory {name: $subcategory})
        MERGE (c:Category {name: $category})-[:CONTAINS]->(s)
        RETURN s
        """
        neo4j_conn.execute_query(query_subcategory, {"category": category, "subcategory": subcategory})

        # Step 4: Insert the Item Node (with extracted attributes)
        item_properties = {key: value for key, value in item_data.items() if value is not None}
        item_query = """
        MERGE (i:Item {name: $name})
        SET """ + ", ".join([f"i.{key} = ${key}" for key in item_properties.keys()]) + """
        MERGE (s:Subcategory {name: $subcategory})-[:CONTAINS]->(i)
        RETURN i
        """
        item_properties["name"] = item_data["name"]
        item_properties["subcategory"] = subcategory
        neo4j_conn.execute_query(item_query, item_properties)

        return {"message": f"Ontology created for {item_data['name']} in {subcategory} under {category}."}

    except Exception as e:
        return {"error": str(e)}

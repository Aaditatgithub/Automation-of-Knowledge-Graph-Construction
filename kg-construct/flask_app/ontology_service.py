from neo4j_connection import neo4j_conn

def is_valid_value(value):
    """Returns True if the value is not None, not empty, and not 'NA'."""
    return value not in [None, "", "NA"]

def create_ontology_node(taxonomical_class):
    """
    Creates an ontology structure in Neo4j using hierarchical attributes, 
    class-specific attributes, and metadata fields.
    """

    # Step 1: Extract hierarchical attributes
    domain = taxonomical_class.domain
    product_class = taxonomical_class.product_class
    category = taxonomical_class.category
    subcategory = taxonomical_class.subcategory

    # Step 2: Create the hierarchy
    query_hierarchy = """
    MERGE (d:Domain {name: $domain})
    MERGE (pc:ProductClass {name: $product_class})
    MERGE (d)-[:HAS_CLASS]->(pc)
    MERGE (cat:Category {name: $category})
    MERGE (pc)-[:HAS_CATEGORY]->(cat)
    MERGE (subcat:Subcategory {name: $subcategory})
    MERGE (cat)-[:HAS_SUBCATEGORY]->(subcat)
    RETURN subcat
    """
    params_hierarchy = {
        "domain": domain,
        "product_class": product_class,
        "category": category,
        "subcategory": subcategory
    }
    neo4j_conn.execute_query(query_hierarchy, params_hierarchy)

    # Step 3: Create the Product node under subcategory
    query_product = """
    MERGE (subcat:Subcategory {name: $subcategory})
    MERGE (p:Product {name: $product_name})
    MERGE (subcat)-[:HAS_PRODUCT]->(p)
    RETURN p
    """
    params_product = {
        "subcategory": subcategory,
        "product_name": subcategory  # Using subcategory as the product name
    }
    neo4j_conn.execute_query(query_product, params_product)

    # Step 4: Get all attributes from the Pydantic model
    attributes = taxonomical_class.model_dump()

    # Step 5: Create feature nodes and dynamically name the relationship based on the field name
    for attr, value in attributes.items():
        if attr not in ["domain", "product_class", "category", "subcategory", "trend_tags", "complementary_items"]:
            if is_valid_value(value):
                # Construct a dynamic relationship type, e.g. "HAS_MATERIAL" if attr is "material"
                rel_type = f"HAS_{attr.upper()}"
                query_feature = f"""
                MATCH (p:Product {{name: $product_name}})
                MERGE (f:Feature {{name: $value, type: $attr}})
                MERGE (p)-[:{rel_type}]->(f)
                """
                params_feature = {
                    "product_name": subcategory,
                    "value": value,
                    "attr": attr
                }
                neo4j_conn.execute_query(query_feature, params_feature)

    # Step 6: Handle trend tags (unchanged)
    trend_tags = attributes.get("trend_tags", []) or []
    for trend in trend_tags:
        trend_name = trend.get("trend")
        influenced_by = trend.get("influenced_by", [])

        if is_valid_value(trend_name):
            # Link Product to Trend
            query_trend = """
            MATCH (p:Product {name: $product_name})
            MERGE (t:Trend {name: $trend_name})
            MERGE (p)-[:BELONGS_TO]->(t)
            """
            params_trend = {
                "product_name": subcategory,
                "trend_name": trend_name
            }
            neo4j_conn.execute_query(query_trend, params_trend)

            # Link Features to Trend via INFLUENCES
            for attr in influenced_by:
                if is_valid_value(attr):
                    query_trend_link = """
                    MATCH (p:Product {name: $product_name})-[:HAS_FEATURE]->(f:Feature {type: $attribute})
                    MATCH (t:Trend {name: $trend_name})
                    MERGE (f)-[:INFLUENCES]->(t)
                    """
                    params_trend_link = {
                        "product_name": subcategory,
                        "attribute": attr,
                        "trend_name": trend_name
                    }
                    neo4j_conn.execute_query(query_trend_link, params_trend_link)

    # Step 7: Handle complementary items (unchanged)
    complementary_items = attributes.get("complementary_items", []) or []
    for item in complementary_items:
        complementary_name = item.get("item")
        relation_type = item.get("relation")

        if is_valid_value(complementary_name):
            query_complementary = """
            MATCH (p1:Product {name: $product_name})
            MERGE (p2:Product {name: $complementary_name})
            MERGE (p1)-[r:PAIRS_WELL_WITH]->(p2)
            SET r.type = $relation_type
            """
            params_complementary = {
                "product_name": subcategory,
                "complementary_name": complementary_name,
                "relation_type": relation_type
            }
            neo4j_conn.execute_query(query_complementary, params_complementary)

    return "Ontology successfully created"

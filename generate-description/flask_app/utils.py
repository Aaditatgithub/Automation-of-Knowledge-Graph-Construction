from fashion_entities import Apparel, Footwear, Accessories, HomeDecor, FashionEntity

def map_response_to_class(response: dict) -> FashionEntity:
    """
    Map LLM response to the appropriate class based on the 'category' field.
    
    Args:
        response (dict): The JSON response from the LLM.
    
    Returns:
        FashionEntity: An instance of the mapped class (e.g., Apparel, Footwear).
    """
    # Define the mapping dictionary
    category_mapping = {
        "Apparel": Apparel,
        "Footwear": Footwear,
        "Accessories": Accessories,
        "HomeDecor": HomeDecor,
    }

    # Extract category from the response
    category = response.get("category")
    if not category or category not in category_mapping:
        raise ValueError(f"Unknown or missing category: {category}")

    # Get the appropriate class
    entity_class = category_mapping[category]

    # Instantiate and return the class
    return entity_class(**response)

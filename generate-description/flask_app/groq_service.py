import requests
from config import Config
from fashion_entities import FashionEntity
from utils import map_response_to_class
import json

# Groq API Configuration
GROQ_API_KEY = Config.GROQ_API_KEY
GROQ_API_ENDPOINT = Config.GROQ_API_ENDPOINT
GROQ_MODEL = Config.GROQ_MODEL

def call_groq_api(row: dict) -> FashionEntity:
    """
    Process the product through the Groq API to determine its type and fill its attributes.
    
    Args:
        row (dict): Input data for the product.
    
    Returns:
        FashionEntity: The mapped entity class.
    """
    product_name = row.get("product_name", "Unknown Product")

    # Step 1: Determine Product Type
    product_type = determine_product_type(product_name)
    if product_type == "Unknown":
        return {"error": "Could not determine product type."}

    # Step 2: Call the respective method for the inferred product type
    if product_type == "Apparel":
        return process_apparel(row)
    elif product_type == "Footwear":
        return process_footwear(row)
    elif product_type == "Accessories":
        return process_accessories(row)
    elif product_type == "HomeDecor":
        return process_home_decor(row)
    else:
        return {"error": f"Unhandled product type: {product_type}"}


def determine_product_type(product_name: str) -> str:
    """
    Call the Groq API to determine the type of product (e.g., Apparel, Footwear).

    Args:
        product_name (str): The name of the product.

    Returns:
        str: The inferred product type (Apparel, Footwear, Accessories, Home Decor, or Unknown).
    """ 
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Classify the product '{product_name}' into one of the following categories: Apparel, Footwear, Accessories, or Home Decor. "
                                f"Return the response in JSON format with the category name under a 'category' field."
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "max_tokens": 64,
        "top_p": 1,
        "stream": False,
        "response_format": {"type": "json_object"},
        "stop": None
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        structured_response = result.get("choices", [{}])[0].get("message", {}).get("content", {})

        if isinstance(structured_response, str):
            try:
                structured_response = json.loads(structured_response)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return "Unknown"

        product_type = structured_response.get("category", "Unknown")
        print(f"Inferred Product Type: {product_type}")
        return product_type
    else:
        print(f"Error determining product type: {response.status_code} - {response.text}")
        return "Unknown"



def process_apparel(row: dict) -> dict:
    """
    Populate all attributes for the Apparel class, including dynamic attributes, using the Groq API.
    """
    combined_text = "\n".join([f"{key}: {value}" for key, value in row.items() if key != "feature_image"])

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Based on the product type 'Apparel', populate all attributes for the Apparel class in JSON format. "
                                f"Include the following fields with descriptions:\n"
                                f"- material: Fabric material (e.g., Cotton, Silk).\n"
                                f"- fit: Fit type (e.g., Slim, Regular).\n"
                                f"- pattern: Patterns (e.g., Solid, Floral).\n"
                                f"- sleeveType: Sleeve types (e.g., Full Sleeve, Sleeveless).\n"
                                f"- neckline: Neckline types (e.g., V-Neck, Round Neck).\n"
                                f"- hemline: Hemlines (e.g., Straight, Asymmetrical).\n"
                                f"- length: Length (e.g., Mini, Midi, Maxi).\n"
                                f"- occasion: Suitable occasions (e.g., Casual, Formal).\n"
                                f"- seasonality: Seasonal relevance (e.g., Summer, Winter).\n"
                                f"- careInstructions: Washing/care instructions.\n"
                                f"- gender: Targeted gender (e.g., Men, Women, Unisex).\n"
                                f"- dynamicAttributes: Add emerging styles and trends specific to apparel (e.g., \"Cold Shoulder\", \"Balloon Sleeves\", \"Athleisure\").\n"
                                f"- hierarchicalFeatures: Include subcategories within apparel, such as \"Polos\" under \"Shirts\", or \"Maxi Dresses\" under \"Dresses\".\n"
                                f"- pairings: List other product types or accessories that pair well with the apparel (e.g., \"Sneakers\" with \"Joggers\", \"Earrings\" with \"Evening Gowns\").\n"
                                f"The product details are as follows:\n{combined_text}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": row.get("feature_image", "")
                        }
                    }
                ]
            }
        ],
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False,
        "response_format": {"type": "json_object"},
        "stop": None
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        structured_response_str = result.get("choices", [{}])[0].get("message", {}).get("content", {})

        if isinstance(structured_response_str, str):
            try:
                structured_response = json.loads(structured_response_str)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return {"error": "Invalid JSON format received from Groq API"}
        else:
            structured_response = structured_response_str

        print("Groq API Apparel Response:", json.dumps(structured_response, indent=2))
        return structured_response
    else:
        print(f"Error filling Apparel parameters: {response.status_code} - {response.text}")
        return {"error": f"Error: {response.status_code} - {response.text}"}



def process_footwear(row: dict) -> dict:
    """
    Populate all attributes for the Footwear class using the Groq API.
    """
    combined_text = "\n".join([f"{key}: {value}" for key, value in row.items() if key != "feature_image"])

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Based on the product type 'Footwear', populate all attributes for the Footwear class in JSON format. "
                                f"Include the following fields with descriptions:\n"
                                f"- material: Shoe material (e.g., Leather, Rubber).\n"
                                f"- soleType: Sole type (e.g., Rubber, Foam).\n"
                                f"- closureType: Closure mechanism (e.g., Laces, Velcro).\n"
                                f"- heelHeight: Heel height (e.g., Flat, Mid).\n"
                                f"- fitType: Fit type (e.g., Regular, Wide).\n"
                                f"- occasion: Suitable occasions (e.g., Casual, Formal).\n"
                                f"- waterResistance: Water resistance level.\n"
                                f"- dynamicAttributes: Add footwear-specific styles and trends (e.g., \"Platform Heels\", \"Chunky Sneakers\", \"Eco-friendly Soles\").\n"
                                f"- hierarchicalFeatures: Include subcategories like \"Loafers\" under \"Casual Shoes\" or \"Hiking Boots\" under \"Outdoor Shoes\".\n"
                                f"- pairings: Specify what outfits or accessories pair well with the footwear (e.g., \"Hiking Boots\" with \"Cargo Pants\").\n"
                                f"The product details are as follows:\n{combined_text}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": row.get("feature_image", "")
                        }
                    }
                ]
            }
        ],
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False,
        "response_format": {"type": "json_object"},
        "stop": None
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        structured_response_str = result.get("choices", [{}])[0].get("message", {}).get("content", {})

        if isinstance(structured_response_str, str):
            try:
                structured_response = json.loads(structured_response_str)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return {"error": "Invalid JSON format received from Groq API"}
        else:
            structured_response = structured_response_str

        print("Groq API Footwear Response:", json.dumps(structured_response, indent=2))
        return structured_response
    else:
        print(f"Error filling Footwear parameters: {response.status_code} - {response.text}")
        return {"error": f"Error: {response.status_code} - {response.text}"}


def process_accessories(row: dict) -> dict:
    """
    Populate all attributes for the Accessories class using the Groq API.
    """
    combined_text = "\n".join([f"{key}: {value}" for key, value in row.items() if key != "feature_image"])

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Based on the product type 'Accessories', populate all attributes for the Accessories class in JSON format. "
                                f"Include the following fields with descriptions:\n"
                                f"- material: The material (e.g., Gold, Silver, Leather).\n"
                                f"- gemstoneType: Type of gemstones used (e.g., Diamond, Ruby).\n"
                                f"- weight: Weight category (e.g., Light, Medium, Heavy).\n"
                                f"- style: Styles (e.g., Boho, Minimalist).\n"
                                f"- functionality: Functionality (e.g., Health Tracker, Chronograph).\n"
                                f"- claspType: Clasp mechanism (e.g., Buckle, Hook).\n"
                                f"- size: Size (e.g., Adjustable, One Size).\n"
                                f"- waterResistance: Water resistance (e.g., Yes, No).\n"
                                f"- dynamicAttributes: Include emerging accessory styles or trends (e.g., \"Layered Necklaces\", \"Statement Earrings\", \"Smart Bands\").\n"
                                f"- hierarchicalFeatures: Include subcategories like \"Cuff Bracelets\" under \"Bracelets\", or \"Pendant Necklaces\" under \"Necklaces\".\n"
                                f"- pairings: List what apparel or other accessories pair well (e.g., \"Statement Earrings\" with \"Evening Gowns\", \"Smart Bands\" with \"Athleisure Outfits\").\n"
                                f"The product details are as follows:\n{combined_text}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": row.get("feature_image", "")
                        }
                    }
                ]
            }
        ],
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False,
        "response_format": {"type": "json_object"},
        "stop": None
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        structured_response_str = result.get("choices", [{}])[0].get("message", {}).get("content", {})

        if isinstance(structured_response_str, str):
            try:
                structured_response = json.loads(structured_response_str)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return {"error": "Invalid JSON format received from Groq API"}
        else:
            structured_response = structured_response_str

        print("Groq API Accessories Response:", json.dumps(structured_response, indent=2))
        return structured_response
    else:
        print(f"Error filling Accessories parameters: {response.status_code} - {response.text}")
        return {"error": f"Error: {response.status_code} - {response.text}"}


def process_home_decor(row: dict) -> dict:
    """
    Populate all attributes for the HomeDecor class using the Groq API.
    """
    combined_text = "\n".join([f"{key}: {value}" for key, value in row.items() if key != "feature_image"])

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Based on the product type 'HomeDecor', populate all attributes for the HomeDecor class in JSON format. "
                                f"Include the following fields with descriptions:\n"
                                f"- material: The material used (e.g., Wood, Metal, Glass).\n"
                                f"- dimensions: Dimensions of the product (e.g., Length, Width, Height).\n"
                                f"- weight: Weight category (e.g., Light, Medium, Heavy).\n"
                                f"- color: Available colors (e.g., White, Black, Beige).\n"
                                f"- functionality: Functional features (e.g., Adjustable Height, Storage).\n"
                                f"- careInstructions: Care instructions (e.g., Wipe Clean Only).\n"
                                f"- style: Styles (e.g., Modern, Rustic, Industrial).\n"
                                f"- dynamicAttributes: Include emerging styles or features for home decor (e.g., \"Smart Lighting\", \"Sustainable Furniture\", \"Rustic Designs\").\n"
                                f"- hierarchicalFeatures: Include subcategories like \"Standing Lamps\" under \"Lighting\" or \"Modular Sofas\" under \"Sofas\".\n"
                                f"- pairings: Specify decor pieces or themes that match (e.g., \"Rustic Tables\" with \"Farmhouse Chairs\").\n"
                                f"The product details are as follows:\n{combined_text}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": row.get("feature_image", "")
                        }
                    }
                ]
            }
        ],
        "temperature": 1,
        "max_tokens": 1024,
        "top_p": 1,
        "stream": False,
        "response_format": {"type": "json_object"},
        "stop": None
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(GROQ_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        structured_response_str = result.get("choices", [{}])[0].get("message", {}).get("content", {})

        if isinstance(structured_response_str, str):
            try:
                structured_response = json.loads(structured_response_str)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return {"error": "Invalid JSON format received from Groq API"}
        else:
            structured_response = structured_response_str

        print("Groq API HomeDecor Response:", json.dumps(structured_response, indent=2))
        return structured_response
    else:
        print(f"Error filling HomeDecor parameters: {response.status_code} - {response.text}")
        return {"error": f"Error: {response.status_code} - {response.text}"}

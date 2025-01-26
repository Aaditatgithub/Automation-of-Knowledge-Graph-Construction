from groq import Groq
from config import Config
from generate_taxonomy import get_taxonomical_class

# Load configurations
IGROQ_MODEL = Config.IGROQ_MODEL
IGROQ_API_KEY = Config.IGROQ_API_KEY

# Prompts for image description based on product class
prompts = {
    "Apparel": "Describe the following of the fashion product: color, pattern, and seasonality.",
    "Footwear": "Describe the following of the fashion product: sole type, closure type, and occasion.",
    "Accessories": "Describe the following of the fashion product: style, functionality, and water resistance.",
    "HomeDecor": "Describe the following of the fashion product: dimensions, style, and placement area."
}

def get_structured_output(product_data, product_class):
    """
    Generate one among the four classes of fashion ontology.
    
    Args:
        product_data (dict): Contains description, metadata, image_url, name, etc.
        product_class (str): Class of the product (e.g., Apparel, Footwear, Accessories, Home Decor).
    
    Returns:
        dict: Structured output from the LLM.
    """
    try:
        print("Entered get_structured_output function")
        image_desc = image_description(product_class, product_data["feature_image"])
        # print(f"Image Description: {image_desc}")
        
        product_data["image_desc"] = image_desc
        del product_data["feature_image"]
        
        taxonomical_class = get_taxonomical_class(product_class, product_data)
        # print(taxonomical_class)
        return taxonomical_class
        

    except Exception as e:
        print(f"Error in get_structured_output: {str(e)}")



def image_description(product_class, product_image_url):
    """
    Generate a description for an image based on its product class.

    Args:
        product_class (str): The product class (e.g., Apparel, Footwear, Accessories, Home Decor).
        product_image_url (str): The URL of the product image.

    Returns:
        str: Description of the image.
    """
    try:
        # Initialize the Groq client
        client = Groq(api_key=IGROQ_API_KEY)

        # Call the Groq API with the appropriate prompt and image URL
        completion = client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": prompts[product_class]  # Use a plain string for the prompt
                },
                {
                    "role": "user",
                    "content": product_image_url  # Use a plain string for the image URL
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        # Extract the response
        # print(type(completion.choices[0].message))
        return completion.choices[0].message.content

    except Exception as e:
        print(f"Error in image_description: {str(e)}")
        return f"Error: {str(e)}"

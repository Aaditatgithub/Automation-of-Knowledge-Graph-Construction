from groq import Groq
from config import Config
from generate_taxonomy import get_taxonomical_class

# Load configurations
IGROQ_MODEL = Config.IGROQ_MODEL
IGROQ_API_KEY = Config.IGROQ_API_KEY

# Prompts for image description based on product class
prompts = {
    "Apparel": (
        "Provide a detailed description of the apparel based on its visual and contextual attributes. "
        "Include the *primary color* and any *secondary or accent colors*, describing their placement and contrast. "
        "Describe the *pattern or design elements* present (e.g., floral, stripes, abstract, embroidery), highlighting "
        # "how they contribute to the overall aesthetic. Additionally, specify the *fabric texture* (e.g., smooth, ribbed, sheer) "
        "and how it influences the look and feel of the garment. Finally, mention the *seasonality*, explaining whether the apparel "
        "is best suited for warm weather, cold climates, or all-season wear."
    ),

    "Footwear": (
        "Provide a detailed description of the footwear, emphasizing its structural and stylistic elements. "
        "Start with the *sole type*, explaining whether it is flat, cushioned, treaded, or designed for grip and durability. "
        "Describe the *closure type*, including laces, buckles, slip-on mechanisms, or velcro, and how they affect usability. "
        "Include details about the *toe shape* (e.g., rounded, pointed, square) and how it contributes to the design. "
        "Discuss the *upper material and texture*, mentioning whether it’s smooth leather, suede, or breathable mesh. "
        "Finally, specify the *occasion and use-case*, indicating whether the footwear is ideal for casual outings, formal events, athletic activities, or everyday wear."
    ),

    "Accessories": (
        "Describe the accessory in terms of its *style, materials, and functional attributes*. "
        "Start with the *dominant color* and any *secondary hues or embellishments*, explaining their effect on the overall design. "
        "Describe the *material and finish* (e.g., polished gold, matte leather, textured metal) and how they influence the aesthetic. "
        "Provide insight into the *functionality*, whether it serves a decorative, practical, or multi-functional purpose (e.g., timekeeping for watches, storage for bags). "
        "Discuss any *gemstones, engravings, or patterns* present, highlighting their significance. "
        "Additionally, mention whether the accessory is *water-resistant or waterproof*, specifying if it is suitable for daily wear, outdoor activities, or formal occasions."
    ),

    "HomeDecor": (
        "Provide a rich and detailed description of the home decor product, focusing on *dimensions, style, and placement area*. "
        "Start with the *primary color and any accent colors*, explaining how they complement different interiors. "
        "Describe the *texture and finish* (e.g., glossy, matte, distressed, smooth) and how they contribute to its appeal. "
        "Mention the *design style* (e.g., minimalist, bohemian, vintage) and any *patterns or embellishments* present. "
        "Provide insights into the *shape and proportions*, explaining how they affect the room’s ambiance. "
        "Finally, describe the *placement area*, specifying whether the item is suited for living rooms, bedrooms, offices, or outdoor spaces."
    )
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

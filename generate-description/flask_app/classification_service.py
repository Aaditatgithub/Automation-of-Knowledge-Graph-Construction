from groq import Groq
from config import Config

# Initialize the Groq client
client = Groq(api_key=Config.GROQ_API_KEY)

def classify_product(product_data):
    """
    Classify product into one of the four categories: Apparel, Footwear, Accessory, or HomeDecor.
    Args:
        product_data (dict): A dictionary containing only the product name.
    Returns:
        str: The product class.
    """
    try:
        # Prepare the chat messages
        messages = [
            {
                "role": "system",
                "content": "You are a fashion expert that classifies products into one of four categories: Apparel, Footwear, Accessory, HomeDecor. Replies in only one word, no punctuation."
            },
            {
                "role": "user",
                "content": f"Classify the following product:\n\nProduct Name: {product_data.get('name'),}"
            }
        ]

        # Call the Groq API
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        # Extract the response
        product_class = chat_completion.choices[0].message.content.strip()
        # print(f"Classified Product Category: {product_class}")
        return product_class

    except Exception as e:
        print(f"Error in product classification: {str(e)}")
        return None

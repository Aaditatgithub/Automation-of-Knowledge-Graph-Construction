import os
from config import Config
from langchain_mistralai import ChatMistralAI
from dto.Accessory import Accessory
from dto.Apparel import Apparel
from dto.Footwear import Footwear
from dto.HomeDecor import HomeDecor
import json
from typing import Any

if not os.environ.get("MISTRAL_API_KEY"):
    os.environ["MISTRAL_API_KEY"] = Config.MISTRAL_API_KEY

llm = ChatMistralAI(model_name="mistral-large-latest")

def get_taxonomical_class(product_class: str, product_data: Any) -> Any:
    try:
        print("-----------------Entered get_taxonomical_class-----------------")

        product_data_str = json.dumps(product_data)

        if product_class == "Apparel":
            structured_llm = llm.with_structured_output(Apparel)
        elif product_class == "Footwear":
            structured_llm = llm.with_structured_output(Footwear)
        elif product_class == "Accessory":
            structured_llm = llm.with_structured_output(Accessory)
        elif product_class == "HomeDecor":
            structured_llm = llm.with_structured_output(HomeDecor)
        else:
            raise ValueError(f"Unknown product class: {product_class}")
        
        taxonomical_class = structured_llm.invoke(product_data_str)
        # print(taxonomical_class)
        return taxonomical_class
    
    except Exception as e:
        print(f"Error in get_taxonomical_class: {e}")
        return None


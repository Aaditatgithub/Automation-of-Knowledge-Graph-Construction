from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Apparel(BaseModel):
    # 📌 Hierarchical Attributes (Ontology Structure)
    domain: str = Field("Fashion", description="The broadest classification encompassing the fashion industry, under which all fashion-related products are grouped.")
    product_class: str = Field("Apparel", description="A high-level classification representing wearable clothing items, grouping products based on their primary function as garments.")
    category: str = Field(..., description="A division within the Apparel class, categorizing products based on common characteristics or intended use, such as outerwear, casual wear, or formal wear.")
    subcategory: Optional[str] = Field(None, description="A more granular classification within a category, distinguishing items by specific design elements or occasions, such as T-Shirts, Blazers, or Evening Gowns.")

    # 📌 Class-Specific Attributes (Stored as `HAS_FEATURE` Nodes)
    pattern: Optional[str] = Field(None, description="The design or motif present on the fabric, defining its aesthetic appearance (e.g., Stripes, Floral, Solid).")
    texture: Optional[str] = Field(None, description="The surface quality or feel of the fabric, affecting touch perception and visual appeal (e.g., Matte, Glossy, Rough).")
    silhouette: Optional[str] = Field(None, description="The overall shape and structure of the apparel when worn, defining its fit and flow (e.g., A-Line, Straight, Fitted).")
    fabric_type: str = Field(..., description="The primary material composition of the apparel, determining comfort, durability, and breathability (e.g., Cotton, Silk, Denim).")
    fabric_composition: Optional[str] = Field(None, description="A breakdown of the fabric blend used, specifying percentages of materials present (e.g., 60% Cotton, 40% Polyester).")
    sleeve_type: Optional[str] = Field(None, description="The design and length of the sleeves, influencing both style and coverage (e.g., Sleeveless, Bell Sleeve, Full Sleeve).")
    closure_type: Optional[str] = Field(None, description="The fastening mechanism that allows the apparel to be opened or secured (e.g., Zipper, Buttons, Tie).")
    fit: Optional[str] = Field(None, description="Describes how closely the apparel conforms to the wearer's body, affecting comfort and style (e.g., Slim, Relaxed, Oversized).")
    length: Optional[str] = Field(None, description="The vertical measurement of the apparel, defining how long it extends on the body (e.g., Mini, Midi, Maxi, Ankle-Length).")
    neckline: Optional[str] = Field(None, description="The shape and style of the neckline, influencing aesthetics and wearability (e.g., V-Neck, Round Neck, Halter).")
    occasion: Optional[str] = Field(None, description="The context or setting where the apparel is most appropriately worn, influencing styling decisions (e.g., Casual, Formal, Party).")
    seasonal_relevance: Optional[List[str]] = Field(None, description="The seasons during which the apparel is best suited for wear, factoring in climate adaptability (e.g., Spring, Winter).")
    climate_suitability: Optional[str] = Field(None, description="Indicates the type of weather conditions the apparel is designed for, affecting material choices and breathability (e.g., Hot, Cold, Humid).")
    layering_potential: Optional[bool] = Field(None, description="A boolean value indicating whether the apparel is designed to be layered with other clothing for styling or temperature regulation.")

    # 📌 Metadata Fields (Trends, Sustainability, Compatibility)
    # eco_certifications: Optional[List[str]] = Field(None, description="Official sustainability labels or environmental compliance marks associated with the product, ensuring ethical production (e.g., FSC Certified, Organic Fabric, Recycled Cotton).")
    trend_tags: Optional[List[Dict[str, Any]]] = Field(
        None, description="Trends related to this product. Example: [{'trend': 'Streetwear', 'influenced_by': ['fabric_type', 'fit']}]"
    )

    complementary_items: Optional[List[Dict[str, str]]] = Field(
        None, description="Complementary items with relation type. Example: [{'item': 'Sneakers', 'relation': 'pairs_well_with'}]"
    )

    recommended_color_pairs: Optional[List[str]] = Field(None, description="Color combinations that enhance the aesthetic appeal of the apparel, based on fashion principles (e.g., Blue pairs well with White & Black).")
    accessory_recommendations: Optional[List[str]] = Field(None, description="Accessories that complement the apparel, enhancing the overall look and style (e.g., Gold Necklace, Leather Watch).")

    
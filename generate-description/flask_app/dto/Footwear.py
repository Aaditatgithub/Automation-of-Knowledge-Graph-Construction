from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Footwear(BaseModel):
    # 📌 Hierarchical Attributes (Ontology Structure)
    domain: str = Field("Fashion", description="Represents the domain of the fashion industry, covering all products related to personal attire and style.")
    product_class: str = Field("Footwear", description="A primary category encompassing all types of shoes and footwear designed to protect and adorn the feet.")
    category: str = Field(..., description="An organizational layer within Footwear, sorting items by their intended activity or style, such as Sneakers, Boots, or Sandals.")
    subcategory: Optional[str] = Field(None, description="A specific breakdown within a category, further defining footwear by functional characteristics or design, like Running Shoes, Dress Shoes, or Hiking Boots.")

    # 📌 Class-Specific Attributes (Stored as `HAS_FEATURE` Nodes)
    sole_material: str = Field(..., description="Material of the sole (e.g., Rubber, EVA, PU).")
    upper_material: str = Field(..., description="Primary material for the upper part (e.g., Leather, Canvas, Synthetic).")
    lining_material: Optional[str] = Field(None, description="Inner material (e.g., Mesh, Foam, Textile).")
    insole_material: Optional[str] = Field(None, description="Material inside for cushioning (e.g., Memory Foam, Leather).")
    durability_rating: Optional[float] = Field(None, description="Durability score indicating the expected lifespan.")
    waterproof: Optional[bool] = Field(None, description="Indicates if the footwear is waterproof or water-resistant.")
    fastening_type: Optional[str] = Field(None, description="Fastening type (e.g., Laces, Velcro, Slip-On).")
    toe_shape: Optional[str] = Field(None, description="Toe box shape (e.g., Round, Pointed, Square).")
    heel_type: Optional[str] = Field(None, description="Type of heel (e.g., Flat, Wedge, Stiletto).")
    heel_height: Optional[str] = Field(None, description="Heel height classification (e.g., Low, Medium, High).")
    sole_type: Optional[str] = Field(None, description="Base structure of the shoe (e.g., Flat, Treaded, Cushioned).")
    occasion: Optional[str] = Field(None, description="Occasions suitable for the footwear (e.g., Casual, Formal, Sports).")

    # 📌 Metadata Fields (Trends, Sustainability, Compatibility)
    # trend_tags: Optional[List[str]] = Field(None, description="Associated fashion trends (e.g., Athleisure, Minimalist).")
    # eco_certifications: Optional[List[str]] = Field(None, description="Sustainability certifications (e.g., Vegan Leather, Recycled Rubber).")
    # complementary_items: Optional[List[str]] = Field(None, description="Clothing items that pair well with the footwear.")
    trend_tags: Optional[List[Dict[str, Any]]] = Field(
        None, description="Trends related to this product. Example: [{'trend': 'Athleisure', 'influenced_by': ['sole_material', 'style_tags']}]"
    )

    complementary_items: Optional[List[Dict[str, str]]] = Field(
        None, description="Complementary items with relation type. Example: [{'item': 'Joggers', 'relation': 'pairs_well_with'}]"
    )
    recommended_color_pairs: Optional[List[str]] = Field(None, description="Best-matching color combinations.")
    accessory_recommendations: Optional[List[str]] = Field(None, description="Recommended accessories.")


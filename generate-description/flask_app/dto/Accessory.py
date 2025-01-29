from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Accessory(BaseModel):
    # 📌 Hierarchical Attributes (Ontology Structure)
    domain: str = Field("Fashion", description="Represents the domain of fashion, covering all related accessories and complementary items.")
    product_class: str = Field("Accessory", description="Designates the product as a supplementary fashion item enhancing style and functionality.")
    category: str = Field(..., description="Groups accessories by primary type and function (e.g., Jewelry, Watches, Belts, Bags).")
    subcategory: str = Field(..., description="Specifies the detailed type of accessory within the category, based on design and purpose (e.g., Pendant Necklace, Analog Watch, Leather Belt).")
    
    # 📌 Class-Specific Attributes (Stored as `HAS_FEATURE` Nodes)
    material: str = Field(..., description="Primary material composition of the accessory (e.g., Gold, Leather, Stainless Steel, Silk).")
    finish: Optional[str] = Field(None, description="Surface treatment affecting the accessory's look and feel (e.g., Polished, Matte, Textured).")
    pattern: Optional[str] = Field(None, description="Visual motif or engraving on the accessory (e.g., Engraved, Solid, Beaded).")
    texture: Optional[str] = Field(None, description="Physical texture of the accessory (e.g., Smooth, Rough, Embossed).")
    dimensions: Optional[str] = Field(None, description="Size specification of the accessory (e.g., 40mm dial for watches, 16-inch necklace length).")
    adjustable: Optional[bool] = Field(None, description="Indicates if the accessory has adjustable features (e.g., Strap Length for Watches).")
    water_resistance: Optional[str] = Field(None, description="Waterproof rating for applicable accessories (e.g., 30m, 50m, None).")
    style_tags: Optional[List[str]] = Field(None, description="Design style descriptors (e.g., Minimalist, Glamorous, Sporty).")
    theme: Optional[str] = Field(None, description="Thematic inspiration influencing the accessory’s aesthetics (e.g., Boho Chic, Vintage, Luxury).")
    shape: Optional[str] = Field(None, description="Geometric form of the accessory (e.g., Round, Oval, Rectangular).")
    gem_type: Optional[List[str]] = Field(None, description="List of gemstones used in the accessory (e.g., Diamond, Sapphire, Zircon).")
    clasp_type: Optional[str] = Field(None, description="Fastening mechanism for accessories (e.g., Buckle, Hook, Magnetic).")

    # 📌 Metadata Fields (Trends, Sustainability, Compatibility)
    # trend_tags: Optional[List[str]] = Field(None, description="Associated fashion trends (e.g., Statement Piece, Minimalist, Luxury Fashion).")
    # eco_certifications: Optional[List[str]] = Field(None, description="Sustainability certifications (e.g., Recycled Gold, Conflict-Free Diamonds, Vegan Leather).")
    # compatible_styles: Optional[List[str]] = Field(None, description="Outfit styles that work well with the accessory.")
    trend_tags: Optional[List[Dict[str, Any]]] = Field(
        None, description="Trends related to this product. Example: [{'trend': 'Casual', 'influenced_by': ['pattern', 'style_tags']}]"
    )

    complementary_items: Optional[List[Dict[str, str]]] = Field(
        None, description="Complementary items with relation type. Example: [{'item': 'Jeans', 'relation': 'pairs_well_with'}]"
    )

    complementary_items: Optional[List[str]] = Field(None, description="Suggested fashion accessories that enhance this product.")
    recommended_color_schemes: Optional[List[str]] = Field(None, description="Ideal color combinations for better styling.")


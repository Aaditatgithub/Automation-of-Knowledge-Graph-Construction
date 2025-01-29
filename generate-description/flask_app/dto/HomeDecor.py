from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class HomeDecor(BaseModel):
    # 📌 Hierarchical Attributes (Ontology Structure)
    domain: str = Field("Fashion", description="The domain capturing the intersection of fashion and home aesthetics, where style extends into living spaces.")
    product_class: str = Field("Home Decor", description="A category for items that contribute to the interior design and ambiance of living environments, blending fashion with functionality.")
    category: str = Field(..., description="A broader grouping within Home Decor, aligning items by their role in home settings, such as Furniture, Lighting, or Wall Art.")
    subcategory: Optional[str] = Field(None, description="A deeper classification within a category, detailing items by specific style or application, like Table Lamps, Vanity Mirrors, or Area Rugs.")

    # 📌 Class-Specific Attributes (Stored as `HAS_FEATURE` Nodes)
    material: str = Field(..., description="Primary material composition of the decor item (e.g., Wood, Ceramic, Metal, Glass).")
    finish: Optional[str] = Field(None, description="Surface treatment of the item affecting its look and feel (e.g., Matte, Glossy, Textured).")
    pattern: Optional[str] = Field(None, description="Visual motif or design (e.g., Solid, Stripes, Floral, Geometric).")
    texture: Optional[str] = Field(None, description="Physical texture of the surface (e.g., Smooth, Rough, Embossed).")
    dimensions: Optional[str] = Field(None, description="Size specification of the decor item (e.g., 36x24x12 inches).")
    placement_area: Optional[str] = Field(None, description="Recommended location for item placement (e.g., Living Room, Bedroom, Bathroom).")
    functionality: Optional[str] = Field(None, description="Main purpose of the item (e.g., Storage, Aesthetic, Illumination).")
    installation_required: Optional[bool] = Field(None, description="Indicates if the item requires assembly or mounting (e.g., True, False).")
    power_source: Optional[str] = Field(None, description="Energy requirement for the item, if applicable (e.g., Electric, Battery, None).")
    weight: Optional[float] = Field(None, description="Weight of the decor item in kilograms.")
    style_tags: Optional[List[str]] = Field(None, description="Design style descriptors (e.g., Minimalist, Rustic, Vintage).")
    theme: Optional[str] = Field(None, description="Thematic inspiration influencing the item's aesthetics (e.g., Scandinavian, Industrial, Coastal).")
    shape: Optional[str] = Field(None, description="Geometric form of the item (e.g., Round, Square, Rectangular).")
    edge_design: Optional[str] = Field(None, description="Specific design details for edges (e.g., Beveled, Smooth, Curved).")

    # 📌 Metadata Fields (Trends, Sustainability, Compatibility)
    # trend_tags: Optional[List[str]] = Field(None, description="Associated home decor trends (e.g., Smart Home, Sustainable Living, Vintage Aesthetics).")
    # eco_certifications: Optional[List[str]] = Field(None, description="Sustainability and energy certifications (e.g., FSC Certified, Energy Star).")
    trend_tags: Optional[List[Dict[str, Any]]] = Field(
        None, description="Trends related to this product. Example: [{'trend': 'Minimalist', 'influenced_by': ['material', 'theme']}]"
    )

    complementary_items: Optional[List[Dict[str, str]]] = Field(
        None, description="Complementary items with relation type. Example: [{'item': 'Wall Art', 'relation': 'pairs_well_with'}]"
    )
    
    # compatible_styles: Optional[List[str]] = Field(None, description="Interior design styles that harmonize with this item (e.g., Modern, Bohemian).")
    recommended_color_schemes: Optional[List[str]] = Field(None, description="Suggested color combinations for better visual appeal.")


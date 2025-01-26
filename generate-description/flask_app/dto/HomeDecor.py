from pydantic import BaseModel, Field
from typing import List, Optional

class HomeDecor(BaseModel):
    # Visual Features
    primary_color: str = Field(..., description="Dominant color of the home decor item")
    secondary_colors: Optional[List[str]] = Field(None, description="Secondary or accent colors")
    material: str = Field(..., description="Primary material used (e.g., Wood, Ceramic, Metal)")
    finish: Optional[str] = Field(None, description="Finish of the item (e.g., Matte, Glossy, Textured)")
    pattern: Optional[str] = Field(None, description="Pattern design on the decor item (e.g., Solid, Striped, Floral)")
    texture: Optional[str] = Field(None, description="Surface texture (e.g., Smooth, Rough, Embossed)")
    dimensions: Optional[str] = Field(None, description="Dimensions of the decor item (e.g., 36x24x12 inches)")

    # Functional Features
    category: str = Field(..., description="Category of the home decor item (e.g., Lighting, Furniture, Art)")
    subcategory: Optional[str] = Field(None, description="Subcategory within the decor type (e.g., Table Lamp, Vanity Mirror)")
    placement_area: Optional[str] = Field(None, description="Recommended placement area (e.g., Living Room, Bathroom)")
    functionality: Optional[str] = Field(None, description="Function or utility of the item (e.g., Storage, Aesthetic)")
    installation_required: Optional[bool] = Field(None, description="Whether the decor item requires installation")
    power_source: Optional[str] = Field(None, description="Power source if applicable (e.g., Electric, Battery)")
    weight: Optional[float] = Field(None, description="Weight of the decor item in kilograms")

    # Design Features
    style_tags: Optional[List[str]] = Field(None, description="Design style tags (e.g., Minimalist, Rustic, Vintage)")
    theme: Optional[str] = Field(None, description="Thematic design inspiration (e.g., Coastal, Industrial, Scandinavian)")
    shape: Optional[str] = Field(None, description="Shape of the item (e.g., Round, Square, Rectangular)")
    edge_design: Optional[str] = Field(None, description="Design of the edges (e.g., Beveled, Smooth, Curved)")

    # Compatibility
    compatible_styles: Optional[List[str]] = Field(None, description="List of compatible decor styles (e.g., Modern, Bohemian)")
    complementary_items: Optional[List[str]] = Field(None, description="Other decor items that pair well with this one")
    recommended_color_schemes: Optional[List[str]] = Field(None, description="Suggested color schemes for pairing")

    # Trend and Cultural Features
    trend_tags: Optional[List[str]] = Field(None, description="Trendy associations (e.g., Smart Home, Sustainable Living)")
    cultural_influence: Optional[str] = Field(None, description="Cultural or regional inspiration (e.g., Japanese Zen, Moroccan Tiles)")
    historical_inspiration: Optional[str] = Field(None, description="Historical design influence (e.g., Victorian, Mid-Century Modern)")

    # Metadata
    durability_rating: Optional[float] = Field(None, description="Durability score of the decor item")
    eco_certifications: Optional[List[str]] = Field(None, description="List of eco-friendly certifications (e.g., FSC, Energy Star)")

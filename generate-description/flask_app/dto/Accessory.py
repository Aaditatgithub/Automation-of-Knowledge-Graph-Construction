from pydantic import BaseModel, Field
from typing import List, Optional

class Accessory(BaseModel):
    # Visual Features
    primary_color: str = Field(..., description="Dominant color of the accessory")
    secondary_colors: Optional[List[str]] = Field(None, description="Secondary or accent colors")
    material: str = Field(..., description="Primary material used (e.g., Gold, Leather, Stainless Steel)")
    finish: Optional[str] = Field(None, description="Finish of the accessory (e.g., Polished, Matte, Textured)")
    pattern: Optional[str] = Field(None, description="Pattern or design on the accessory (e.g., Engraved, Solid, Beaded)")
    texture: Optional[str] = Field(None, description="Surface texture (e.g., Smooth, Rough, Embossed)")
    dimensions: Optional[str] = Field(None, description="Dimensions of the accessory (e.g., 40mm dial for watches)")

    # Functional Features
    category: str = Field(..., description="Category of the accessory (e.g., Jewelry, Watches, Belts, Bags)")
    subcategory: Optional[str] = Field(None, description="Subcategory within the accessory type (e.g., Pendant Necklace, Analog Watch)")
    functionality: Optional[str] = Field(None, description="Functionality or purpose of the accessory (e.g., Timekeeping, Aesthetic)")
    adjustable: Optional[bool] = Field(None, description="Whether the accessory is adjustable (e.g., Strap Length for Watches)")
    water_resistance: Optional[str] = Field(None, description="Level of water resistance (e.g., 30m, 50m, None)")

    # Design Features
    style_tags: Optional[List[str]] = Field(None, description="Design style tags (e.g., Minimalist, Glamorous, Sporty)")
    theme: Optional[str] = Field(None, description="Theme or inspiration behind the design (e.g., Boho Chic, Vintage)")
    shape: Optional[str] = Field(None, description="Shape of the accessory (e.g., Round, Oval, Rectangular for watches or earrings)")
    gem_type: Optional[List[str]] = Field(None, description="List of gemstones used, if any (e.g., Diamond, Sapphire, Zircon)")
    clasp_type: Optional[str] = Field(None, description="Type of clasp or fastening mechanism (e.g., Buckle, Hook, Magnetic)")

    # Compatibility
    compatible_styles: Optional[List[str]] = Field(None, description="List of compatible fashion styles (e.g., Formal, Casual, Party)")
    complementary_items: Optional[List[str]] = Field(None, description="Other accessories or clothing that pair well with this item")
    
    # Trend and Cultural Features
    trend_tags: Optional[List[str]] = Field(None, description="Trendy associations (e.g., Eco-Friendly, Statement Piece)")
    cultural_influence: Optional[str] = Field(None, description="Cultural or regional inspiration (e.g., Indian Ethnic, Italian Design)")
    historical_inspiration: Optional[str] = Field(None, description="Historical design influence (e.g., Victorian, Art Deco)")
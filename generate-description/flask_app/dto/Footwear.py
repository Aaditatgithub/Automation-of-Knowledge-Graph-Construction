from pydantic import BaseModel, Field
from typing import List, Optional

class Footwear(BaseModel):
    # Visual Features
    primary_color: str = Field(..., description="Dominant color of the footwear")
    secondary_colors: Optional[List[str]] = Field(None, description="List of secondary or accent colors")
    pattern: Optional[str] = Field(None, description="Pattern design on the footwear (e.g., Solid, Striped, Animal Print)")
    texture: Optional[str] = Field(None, description="Texture or surface quality (e.g., Smooth, Grainy, Embossed)")
    sole_color: Optional[str] = Field(None, description="Color of the sole or outsole")

    # Material and Construction
    upper_material: str = Field(..., description="Material of the upper part (e.g., Leather, Canvas, Synthetic)")
    sole_material: str = Field(..., description="Material of the sole (e.g., Rubber, EVA, PU)")
    lining_material: Optional[str] = Field(None, description="Material of the inner lining (e.g., Mesh, Foam, Textile)")
    insole_material: Optional[str] = Field(None, description="Material of the insole for cushioning (e.g., Memory Foam, Leather)")
    durability_rating: Optional[float] = Field(None, description="Score indicating the expected durability of the footwear")
    waterproof: Optional[bool] = Field(None, description="Whether the footwear is waterproof or water-resistant")

    # Design Features
    toe_shape: Optional[str] = Field(None, description="Shape of the toe box (e.g., Round, Pointed, Square)")
    heel_type: Optional[str] = Field(None, description="Type of heel (e.g., Flat, Wedge, Stiletto, Block)")
    heel_height: Optional[str] = Field(None, description="Height of the heel (e.g., Low, Medium, High)")
    fastening_type: Optional[str] = Field(None, description="Type of fastening (e.g., Laces, Velcro, Slip-On)")
    sole_type: Optional[str] = Field(None, description="Type of sole (e.g., Flat, Treaded, Cushioned)")
    ankle_height: Optional[str] = Field(None, description="Height of the footwear around the ankle (e.g., Low-Cut, Mid-Cut, High-Cut)")

    # Functionality and Context
    occasion: Optional[str] = Field(None, description="Occasion where the footwear is suitable (e.g., Casual, Formal, Sports)")
    activity_type: Optional[str] = Field(None, description="Activity the footwear is designed for (e.g., Running, Hiking, Office Wear)")
    seasonal_suitability: Optional[List[str]] = Field(None, description="Seasons where the footwear is relevant (e.g., Winter, Summer)")
    climate_suitability: Optional[str] = Field(None, description="Climate suitability (e.g., Wet, Dry, Snow)")
    comfort_level: Optional[str] = Field(None, description="Perceived comfort of the footwear (e.g., High, Medium, Low)")
    arch_support: Optional[str] = Field(None, description="Type of arch support (e.g., Neutral, High, Flat)")

    # Trend and Aesthetic Features
    trend_tags: Optional[List[str]] = Field(None, description="Trend associations (e.g., Retro Sneakers, Athleisure, Minimalist)")
    cultural_influence: Optional[str] = Field(None, description="Cultural or regional inspiration (e.g., Italian Leather, Streetwear)")
    historical_inspiration: Optional[str] = Field(None, description="Historical influence (e.g., '90s Retro, Vintage Boots)")

    # Compatibility
    complementary_items: Optional[List[str]] = Field(None, description="Suggested items that pair well with this footwear (e.g., Jeans, Sportswear)")
    recommended_color_pairs: Optional[List[str]] = Field(None, description="Colors that pair well with the footwear")
    accessory_recommendations: Optional[List[str]] = Field(None, description="Suggested accessories (e.g., Shoe Bags, Socks)")

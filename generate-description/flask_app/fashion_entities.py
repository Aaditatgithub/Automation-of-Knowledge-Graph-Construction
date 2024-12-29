from pydantic import BaseModel
from typing import List, Optional, Dict

class FashionEntity(BaseModel):
    name: str  # Name of the product (e.g., "T-Shirts", "Sneakers")
    description: Optional[str]  # Description of the product
    attributes: Optional[Dict[str, str]]  # Additional generic attributes
    dynamicTrends: Optional[Dict[str, str]]  # Trends with phases (e.g., {"Athleisure": "Emerging"})

class Apparel(FashionEntity):
    material: List[str]  # Fabric material (e.g., "Cotton", "Polyester", "Silk")
    fit: Optional[List[str]]  # Fit type (e.g., "Slim", "Regular", "Oversized")
    pattern: Optional[List[str]]  # Patterns (e.g., "Solid", "Striped", "Floral")
    sleeveType: Optional[List[str]]  # Sleeve types (e.g., "Full Sleeve", "Sleeveless")
    neckline: Optional[List[str]]  # Neckline types (e.g., "V-Neck", "Round Neck")
    hemline: Optional[List[str]]  # Hemlines (e.g., "Straight", "Asymmetrical")
    length: Optional[List[str]]  # Length (e.g., "Mini", "Midi", "Maxi")
    occasion: Optional[List[str]]  # Suitable occasions (e.g., "Casual", "Formal")
    seasonality: Optional[List[str]]  # Seasonal relevance (e.g., "Summer", "Winter")
    gender: Optional[List[str]]  # Targeted gender (e.g., "Men", "Women", "Unisex")
    careInstructions: Optional[List[str]]  # Washing/care instructions (e.g., "Dry Clean Only")
    specialFeatures: Optional[List[str]]  # Unique features (e.g., "Moisture Wicking", "Stretchable")

class Footwear(FashionEntity):
    material: List[str]  # Shoe material (e.g., "Leather", "Rubber", "Synthetic")
    soleType: Optional[List[str]]  # Sole type (e.g., "Rubber", "Foam", "EVA")
    closureType: Optional[List[str]]  # Closure mechanism (e.g., "Laces", "Velcro", "Slip-On")
    heelHeight: Optional[List[str]]  # Heel height (e.g., "Flat", "Mid", "High")
    fitType: Optional[List[str]]  # Fit type (e.g., "Regular", "Wide")
    occasion: Optional[List[str]]  # Suitable occasions (e.g., "Casual", "Formal", "Sports")
    waterResistance: Optional[List[str]]  # Water resistance level (e.g., "Waterproof", "Water-Resistant")
    weight: Optional[str]  # Weight category (e.g., "Lightweight", "Medium", "Heavy")
    durability: Optional[str]  # Durability rating (e.g., "High", "Medium", "Low")
    specialFeatures: Optional[List[str]]  # Unique features (e.g., "Shock Absorbent", "Breathable")

class Accessories(FashionEntity):
    material: List[str]  # Material (e.g., "Gold", "Silver", "Leather")
    gemstoneType: Optional[List[str]]  # Gemstones used (e.g., "Diamond", "Ruby", "Sapphire")
    weight: Optional[str]  # Weight category (e.g., "Light", "Medium", "Heavy")
    style: Optional[List[str]]  # Styles (e.g., "Boho", "Minimalist", "Classic")
    functionality: Optional[List[str]]  # Functionality (e.g., "Health Tracker", "Chronograph")
    claspType: Optional[List[str]]  # Clasp mechanism (e.g., "Buckle", "Hook", "Magnetic")
    size: Optional[str]  # Size (e.g., "Adjustable", "One Size")
    waterResistance: Optional[str]  # Water resistance (e.g., "Yes", "No")
    specialFeatures: Optional[List[str]]  # Unique features (e.g., "Smart Features", "Glow in the Dark")

class HomeDecor(FashionEntity):
    material: List[str]  # Material (e.g., "Wood", "Metal", "Glass")
    dimensions: Optional[Dict[str, str]]  # Dimensions (e.g., {"Length": "50cm", "Width": "20cm"})
    weight: Optional[str]  # Weight category (e.g., "Light", "Medium", "Heavy")
    color: Optional[List[str]]  # Available colors (e.g., "White", "Black", "Beige")
    functionality: Optional[List[str]]  # Functionality (e.g., "Adjustable Height", "Storage")
    careInstructions: Optional[List[str]]  # Care instructions (e.g., "Wipe Clean Only")
    style: Optional[List[str]]  # Styles (e.g., "Modern", "Rustic", "Industrial")
    specialFeatures: Optional[List[str]]  # Unique features (e.g., "Eco-Friendly", "Smart Lighting")

from pydantic import BaseModel, Field
from typing import List, Optional

class Apparel(BaseModel):
    # Visual Features
    primary_color: str = Field(..., description="Dominant color of the apparel")
    secondary_colors: Optional[List[str]] = Field(None, description="Secondary or accent colors")
    pattern: Optional[str] = Field(None, description="Pattern design (e.g., Floral, Stripes, Solid)")
    texture: Optional[str] = Field(None, description="Texture or surface quality (e.g., Glossy, Matte, Rough)")
    silhouette: Optional[str] = Field(None, description="Overall silhouette or shape of the apparel (e.g., A-Line, Straight)")
    decoration_details: Optional[List[str]] = Field(None, description="Decorative elements (e.g., Embroidery, Sequins, Lace)")

    # Material and Construction
    fabric_type: str = Field(..., description="Material or fabric of the apparel (e.g., Cotton, Silk, Denim)")
    fabric_composition: Optional[str] = Field(None, description="Detailed fabric breakdown (e.g., 60% Cotton, 40% Polyester)")
    fabric_weight: Optional[str] = Field(None, description="Weight classification of the fabric (e.g., Lightweight, Heavyweight)")
    construction: Optional[str] = Field(None, description="Construction details (e.g., Knit, Woven, Non-Woven)")

    # Style and Aesthetic Attributes
    fit: Optional[str] = Field(None, description="Fit of the apparel (e.g., Slim, Relaxed, Oversized)")
    length: Optional[str] = Field(None, description="Length of the apparel (e.g., Mini, Midi, Maxi, Ankle-Length)")
    neckline: Optional[str] = Field(None, description="Style of the neckline (e.g., V-Neck, Round Neck, Halter)")
    sleeve_type: Optional[str] = Field(None, description="Type of sleeves (e.g., Sleeveless, Bell Sleeve, Full Sleeve)")
    hemline: Optional[str] = Field(None, description="Hemline style (e.g., Asymmetrical, Straight, Flared)")
    closure_type: Optional[str] = Field(None, description="Type of closure (e.g., Zipper, Buttons, Tie)")
    layering_potential: Optional[bool] = Field(None, description="Whether the apparel is suitable for layering")
    
    # Functional and Contextual Features
    occasion: Optional[str] = Field(None, description="Occasion where the apparel is suitable (e.g., Casual, Formal, Party)")
    seasonal_relevance: Optional[List[str]] = Field(None, description="Seasons when the apparel is most relevant (e.g., Spring, Winter)")
    climate_suitability: Optional[str] = Field(None, description="Climate suitability (e.g., Hot, Cold, Humid)")
    comfort_level: Optional[str] = Field(None, description="Perceived comfort of the apparel (e.g., High, Medium, Low)")

    # Trend and Cultural Features
    trend_tags: Optional[List[str]] = Field(None, description="Trend associations (e.g., Y2K Revival, Boho Chic)")
    cultural_influence: Optional[str] = Field(None, description="Cultural or regional inspiration (e.g., Indian Ethnic, Parisian Chic)")
    historical_inspiration: Optional[str] = Field(None, description="Historical fashion influence (e.g., '70s Retro, Victorian)")

    # Compatibility Features
    complementary_items: Optional[List[str]] = Field(None, description="Suggested items that pair well with this apparel")
    recommended_color_pairs: Optional[List[str]] = Field(None, description="Colors that pair well with the apparel")
    accessory_recommendations: Optional[List[str]] = Field(None, description="Suggested accessories (e.g., Belts, Scarves, Hats)")



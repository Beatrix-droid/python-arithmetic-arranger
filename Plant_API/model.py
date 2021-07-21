from pydantic import BaseModel
from typing import Optional



class Plant(BaseModel):
		latin_name: str
		common_name: str
		edible_parts: str
		leaf_image: str
		flower_image: str
		fruit_or_seed_image: str
		bark_or_stem_image: str

#creating a plant class that would allow one to update just certain parameters of the plants,
#without entering all the details of a plant each time.

class Update_Plant(BaseModel):
	latin_name: Optional[str] = None
	common_name: Optional[str] = None
	edible_parts: Optional[str] = None
	leaf_image: Optional[str] = None
	flower_image: Optional[str] = None
	fruit_or_seed_image: Optional[str] = None
	bark_or_stem_image: Optional[str] = None
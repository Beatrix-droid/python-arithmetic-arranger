from model import Plant
from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()


from database import (
fetch_one_latin_name_plant,
fetch_one_common_name_plant,
fetch_all_plants,
update_plant,
create_plant,
delete_plant
)


plant_database = {}


#creating the root directory of the plant api

@app.get("/")
def home():
	return {"Welcome to the Uk": "Edible Wild plants API"}



#adding new plants to the database

@app.post("/create-plant/plant", response_model=Plant)
async def create_plant( plant: Plant):
	response = await create_plant(plant.dict())
	if response:
		return response
	raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something went wrong")


#Get requests to search plants their id, latin name, and common name

@app.get("/plants")
async def get_all_plants():
	response = await fetch_all_plants()
	return response


@app.get("/get-by-common-name", response_model=Plant)
async def get_common_name(common_name):
	response = await fetch_one_common_name_plant(common_name)
	if response:
		return response
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no plant with this common name")


@app.get("/get-by-Latin-name", response_model=Plant)
async def get_latin_name(latin_name):
	response = await fetch_one_latin_name_plant(latin_name)
	if response:
		return response
	raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no plant with this latin name")


#updating information in the database

@app.put("/update-plant/{plant_id}")
async def update_plant(plant_id: int, plant: Update_Plant):
	if plant_id not in plant_database:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exist")

	if plant.latin_name != None:
		plant_database[plant_id].latin_name = plant.latin_name

	if plant.common_name != None:
		plant_database[plant_id].latin_name = plant.common_name

	if plant.leaf_image != None:
		plant_database[plant_id].leaf_image = plant.leaf_image

	if plant.flower_image != None:
		plant_database[plant_id].flower_image = plant.flower_image

	if plant.fruit_or_seed_image != None:
		plant_database[plant_id].fruit_or_seed_image = plant.fruit_or_seed_image

	if plant.bark_or_stem_image != None:
		plant_database[plant_id].bark_or_stem_image = plant.bark_or_stem_image

	return plant_database[plant_id]


#deleting plants from the database by plant id, latin name and common name:

@app.delete("/delete-by-plant-ID")
async def delete_plant(plant_id: int = Query(..., description="The Id of the plant to delete", gt = 0)):
		if plant_id not in plant_database:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exist")
		del plant_database[plant_id]
		raise HTTPException(status_code=status.HTTP_200_OK, detail="Success Plant was deleted")


@app.delete("/delete-plant/{latin_name}")
async def delete_plant(latin_name: str = Path(None, description="The latin name of the plant you'd like to delete")):
		for plant_id in plant_database:
			if plant_id[plant_id].latin_name not in plant_database:
				raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Latin name does not exist")

			del plant_database[plant_id]
			raise HTTPException(status_code=status.HTTP_200_OK, detail="Success Plant was deleted")



@app.delete("/delete-plant/{common_name}")
async def delete_plant(common_name: str, plant: Plant):
		for plant_id in plant_database:
			if plant_id[plant_id].common_name not in plant_database:
				raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Common name does not exist")
			del plant_database[plant_id]
			raise HTTPException(status_code=status.HTTP_200_OK, detail="Success Plant was deleted")
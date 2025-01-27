from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DishPayload(BaseModel):
    dish_name: str
    dish_type: str
    budget: int

@app.post("/restaurant/")
async def get_restaurant(request: DishPayload):
    """
    Returns suitable restaurants based on dish name, type, and budget.
    """

    # Dummy restaurant data
    restaurants = {
        "Pizza Hut": {"dishes": ["Pizza", "Pasta", "Garlic Bread"], "type": "veg/non-veg", "budget": 300},
        "KFC": {"dishes": ["Chicken Burger", "Fries", "Chicken Popcorn"], "type": "non-veg", "budget": 200},
        "Subway": {"dishes": ["Sandwich", "Salad", "Wrap"], "type": "veg/non-veg", "budget": 250},
        "Dominos": {"dishes": ["Pizza", "Garlic Bread", "Taco"], "type": "veg/non-veg", "budget": 400},
        "Saravana Bhavan": {"dishes": ["Dosa", "Idli", "Vada"], "type": "veg", "budget": 150},
        "Paradise": {"dishes": ["Biryani", "Kebabs"], "type": "non-veg", "budget": 350},
    }

    suitable_restaurants = []
    # Find suitable restaurants based on criteria
    for restaurant, details in restaurants.items():
        if request.dish_name.lower() in [dish.lower() for dish in details["dishes"]]:
            if request.dish_type.lower() in details["type"].lower():
                if request.budget >= details["budget"]:
                    suitable_restaurants.append(restaurant)

    # Return suitable restaurants or a default message
    if suitable_restaurants:
        return {"restaurants": suitable_restaurants}
    else:
        return {"message": "No suitable restaurants found."}
    

# curl -X POST 'http://127.0.0.1:8000/restaurant/' -H "Content-Type: application/json" -d '{"dish_name": "Pizza", "dish_type":"veg", "budget": 350}'
from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s -%(message)s')
LOGGER = logging.getLogger(__name__)

app = FastAPI()

class DishPayload(BaseModel):
    dish_name: str
    dish_type: str
    budget: int

class RestaurantDishesResponse(BaseModel):
    restaurants: dict[str, list[str]]

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
    


@app.get("/privacy")
async def privacy_policy():
   """
   Endpoint for the privacy policy.
   Returns:
       str: The privacy policy text.
   """
   policy_text = """
   This is a sample privacy policy.
   We may collect some information from you, such as:
   - Your name
   - Your email address
   - Your usage data
   We will use this information to:
   - Provide you with our services
   - Improve our services
   - Communicate with you
   We will not share your personal information with third parties, except as required by law.
   You have the right to access, update, and delete your personal information.
   If you have any questions about our privacy policy, please contact us.
   """
   return policy_text

@app.post("/restaurant/v2/", response_model=RestaurantDishesResponse)
async def get_dishes(request: DishPayload):
    """
    Returns suitable restaurantsand available dishes based on dish name, type, and budget.
    """

    LOGGER.info(f"Request Payload is: {request}")

    df = pd.read_csv('restaurant_dataset.csv')
    # Filter the DataFrame based on the input parameters
    import pdb; pdb.set_trace()
    filtered_df = df[
        (df['dish_category'] == request.dish_name) &
        (df['dish_type'] == request.dish_type) &
        (df['budget'] <= request.budget)
    ]

    LOGGER.info(f"Dataframe Created from the restaurants dataset.")
    # Check if any restaurants match the criteria
    if filtered_df.empty:
        raise HTTPException(status_code=404, detail="No matching restaurants found")

    # Get the first matching restaurant and dish type
    # Group by restaurant name and get list of dishes
    restaurant_dishes = filtered_df.groupby('restaurant_name')['dish_name'].apply(list).to_dict()

    LOGGER.info(f"Returning restaurants and dishes: {restaurant_dishes}")
    return {"restaurants": restaurant_dishes}
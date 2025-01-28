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

# curl -X POST 'http://127.0.0.1:8000/restaurant/' -H "Content-Type: application/json" -d '{"dish_name": "Pizza", "dish_type":"veg", "budget": 350}'
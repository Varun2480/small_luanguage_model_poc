import pandas as pd
import numpy as np

# Define categories and their corresponding dish names (5-10 options each)
dish_data = {
    'Pizza': ['Classic Margherita', 'Paneer Tikka Pizza', 'Chicken Tikka Pizza', 'Veggie Supreme', 'Pepperoni Pizza', 'Hawaiian Pizza', 'BBQ Chicken Pizza', 'Mushroom Pizza'],
    'Burger': ['Chicken Burger', 'Veg Overload Burger', 'Cheese Burger', 'Bacon Burger', 'Fish Burger', 'Veggie Burger', 'Lamb Burger'],
    'Pasta': ['Arrabiata Pasta', 'White Sauce Pasta', 'Pesto Pasta', 'Carbonara', 'Alfredo', 'Lasagna'],
    'Sandwich': ['Club Sandwich', 'Grilled Cheese Sandwich', 'BLT Sandwich', 'Chicken Sandwich', 'Veg Sandwich', 'Tuna Sandwich'],
    'Salad': ['Chicken Salad', 'Veg Salad', 'Greek Salad', 'Caesar Salad', 'Caprese Salad', 'Cobb Salad'],
    'Wrap': ['Paneer Wrap', 'Chicken Wrap', 'Falafel Wrap', 'Veggie Wrap', 'Shawarma Wrap', 'Burrito'],
    'Taco': ['Veg Taco', 'Non-veg Taco', 'Fish Taco', 'Shrimp Taco', 'Beef Taco', 'Chicken Taco'],
    'Dosa': ['Masala Dosa', 'Plain Dosa', 'Rava Dosa', 'Onion Dosa', 'Mysore Masala Dosa', 'Paper Dosa'],
    'Idli': ['Rava Idli', 'Idli with Chutney', 'Idli with Sambar', 'Fried Idli', 'Steamed Idli'],
    'Vada': ['Medu Vada', 'Sambar Vada', 'Masala Vada', 'Onion Vada', 'Dahi Vada'],
    'Biryani': ['Chicken Biryani', 'Mutton Biryani', 'Veg Biryani', 'Fish Biryani', 'Prawn Biryani', 'Egg Biryani'],
    'Kebabs': ['Seekh Kebabs', 'Chicken Kebabs', 'Paneer Tikka', 'Reshmi Kebab', 'Galouti Kebab', 'Hara Bhara Kebab']
}

dish_types = ['veg', 'non-veg']
budgets = [100, 150, 200, 250, 300, 350, 400, 450, 500]

# Create a list to store the data
data = []

# Generate 100 unique entries
for i in range(100):
    dish_category = np.random.choice(list(dish_data.keys()))
    dish_name = np.random.choice(dish_data[dish_category])
    dish_type = np.random.choice(dish_types)
    budget = np.random.choice(budgets)
    
    data.append([dish_category, dish_name, dish_type, budget])

# Create the DataFrame
df = pd.DataFrame(data, columns=['dish_category', 'dish_name', 'dish_type', 'budget'])

restaurant_prefixes = {
    'Pizza': ['Pizza Hut', 'Dominos', 'Papa Johns', "Little Italy"],
    'Burger': ['Burger King', 'McDonald\'s', 'Wendy\'s', "In-N-Out Burger"],
    'Pasta': ['Olive Garden', 'Fazoli\'s', 'The Cheesecake Factory', "Romano's Macaroni Grill"],
    'Sandwich': ['Subway', 'Quiznos', 'Panera Bread', "Jersey Mike's Subs"],
    'Salad': ['Sweetgreen', 'Chopt Creative Salad Co.', 'Saladworks', "Just Salad"],
    'Wrap': ['Chipotle', 'Moe\'s Southwest Grill', 'Freebirds World Burrito', "Qdoba Mexican Eats"],
    'Taco': ['Taco Bell', 'Del Taco', 'Baja Fresh', "Chronic Tacos"],
    'Dosa': ['Saravana Bhavan', 'Madras Cafe', 'Dosa Hut', "Udupi Sri Krishna Vilas"],
    'Idli': ['Saravana Bhavan', 'Madras Cafe', 'Idli Factory', "Dakshin"],
    'Vada': ['Saravana Bhavan', 'Madras Cafe', 'Vada Pav King', "Vinayaka Mylari"],
    'Biryani': ['Paradise Biryani', 'Bawarchi', 'Behrouz Biryani', "Hyderabad House"],
    'Kebabs': ['Karim\'s', 'Al Jawahar', 'Barbeque Nation', "The Great Kabab Factory"]
}

# Function to generate a restaurant name based on dish category
def generate_restaurant_name(dish_category: str):
    prefixes = restaurant_prefixes.get(dish_category, ['Restaurant'])  # Default to 'Restaurant' if category not found
    return np.random.choice(prefixes)

# Apply the function to create the 'restaurant_name' column
df['restaurant_name'] = df['dish_category'].apply(generate_restaurant_name)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file (optional)
df.to_csv('restaurant_dataset.csv', index=False)
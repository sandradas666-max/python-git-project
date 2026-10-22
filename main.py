

from tripdata import get_trip
from datetime import datetime
import json

# Create a list of trip dictionaries
trips = [
    get_trip("Paris", "15-05-2023", "Visited the Eiffel Tower"),
    get_trip("London", "20-06-2024", "Explored the museums"),
    get_trip("Tokyo", "10-01-2025", "Tried local Japanese food")
]

# Convert each date string into a date object
for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y").date()

    # Format the date as Month Day, Year
    trip["date"] = date_object.strftime("%B %d, %Y")

# Convert the list of dictionaries into a JSON string
json_string = json.dumps(trips, indent=4)

# Print the JSON string
print(json_string)

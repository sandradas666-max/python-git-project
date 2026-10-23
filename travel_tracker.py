from tracker import create_record
from datetime import datetime
import json

# Create a list of travel records
trips = [
    create_record("Paris", "Visited the Eiffel Tower", "15-05-2023"),
    create_record("London", "Explored the museums", "20-06-2024"),
    create_record("Tokyo", "Tried Japanese food", "10-01-2025"),
]

# Convert date strings into readable format
for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_object.strftime("%B %d, %Y")

# Convert the list into a JSON string
json_data = json.dumps(trips, indent=4)
print("JSON Data:")
print(json_data)

# Parse JSON back into a Python object
python_data = json.loads(json_data)

# Display each record on a separate line
print("\nTravel Records:")
for record in python_data:
    print(record)

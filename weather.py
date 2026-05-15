import json
from datetime import datetime
import requests

latitude = 38.44
longitude = -0.43

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}"
    "&hourly=temperature_2m"
)

response = requests.get(url)
data = response.json()

temperatures = data["hourly"]["temperature_2m"]

print("Temperatures fetched successfully!")
print(temperatures[:10])
# Calculate max, min, average
max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)

print("\nStatistics:")
print("Max temperature:", max_temp)
print("Min temperature:", min_temp)
print("Average temperature:", avg_temp)
# Create results dictionary
results = {
    "max_temperature": max_temp,
    "min_temperature": min_temp,
    "average_temperature": avg_temp
}

# Create filename with today's date
today = datetime.now().strftime("%Y%m%d")
filename = f"temp_{today}.json"

# Save JSON file
with open(filename, "w") as f:
    json.dump(results, f, indent=4)

print("\nJSON file created:", filename)
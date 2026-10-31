
# Environmental Monitoring Data Analyzer

# Nested list containing AQI readings
stations = [
    ["Station 1", [35, 45, 50, 40]],
    ["Station 2", [65, 75, 85, 90]],
    ["Station 3", [110, 125, 135, 145]],
    ["Station 4", [160, 175, 185, 195]]
]

# Function to classify environmental readings
def classify_aqi(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    else:
        return "Unhealthy"

# Display report
print("ENVIRONMENTAL MONITORING REPORT")
print("------------------------------------------")

for station in stations:

    name = station[0]
    readings = station[1]

    # Calculate average, maximum and minimum
    average = sum(readings) / len(readings)
    maximum = max(readings)
    minimum = min(readings)

    # Classify based on average
    category = classify_aqi(average)

    # Display results
    print("\nStation:", name)
    print("Readings:", readings)
    print("Average AQI:", round(average, 2))
    print("Maximum AQI:", maximum)
    print("Minimum AQI:", minimum)
    print("Environmental Condition:", category)

print("\nAnalysis Completed.")


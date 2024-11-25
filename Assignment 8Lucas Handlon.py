def list_unique_cities_by_date(filepath):
    # Open the CSV file and read its lines
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: The file was not found.")
        return

    # Check if the file has at least a header and some data
    if len(lines) < 2:
        print("Error: The file is empty or does not have sufficient data.")
        return

    # Read the header line and split it, cleaning up extra spaces or quotes
    header = [h.strip().strip('"') for h in lines[0].strip().split(',')]

    # Get indices for necessary columns with error handling
    try:
        origin_city_index = header.index("Origin_city")
        destination_city_index = header.index("Destination_city")
        fly_date_index = header.index("Fly_date")
    except ValueError:
        print("Error: One or more required columns ('Origin_city', 'Destination_city', 'Fly_date') are not found in the file.")
        return

    # Dictionary to hold unique cities for each fly date
    cities_by_date = {}

    # Iterate through each line in the file, starting from the second line (skip the header)
    for line in lines[1:]:
        parts = [p.strip().strip('"') for p in line.strip().split(',')]

        # Ensure the line has enough columns to avoid IndexError
        if len(parts) > max(origin_city_index, destination_city_index, fly_date_index):
            try:
                origin_city = parts[origin_city_index]
                destination_city = parts[destination_city_index]
                fly_date = parts[fly_date_index]
            except IndexError:
                # Skip lines with missing data
                continue

            # Add the cities to the appropriate fly_date entry
            if fly_date not in cities_by_date:
                cities_by_date[fly_date] = {"origin_cities": set(), "destination_cities": set()}

            cities_by_date[fly_date]["origin_cities"].add(origin_city)
            cities_by_date[fly_date]["destination_cities"].add(destination_city)

    # Write the results
    for date, cities in cities_by_date.items():
        print(f"Fly Date: {date}")
        print("  Unique Origin Cities:")
        for city in cities["origin_cities"]:
            print(f"    - {city}")
        print("  Unique Destination Cities:")
        for city in cities["destination_cities"]:
            print(f"    - {city}")

# Filepath to your CSV
filepath = "/Users/lucashandlon/Desktop/Information Infrastructure/Airports2.csv"
list_unique_cities_by_date(filepath)

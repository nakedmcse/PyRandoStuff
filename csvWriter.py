import csv

# Define the headers
headers = ['companyName', 'fullName', 'contactNumber', 'numberE164', 'plan', 'email', 'address_premises', 'address_street', 'address_town', 'address_county', 'address_postcode']

# Open a CSV file for writing
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for i in range(1, 501):
        row = [
            f"company_{i}",
            f"full_name_{i}",
            f"{100000+i}",
            f"{200000+i}",
            f"phoneline_plus",
            f"name{i}@example.com",
            f"premises{i}",
            f"street{i}",
            f"town{i}",
            f"county{i}",
            f"postcode{i}"
        ]
        writer.writerow(row)

print("CSV file generated successfully.")

##### Business_sentiment  #####
#
# import json
# import csv
#
# # Path to your JSON file
# json_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/business_sentiments.json'  # Replace with your JSON file path
# csv_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/business_sentiments.csv'      # The CSV file that will be created
#
# # Load JSON data
# try:
#     with open(json_file_path, 'r') as json_file:
#         data = json.load(json_file)
#     print("JSON data loaded successfully.")
# except Exception as e:
#     print(f"Error loading JSON data: {e}")
#     exit()
#
# # Write data to CSV
# try:
#     with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['business_id', 'sentiment_score'])  # Writing header
#
#         for business_id, sentiment_score in data.items():
#             writer.writerow([business_id, sentiment_score])
#
#     print("CSV file created successfully.")
# except Exception as e:
#     print(f"Error writing to CSV: {e}")


##### Reviews #####
#
# import json
# import csv
#
# # Path to your JSON file
# json_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001_CA.json'  # Replace with your JSON file path
# csv_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001_CA.csv'      # The CSV file that will be created
#
# # Read and parse the JSON data
# data = []
# try:
#     with open(json_file_path, 'r') as json_file:
#         for line in json_file:
#             data.append(json.loads(line))
#     print("JSON data loaded successfully.")
# except Exception as e:
#     print(f"Error loading JSON data: {e}")
#     exit()
#
# # Write data to CSV
# try:
#     with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file)
#
#         # Writing header based on the keys of the first JSON object
#         writer.writerow(data[0].keys())
#
#         for item in data:
#             writer.writerow(item.values())
#
#     print("CSV file created successfully.")
# except Exception as e:
#     print(f"Error writing to CSV: {e}")


##### Business Details #####

import json
import csv

json_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business_CA.json'  # Replace with your JSON file path
csv_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business_CA.csv'      # The CSV file that will be created

# Function to flatten nested JSON
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# Read and parse the JSON data
data = []
all_keys = set()
try:
    with open(json_file_path, 'r') as json_file:
        for line in json_file:
            flattened = flatten_json(json.loads(line))
            data.append(flattened)
            all_keys.update(flattened.keys())
    print("JSON data loaded successfully.")
except Exception as e:
    print(f"Error loading JSON data: {e}")
    exit()

# Write data to CSV
try:
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=all_keys)
        writer.writeheader()

        for item in data:
            writer.writerow(item)

    print("CSV file created successfully.")
except Exception as e:
    print(f"Error writing to CSV: {e}")

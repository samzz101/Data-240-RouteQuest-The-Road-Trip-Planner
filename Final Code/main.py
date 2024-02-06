import json
file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business.json'

# Read the file line by line
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            # Parse each line as a separate JSON object
            data = json.loads(line)
            print(data)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON on line: {line}")
            print(f"Error: {e}")

input_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business.json'
output_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business_CA.json'

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r', encoding='utf-8') as input_file, \
     open(output_file_path, 'w', encoding='utf-8') as output_file:

    # Process each line (which represents a JSON object) in the input file
    for line in input_file:
        try:
            data = json.loads(line)
            # Check if the 'state' key is 'CA'
            if data.get('state') == 'CA':
                # Write the JSON object to the output file
                output_file.write(json.dumps(data) + '\n')  # Adds a newline character to separate JSON objects
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON on line: {line}")
            print(f"Error: {e}")

print(f"File with CA state entries has been created at: {output_file_path}")

#
# import json
#
# # Replace these paths with your actual file paths
# businesses_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business_CA.json'
# reviews_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001.json'
# output_reviews_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001_CA.json'
#
# # Step 1: Create a set of "CA" business IDs
# ca_business_ids = set()
# with open(businesses_file_path, 'r', encoding='utf-8') as businesses_file:
#     for line in businesses_file:
#         business = json.loads(line)
#         ca_business_ids.add(business['business_id'])
#
# # Check the number of CA businesses loaded
# print(f"Number of CA businesses loaded: {len(ca_business_ids)}")
#
# # Step 2: Filter out reviews that match the "CA" business IDs
# ca_reviews = []
# with open(reviews_file_path, 'r', encoding='utf-8') as reviews_file:
#     for line in reviews_file:
#         review = json.loads(line)
#         if review['business_id'] in ca_business_ids:
#             ca_reviews.append(review)
#
# # Check the number of matching reviews found
# print(f"Number of reviews for CA businesses: {len(ca_reviews)}")
#
# # Step 3: Sort the reviews by business ID
# ca_reviews.sort(key=lambda review: review['business_id'])
#
# # Step 4: Write the filtered and sorted reviews to a new JSON file
# with open(output_reviews_file_path, 'w', encoding='utf-8') as output_reviews_file:
#     for review in ca_reviews:
#         output_reviews_file.write(json.dumps(review) + '\n')
#
# print(f"File with reviews from CA businesses has been created at: {output_reviews_file_path}")


#Filtering CA based business reviews into a new file

# import json
# from collections import defaultdict
#
# # Replace these paths with your actual file paths
# business_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business.json'
# reviews_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001.json'
#
# # Step 1: Create a dictionary mapping business IDs to states
# business_states = {}
# with open(business_file_path, 'r', encoding='utf-8') as business_file:
#     for line in business_file:
#         business = json.loads(line)
#         business_states[business['business_id']] = business['state']
#
# # Step 2: Count the reviews for each state
# state_review_counts = defaultdict(int)
# with open(reviews_file_path, 'r', encoding='utf-8') as reviews_file:
#     for line in reviews_file:
#         review = json.loads(line)
#         state = business_states.get(review['business_id'])
#         if state:
#             state_review_counts[state] += 1
#
# # Step 3: Print out the count of reviews for each state
# for state, count in state_review_counts.items():
#     print(f"State: {state}, Number of reviews: {count}")
#

# import json
#
# # Replace these paths with your actual file paths
# business_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_dataset/yelp_academic_dataset_business.json'
# reviews_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001.json'
# output_reviews_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001_CA.json'
#
# # Step 1: Create a set of business IDs located in CA
# ca_business_ids = set()
# with open(business_file_path, 'r', encoding='utf-8') as business_file:
#     for line in business_file:
#         business = json.loads(line)
#         if business['state'] == 'CA':
#             ca_business_ids.add(business['business_id'])
#
# # Verify we have business IDs collected
# print(f"Number of CA businesses collected: {len(ca_business_ids)}")
#
# # Step 2: Filter out reviews for CA businesses
# ca_reviews = []
# with open(reviews_file_path, 'r', encoding='utf-8') as reviews_file:
#     for line in reviews_file:
#         review = json.loads(line)
#         if review['business_id'] in ca_business_ids:
#             ca_reviews.append(review)
#
# # Verify we have reviews collected
# print(f"Number of reviews for CA businesses: {len(ca_reviews)}")
#
# # Step 3: Sort the reviews by business ID
# ca_reviews.sort(key=lambda review: review['business_id'])
#
# # Step 3: Write the filtered reviews to a new file
# with open(output_reviews_file_path, 'w', encoding='utf-8') as output_file:
#     for review in ca_reviews:
#         output_file.write(json.dumps(review) + '\n')
#
# print(f"File with reviews from CA businesses has been created at: {output_reviews_file_path}")


# # Sentiment Analysis code
# import json
# import nltk
# nltk.download('vader_lexicon')
# from nltk.sentiment import SentimentIntensityAnalyzer
# from collections import defaultdict
#
# # Initialize the SentimentIntensityAnalyzer
# sia = SentimentIntensityAnalyzer()
#
# # Replace with the path to your file containing reviews for CA businesses
# reviews_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/yelp_academic_dataset_review-001_CA.json'
# output_sentiment_file_path = 'C:/Users/Siddharth/Desktop/Data240_datamining_Project/Dataset_test/business_sentiments.json'
#
# # This dictionary will hold the reviews for each business
# business_reviews = defaultdict(list)
#
# # Read the reviews file and aggregate reviews by business
# with open(reviews_file_path, 'r', encoding='utf-8') as reviews_file:
#     for line in reviews_file:
#         review = json.loads(line)
#         business_reviews[review['business_id']].append(review['text'])
#
# # This dictionary will hold the average sentiment score for each business
# business_sentiment_scores = {}
#
# # Perform sentiment analysis for each business
# for business_id, reviews in business_reviews.items():
#     # Aggregate sentiment scores
#     sentiment_scores = [sia.polarity_scores(review)['compound'] for review in reviews]
#     # Calculate the average sentiment score for the business
#     business_sentiment_scores[business_id] = sum(sentiment_scores) / len(sentiment_scores)
#
# # Now business_sentiment_scores contains the average sentiment compound score for each business
# # The compound score is a normalized score between -1 (most extreme negative) and +1 (most extreme positive).
#
# # Optionally, print or save the sentiment scores
# for business_id, sentiment_score in business_sentiment_scores.items():
#     print(f"Business ID: {business_id}, Average Sentiment Score: {sentiment_score}")
# # Write the business sentiment scores to a JSON file
# with open(output_sentiment_file_path, 'w', encoding='utf-8') as output_file:
#     json.dump(business_sentiment_scores, output_file, indent=4)
#
# print(f"Sentiment scores have been written to {output_sentiment_file_path}")

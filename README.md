# Data-240-RouteQuest-The-Road-Trip-Planner

## Introduction
Traveling in a new country presents a unique set of challenges, particularly when it comes to navigating unfamiliar landscapes and identifying must-see attractions. As the trend of turning long road journeys into immersive, full-day experiences grows in popularity, there is a clear need for a solution that can enhance the road trip experience for tourists. Motivated by this demand, the development of a travel suggestion system aims to improve how tourists explore new destinations. By focusing on the departure and arrival points of a journey, this system helps travelers discover the best sights along their chosen routes, transforming their road trips into memorable adventures.

The foundation of this travel suggestion system lies in addressing the unique challenges faced by individuals who migrate to new countries, particularly in terms of navigation and unfamiliarity with local attractions. By leveraging the Open Route Service API, the system recommends strategically located destinations between the start and end points of a trip. Through the seamless integration of navigation features and real-time location data, the system not only provides directions to intriguing spots but also offers suggestions based on distance, potential costs, popularity, and ratings. This comprehensive approach ensures that travelers receive tailored recommendations, enriching their entire road trip experience.

## Methodology
### Data Collection
The data for this project was obtained from GitHub. In total, there were four datasets. In total, there were four datasets. Critical information included in these databases included prices, names, reviews, and ratings of attractions, as well as geographic coordinates, state and country, and pricing information. 
Of the four datasets, two in particular had detailed information about the attractions, such as their latitude and longitude coordinates, the accompanying information about the state and country, and their prices. At the same time, the remaining two datasets contained information critical to user experiences, such as attraction names, reviews, and ratings. These four datasets were combined into two separate datasets during a deliberate preprocessing step. Attraction details were smoothly merged into one dataset to create a comprehensive library of contextual, price, and geographic data. The other dataset balanced opinions and reviews related to various attractions, creating a unified and consolidated dataset.

### Feature Extraction
In the attraction dataset, which includes multiple reviews and ratings for each attraction, two new features, namely 'sentiment' and 'popularity,' were derived based on the reviews and ratings, respectively. The sentiment feature captured the overall sentiment conveyed in the reviews, while the popularity feature reflected the collective rating scores. Following the creation of these new features, an analysis was conducted to observe how the sentiment evolved over time.

### Data Transformation
To standardize the sentiment and popularity scores in the dataset, Z-score normalization was used. A crucial element is the sentiment score, which captures the overall sentiment expressed in user reviews. Meanwhile, the popularity score is an average of the rating scores and serves as a measure of public favor. Z-score normalization, also known as standard score normalization, is a statistical technique that translates data points in terms of their standard deviation from the mean. This procedure yields a distribution with a mean of 0 and a standard deviation of 1. This normalization method properly scaled both the sentiment and popularity scores in the application to fall inside a range of -1 to 1.
The sentiment and popularity scores contributed equally to the analysis by normalizing them in this way, regardless of their original magnitude or distribution. This methodological decision contributed significantly to the robustness and dependability of a data-driven conclusions.

Similarly, with the price column, it starst by extracting values from the CSV file and converting them into a list of floating-point numbers. This step is critical for later data processing. After creating this list, calculate the minimum (min_price) and maximum (max_price) values among these prices, which sets the stage for the normalization step.
The code then starts the normalization step. It processes each row of data sequentially, applying a normalization method to the 'price' value. The price is standardized to a scale of 1 to 5 using the following formula: 1 + (price - min_price) / (max_price - min_price) * 4. This formula is intended to linearly adjust each price so that the least price corresponds to 1 and the greatest price corresponds to 5. As a result, a consistent price scale is created, which improves the data's consistency and comparability, which is an important step in preparing the dataset for further analysis or application within the project. Figure 1 shows the final dataset after data preprocessing.

## Experiments and Results
K-means clustering was employed to group the normalized sentiment and popularity columns, with several values of k tested to identify the most effective clustering. The quality of the clusters was assessed using the Silhouette score, which measures how similar an object is to its own cluster compared to other clusters. To determine the optimal number of clusters, the elbow method was utilized, where the Silhouette score was calculated for each candidate k, helping to identify the point at which increasing k no longer significantly improved clustering quality.

Once the optimal k value was determined, the data was grouped into categories based on the identified clusters. Descriptive labels such as "Bad," "OK," "Good," and "Very Good" were assigned to the sentiment clusters based on the sentiment scores within each cluster. For example, cluster 2, which contained sentiment scores greater than 0.4, was labeled as "Very Good." A similar approach was applied to the popularity data, resulting in categories like "Not Popular," "Popular," and "Very Popular."

#### Popularity as Not Popular, Popular, Very Popular
<img width="620" alt="Screenshot 2024-08-08 at 6 04 33 PM" src="https://github.com/user-attachments/assets/2f5e894e-d6d6-4660-9d6c-3f996201a4f8">  

#### Sentiment as Bad, Ok, Good, Very Good
<img width="599" alt="Screenshot 2024-08-08 at 6 04 42 PM" src="https://github.com/user-attachments/assets/601dfeac-b276-4ada-9c81-289296b6cb98">

#### Sentiment vs Popularity
<img width="613" alt="Screenshot 2024-08-08 at 6 04 14 PM" src="https://github.com/user-attachments/assets/d5341dfb-28a4-4f1b-a974-24fe3157ff3e">

## Recommendation System
The dataset, which has been optimized through extensive pre-processing, serves as the cornerstone for the recommendation engine. The project begins by compiling a list of coordinates for various cities across Canada. This list is used to acquire the corresponding coordinates after receiving the user's input for starting and finishing locations. The OpenRouteService API then uses these coordinates to generate precise route information. This provides street names, starting and ending coordinates (latitude and longitude), distance in meters, and estimated travel time in seconds for each street segment. The resulting data, which is initially in JSON format, is saved carefully into a JSON file. This file is then converted to CSV format for improved usage.
The final dataset includes the precise coordinates of all Points of Interest (POIs), as well as various other features. Calculation of the distance to the POIs, is next,  using these coordinates and the coordinate range of every particular street on the suggested route. In addition, if the user indicates a preference for a specific type of POI, the system generates a curated list of relevant POIs. This output list includes not only the name of each POI but also useful information such as its sentiment type, popularity, and price level. The findings part of the report includes a visual representation of this output, providing a clear and succinct summary of the system's capabilities.

## Results
The system utilizes input parameters such as the starting city, ending city, and category filter. Based on these inputs, it generates a comprehensive list of Points of Interest in Canada. The list includes how people feel about each place (sentiment), how popular they are, and their price level. The resulting output comprises four columns:
* Name: Represents the name of the tour.
* Sentiment: Reflects the average rating of the POI, ranging from "Very Good" to "Bad."
* Popularity: Indicates the relative popularity of the POI, spanning from "Not Popular" to "Very Popular."
* Price Level: Represents the price level of the POI, categorized from "$" to "$$$$$." This structured output format provides users with clear and organized information, aiding in their decision-making process.
<img width="1037" alt="Screenshot 2024-08-08 at 6 10 34 PM" src="https://github.com/user-attachments/assets/a7388fcf-3430-4bbf-b908-8f9de79af978">

## Futurework
### Dataset Augmentation for Robustness
Future improvements include expanding the dataset by adding more Points of Interest (POIs) and their geographic coordinates. This will enhance the stability of the recommendations and broaden the demographic reach.
### User-Specific Data Integration
Plans are in place to incorporate user-specific data into the recommendation algorithms, allowing for more personalized and tailored suggestions, ultimately improving user satisfaction.
### Intuitive User Interface Development
An initiative is underway to design a more intuitive user interface, aimed at enhancing accessibility and providing a seamless, engaging experience for users.

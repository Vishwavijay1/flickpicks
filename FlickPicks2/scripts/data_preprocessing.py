import pandas as pd
import re

def load_and_preprocess_data():
    #dataset path
    dataset_path = 'MoviesLens'
    
    # Load ratings data
    ratings = pd.read_csv(f'{dataset_path}/ratings.csv')
    # Load movies data
    movies = pd.read_csv(f'{dataset_path}/movies.csv')
    # Drop unnecessary columns from ratings
    tags = pd.read_csv(f'{dataset_path}/tags.csv')
    ratings = ratings.drop(columns=['timestamp'])

    """
    print(movies.head())
    print(ratings.head())
    print(movies.info())
    print(ratings.info())

    print(movies.isnull().sum())
    print(ratings.isnull().sum())
    """

    # Since there are no null values, we will further clean the data

    # split genres into lists
    movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

    # Extract year from title
    def extract_year(title):
        match = re.search(r'\((\d{4})\)', title)
        return int(match.group(1)) if match else None

    movies['year'] = movies['title'].apply(extract_year)

    # Remove the year from the title
    movies['title'] = movies['title'].apply(lambda x: re.sub(r'\(\d{4}\)', '', x).strip())
    # Remove the year column from the dataset
    movies = movies.drop(columns=['year'])

    """
    # Group the tags DataFrame by movieId and aggregate the tags into lists
    grouped_tags = tags.groupby('movieId')['tag'].apply(list).reset_index()

    # Merge the movies DataFrame with the grouped tags DataFrame on movieId
    movies_updated = pd.merge(movies, grouped_tags, on='movieId', how='left')

    # Save the resulting DataFrame to the same movies.csv file
    movies_updated.to_csv(f'{dataset_path}/movies.csv', index=False)"""

    
    return ratings, movies

if __name__ == "__main__":
    ratings, movies = load_and_preprocess_data()



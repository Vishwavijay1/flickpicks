import streamlit as st
import pandas as pd
from scripts.recommendation_engine import UserBasedCollaborativeFiltering
from scripts.data_preprocessing import load_and_preprocess_data

def main():
    # Load and preprocess data
    ratings, movies = load_and_preprocess_data()

    # Initialize User-Based Collaborative Filtering model
    ubcf = UserBasedCollaborativeFiltering(ratings)

    # Streamlit app
    st.title('What you might like!')

    st.sidebar.header('User Information')
    userId = st.sidebar.number_input('User ID', min_value=1, max_value=ratings['userId'].max(), value=None)
    num_recommendations = st.sidebar.slider('Number of Recommendations', min_value=1, max_value=20, value=5)

    if st.sidebar.button('Get Recommendations'):
        if userId not in ratings['userId'].values or userId is None:
            st.write('User ID not found. Please enter a valid User ID.')
        else:
            recommendations = ubcf.recommend_movies(userId=userId, num_recommendations=num_recommendations)

            # Create a DataFrame for the recommendations
            recommendations_df = pd.DataFrame(recommendations, columns=['movieId', 'Predicted Rating'])
            recommendations_df['Movie'] = recommendations_df['movieId'].apply(lambda x: movies[movies['movieId'] == x]['title'].values[0])

            # Reorder columns
            recommendations_df = recommendations_df[['Movie', 'Predicted Rating']]
            st.write(f'Top {num_recommendations} movie recommendations for User {userId}:')
            st.dataframe(recommendations_df)

if __name__ == "__main__":
    main()

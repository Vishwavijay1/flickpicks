import streamlit as st
import pandas as pd
from scripts.recommendation_engine import ItemBasedCollaborativeFiltering
from scripts.data_preprocessing import load_and_preprocess_data

def main():
    # Load and preprocess data
    ratings, movies = load_and_preprocess_data()

    # Initialize Item-Based Collaborative Filtering model
    ibcf = ItemBasedCollaborativeFiltering(ratings)

    # Streamlit app
    st.title('Explore Similar Movies')

    st.sidebar.header('Explore')
    input_movie = st.sidebar.text_input('Enter Movie Name')

    if input_movie:
        filtered_movies = movies[movies['title'].str.contains(input_movie, case=False, na=False)]
        movie_titles = filtered_movies['title'].tolist()
        if not movie_titles:
            st.sidebar.write(f'Sorry, no movies found containing "{input_movie}".')
            selected_movie = None
        else:
            selected_movie = st.sidebar.selectbox('Select your choice from the list', movie_titles)
    else:
        selected_movie = None

    num_recommendations = st.sidebar.slider('Number of Recommendations', min_value=1, max_value=20, value=5)

    if st.sidebar.button('Get Recommendations'):
        if input_movie and selected_movie is None:
            st.write(f'Sorry, no movies found containing "{input_movie}".')
        else:
            movieId = movies[movies['title'] == selected_movie]['movieId'].values[0]
            recommendations = ibcf.recommend_movies(movieId=movieId, num_recommendations=num_recommendations)

            # Create a DataFrame for the recommendations
            recommendations_df = pd.DataFrame(recommendations, columns=['movieId', 'Similarity'])
            recommendations_df['Movie'] = recommendations_df['movieId'].apply(lambda x: movies[movies['movieId'] == x]['title'].values[0])
            
            # Reorder columns
            recommendations_df = recommendations_df[['Movie', 'Similarity']]
            st.write(f'Top {num_recommendations} movie recommendations similar to {selected_movie}:')
            st.dataframe(recommendations_df)

if __name__ == "__main__":
    main()

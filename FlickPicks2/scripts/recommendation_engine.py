import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class ItemBasedCollaborativeFiltering:
    def __init__(self, ratings):
        self.ratings = ratings
        self.user_movie_matrix = self.create_user_movie_matrix()
        self.item_similarity_matrix = self.calculate_item_similarity()

    def create_user_movie_matrix(self):
        return self.ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    def calculate_item_similarity(self):
        return cosine_similarity(self.user_movie_matrix.T)

    def recommend_movies(self, movieId, num_recommendations=5):
        # Find similar items
        movie_idx = self.user_movie_matrix.columns.get_loc(movieId)
        similar_movies = self.item_similarity_matrix[movie_idx]
        
        # Get the top N similar items
        similar_movies_indices = similar_movies.argsort()[-(num_recommendations + 1):-1][::-1]
        
        return [(self.user_movie_matrix.columns[i], similar_movies[i]) for i in similar_movies_indices]
    
class UserBasedCollaborativeFiltering:
    def __init__(self, ratings):
        self.ratings = ratings
        self.user_movie_matrix = self.create_user_movie_matrix()

    def create_user_movie_matrix(self):
        return self.ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    
    def get_user_similarity(self):
        return cosine_similarity(self.user_movie_matrix)
    
    def recommend_movies(self, userId, num_recommendations=5):
        user_similarity = self.get_user_similarity()
        user_idx = self.user_movie_matrix.index.get_loc(userId)
        similar_users = user_similarity[user_idx].argsort()[-2::-1]

        recommendations = {}
        for similar_user in similar_users:
            similar_user_id = self.user_movie_matrix.index[similar_user]
            similar_user_ratings = self.ratings[self.ratings['userId'] == similar_user_id]
            for _, row in similar_user_ratings.iterrows():
                if row['movieId'] not in recommendations:
                    recommendations[row['movieId']] = row['rating']
                if len(recommendations) >= num_recommendations:
                    break
            if len(recommendations) >= num_recommendations:
                break
        
        return sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:num_recommendations]


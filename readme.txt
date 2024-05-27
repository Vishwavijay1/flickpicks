# FlickPicks

# Team members
- Harshal Kariya
- Vishwavijay

# College name
- Puducherry Technological University

FlickPicks is a movie recommendation application built using Streamlit. It offers two main functionalities:
- *Explore Similar Movies*: Get movie recommendations based on a selected movie using Item-Based Collaborative Filtering.
- *User Recommendations*: Get personalized movie recommendations for a specific user using User-Based Collaborative Filtering.

## Table of Contents
- [Summary](#summary)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Summary
=======

This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org), a movie recommendation service. It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. This dataset was generated on September 26, 2018.

Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.

The data are contained in the files `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. More details about the contents and use of all these files follows.

This is a *development* dataset. As such, it may change over time and is not an appropriate dataset for shared research results. See available *benchmark* datasets if that is your intent.

This and other GroupLens data sets are publicly available for download at <http://grouplens.org/datasets/>.


## Installation

To run FlickPicks_final locally, follow these steps:

1. *Clone the repository*:
    bash
    git clone https://github.com/UnknownHaK11/FlickPicks_final.git
    cd FlickPicks_final
    

2. *Set up a virtual environment*:
    bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    

3. *Install the required dependencies*:
    bash
    pip install -r requirements.txt
    

## Usage

To start the FlickPicks_final application, run the following command:

bash
streamlit run homepage.py   #or
python -m streamlit run homepage.py


Open your web browser and navigate to http://localhost:8501 to use the application.

### Navigation

- *Home*: The homepage of FlickPicks.
- *Explore Similar Movies*: Enter a movie name to get recommendations based on similar movies.
- *User Recommendations*: Enter a user ID to get personalized movie recommendations.

## Project Structure

plaintext
FlickPicks_final/
│
├── scripts/
│   ├── data_preprocessing.py        # Functions for loading and preprocessing data
│   ├── recommendation_engine.py     # Item and User-Based Collaborative Filtering models
│
├── explore.py                       # Script for "Explore Similar Movies" functionality
├── user.py                          # Script for "User Recommendations" functionality
├── homepage.py                      # Main script for the Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation


## 

Thank you for using FlickPicks! If you have any questions or feedback, please feel free to contact us.
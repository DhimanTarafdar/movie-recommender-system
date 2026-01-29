# Movie Recommender System 🎬

A content-based movie recommendation system built with **Python** and **Machine Learning**. This application suggests five similar movies based on the user's input, leveraging natural language processing (NLP) techniques.

## Live Demo
You can try out the live application here:  
**[Link to your Hugging Face Space]([https://hugging-face-app-link-ekhane-din](https://huggingface.co/spaces/Dhiman22/Movie-Recommender-System))

## Project Overview
This project uses metadata (genres, keywords, cast, and crew) from thousands of movies to find similarities. It uses **Cosine Similarity** to measure the distance between movies in a high-dimensional vector space.

### Key Features:
- **Personalized Recommendations:** Get 5 movie suggestions based on your favorite film.
- **NLP Powered:** Uses `CountVectorizer` to convert text into vectors.
- **Interactive UI:** Simple and clean user interface built with **Streamlit**.

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, Scikit-learn, NLTK
- **Framework:** Streamlit
- **Deployment:** Hugging Face Spaces

## Project Structure
```text
├── app.py                # Streamlit web application code
├── movie_list.pkl        # Processed movie data (Serialized)
├── similarity.pkl        # Cosine similarity matrix (Serialized)
└── requirements.txt      # Project dependencies

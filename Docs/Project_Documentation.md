# Diet Recommendation System - Project Documentation

## Overview

This project is a diet recommendation system that uses a content-based approach with nutritional data and ingredients to recommend recipes. It consists of two main components:

- **Backend**: A FastAPI server that hosts the recommendation model and exposes API endpoints.
- **Frontend**: A Streamlit web application that provides an interactive user interface and consumes the backend API.

---

## Backend (FastAPI)

### Key Files

- `main.py`: The FastAPI application that loads the dataset, handles API requests, and returns recommendations.
- `model.py`: Contains the recommendation logic using scikit-learn.

### main.py Explanation

- Loads the dataset from `Data/dataset.csv` (compressed gzip CSV).
- Defines Pydantic models for request and response validation:
  - `PredictionIn`: Input model with nutrition input (list of 9 floats), optional ingredients list, and optional parameters.
  - `Recipe`: Output model representing a recipe with nutritional info, ingredients, and instructions.
  - `PredictionOut`: Output model wrapping a list of `Recipe` objects.
- Defines two endpoints:
  - `GET /`: Health check endpoint returning `{"health_check": "OK"}`.
  - `POST /predict/`: Accepts nutrition input, ingredients, and parameters; calls the `recommend` function from `model.py` to get recommendations; formats output using `output_recommended_recipes`.
- The recommendation logic filters recipes by ingredients, scales nutritional features, and uses nearest neighbors with cosine similarity to find similar recipes.

### model.py Explanation

- Uses `StandardScaler` to scale nutritional features.
- Uses `NearestNeighbors` with cosine similarity to find nearest recipes.
- Builds a pipeline combining scaling and nearest neighbor search.
- Filters recipes by ingredients using regex matching.
- The `recommend` function applies the pipeline and returns recommended recipes.
- The `output_recommended_recipes` function formats the output for API response.

---

## Frontend (Streamlit)

### Key Files

- `Hello.py`: Main entry point for the Streamlit app.
- `pages/1_💪_Diet_Recommendation.py`: Page for diet recommendations.
- `pages/2_🔍_Custom_Food_Recommendation.py`: Page for custom food recommendations.
- `Generate_Recommendations.py`: Contains the `Generator` class that calls the backend API to get recommendations.
- `ImageFinder/ImageFinder.py`: Fetches images for recommended recipes.

### Frontend Workflow

- User inputs nutritional values and optional ingredients via the Streamlit UI.
- The frontend calls the backend API `/predict/` endpoint with the input data.
- Receives recommended recipes from the backend.
- Displays the recommendations with images and detailed nutritional info.
- Provides interactive features like custom food search and visualization.

---

## How the Model is Made and Hosted

- The model is a content-based recommender using nutritional data and ingredients.
- It uses scikit-learn's `StandardScaler` and `NearestNeighbors` with cosine similarity.
- The model is implemented in `model.py` and used by the FastAPI backend.
- The backend exposes a REST API for prediction.
- The frontend Streamlit app consumes this API to provide an interactive user experience.
- Both backend and frontend can be run locally or via Docker.

---

## How to Run

1. Install dependencies for backend and frontend.
2. Run the backend FastAPI server:
   ```
   cd FastAPI_Backend
   python -m uvicorn main:app --host 0.0.0.0 --port 8080
   ```
3. Run the frontend Streamlit app:
   ```
   cd Streamlit_Frontend
   python -m streamlit run Hello.py
   ```
4. Open browser at http://localhost:8501 to use the app.

---

If you have any questions or need further assistance, feel free to ask.

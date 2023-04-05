
import requests

api_token = ""
endpoint = "https://api.themoviedb.org/3/movie/"
headers = {"Authorization": f"Bearer {api_token}"}

def get_popular_movies():
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]
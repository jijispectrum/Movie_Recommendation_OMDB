from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

# ✅ OMDb API Key
OMDB_API_KEY = '9b4f912c'

# ✅ Malayalam Movies List
malayalam_movies = [
    'Drishyam', 'Premam', 'Bangalore Days', 'Kumbalangi Nights', 'Uyare',
    'Charlie', 'Jallikattu', 'Take Off', 'Angamaly Diaries', 'Thondimuthalum Driksakshiyum',
    'Njan Prakashan', 'Virus', 'Maheshinte Prathikaaram', 'Anjaam Pathiraa', 'Ee.Ma.Yau',
    'The Great Indian Kitchen', 'C U Soon', 'Minnal Murali', 'Hridayam', 'Rorschach',
    '1983', 'Ennu Ninte Moideen', 'Ramaleela', 'Drishyam 2', 'Operation Java',
    'Manichitrathazhu', 'Kilukkam', 'Godha', 'Joseph', 'Kali'
]

# ✅ Function to fetch movie data
def get_movie_data(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()

    if response['Response'] == 'True':
        return {
            'Title': response['Title'],
            'Genre': response['Genre'],
            'Director': response['Director'],
            'Rating': float(response['imdbRating']) if response['imdbRating'] != 'N/A' else 0,
            'Year': response['Year'],
            'Poster': response['Poster']
        }
    else:
        return None



# ✅ Recommend Movies View
def recommend_movies(request):
    user_movie_title = request.GET.get('movie')  # Get user input

    selected_movie = get_movie_data(user_movie_title)
    if not selected_movie:
        return render(request, 'recommend.html', {'error': f"Movie '{user_movie_title}' not found."})

    # Find similar movies
    similar_movies = []
    for movie in malayalam_movies:
        if movie.lower() == user_movie_title.lower():
            continue
        
        movie_data = get_movie_data(movie)
        if movie_data and (selected_movie['Genre'].split(',')[0] in movie_data['Genre'] or
                           selected_movie['Director'] == movie_data['Director']):
            similar_movies.append(movie_data)

    # Get Top 5 by IMDb Rating
    top_5 = sorted(similar_movies, key=lambda x: x['Rating'], reverse=True)[:5]

    return render(request, 'recommend.html', {
        'selected_movie': selected_movie,
        'recommendations': top_5
    })

# ✅ Home Page
def home(request):
    return render(request, 'home.html')
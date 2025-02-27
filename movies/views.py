from django.shortcuts import render
import requests

movies = [
    # Malayalam Movies
    'Yodha', 'Virus', 'Kilukkam', 'Titanic', 'Mayamohini', 'Neelathamara',
    'Joseph', 'Drishyam', 'Kali', '1983', 'Take Off', 'Angamaly Diaries',
    'Operation Java', 'Manichitrathazhu', 'C U Soon', 'Minnal Murali',
    'Hridayam', 'Rorschach', 'Charlie', 'Jallikattu', 'Bangalore Days',
    'RRR', 'Kumbalangi Nights', 'Ennu Ninte Moideen', 'Ramaleela',
    'Drishyam 2', 'Thondimuthalum Driksakshiyum', 'Thilakkam', 'Ravanaprabhu',
    'Marco', 'Identity', 'Sookshma Darshini', 'Ponman', 'The Great Indian Kitchen',
    'Aavesham', 'Rifle Club', 'Kishkindha Kaandam', 'Rekhachithram', 'Manjummel Boys',
    'Pani', 'Bramayugam', 'Premalu', 'Bhoothakaalam', 'Narayaneente Moonnaanmakkal',
    'Bougainvillea', 'Iratta', 'Anweshippin Kandethum', 'Kurup', 'Malik', 'A.R.M',
    'Painkili', 'Kannur Squad', 'Anand Sreebala', 'Varshangalkku Shesham', 
    'Turbo', 'Nadikar', 'Bandra', 'Guruvayoor Ambalanadayil', 'Thallumaala', 
    'Kaapa', 'Palthu Janwar', 'John Luther', 'Bheemante Vazhi', 'Jana Gana Mana',

    # English Movies
    'The Dark Knight', 'Black Panther', 'The Woman King', 'Thor: Love and Thunder',
    'Jurassic World: Dominion', 'The Batman', 'Avengers', 'The Antman', 'The Lord of the Rings',
    'Inception', 'Spiderman', 'Avatar', 'The Shawshank Redemption', 'John Wick',
    'Gladiator', 'Avengers Endgame', 'The Fast and the Furious', 'The Suicide Squad',
    'The Mummy', 'The Lord of the Rings: The Return of the King', 'Infinite',
    'Ford v Ferrari', 'Doctor Strange in the Multiverse of Madness', 'Beast',
    'Guardians of the Galaxy', 'Murder Mystery', 'Star Wars', 'Suicide Squad',
    'Infinity War', 'Transformers: Rise of the Beasts', 'Wonder Woman 1984',
    'Deadpool', 'Deadpool 2', 'Kingsman: The Secret Service', 
    'Pirates of the Caribbean: The Curse of the Black Pearl', 'Interstellar',
    'Oppenheimer', 'Dune: Part One', 'Dune: Part Two', 'The Matrix', 'Tenet',
    'Everything Everywhere All at Once', 'The Prestige', 'The Revenant', 'Logan',

    # Hindi Movies
    'The Kashmir Files', 'Rang De Basanti', '3 Idiots', 'Like Stars on Earth',
    'Lagaan: Once Upon a Time in India', 'Barfi!', 'Anand', 'Queen', 'Udaan',
    'Kahaani', 'Dilwale Dulhania Le Jayenge', 'Black', 'Madras Cafe', 
    'Vicky Donor', 'Highway', 'Oye Lucky! Lucky Oye!', 'Black Friday', 
    'Robber', 'Omkara', 'Sanam Teri Kasam', 'All We Imagine as Light',
    'Slumdog Millionaire', 'Animal', 'Do Patti', 'Dangerous', 'PK', 
    'Gangubai Kathiawadi', 'My Name Is Khan', 'Aashiqui 2', 'Shaitaan', 
    'La Vaste', 'Devdas', 'Ghajini', 'Laila Majnu', 'Maidaan', 'Shershaah',
    'Pathaan', 'Mohabbatein', 'Om Shanti Om', 'Padmaavat', 'Yeh Jawaani Hai Deewani',
    'Krrish 3', 'Krrish', 'Koi... Mil Gaya', 'Gadar 2', 'Rocky Aur Rani Ki Prem Kahani',
    'Dunki', 'Jawan', 'Bajrangi Bhaijaan', 'Drishyam (Hindi)', 'Airlift', 'Chak De! India',

    # Tamil Movies
    'Meiyazhagan', 'Nayakan', 'Anbe Sivam', 'Vaaranam Aayiram', '96', 'Pithamagan',
    'A Peck on the Cheek', 'Kaithi', 'Mahanadi', 'Hey Ram', 'Aadukalam',
    'Kaakha Kaakha', 'Ghajini', 'Aayitha Ezhuthu', 'Thalapathi', 'Kadhalikka Neramillai',
    'Mudhalvan', 'Indian', 'Ayan', 'Enthiran', 'Vishwaroopam', 'Thuppakki', 'Nanban',
    'Kaththi', 'Ghilli', 'Anniyan', 'Saamy', 'Kanguva', 'Jai Bhim', 'Raatchasan',
    'Jailer', 'Leo', 'Vettaiyan', 'Theri', 'Madraskaaran', 'Jigarthanda Double X',
    'Master', 'Vaazhai', 'Thunivu', 'Soorarai Pottru', 'Aranmanai 4', 'Aranmanai 3',
    'Aranmanai 2', 'Aranmanai', 'Ponniyin Selvan: Part I', 'Ponniyin Selvan: Part II',
    'Mersal', 'Chithha', 'Dasavatharam', 'Gargi', 'Sarpatta Parambarai', 'Billa',
    'Thirupaachi', 'Vallavan', 'Engeyum Kadhal', 'Raatchasi', 'Kanthaswamy',
    'Neethaane En Ponvasantham', 'Maari', 'Maattrraan', 'Remo', 'Mark Antony',
    'Cobra', 'Maamannan', 'Viduthalai Part 1', 'Viduthalai Part 2', 'Don'
]

OMDB_API_KEY = '6df4500d'

def get_movie_data(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()
    
    if response.get('Response') == 'True':
        return {
            'Title': response.get('Title', 'Unknown'),
            'Genre': response.get('Genre', 'Unknown'),
            'Director': response.get('Director', 'Unknown'),
            'Rating': float(response.get('imdbRating', 0)) if response.get('imdbRating', 'N/A') != 'N/A' else 0,
            'Year': int(response.get('Year', 0)) if response.get('Year', 'Unknown').isdigit() else 0,
            'Poster': response.get('Poster', ''),
            'Language': response.get('Language', 'Unknown')
        }
    return None

def recommend_movies(request):
    user_movie_title = request.GET.get('movie', '')
    
    if not user_movie_title:
        return render(request, 'recommend.html', {'error': "Enter a movie name to get recommendations!"})
    
    user_movie = get_movie_data(user_movie_title)
    
    if not user_movie:
        return render(request, 'recommend.html', {'error': f"Movie '{user_movie_title}' not found."})
    
    user_genres = set(user_movie['Genre'].split(', '))
    user_director = user_movie['Director']
    user_language = user_movie['Language']
    user_year = user_movie['Year']

    similar_movies = []
    
    for movie in movies:
        if movie.lower() == user_movie_title.lower():
            continue
        movie_data = get_movie_data(movie)
        if not movie_data:
            continue
        
        movie_genres = set(movie_data['Genre'].split(', '))
        genre_match = len(user_genres & movie_genres) / len(user_genres) if user_genres else 0
        director_match = user_director == movie_data['Director'] and user_director != "Unknown"
        language_match = user_language == movie_data['Language'] and user_language != "Unknown"
        year_match = abs(user_year - movie_data['Year']) <= 5 if user_year and movie_data['Year'] else False
        match_score = (genre_match * 3) + (director_match * 2) + (language_match * 2) + (year_match * 1)

        if match_score >= 2:
            similar_movies.append((match_score, movie_data))

    top_similar = sorted(similar_movies, key=lambda x: (x[0], x[1]['Rating']), reverse=True)[:5]

    return render(request, 'recommend.html', {
        'user_movie': user_movie,
        'recommendations': [movie[1] for movie in top_similar]
    })


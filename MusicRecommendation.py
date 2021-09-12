import pandas as pd
import streamlit as st
from PIL import Image

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("datasetFinal.csv")
data.drop_duplicates()

###################### streamlit setup ######################


logo = Image.open("./music_symbol.jpeg")
st.set_page_config("Resonance", logo)
page_bg_img = '''
<style>
.stApp {
background-image: url("https://free4kwallpapers.com/uploads/originals/2021/01/20/music-wallpaper.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title('Resonance')
st.write("Find music that resonates with you")
st.write("A Howdyhack 2021 Project by Jiaming Fu and Yifan Sun")
image = st.sidebar.image(logo,"",200)
mainTab = st.sidebar.selectbox(
    "",
    ("Music Recommender", "Feeling lucky?")
)

default_input = [[-9999]*9]

user_input = default_input
compute = False

if mainTab == "Music Recommender":
    user_input_song = st.text_input("Your favorite song is...", "song")
    if user_input_song in data["Track Name"].tolist():
        compute = st.button("Find")
    elif user_input_song != "song":
        st.write("Song not in database, could you provide a different one?")

###################### backend ######################

features = ['danceability', 'energy', 'key','loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
       'liveness', 'valence', 'tempo', 'duration_in min/ms']

def combine_features(row):
    return str(row['danceability']) +" "+str(row['energy'])+" "+str(row["key"])+" "+str(row["loudness"])+" "+str(row["mode"])+" "+str(row["speechiness"])+" "+str(row["acousticness"])+" "+str(row["instrumentalness"])+" "+str(row["liveness"])+" "+str(row["valence"])+" "+str(row["tempo"])+" "+str(row["duration_in min/ms"])

data["combined_features"] = data.apply(combine_features,axis=1)
cv = CountVectorizer()
count_matrix = cv.fit_transform(data["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_track_from_index(index):
    return data[data.index == index]["Track Name"].values[0]

def get_artist_from_index(index):
    return data[data.index == index]["Artist Name"].values[0]

def get_index_from_track(track):
    return data[data["Track Name"] == track]["index"].values[0]

def find_df(user_input_song):
    song_user_likes = user_input_song
    song_index = get_index_from_track(song_user_likes)
    similar_songs =  list(enumerate(cosine_sim[song_index]))
    sorted_similar_songs = sorted(similar_songs,key=lambda x:x[1],reverse=True)[1:]
    i=0
    song_result = []
    for element in sorted_similar_songs:
        song_result.append(get_track_from_index(element[0])+" by "+get_artist_from_index(element[0]))
        i=i+1
        if i>=5:
            break
    return song_result

if mainTab == "Music Recommender" and compute:
    songResult = find_df(user_input_song)
    st.title("Those are the songs that are recommended...")
    div1, div2, div3, div4 = int((len(songResult)+3) // 5), int(2*(len(songResult)+2) // 5), int(3*(len(songResult)+1) // 5), int(4*(len(songResult)) // 5)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        for i in range(div1):
            st.write(songResult[i])

    with col2:
        for i in range(div1, div2):
            st.write(songResult[i])

    with col3:
        for i in range(div2, div3):
            st.write(songResult[i])
    with col4:
        for i in range(div3, div4):
            st.write(songResult[i])
            
    with col5:
        for i in range(div4, len(songResult)):
            st.write(songResult[i])
    
    
    
    
    
    
    
    
    
    
    
    
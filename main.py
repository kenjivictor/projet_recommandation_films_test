import streamlit as st
import pandas as pd
from datetime import date, time

# Titre principal de l'application (affiché en haut de la page)
st.title("The title of my page")

# Titre de section important (taille 1)
st.header("An Important Header")

# Sous-titre (taille 2), utile pour organiser le contenu par sous-sections
st.subheader("A Secondary Header")

# Affiche une ligne de texte simple (sans mise en forme particulière)
st.text("My classic text")

# Affiche du texte avec mise en forme Markdown
st.markdown(''':rainbow: :rainbow[My markdown]''')  # Ici, un effet arc-en-ciel est appliqué

# Affiche un dataframe (st.write accepte plusieurs arguments et plusieurs types de données)
st.write(
    pd.DataFrame({
            "Cards": ['Name 1', 'Name 2', 'Name 3', 'Name 4'],
            "Quantity": [0, 1, 0, 3]}
    )
)

if st.button("Ajouter"):
    st.write("+1")
    
st.write('___')# Ligne de séparation pour aérer l’interface visuellement.


# La commande st.checkbox vous permet d’afficher une case à cocher. Plusieurs checkbox peuvent être cocher en même temps.
st.checkbox(label = "Tu es incollable sur l'univers du Roi lion.") # label : paramètre (facultatif à écrire) qui permet d'afficher le contenu associé 
st.write('___')  

# La commande radio permet à l'utilisateur de choisir UNE seule réponse parmi plusieurs propositions.
st.radio("Est-ce que Le Roi lion est le meilleur Disney ?", 
         ['Oui !', 'Evidemment !', 'La question ne se pose même pas.']) #Les réponses possibles sont stockées dans une liste 
st.write('___')

# Un interrupteur (toggle). Il s’agit d’un bouton on/off. 
st.toggle("Tu as vu Le Roi lion", value=True) #Ici, il est activé par défaut (value=True).
st.write('___')

# Un menu déroulant où l'utilisateur peut sélectionner une seule option.
st.selectbox("Qui a tué Mufasa ?",
             ['Simba', 'Scar', 'Zazu']) 
st.write('___')

# Une liste à choix multiples. L’utilisateur peut sélectionner plusieurs réponses à la fois.
st.multiselect("Quels sont vos personnages favoris ?", 
               ['Simba', 'Mufasa', 'Scar', 'Nala']) 
st.write('___')

# Un curseur avec des valeurs textuelles. L’utilisateur choisit son appréciation du film.
st.select_slider("Donnez votre appréciation sur le Roi lion", 
                 ['Mauvais', 'Bon', 'Excellent'], 
                 value='Excellent') # Paramètre permettant de positiionner le curseur par défaut sur "Excellent"
st.write('___')

#permet la saisie de texte sur une seule ligne
st.text_input("Quel est le titre de votre film favori ?", "Le Roi lion :D")
st.write('___')

#permet la saisie de texte sur plusieurs lignes
st.text_area("Peux-tu expliquer pourquoi c'est ton film favori")
st.write('___')

#permet à l’utilisateur de rentrer une valeur numérique
#paramètres 
#  min_value : borne minimale
# max_value : borne maximale
# step : changer l’intervalle entre les valeurs
st.number_input("Tu en possèdes :", min_value=0)
st.write('___')

#fonctionne comme st.select_slider sauf qu’il n’accepte que les types : int, float, date, time et datetime
st.slider("Sélectionnez la plage de date :",
           min_value=1923,
           max_value=date.today().year,
           value=(1923, date.today().year)
          )
st.write('___')

#fonctionne comme une st.selectbox sauf qu’il propose un calendrier
st.date_input("Sélectionnez votre date de naissance")
st.write('___')

#fonctionne comme une st.selectbox sauf qu’il propose une here
st.time_input("Configurez une alarme à ", time(7, 30))
st.write('___')



st.text('TODO list')
task1 = st.checkbox("Lire un livre")
task2 = st.checkbox("Développer mes projets")
task3 = st.checkbox("Me promener")

st.write("\n\n")

if task1 and task2 and task3:
    st.write("Bravo, tu as réalisé tous tes objectifs du moment. :sunglasses:")
elif task1 or task2 or task3:
    st.write("Tu es sur la bonne voie, continue comme ça. :smile:")
else:
    st.write("Tu dois revoir tes priorités, tu n'as encore réalisé aucunes de tes tâches. :pleading:")

st.write('___')


#ajouter une image
st.image("1_intro/bird.jpg", caption="Image : Oiseau, Flottant, Baies. Utilisation gratuite. (Pixabay)")
st.write('___')

#ajouter une video
video_file = open("1_intro/escargot.mp4", "rb") 
video_bytes = video_file.read()
st.video(video_bytes) 
st.write('___')


#ajouter une piste audio
st.audio("1_intro/christmas-is-christmas-60s.mp3", format="audio/mpeg", loop=True)
st.write('___')
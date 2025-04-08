import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 🔹 Charger les données combinées
df = pd.read_csv("donnees_climatiques_combinees.csv")

# 🔹 Ajouter manuellement les latitudes / longitudes pour chaque pays
coordonnees = {
    'France': {'lat': 46.603354, 'lon': 1.888334},
    'Inde': {'lat': 20.593684, 'lon': 78.96288}
}
df['latitude'] = df['pays'].map(lambda x: coordonnees[x]['lat'])
df['longitude'] = df['pays'].map(lambda x: coordonnees[x]['lon'])

# 🔹 Créer une carte centrée sur l’axe France–Inde
carte = folium.Map(location=[30, 30], zoom_start=2)
cluster = MarkerCluster().add_to(carte)

# 🔹 Ajouter un marqueur par ligne (année + infos climatiques)
for _, row in df.iterrows():
    popup_info = (
        f"<b>Pays :</b> {row['pays']}<br>"
        f"<b>Année :</b> {int(row['année'])}<br>"
        f"Température : {row['anomalie_temp']} °C<br>"
        f"Précipitations : {row['precipitations_mm']} mm<br>"
        f"CO₂ émis : {row['co2_emis']} Mt<br>"
        f"Catastrophes : {float(row['nb_catastrophes'])}"
    )
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(popup_info, max_width=250),
        icon=folium.Icon(color='blue' if row['pays'] == 'France' else 'green', icon='info-sign')
    ).add_to(cluster)

# 🔹 Sauvegarder la carte
carte.save("carte_interactive_climat.html")
print("✅ Carte générée : carte_interactive_climat.html")

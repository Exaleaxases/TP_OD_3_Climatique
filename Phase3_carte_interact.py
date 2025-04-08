import pandas as pd
import folium
from folium.plugins import HeatMap

# 🔹 Charger les données combinées
df = pd.read_csv("donnees_climatiques_combinees.csv")

# 🔹 Ajouter manuellement les latitudes / longitudes pour chaque pays
coordonnees = {
    'France': {'lat': 46.603354, 'lon': 1.888334},
    'Inde': {'lat': 20.593684, 'lon': 78.96288}
}
df['latitude'] = df['pays'].map(lambda x: coordonnees[x]['lat'])
df['longitude'] = df['pays'].map(lambda x: coordonnees[x]['lon'])

# Créer une carte centrée sur le globe
carte = folium.Map(location=[20, 0], zoom_start=2)

# Ajouter une heatmap
heat_data = [[row['latitude'], row['longitude']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(carte)

# Enregistrer
carte.save("heatmap_catastrophes.html")

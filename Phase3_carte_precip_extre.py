import pandas as pd
import plotly.express as px


# 🔹 Charger les données combinées
df = pd.read_csv("donnees_climatiques_combinees.csv")

# 🔹 Ajouter manuellement les latitudes / longitudes pour chaque pays
coordonnees = {
    'France': {'lat': 46.603354, 'lon': 1.888334},
    'Inde': {'lat': 20.593684, 'lon': 78.96288}
}
df['latitude'] = df['pays'].map(lambda x: coordonnees[x]['lat'])
df['longitude'] = df['pays'].map(lambda x: coordonnees[x]['lon'])

# Précipitations max par pays
df_max_precip = df.groupby("pays")[['precipitations_mm']].max().reset_index()
df_max_precip['pays_plotly'] = df_max_precip['pays'].replace({'France': 'France', 'Inde': 'India'})

# Carte choropleth
fig = px.choropleth(df_max_precip,
                    locations='pays_plotly',
                    locationmode='country names',
                    color='precipitations_mm',
                    color_continuous_scale='Blues',
                    title='Précipitations extrêmes maximales (1970–2020)',
                    labels={'precipitations_mm': 'Précipitations max (mm)'},
                    scope='world')
fig.show()

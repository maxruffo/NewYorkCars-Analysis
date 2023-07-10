from helper import merge_dataframes
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import pandas as pd

file1_path = 'data/NewYorkCars/New_York_cars_part1.csv'
file2_path = 'data/NewYorkCars/New_York_cars_part2.csv'

data = merge_dataframes(file1_path, file2_path)
print(data.columns)

# Machine Learning: K-Means-Clustering und Bewertung
def perform_clustering(data):
    # Ausgewählte Merkmale für das Clustering
    features = ['money', 'Mileage', 'Exterior color', 'Interior color', 'Drivetrain', 'MPG',
                'Fuel type', 'Transmission', 'Engine', 'Convenience', 'Entertainment',
                'Exterior', 'Safety', 'Seating', 'Accidents or damage', 'Clean title',
                '1-owner vehicle', 'Personal use only']

    # Daten vorbereiten und fehlende Werte behandeln
    X = data[features]
    imp = SimpleImputer(strategy='most_frequent')
    X_imputed = imp.fit_transform(X)

    # Kategorische Spalten in numerische Werte umwandeln
    le = LabelEncoder()
    for feature in ['Exterior color', 'Interior color', 'Drivetrain', 'Fuel type', 'Transmission']:
        X_imputed[:, features.index(feature)] = le.fit_transform(X_imputed[:, features.index(feature)])

    # Daten normalisieren
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(X_imputed)

    # K-Means-Clustering durchführen
    kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
    kmeans.fit(scaled_data)

    # Clusteretiketten den Daten hinzufügen
    data['Cluster'] = kmeans.labels_

    # Bewertung der Autos basierend auf dem Cluster
    data['Score'] = 10 - data['Cluster']

    # Die besten bewerteten Autos auswählen
    top_cars = data.sort_values(by='Score', ascending=False)

    return top_cars

# Plots erstellen und Bewertung durchführen
top_cars = perform_clustering(data)

# Die besten bewerteten Autos als Tabelle anzeigen
top_cars_table = top_cars[['brand', 'Model', 'Score']]
print(top_cars_table)

# Gruppierung nach Fahrzeugmodellen und Durchschnittsberechnung
grouped_cars_avg = top_cars.groupby(['brand', 'Model']).agg({'Score': 'mean'}).reset_index()
grouped_cars_avg = grouped_cars_avg.sort_values(by='Score', ascending=False)
print(grouped_cars_avg)

# Gruppierung nach Marken und Durchschnittsberechnung
grouped_brands_avg = top_cars.groupby('brand').agg({'Score': 'mean'}).reset_index()
grouped_brands_avg = grouped_brands_avg.sort_values(by='Score', ascending=False)
print(grouped_brands_avg)

# Plotten der durchschnittlichen Score pro Marke
grouped_brands_avg.plot(x='brand', y='Score', kind='bar', figsize=(12, 6))
plt.xlabel('Marke')
plt.ylabel('Score')
plt.title('Durchschnittlicher Score pro Marke')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

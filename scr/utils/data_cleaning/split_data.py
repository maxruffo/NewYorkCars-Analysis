import os
import pandas as pd

# Pfad zum Ordner
folder_path = 'data/NewYorkCars/'

# Dateipfade für die aufgeteilten Dateien
file1_path = os.path.join(folder_path, 'New_York_cars_part1.csv')
file2_path = os.path.join(folder_path, 'New_York_cars_part2.csv')

# Überprüfen, ob die aufgeteilten Dateien bereits existieren
if os.path.exists(file1_path) and os.path.exists(file2_path):
    print("Die Dateien wurden bereits aufgeteilt.")
else:
    # Pfad zur CSV-Datei
    file_path = os.path.join(folder_path, 'New_York_cars.csv')

    # Daten aus der CSV-Datei lesen
    data = pd.read_csv(file_path)

    # Anzahl der Zeilen im DataFrame berechnen
    num_rows = len(data)

    # Die Hälfte der Zeilen berechnen
    half_rows = num_rows // 2

    # Die erste Hälfte der Daten
    part1 = data[:half_rows]

    # Die zweite Hälfte der Daten
    part2 = data[half_rows:]

    # Die aufgeteilten Daten als separate CSV-Dateien speichern
    part1.to_csv(file1_path, index=False)
    part2.to_csv(file2_path, index=False)

    # Bestätigungsnachricht
    print("Die Datei wurde erfolgreich aufgeteilt.")
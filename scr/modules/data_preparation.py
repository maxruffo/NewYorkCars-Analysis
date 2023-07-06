import os
import pandas as pd

def merge_dataframes(file1_path, file2_path):
    import os

    # Überprüfen, ob die Dateien existieren
    if not os.path.exists(file1_path) or not os.path.exists(file2_path):
        print("Die aufgeteilten Dateien wurden nicht gefunden.")
        return None

    # Daten aus den beiden Dateien lesen
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Die beiden DataFrames zusammenführen
    merged_df = pd.concat([df1, df2], ignore_index=True)

    return merged_df

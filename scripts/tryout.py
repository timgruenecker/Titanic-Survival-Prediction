
import pandas as pd
from ydata_profiling import ProfileReport

# CSV laden
df = pd.read_csv("data/train.csv")  # Pfad ggf. anpassen

# EDA-Profil erzeugen
profile = ProfileReport(df, title="🛳 Titanic EDA Report", explorative=True)

# Ausgabe als HTML-Datei
profile.to_file("titanic_eda_report.html")

print("✅ Report erfolgreich erstellt: titanic_eda_report.html")

# Titanic-Survival-Prediction
Machine Learning Klassifikation: Überleben von Titanic-Passagieren vorhersagen

# Kleine Notizen:

## Der Datensatz ist nicht komplett, in den zwei Spalten Alter und Kabinennummer etc. fehlen Werte!

sibsp: Anzahl von Geschwistern oder Ehepartnern, die mit der Person gereist sind, bei sibsp = 1 => eine Begleitperson: Bruder, Schwester, Ehepartner ...
parch: Anzahl Eltern oder Kinder, die zusammen gereist sind, bei parch = 2: z.B. Vater und Tochter sind zusammen aufs Schiff
Ticket: Die Ticketnummer, teils mehrfach vergeben (z. B. für Familien oder Gruppen) - meistens eher unwichtig
fare: Ticketpreis, den Person X gezahlt hat - korreliert meist mit Pclass - class 1 = teuer, class 3 = billig
cabin: Kabinenbezeichnung - hat viele fehlende Werte (also selbst wenn wichtig womöglich schwer zu berücksichtigen, weil das fast nirgends dabei steht)
embarked: Abfahrthafen: C = Cherbourg (Frankreich), Q = Queenstown (Irland), S = Southampton (England)

In der Excel wo CSV importiert ist, ist z.B. Age 285 28.5, also kein ausreißer


Aussagekräftigste Features:
Sex (Frauen überleben 70%, männer nur 15), 
Fare bzw. Pc Class (je teurer desto höher survival),

Weniger aussagekräftig, aber nicht random
Embarked
Age
Sibsp
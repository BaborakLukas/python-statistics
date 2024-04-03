# po spuštění si dejte otevřené okno na full screen budete muset dole vedle ikonky „uložit“
# budete mít nastavení s inkoukou sliderů to otevřete a posuňte si
# left a right aby šla vidět všechna čísla :)

import pandas as pd
import matplotlib.pyplot as plt

# Cesta k externímu JSON souboru
json_file_path = 'spainM.json'

# Načteme data z externího JSON souboru
data = pd.read_json(json_file_path)

# Převedeme hodnoty v sloupci 'Year' na celá čísla
data['Year'] = data['Year'].astype(int)

# Vytvoříme graf, který zobrazuje počet sebevražd pro muže v Albánii v různých letech
plt.bar(data['Year'], data['SuicideCount'])
plt.xlabel('Year')
plt.ylabel('Suicide Count')
plt.title('Suicide Count in Spain for Men')

# Nastavíme hodnoty na ose x na celá čísla
plt.xticks(data['Year'])

plt.show()

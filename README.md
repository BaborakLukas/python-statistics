# Suicide Count Graph Generator

Tento projekt generuje grafy zobrazující počet sebevražd pro muže v Albánii v různých letech z dat uložených v JSON souboru.

## Požadavky

- Python 3.x
- Pandas
- Matplotlib

## Instalace

1. Ujistěte se, že máte Python 3.x nainstalovaný.
2. Nainstalujte potřebné knihovny pomocí pip:
    pip install matplotlib pandas


3. Stáhněte nebo vytvořte JSON soubor s daty o sebevraždách, například `albaniaM.json`.

## Spuštění

1. Otevřete terminál nebo příkazovou řádku.
2. Přejděte do adresáře projektu.
3. Spusťte skript Pythonu:


4. Graf se zobrazí v okně matplotlib.

## Výsledky

Graf zobrazuje počet sebevražd pro muže v Albánii v různých letech. Hodnoty na ose x jsou nastaveny na celá čísla pro lepší čitelnost.

## Příklad JSON struktury

    {
      "RegionCode": "EU",
      "RegionName": "Europe",
      "CountryCode": "ALB",
      "CountryName": "Albania",
      "Year": "1992",
      "Sex": "Male",
      "SuicideCount": "33",
      "CauseSpecificDeathPercentage": "0.33195856",
      "StdDeathRate": "2.33580198",
      "DeathRatePer100K": "2.07638583",
      "Population": "3247039",
      "GDP": "652174990.8",
      "GDPPerCapita": "200.8522198",
      "GNI": "906184212.3",
      "GNIPerCapita": "1740",
      "InflationRate": "226.0054213",
      "EmploymentPopulationRatio": "45.315"
    }

## Je tu více dat ze kterých si můžete vybrat

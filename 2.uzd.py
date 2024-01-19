import csv

def lasit_otro_kolonnu(csv_fails):
    try:
        with open(csv_fails, 'r') as fails:
            lasītājs = csv.reader(fails)
            
            print("Otrās kolonnas dati:")
            for rinda in lasītājs:
                if len(rinda) >= 2:
                    print(rinda[1])
    except FileNotFoundError:
        print(f"Faila '{csv_fails}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Aizstājiet 'dati.csv' ar vēlamā faila nosaukumu
csv_fails = 'dati.csv'
lasit_otro_kolonnu(csv_fails)

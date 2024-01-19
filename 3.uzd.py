def lasit_trešo_rindu(faila_nosaukums):
    try:
        with open(faila_nosaukums, 'r') as fails:
            rindas = fails.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2].strip()  # Nolasīt trešo rindu un noņemt liekos atstarpes
                print("Trešās rindas saturs:")
                print(tresa_rinda)
            else:
                print(f"Failā '{faila_nosaukums}' nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print(f"Faila '{faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Aizstājiet 'teksta_fails.txt' ar vēlamā faila nosaukumu
faila_nosaukums = 'teksta_fails.txt'
lasit_trešo_rindu(faila_nosaukums)

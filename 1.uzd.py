def lasit_un_izdrukāt_failu(skolena_atzīmes):
    try:
        with open(skolena_atzīmes, 'r') as fails:
            saturs = fails.read()
            print("atzīmes:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{skolena_atzīmes}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

# Aizstājiet 'teksta_fails.txt' ar vēlamā faila nosaukumu
faila_nosaukums = 'skolena_atzīmes'
lasit_un_izdrukāt_failu(faila_nosaukums)
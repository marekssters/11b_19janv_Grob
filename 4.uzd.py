def nolasit_un_izdrukāt_faila_saturu():
    try:
        faila_nosaukums = input("datagit init.py: ")
        faila_paplašinājums = input("datilaikapstakliem (piemēram, sniegputeni): ")
        
        pilns_faila_nosaukums = f"{faila_nosaukums}.{faila_paplašinājums}"

        with open(pilns_faila_nosaukums, 'r') as fails:
            saturs = fails.read()
            print(f"Faila '{pilns_faila_nosaukums}' saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Faila '{pilns_faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: {e}")

nolasit_un_izdrukāt_faila_saturu()

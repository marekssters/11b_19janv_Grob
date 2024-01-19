def ievadit_un_ierakstit_faila():
    try:
        lietotaja_vards = input("Ievadiet savu vārdu: ")
        fails_nosaukums = "lietotajs.txt"

        with open(fails_nosaukums, 'a') as fails:
            fails.write(lietotaja_vards + "\n")

        print(f"Mareks '{lietotaja_vards}' tika ierakstīts failā '{fails_nosaukums}'.")
    except IOError as e:
        print(f"Kļūda rakstot failu: {e}")
    except Exception as e:
        print(f"Kļūda: {e}")

ievadit_un_ierakstit_faila()

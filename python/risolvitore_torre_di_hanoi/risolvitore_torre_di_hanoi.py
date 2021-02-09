#!/usr/bin/python
"""
--------------------------------------------------------------------------------------------
Autore: Nicolò Zorzetto
--------------------------------------------------------------------------------------------
Titolo: Risolvitore Torre di Hanoi.
--------------------------------------------------------------------------------------------
Descrizione: questo programma calcola i passaggi necessari per la risoluzione 
della Torre di Hanoi usando la recursione; questa può avere un numero di anelli arbitrario.
--------------------------------------------------------------------------------------------
Argomenti: Risolvitore Torre di Hanoi accetta 2 argomenti alla chiamata: il numero
di anelli presenti e "-s" o "--sequenziale", che fornisce l'output sequenziale.
--------------------------------------------------------------------------------------------
"""

import sys
import os

def print_aiuto():
    """
    Questa funzione stampa l'aiuto del programma.
    """
    print("Uso risolvitore_torre_di_hanoi.py")
    print("\tpython risolvitore_torre_di_hanoi.py [numero di dischi] [argomenti]")
    print("[numero di dischi]:\n\til numero di dischi che si vogliono spostare dal piolo A al piolo C. Deve essere un numero intero positivo in base 10")
    print("[argomenti]:\n\t-h, --help\t\t\tper aiuto")
    print("\t-s, --sequenziale\tper avere un output sequenziale")

def analisi_argomenti(argomenti):
    """
    Questa funzione analizza gli argomenti forniti dalla shell, fornisce una schermata di 
    aiuto ("help"), returna gli argomenti uguali a "-s" o "--sequenziale" per utilizzo 
    successivo (risolvitore_hanoi) e riporta all'utente il passaggio di argomenti non definiti.
    """
    argomento = "placeholder"
    numero_dischi = None
    for arg in argomenti:
        if arg == "-s" or arg == "--sequenziale":
            argomento = arg
        elif arg.isdigit():
            numero_dischi = int(arg)
        else:
            if arg == __file__:
                pass
            else:
                if arg == "-h" or arg == "--help":
                    print_aiuto()
                    argomento = ""
                else:
                    if (arg.replace('-', '')).isdigit():
                        print(CRED + "ERRORE l'argomento ", arg, " non è un numero positivo in base 10." + CRES)
                    else:
                        print(CRED + "ERRORE l'argomento " + arg + " non è definito" + CRES)
                        if argomenti.index(arg) == len(argomenti)-1:
                            print_aiuto()
                            argomento = ""

                argomento = ""
    return argomento, numero_dischi
									
def raccoglimento_dati():
    """
    Questa funzione è responsabile del raccoglimento del numero di anelli.
    """
    try:
        numero_dischi = int(input("Inserire il numero di dischi: "))
    except ValueError:
        print(CRED + "ERRORE il valore inserito non è un numero in base 10" + CRES)
        return raccoglimento_dati()
    else:
        if numero_dischi<0:
            print(CRED + "ERRORE inserire un numero in base 10 positivo" + CRES)
            return raccoglimento_dati()
        else:
            return numero_dischi

def risolvitore_hanoi(numero_dischi, da, attraverso, a, argomento):
    """
    Questa funzione è il motore di risoluzione per la Torre di Hanoi.
    """
    if numero_dischi == 0:
        pass
    else:
        risolvitore_hanoi(numero_dischi-1, da, a, attraverso, argomento)
        print("Muovi disco da {} a {}.".format(da, a))
        # se gli argomenti sono -s o --sequenziale richiedere RETURN per continuare
        if argomento == "-s" or argomento == "--sequenziale":
            input_sequenziale = input()
            if input_sequenziale == "q" or input_sequenziale == "Q":
                sys.exit()
        risolvitore_hanoi(numero_dischi-1, attraverso, da, a, argomento)

def main():
    """
    Questa è la funzione main.
    """
    argomento, numero_dischi = analisi_argomenti(sys.argv)
    if argomento == "":
        print(argomento)
        return 0
    if numero_dischi == None:
        numero_dischi = raccoglimento_dati()
    risolvitore_hanoi(numero_dischi, "A", "B", "C", argomento)
    print(CGREEN + "Torre di Hanoi risolta con successo." + CRES)
    return 0

if __name__ == "__main__":
    #colori errore/successo
    CRED = '\033[91m'
    CGREEN = '\033[32m'
    CRES = '\033[0m'
    main()

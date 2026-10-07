"""
Parche 2 del visor (ficha de edificios): cambia la frase final de la ventana de la casilla.
Uso, desde ~/visor-ribera-de-arriba:   python3 parche_edificios_v2.py
Si el texto no se encuentra exactamente una vez, no toca nada.
"""
import sys
js = open("visor.js", encoding="utf-8").read()
VIEJA = "Esta lista no sustituye al informe de la Confederación Hidrográfica del Cantábrico.'"
NUEVA = "Sirve como base de trabajo para el programa de adaptación y para preparar la consulta con la Confederación Hidrográfica del Cantábrico, organismo competente en zonas inundables.'"
if NUEVA in js:
    print("Ya estaba aplicado."); sys.exit(0)
if js.count(VIEJA) != 1:
    sys.exit("ERROR: no encuentro la frase exactamente una vez (%d). No se ha tocado nada." % js.count(VIEJA))
open("visor.js", "w", encoding="utf-8").write(js.replace(VIEJA, NUEVA))
print("Hecho: frase de la ventana actualizada.")

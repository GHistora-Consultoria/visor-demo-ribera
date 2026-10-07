"""Superficie del tooltip de parcela con 2 decimales (148.905,28) en lugar de redondeada.
Uso, desde ~/visor-ribera-de-arriba:  python3 parche_superficie_v2.py
"""
import sys
f = "terra_layers.js"
s = open(f, encoding="utf-8").read()
viejo = "Math.round(parseFloat(layer.feature.properties[v])).toLocaleString('es-ES')"
nuevo = "parseFloat(layer.feature.properties[v]).toLocaleString('es-ES', {minimumFractionDigits: 2, maximumFractionDigits: 2})"
n = s.count(viejo)
if n != 1:
    sys.exit(f"Esperaba 1 coincidencia y hay {n}. No se ha cambiado nada.")
open(f, "w", encoding="utf-8").write(s.replace(viejo, nuevo))
print("Hecho: superficie con 2 decimales.")

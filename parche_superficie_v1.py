"""Redondea la superficie del tooltip de parcela en terra_layers.js (148905.2754... -> 148.905).
Uso, desde ~/visor-ribera-de-arriba:  python3 parche_superficie_v1.py
"""
import sys
f = "terra_layers.js"
s = open(f, encoding="utf-8").read()
ancla = 'let aliases = ["Ref. catastral:", "Superficie (m\\u00b2):"];'
i = s.find(ancla)
if i < 0:
    sys.exit("No encuentro el bloque del tooltip de parcela. No se ha cambiado nada.")
viejo = "<td>${handleObject(layer.feature.properties[v])}</td>"
j = s.find(viejo, i)
if j < 0 or j - i > 600:
    sys.exit("No encuentro la celda a cambiar junto al bloque. No se ha cambiado nada.")
nuevo = ("<td>${v === 'area_m2' && isFinite(parseFloat(layer.feature.properties[v])) "
         "? Math.round(parseFloat(layer.feature.properties[v])).toLocaleString('es-ES') "
         ": handleObject(layer.feature.properties[v])}</td>")
s = s[:j] + nuevo + s[j + len(viejo):]
open(f, "w", encoding="utf-8").write(s)
print("Hecho: superficie redondeada en el tooltip de parcela.")

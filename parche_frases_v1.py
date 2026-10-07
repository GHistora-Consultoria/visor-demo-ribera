"""
Suaviza las frases "no sustituye ..." del visor: dicen lo mismo (que hay un paso posterior de confirmacion) pero
empiezan por lo que la herramienta aporta.
Uso, desde ~/visor-ribera-de-arriba:   python3 parche_frases_v1.py
Cada cambio se aplica solo si el texto aparece exactamente las veces esperadas; si no, se salta y se avisa.
"""
CAMBIOS = [
 ("visor.js", "Cartografía oficial del Ministerio: el visor la cruza con el planeamiento y no la sustituye.",
  "Cartografía oficial del Ministerio, mostrada tal como la publica y cruzada por el visor con el planeamiento.", 1),
 ("visor.js", "y no sustituye el informe de la Confederación Hidrográfica.'",
  "y sirve de base para la consulta con la Confederación Hidrográfica.'", 1),
 ("visor.js", "No sustituye un estudio geotécnico de campo.",
  "Es un primer filtro de gabinete, que un estudio geotécnico de campo permite confirmar sobre el terreno.", 3),
 ("visor.js", "Esa medida es aproximada y no sustituye a un levantamiento topográfico.",
  "Esa medida es aproximada y sirve para planificar y priorizar; si hace falta precisión, se confirma con un levantamiento topográfico.", 1),
 ("index.html", "No sustituye al planeamiento municipal vigente: el ",
  "Complementa al planeamiento municipal vigente: el ", 1),
 ("index.html", "no sustituye asesoría jurídica de un abogado o técnico urbanista colegiado. Antes de cualquier actuación concreta, verifica el texto vigente y actualizado de cada norma.",
  "sirve como punto de partida: para cada actuación concreta conviene contrastarlo con el texto vigente de cada norma y con el criterio de un técnico urbanista o un abogado colegiado.", 1),
 ("index.html", "no sustituye un estudio geotécnico de campo.",
  "es un primer filtro de gabinete, que un estudio geotécnico de campo permite confirmar sobre el terreno.", 1),
 ("index.html", "del Principado, no sustituye al documento legal vigente (",
  "del Principado; el documento legal de referencia sigue siendo el planeamiento vigente (", 1),
 ("gestion.js", "(medida aproximada, no sustituye a un levantamiento topográfico)",
  "(medida aproximada para planificar; si hace falta precisión, se confirma con un levantamiento topográfico)", 1),
 ("gestion.js", "<b>no sustituye</b> al registro oficial ni a los expedientes administrativos del ayuntamiento.",
  "<b>complementa</b> al registro oficial y a los expedientes administrativos del ayuntamiento, que siguen siendo la referencia.", 1),
]
cont = {}
hechos = saltados = 0
for f, viejo, nuevo, n in CAMBIOS:
    if f not in cont:
        cont[f] = open(f, encoding="utf-8").read()
    veces = cont[f].count(viejo)
    if veces == n:
        cont[f] = cont[f].replace(viejo, nuevo); hechos += 1
    elif cont[f].count(nuevo) >= 1 and veces == 0:
        print("  ya estaba:", viejo[:60]); 
    else:
        saltados += 1; print(f"  SALTADO ({f}): esperaba {n} vez/veces y hay {veces}: {viejo[:70]}...")
for f, t in cont.items():
    open(f, "w", encoding="utf-8").write(t)
print(f"Hecho: {hechos} cambios aplicados, {saltados} saltados.")

import sys, io
ruta = 'gestion.js'
s = io.open(ruta, encoding='utf-8').read()
cambios = [
 ("Es una <b>libreta de avisos pegada al mapa</b>: apuntas qué hay que revisar o arreglar, dónde está exactamente y en qué punto va, sin papeles sueltos ni hojas de cálculo.",
  "Es un <b>registro de avisos y actuaciones vinculado al mapa</b>: permite anotar qué hay que revisar o arreglar, su localización exacta y su estado de tramitación, de forma centralizada y sin depender de papeles sueltos ni hojas de cálculo."),
 ("<li>Alcaldía, concejales, técnicos y operarios de ayuntamientos pequeños que no tienen (ni pueden pagar) un programa de mapas profesional.</li>",
  "<li>Alcaldía, concejalías y personal técnico del ayuntamiento, para coordinar el seguimiento de incidencias, inspecciones y actuaciones sobre el territorio municipal.</li>"),
 ("<li>Cualquier persona que acompañe a un ayuntamiento rural y necesite llevar un control sencillo de lo pendiente.</li>",
  "<li>Personal técnico de las áreas de urbanismo, obras y medio ambiente, que puede compartir la copia exportada y mantener un control común de lo pendiente.</li>"),
]
faltan = [a[:60] for a, b in cambios if a not in s]
if faltan:
    print('ABORTO: no encuentro estos textos (¿ya aplicado?):'); [print(' -', f) for f in faltan]; sys.exit(1)
for a, b in cambios:
    s = s.replace(a, b)
io.open(ruta, 'w', encoding='utf-8').write(s)
print('OK: 3 frases (v2) reescritas en gestion.js')

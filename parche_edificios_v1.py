"""
Parche del visor: ficha "Edificios en zona inundable".
Uso, desde ~/visor-ribera-de-arriba:   python3 parche_edificios_v1.py
- index.html: anade la casilla "Edificios en zona inundable" en Alerta de Planeamiento y carga edificios.js
- visor.js:   anade la ficha (ventana) 'alerta-edificios' y corrige la frase del art. 23.2.b
No hace nada si ya esta aplicado. Si algun texto no se encuentra una sola vez, se detiene SIN tocar nada.
"""
import sys, re

def leer(n):
    return open(n, encoding="utf-8").read()

html, js = leer("index.html"), leer("visor.js")
novedades = []

# ---------- index.html ----------
if "alerta-edificios" in html:
    print("index.html: la casilla ya estaba aplicada")
else:
    m = [x for x in re.finditer(r'^.*data-key="alerta-reparto".*$', html, re.M)]
    if len(m) != 1:
        sys.exit("ERROR: no encuentro (o hay mas de una) la casilla alerta-reparto en index.html. No se ha tocado nada.")
    caja = ('        <div class="dash-caja" data-key="alerta-edificios" style="cursor:pointer;"><span class="dash-caja-swatch" style="background:#00897b;"></span>'
            '<span class="dash-caja-label">Edificios en zona inundable (T500)</span><div class="dash-caja-val" id="ed-caja-val">Ver lista</div>'
            '<div class="dash-caja-sub" id="ed-caja-sub">Edificios de servicios públicos, sin uso asignado o con pista, según Catastro; los completa el ayuntamiento</div></div>')
    fin = m[0].end()
    html = html[:fin] + "\n" + caja + html[fin:]
    novedades.append("index.html: casilla nueva")

if 'src="edificios.js"' in html:
    print("index.html: edificios.js ya estaba cargado")
else:
    ancla = '<script src="gestion.js"></script>'
    if html.count(ancla) != 1:
        sys.exit("ERROR: no encuentro la linea de gestion.js en index.html. No se ha tocado nada.")
    html = html.replace(ancla, '<script src="edificios.js"></script>\n' + ancla)
    novedades.append("index.html: carga de edificios.js")

# ---------- visor.js ----------
ENTRADA = """    'alerta-edificios': {
      titulo: 'Edificios en zona inundable: uso según Catastro y verificación del ayuntamiento', valor: 'Lista de edificios que tocan la zona inundable T500', fuente: 'Catastro (edificios INSPIRE y ficha de la Sede Electrónica); SNCZI y zona de flujo preferente (MITECO); OpenStreetMap solo como pista no oficial',
      explicación: 'El proyecto de Real Decreto (en tramitación, sin aprobar) pide que el programa municipal de adaptación identifique los edificios públicos, equipamientos básicos y zonas comerciales situados en zonas inundables (art. 23.2.b). Esta ficha cruza los edificios del Catastro del municipio con las zonas T10, T100 y T500 y con la zona de flujo preferente, y lista los de uso «servicios públicos», sin uso asignado o con una pista de OpenStreetMap cuya huella toca la zona T500.<br><br><b>Qué es oficial y qué no.</b> De cada edificio se muestra el uso que figura en la ficha de Catastro (oficial). Si hay algo marcado en OpenStreetMap, se enseña aparte y explicado como pista no oficial. Lo que ni Catastro ni OpenStreetMap pueden decir, como si un edificio es un equipamiento básico o si un deportivo es cubierto o al aire libre, lo completa el ayuntamiento en la propia ficha, con notas y fotos.<br><br><b>«Tocar» no es «estar afectado».</b> Significa que parte de la huella del edificio cae dentro de la zona; la ficha indica el porcentaje. No incluye todavía los edificios de uso comercial o industrial ni las viviendas.',
      recomendacion: '💡 El proyecto no define qué es un «equipamiento básico»: cita ejemplos y deja la decisión a quien conoce cada edificio. Lo que escribe el ayuntamiento se guarda solo en su navegador; para conservarlo hay que exportarlo. Esta lista no sustituye al informe de la Confederación Hidrográfica del Cantábrico.',
      gráfico: '<button type="button" onclick="abrirEdificios()" style="background:#00897b; color:#fff; border:none; border-radius:6px; padding:10px 16px; font-size:15px; cursor:pointer;">Abrir la lista de edificios</button>'
    },
"""
if "'alerta-edificios'" in js:
    print("visor.js: la ficha ya estaba aplicada")
else:
    ancla = "    'alerta-escenarios': {"
    if js.count(ancla) != 1:
        sys.exit("ERROR: no encuentro 'alerta-escenarios' en visor.js. No se ha tocado nada.")
    js = js.replace(ancla, ENTRADA + ancla)
    novedades.append("visor.js: ficha nueva")

VIEJA = "los edificios públicos, equipamientos y zonas industriales en zona inundable."
NUEVA = "los edificios públicos, equipamientos básicos y zonas comerciales situados en zonas inundables (art. 23.2.b) y, por separado, las zonas industriales (art. 23.2.d)."
if VIEJA in js:
    if js.count(VIEJA) != 1:
        sys.exit("ERROR: la frase del articulo 23 aparece mas de una vez. No se ha tocado nada.")
    js = js.replace(VIEJA, NUEVA)
    novedades.append("visor.js: frase del art. 23 corregida")
else:
    print("visor.js: la frase del art. 23 ya estaba corregida (o no aparece)")

open("index.html", "w", encoding="utf-8").write(html)
open("visor.js", "w", encoding="utf-8").write(js)
print("Hecho:", "; ".join(novedades) if novedades else "nada que cambiar")

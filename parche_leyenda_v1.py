"""Leyenda extensible del mapa exportado (cámara): cualquier módulo del visor puede registrar lo que dibuja.
Uso, desde ~/visor-ribera-de-arriba:  python3 parche_leyenda_v1.py
"""
import sys
f = "terra_layers.js"
s = open(f, encoding="utf-8").read()
if "GHISTORA_LEYENDA" in s:
    sys.exit("Este parche ya está aplicado. No se ha cambiado nada.")

a1 = "                var estilos = {"
a2 = "                        est = est || {tipo: 'poligono', color: '#888888'};"
if s.count(a1) != 1 or s.count(a2) != 1:
    sys.exit(f"No encuentro los puntos de anclaje (estilos={s.count(a1)}, est={s.count(a2)}). No se ha cambiado nada.")

bloque = """                // 07/10/2026: leyenda extensible. Cualquier modulo del visor (edificios.js, gestion.js...) puede anadir una funcion a
                // window.GHISTORA_LEYENDA que, dado el mapa, devuelva lo que dibuja y se ve: [{nombre, tipo, color, borde, dash}].
                var extrasLeyenda = {};
                (window.GHISTORA_LEYENDA || []).forEach(function (fn) {
                    try {
                        (fn(mapa) || []).forEach(function (e) {
                            if (e && e.nombre && !nombresVistos[e.nombre]) { nombresVistos[e.nombre] = true; nombres.push(e.nombre); extrasLeyenda[e.nombre] = e; }
                        });
                    } catch (errLey) { console.warn('Leyenda: un modulo fallo al registrar sus entradas', errLey); }
                });
"""
s = s.replace(a1, bloque + a1, 1)
s = s.replace(a2, "                        if (extrasLeyenda[n]) { est = extrasLeyenda[n]; }\n" + a2, 1)
open(f, "w", encoding="utf-8").write(s)
print("Hecho: leyenda extensible aplicada (2 cambios).")

import sys, io
s = io.open('gestion.js', encoding='utf-8').read()
a = """'<details class="g-ayuda"' + (items.length ? '' : ' open') + '><summary>"""
b = """'<details class="g-ayuda"><summary>"""
if s.count(a) != 1:
    print('ABORTO: encuentro', s.count(a), 'veces el texto (esperaba 1; ¿ya aplicado?)'); sys.exit(1)
io.open('gestion.js', 'w', encoding='utf-8').write(s.replace(a, b))
print('OK: el desplegable «¿Para qué sirve esto y para quién?» ahora aparece siempre recogido')

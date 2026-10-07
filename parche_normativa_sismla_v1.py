# Añade a «Normativa aplicable» (index.html) una fila con el visor SIS_MLA, con el mismo formato que las demás.
import io, sys
ruta = 'index.html'
s = io.open(ruta, encoding='utf-8').read()
if 'SIS_MLA' in s:
    print('ABORTO: index.html ya menciona SIS_MLA (¿ya aplicado?)'); sys.exit(1)
ancla = '(Cueva de las Caldas, Desfiladero de las Xanas)</td></tr>'
if s.count(ancla) != 1:
    print('ABORTO: ancla encontrada %d veces (esperaba 1)' % s.count(ancla)); sys.exit(1)
SIS = 'https://app.powerbi.com/view?r=eyJrIjoiMDE2M2QxODUtYjZiZC00ZjgwLTgxOTctZWQ1YzhlZmEwNjkwIiwidCI6ImIwOTViNzZhLTAzZDYtNGM4Yi04N2QwLWUxYTA2ZTc3OTYwYyIsImMiOjl9'
fila = ('\n        <tr style="border-bottom:1px solid #2a3d5c;"><td style="padding:6px 8px;">Sostenibilidad y ODS (consulta informativa)</td>'
        '<td style="padding:6px 8px;">También puede servir de ayuda consultar el <a href="%s" target="_blank" rel="noopener" style="color:#e6c07a;">SIS_MLA, Sistema de Información de Sostenibilidad en el Mapa Local Asturiano ↗</a> '
        '(Cátedra Concepción Arenal, Universidad de Oviedo): visor público e informativo sobre la sostenibilidad y los Objetivos de Desarrollo Sostenible (Agenda 2030) en los concejos asturianos. No es una norma: es un recurso de consulta.</td></tr>') % SIS
io.open(ruta, 'w', encoding='utf-8').write(s.replace(ancla, ancla + fila))
print('OK: fila añadida a «Normativa aplicable»')

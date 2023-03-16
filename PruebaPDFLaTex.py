import subprocess
import os
#import shutil

# Crea un archivo con contenido LaTex
latex_code = """\\documentclass{article}
\\begin{document}
Hola mundo!
\\end{document}
"""

with open('documento.tex', 'w') as f: #'documento.tex' documento es el nombre del documento y .tex es el formato
    f.write(latex_code)

# Compila el archivo LaTex en un archivo PDF
subprocess.call(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'documento.tex'])
#subprocess.call(['pdflatex', 'documento.tex'])

# Elimina los archivos intermedios generados por LaTeX
for extension in ['aux', 'log', 'out']:
    os.remove(f'documento.{extension}')

# Mueve el archivo PDF a una ubicación específica
#shutil.move('documento.pdf', 'C:\Users\Fiorela\Desktop\documento.pdf')
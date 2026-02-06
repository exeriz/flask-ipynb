from flask import Flask, render_template
import nbformat
from nbconvert import HTMLExporter
import os

app = Flask(__name__)

NOTEBOOK_FILE = './preprocessing.ipynb'
OUTPUT_HTML = 'notebook_output.html'

@app.route('/')
def index():
    with open(NOTEBOOK_FILE, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = True
    (body, _) = html_exporter.from_notebook_node(nb)

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(body)

    return render_template('index.html')
  
@app.route('/output')
def show_output():
    with open(OUTPUT_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, send_file, render_template
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    content = f"{data['variables']} {data['clauses']}\n" + data['clauseText']

    with open("cnf_test1.txt", "w") as f:
        f.write(content)

    try:
        with open("sat_solver.ipynb", encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=300, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': './'}})

    except Exception as e:
        print("Notebook execution error:", e)
        return f"Notebook execution failed: {str(e)}", 500

    if not os.path.exists("output.png"):
        return "output.png not generated.", 500

    return send_file("output.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
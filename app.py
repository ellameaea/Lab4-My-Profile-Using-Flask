from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('index'))

@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def upper():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contacts.html')

@app.route('/areaofcircle', methods=['GET', 'POST'])
def circle():
    radius = None
    result = None
    pi = 3.142
    if request.method == 'POST':
        try:
            radius = request.form.get('inputRadius', '')
            result = pi * float(radius)**2
        except ValueError:
            pass
    return render_template('circle.html', radius=radius, result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def triangle():
    base = None
    height = None
    result = None
    constant = 1/2
    if request.method == 'POST':
        try:
            base = request.form.get('inputBase', '')
            height = request.form.get('inputHeight', '')
            result = constant * float(base) * float(height)
        except ValueError:
            pass
    return render_template('triangle.html', base=base, height=height, result=result)

if __name__ == "__main__":
    app.run(debug=True)

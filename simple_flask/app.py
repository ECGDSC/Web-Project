from flask import Flask, render_template, request

app = Flask(__name__)

# Route for handling GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handling POST request
        name = request.form['name']
        return render_template('result.html', name=name)
    else:
        # Handling GET request
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
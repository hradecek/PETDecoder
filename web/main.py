from flask import Flask, render_template, request

from pet.decoder import DecodedPETVarbind
from pet.snmp import PETVarbind

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


def split_bytes(bytes_string, separator):
    return bytes_string.split(separator)


@app.route('/', methods=['POST'])
def home_post():
    variable_binding = request.form['variable_binding']
    return {
        '1.3.6.1.4.1.3183.1.1.0.?': 'To be done',
        '1.3.6.1.4.1.3183.1.1.1': DecodedPETVarbind(PETVarbind(split_bytes(variable_binding, ' '))).to_dict()
    }


if __name__ == '__main__':
    app.run(debug=False)

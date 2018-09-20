from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post">
        <label>Rotate by:
            <input type="text" name="rot" value="0" />
        </label>
        
        <textarea name="text">{0}</textarea>

        <input type="submit" />
      </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    user_rotation = request.form['rot']
    user_message = request.form['text']

    encrypted_string = rotate_string(user_message, int(user_rotation))
    #return encrypted_string
    return form.format(encrypted_string)

@app.route("/")
def index():
    return form.format('')

app.run()
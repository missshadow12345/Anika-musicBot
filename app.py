from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
      return 'GreyMatters'


if_ _name_ _ == "_ _main_ _":
    app.run()

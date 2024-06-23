from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
      return 'GreyMatters'


if__name__ == "_ _main_ _":
    app.run()

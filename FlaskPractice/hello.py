from flask import Flask
app = Flask(__name__)


def make_bold(func):
    def add_html():
        return f"<b>{func()}</b>"
    return add_html


def make_underlined(func):
    def add_html():
        return f"<u>{func()}</u>"
    return add_html


def make_emphasized(func):
    def add_html():
        return f"<em>{func()}</em>"
    return add_html


@app.route("/")
@make_bold
@make_emphasized
@make_underlined
def hello_world():
    return "<h1>Hello world!</h1>"


@app.route("/name/<name>")
def greeting(name):
    return f"Nice to see you, {name.title()}."


if __name__ == "__main__":
    app.run(debug=True)

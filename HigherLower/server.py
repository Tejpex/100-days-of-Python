from flask import Flask
from random import randint
app = Flask(__name__)

correct_number = randint(0, 9)


def add_flex(function):
    def add_html(*args, **kwargs):
        return (f"<div style='display: flex; flex-direction: column; align-items: center'>{function(*args, **kwargs)}"
                f"</div>")
    return add_html


@app.route("/")
def start_page():
    global correct_number
    correct_number = randint(0, 9)
    return (f"<div style='display: flex; flex-direction: column; align-items: center'>"
            f"<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"
            f"<p>Write your guess after a '/' in the url in your browser.</p>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnE2b3N2dGY0OW0xNGF0NGhjenIyYm"
            "RoNGE2eW4wc3UxZ2l5bmttNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/33zX3zllJBGY8/giphy.webp' "
            "style='width: 500px'/></div>")


@app.route("/<int:number>")
@add_flex
def result(number):
    if number == correct_number:
        return ("<h1 style='color: green'>Correct</h1><img src='https://media0.giphy.com/media/v1."
                "Y2lkPTc5MGI3NjExc3FrbnF0dWc3Zzg3azI2MHh5cTZzZmR6aXhwejFwcjhpcHJubHljaiZlcD12MV9pbnR"
                "lcm5hbF9naWZfYnlfaWQmY3Q9Zw/ri8Kb9LOe5Nza/200.webp' style='width: 500px' />")
    elif number > correct_number:
        return ("<h1 style='color: purple'>Too high!</h1><img src='https://media1.giphy.com/media/v1."
                "Y2lkPTc5MGI3NjExamwwcW1qN3o2Z3ZwMXhic3plOWFtM3g2Z2preGk0ejFsaXM2ZXV6eCZlcD12MV9pbnRlcm"
                "5hbF9naWZfYnlfaWQmY3Q9Zw/AUYhIMdGrg23e/giphy.webp' style='width: 500px'/>")
    else:
        return ("<h1 style='color: red'>Too low!</h1><img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3N"
                "jExNWwzcWxtZ3dybm5wM3k0MjRhZTA3eDBuOGQ3NGduN3JmaXptNHA0dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQm"
                "Y3Q9Zw/BizefE576ASY0/giphy.webp' style='width: 500px'/>")


if __name__ == "__main__":
    app.run(debug=True)

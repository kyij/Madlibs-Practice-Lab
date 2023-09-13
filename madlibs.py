"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."



@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Show form to play Madlibs"""

    response = request.args.get("play")
    print(f'Response is {response}')
    
    if response == "no":
        return render_template("goodbye.html")
    elif response == "yes":
        return render_template("game.html")
    else:
        return "Sorry, that was an invalid input."


madlibs_list = ["madlib.html", "madlib1.html" , "madlib2.html", "madlib3.html"]
@app.route("/madlib", methods = ['POST'])
def show_madlib():
    """Show madlib"""
    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    hobbies = request.form.get("hobbies")

    return render_template(
        choice(madlibs_list),
        person=person,
        color=color,
        noun=noun,
        adjective=adjective,
        hobbies=hobbies)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")

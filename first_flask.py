from flask import Flask, request, render_template
# provide webserver/application to answer requests

app = Flask(__name__)

@app.route("/") # registeres function with flask framework --> request route URL of project: then return hello world
def start():
    return render_template("start.html", title='Start the Reverso-Magic!!')

@app.route("/reverse")
def reverse():
    if not 'rev' in request.args:
        return "YOU FIEND! DO NOT TRY TO HACK ME AGAIN!! >:C"
    rev = request.args['rev'] # access what user has written --> 'rev' matches name='rev' from input
    return render_template("reverse.html", result= [rev, rev, rev])
from flask import Flask, request, render_template
from crawler import crawl
# provide webserver/application to answer requests


app = Flask(__name__)

@app.route("/") # registeres function with flask framework --> request route URL of project: then return hello world
def start():
    return render_template("start.html", title='Search Engine')

@app.route("/answer")
def reverse():
    if not 'rev' in request.args:
        return "YOU FIEND! DO NOT TRY TO HACK ME AGAIN!! >:C"
    
    rev = request.args['rev'] # access what user has written --> 'rev' matches name='rev' from input
    
    answer = crawl(first_URL="https://vm009.rz.uos.de/crawl/index.html", search=rev)
   
    return render_template("answer.html", result = answer, rev = rev)

# for console: flask --app flask_app.py run
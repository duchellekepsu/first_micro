from flask import Flask, render_template, request
import requests
import logging
import sys
import os


app = Flask(__name__)

LOGGER = logging.getLogger(__name__)

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-B42PCT518X"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-B42PCT518X');
</script>
 """


@app.route('/', methods = ['POST'])
def redirect_response():
    if request.form["submit"] == "Logger":
        return redirect(url_for("logger"))
    return "Connecté!"

# Define logger on deta
@app.route('/logger', methods = ['GET', 'POST'])
def logger():

    global user_input

    print('Back-end log!', file=sys.stderr)
    logging.info("Logging test")
    value = request.form.get("textbox_input")

    return render_template("logger.html",text=value) 
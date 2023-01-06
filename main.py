from flask import Flask, render_template, request
import requests
import logging
import sys
import os
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/', methods=["GET"])

def hello_world():
    prefix_google = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-250912185-1"></script> <script>
window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date());
gtag('config', 'UA-250912185-1'); </script>
"""
    
    return prefix_google+"Hello Word"

@app.route('/logs', methods=["GET"])
def log():
    return render_template("logger.html")+"My console"

@app.route('/textbox')
def textlog():
    return "Write something"+render_template("textbox.html")+"my console"

@app.route('/cookie', methods=["GET","POST"])
def mycookies():
    req = requests.get("https://www.google.com/")
    return req.cookies.get_dict() 

@app.route('/cookieganalytics', methods=["GET","POST"])
def mycookies():
    req = requests.get("https://analytics.google.com/analytics/web/#/report-home/a250912185w345031321p281211325")
    return req.text

@app.route('/visitor', methods = ['GET', 'POST'])
def get_nb_visitors():

    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    nb_visitor = print_response(response)
    return "Number of visitors : " + str(nb_visitor) 

@app.route('/ganalytics', methods = ['GET', 'POST'])
def get_analytics():

    mail = os.getenv("Google_mail")
    password = os.getenv("Google_password")

    payload = {'inUserName': mail, 'inUserPass': password}
    # url = 'http://www.example.com'
    other_url = "https://analytics.google.com/analytics/web/#/report-home/a164062586w272485488p243020933"
    r = requests.post(other_url, data=payload)
    req = requests.get(other_url, cookies=r.cookies)
    return req.text

if __name__ == '__main__':
    app.run(debug = True)
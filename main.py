
from flask import Flask, render_template, send_file, redirect, request, send_from_directory
from threading import Thread

from libgen_api import LibgenSearch
import json
import requests
import time

app = Flask('discord bot')

@app.route('/', methods=('GET', 'POST'))
def book():
     if request.method == "POST":
       xx = request.form.get("book")
       s = LibgenSearch()
    #   title_filters = {"Extension": "pdf"}
     #  results = s.search_title_filtered(xx, title_filters, exact_match=True)
       results = s.search_title(xx)


       ddl = results[0]
       lnks = s.resolve_download_links(ddl)
       url = lnks['Cloudflare']
       return redirect(url, code=302)
     return render_template('index.html')








def start_server():
  app.run(host='0.0.0.0',port=8080)
  
t = Thread(target=start_server)
t.start()

from flask import Flask, render_template, request, redirect, send_file
from wework import get_wework_jobs
from SO import get_so_jobs
from remoteok import get_remoteok_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

DB = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
   word = word.lower()
   fromDB = DB.get(word)
   if fromDB:
     jobs = fromDB
   else: 
     jobs = get_so_jobs(word)+get_wework_jobs(word)+get_remoteok_jobs(word)
     DB[word] = jobs
  else:
    return redirect
  return render_template("report.html",searchingBy=word,
  resultsNumber=len(jobs), jobs=jobs)

@app.route("/export")
def export():
  try:
   word = request.args.get('word')
   if not word:
    raise Exception()
   word = word.lower()
   jobs = DB.get(word)
   if not jobs:
     raise Exception()
   save_to_file(jobs)  
   return send_file("jobs.csv")
  except:
   return redirect("/")



app.run(host="0.0.0.0")


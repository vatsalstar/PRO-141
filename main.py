from flask import Flask,jsonify,request
import csv

all_articles=[]
with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
    
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"SUCCESS"
    })
    
if __name__ == '__main__':
    app.run()
    

@app.route("/liked_articles",methods=["POST"])
def liked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"SUCCESS"
    }),201
    
@app.route("/not-liked-articles",methods=["POST"])
def not_liked_movie():
    article=all_articles[0]
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"SUCCESS"
    }),201
    
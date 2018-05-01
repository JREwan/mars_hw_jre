from flask import Flask, render_template, jsonify, redirect
#from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

##mongo = PyMongo(app)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_hw_jre
collection = db.collection

#mars_news_dict = {'title': 'NASA...', 'mn_para': 'NASA’s next ...'}

@app.route("/")
def index():
    listings = db.collection.find_one()
    #return render_template("index.html",  dict = mars_news_dict, listings = listings)
    return render_template("index.html",  listings = listings)
    
@app.route("/scrape")
def scrape():
    #listings = mongo.db.listings
    listings = db.collection
    listings_data = scrape_mars.mars_news()
    listings.update(
        {},
        listings_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

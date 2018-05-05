from flask import Flask, render_template, jsonify, redirect
import scrape_mars
import pymongo

app = Flask(__name__)

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.mars_hw_jre

# Declare the collection
collection = db.mars_news

mars_dict = {"mn_title": "NASA...",
             "mn_para": "NASA’s next ...",
             "mfi": "https://static3.srcdn.com/wp-content/uploads/Tim-Burtons-Mars-Attacks.jpg?q=50&w=1000&h=500&fit=crop",
             "mw": "current martian weather",
             "mf_ed": "wide",
             "mf_pd": "high",
             "mf_m": "heavy",
             "mf_moons": "yes",
             "mf_od": "around",
             "mf_op": "martian year",
             "mf_st": "not hot",
             "mf_fr": "ages ago",
             "mf_rb":  "king tut",
             "mh1_title": "Mars Attacks",
             "mh1_link": "https://theawesomer.com/photos/2012/11/110912_mars_attacks_ornament_1.jpg",
             "mh2_title": "and Attacks",
             "mh2_link": "http://www.flore-maquin.com/wp-content/uploads/Mars_Attack_FLOREMAQUIN.jpg",
             "mh3_title": "and Attacks",
             "mh3_link": "https://mfiles.alphacoders.com/611/611833.jpg",
             "mh4_title": "and it ends",
             "mh4_link": "https://i.pinimg.com/564x/1e/94/a5/1e94a52c15a5a266e95792dbdc02d529.jpg"}

@app.route("/")
def index():
    return render_template("index.html",  dict=mars_dict)
    
@app.route("/scrape")
def scrape():
    # mars news
    mars_news_junk = scrape_mars.mars_news()
    mars_dict["mn_title"] = mars_news_junk[0]
    mars_dict["mn_para"] = mars_news_junk[1]
    # featured image
    mars_featured_image_link = scrape_mars.mars_feat_image()
    mars_dict["mfi"] = mars_featured_image_link
    # mars weather
    mars_latest_weather = scrape_mars.mars_weather()
    mars_dict["mw"] = mars_latest_weather
    # mars hemispheres
    # hemi 1
    mars_hemi1_list = scrape_mars.mars_hemi1()
    mars_dict["mh1_title"] = mars_hemi1_list[0]
    mars_dict["mh1_link"] = mars_hemi1_list[1]
    # hemi 2
    mars_hemi2_list = scrape_mars.mars_hemi2()
    mars_dict["mh2_title"] = mars_hemi2_list[0]
    mars_dict["mh2_link"] = mars_hemi2_list[1]
    # hemi 3
    mars_hemi3_list = scrape_mars.mars_hemi3()
    mars_dict["mh3_title"] = mars_hemi3_list[0]
    mars_dict["mh3_link"] = mars_hemi3_list[1]
    # hemi4
    mars_hemi4_list = scrape_mars.mars_hemi4()
    mars_dict["mh4_title"] = mars_hemi4_list[0]
    mars_dict["mh4_link"] = mars_hemi4_list[1]

    # insert the updated dictionary into Mongo
    # Insert the document into the database
    collection.insert_one(mars_dict)
    
    return redirect("http://localhost:5000/", code=302)
 
if __name__ == "__main__":
    app.run(debug=True)

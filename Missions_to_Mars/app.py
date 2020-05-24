# ensure Mongo is running
# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars as scrape


# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Or set inline
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Route that will trigger scrape functions
@app.route("/scrape")
def scraped():
    print("working ")

    # Run scraped functions
    scrapedata = scrape.scrape()
    print(scrapedata)

    # Insert mars_dict into database
    mongo.db.collection.update({}, scrapedata, upsert = True)

    # Redirect back to home page
    return redirect("/", code=302)

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_data = mongo.db.collection.find_one()

    # return template and data
    return render_template("index.html", mars_data=mars_data)



if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
from logic.recommender import recommend_ingredients

app = Flask(__name__)

# Load dataset
df = pd.read_csv("data/ingredientsList.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    skin_type = request.form["skin_type"]
    concern = request.form["concern"]

    recommendations = recommend_ingredients(df, skin_type, concern)

    return render_template(
        "results.html",
        skin_type=skin_type,
        concern=concern,
        ingredients=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
models = joblib.load("models/selected_models.pkl")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    input_data = {
        "age": int(request.form["age"]),
        "workclass": request.form["workclass"],
        "fnlwgt": float(request.form["fnlwgt"]),
        "education": request.form["education"],
        "education.num": int(request.form["education.num"]),
        "marital.status": request.form["marital.status"],
        "occupation": request.form["occupation"],
        "relationship": request.form["relationship"],
        "race": request.form["race"],
        "sex": request.form["sex"],
        "capital.gain": float(request.form["capital.gain"]),
        "capital.loss": float(request.form["capital.loss"]),
        "hours.per.week": int(request.form["hours.per.week"]),
        "native.country": request.form["native.country"]
    }
    input_df = pd.DataFrame([input_data])
    predictions = {}
    for model_name, model in models.items():
        prediction = model.predict(input_df)[0]
        if str(prediction).strip() == ">50K":
            result = "Income >50K"
        else:
            result = "Income <=50K"

        predictions[model_name] = result
    return render_template(
        "index.html",
        predictions=predictions
    )
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)

from flask import Flask, request, render_template

from src.pipeline.prediction_pipeline import CustomData, Predictdata
from src.pipeline.train_pipeline import TrainingPipeline




application = Flask(__name__)

app = application



@app.route("/")
def index():

    return render_template("index.html")

@app.route('/predictdata', methods = ['GET', 'POST'])
def predict():

    if request.method == "GET":

        return render_template("home.html")

    else:

        training_result = TrainingPipeline().run_pipeline()

        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )


        conveted_df = data.get_data_from_dataframe()

        pred_pipeline = Predictdata()

        results = pred_pipeline.predict(conveted_df)

        return render_template(
            'home.html',
            results=results,
            training_result=training_result,
        ) 






if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

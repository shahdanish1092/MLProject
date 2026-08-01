import app as app_module


def test_predict_route_trains_before_predict(monkeypatch):
    calls = []

    class DummyTrainingPipeline:
        def run_pipeline(self):
            calls.append("train")
            return {"r2_score": 0.91}

    class DummyPredictData:
        def predict(self, features):
            calls.append(("predict", features))
            return [42.0]

    monkeypatch.setattr(app_module, "TrainingPipeline", DummyTrainingPipeline)
    monkeypatch.setattr(app_module, "Predictdata", lambda: DummyPredictData())

    client = app_module.app.test_client()
    response = client.post(
        "/predictdata",
        data={
            "gender": "male",
            "ethnicity": "group A",
            "parental_level_of_education": "high school",
            "lunch": "standard",
            "test_preparation_course": "none",
            "reading_score": "80",
            "writing_score": "85",
        },
    )

    assert response.status_code == 200
    assert calls[0] == "train"
    assert calls[1][0] == "predict"

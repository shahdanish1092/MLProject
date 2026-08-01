from src.pipeline import train_pipeline


def test_run_pipeline_calls_components_in_order(monkeypatch):
    calls = []

    class DummyIngestion:
        def ingestion_pipeline(self):
            calls.append("ingest")
            return "train.csv", "test.csv"

    class DummyTransformation:
        def initiate_data_transformation(self, train_path, test_path):
            calls.append(("transform", train_path, test_path))
            return "train_arr", "test_arr", "preprocessor.pkl"

    class DummyTrainer:
        def initiate_model_training(self, train_arr, test_arr):
            calls.append(("train", train_arr, test_arr))
            return 0.82

    monkeypatch.setattr(train_pipeline, "DataIngestion", lambda: DummyIngestion())
    monkeypatch.setattr(train_pipeline, "DataTransformation", lambda: DummyTransformation())
    monkeypatch.setattr(train_pipeline, "ModelTrainer", lambda: DummyTrainer())

    pipeline = train_pipeline.TrainingPipeline()
    result = pipeline.run_pipeline()

    assert calls[0] == "ingest"
    assert calls[1] == ("transform", "train.csv", "test.csv")
    assert calls[2] == ("train", "train_arr", "test_arr")
    assert result["r2_score"] == 0.82
    assert result["preprocessor_path"] == "preprocessor.pkl"

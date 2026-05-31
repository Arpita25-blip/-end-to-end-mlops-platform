import joblib, os, numpy as np

def test_model_exists():
    assert os.path.exists("models/model.pkl")

def test_model_predicts_valid_class():
    model = joblib.load("models/model.pkl")
    sample = np.array([[13.2,2.77,2.51,18.5,96.6,
                        1.04,2.55,0.57,1.47,6.2,
                        1.05,3.33,820]])
    pred = model.predict(sample)
    assert pred[0] in [0, 1, 2]

def test_model_accuracy_above_90():
    from sklearn.datasets import load_wine
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import pandas as pd
    data = load_wine()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target)
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = joblib.load("models/model.pkl")
    acc = accuracy_score(y_test, model.predict(X_test))
    assert acc > 0.90
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

def load_data():
    df = pd.read_csv("data/traffic.csv")
    return df["vehicles"].values

def build_and_train_model():
    data = load_data()

    data = np.array(data).reshape(-1, 1)

    generator = TimeseriesGenerator(data, data, length=3, batch_size=1)

    model = Sequential([
        LSTM(16, activation="relu", input_shape=(3, 1)),
        Dense(1)
    ])

    model.compile(optimizer="adam", loss="mse")
    model.fit(generator, epochs=50, verbose=0)

    return model

model = build_and_train_model()

def predict_next(value1, value2, value3):
    x = np.array([[value1, value2, value3]]).reshape((1, 3, 1))
    return float(model.predict(x, verbose=0)[0][0])

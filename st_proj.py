import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from imblearn.over_sampling import RandomOverSampler

import copy

import seaborn as sns


df = pd.read_csv("train.csv")
dataset_cols = [
  "Passenger",
  "CryoSleep",
  "HomePlanet",
  "Cabin",
  "Destination",
  "Age",
  "VIP",
  "RoomService",
  "FoodCourt",
  "ShoppingMall",
  "Spa",
  "VRDeck",
  "Transported"
]

df.cols = dataset_cols
df.head()


df = df.drop(["PassengerId"], axis = 1)
df = df.drop(["Name"], axis = 1)


print("Unique Home Planets:", df['HomePlanet'].unique())
planet_map = {"Europa": 1, "Earth": 2, "Mars": 3, np.nan: -1}  # Include np.nan mapping
df["HomePlanet"] = df["HomePlanet"].map(planet_map).fillna(-1).astype(int)  # home planet to int
df.head()
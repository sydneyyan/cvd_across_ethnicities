# -*- coding: utf-8 -*-
"""predicting_on_cross_ethnicities

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OQ-Xg9s_bOL4rgjicNvA-JZzJuvY2VUo
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/drive', force_remount=True)
file_path = '/content/drive/Shareddrives/CS 229 Final Project/cvd-dataset/2022/heart_2022_no_nans.csv'

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import csv
import numpy as np

df=  pd.read_csv(file_path)

from sklearn.model_selection import train_test_split

WHITE = "White only, Non-Hispanic"
HISPANIC = "Hispanic"
BLACK = "Black only, Non-Hispanic"

df_no = df[df['HadHeartAttack'] == "No"]
df_no_sample = df_no.sample(df[['HadHeartAttack']].value_counts()["Yes"])
df_yes = df[df['HadHeartAttack'] == "Yes"]
df_balanced = pd.concat([df_no_sample, df_yes])
X = df_balanced.drop(['HadHeartAttack'], axis=1)
y = df_balanced[["HadHeartAttack"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
df_train = pd.concat([X_train, y_train], axis=1)

df_yes_white = df_yes[df_yes['RaceEthnicityCategory'] == WHITE]
df_no_white_sample = df_no[df_no['RaceEthnicityCategory'] == WHITE].sample(df_yes_white['HadHeartAttack'].value_counts()["Yes"])
df_yes_hispanic = df_yes[df_yes['RaceEthnicityCategory'] == HISPANIC]
df_no_hispanic_sample = df_no[df_no['RaceEthnicityCategory'] == HISPANIC].sample(df_yes_hispanic['HadHeartAttack'].value_counts()["Yes"])
df_yes_black = df_yes[df_yes['RaceEthnicityCategory'] == BLACK]
df_no_black_sample = df_no[df_no['RaceEthnicityCategory'] == BLACK].sample(df_yes_black['HadHeartAttack'].value_counts()["Yes"])

df_white_balanced = pd.concat([df_no_white_sample, df_yes_white])
df_black_balanced = pd.concat([df_no_black_sample, df_yes_black])
df_hispanic_balanced = pd.concat([df_no_hispanic_sample, df_yes_hispanic])
X_white = df_white_balanced.drop(['HadHeartAttack'], axis=1)
y_white = df_white_balanced[['HadHeartAttack']]
df_white = pd.concat([X_white, y_white], axis=1)
X_hispanic = df_hispanic_balanced.drop(['HadHeartAttack'], axis=1)
y_hispanic = df_hispanic_balanced[['HadHeartAttack']]
df_hispanic = pd.concat([X_hispanic, y_hispanic], axis=1)
X_black = df_black_balanced.drop(['HadHeartAttack'], axis=1)
y_black = df_black_balanced[['HadHeartAttack']]
df_black = pd.concat([X_black, y_black], axis=1)

#converting variables into parsable 0s and 1s ()
def convert_values(df_train):
  df_train["y"] = (df_train["HadHeartAttack"] == "Yes").astype(int)
  df_train['had_skin_cancer'] = (df_train["HadSkinCancer"] == "Yes").astype(int)
  df_train['had_depression'] = (df_train["HadDepressiveDisorder"] == "Yes").astype(int)
  df_train['HadKidneyDisease'] = (df_train["HadKidneyDisease"] == "Yes").astype(int)
  df_train["physical_activities"] = (df_train["PhysicalActivities"] == "Yes").astype(int)
  df_train['had_stroke'] = (df_train["HadStroke"] == "Yes").astype(int)
  df_train['HighRiskLastYear'] = (df_train["HighRiskLastYear"] == "Yes").astype(int)
  df_train['sex'] = (df_train["Sex"] == "Male").astype(int)
  df_train["alcohol_drinkers"] = (df_train["AlcoholDrinkers"] == "Yes").astype(int)
  df_train["Black"] = (df_train["RaceEthnicityCategory"] == "Black only, Non-Hispanic").astype(int)
  df_train["White"] = (df_train["RaceEthnicityCategory"] == "White only, Non-Hispanic").astype(int)
  df_train["Hispanic"] = (df_train["RaceEthnicityCategory"] == "Hispanic").astype(int)
  df_train['had_diabetes'] = (df_train["HadDiabetes"] == "Yes").astype(int)
  for s in ['DifficultyConcentrating',
        'DifficultyWalking', 'DifficultyDressingBathing', 'DifficultyErrands', 'HIVTesting','ChestScan', 'HadAsthma', 'CovidPos']:
        df_train[s] = (df_train[s] == "Yes").astype(int)
  df_train['copd'] = (df_train["HadCOPD"] == "Yes").astype(int)
  df_train['had_angina'] = (df_train["HadAngina"] == "Yes").astype(int)
  df_train['had_stroke'] = (df_train["HadStroke"] == "Yes").astype(int)

convert_values(df_train)
convert_values(df_white)
convert_values(df_hispanic)
convert_values(df_black)

X = df_train.drop(['y', 'HadHeartAttack'], axis=1)
y = df_train['y']
train_X, test_X, train_y, test_y = train_test_split(
    X,
    y,
    test_size=.33,
    random_state=42
)

train_X_white, test_X_white, train_y_white, test_y_white = train_test_split(
    df_white.drop(['y', 'HadHeartAttack'], axis=1),
    df_white['y'],
    test_size=.33,
    random_state=42)

train_X_hispanic, test_X_hispanic, train_y_hispanic, test_y_hispanic = train_test_split(
    df_hispanic.drop(['y', 'HadHeartAttack'], axis=1),
    df_hispanic['y'],
    test_size=.33,
    random_state=42
)
train_X_black, test_X_black, train_y_black, test_y_black = train_test_split(
    df_black.drop(['y', 'HadHeartAttack'], axis=1),
    df_black['y'],
    test_size=.33,
    random_state=42
)
total_X_black = df_black.drop(['y', 'HadHeartAttack'], axis=1)
total_y_black = df_black['y']
total_X_hispanic = df_hispanic.drop(['y', 'HadHeartAttack'], axis=1)
total_y_hispanic = df_hispanic['y']
test_white_together = pd.concat([test_X_white, test_y_white], axis=1)

from sklearn.linear_model import LinearRegression

good_cols = [
    "DifficultyConcentrating",
    "DifficultyDressingBathing",
    "DifficultyErrands",
    "sex",
    "HadKidneyDisease",
    "copd",
    "PhysicalHealthDays",
    "had_stroke",
    "had_diabetes",
    "DifficultyWalking",
    "ChestScan",
    "had_angina",
    "physical_activities",
    "alcohol_drinkers"
]

reg = LinearRegression()
reg.fit(train_X[good_cols], train_y)
reg.coef_

linear_test_y_pred = reg.predict(test_X[good_cols])

linear_test_y_pred

from sklearn.metrics import f1_score, confusion_matrix
f1 = f1_score(test_y, linear_test_y_pred > .5)
confusion = confusion_matrix(test_y, linear_test_y_pred > .5)

confusion



train_X['RaceEthnicityCategory'].value_counts()

def ethnic_subset(train_X, train_y, test_X, test_y, category):
  subset_train = (train_X['RaceEthnicityCategory']==category)
  subset_test = (test_X['RaceEthnicityCategory']==category)
  subset_X = train_X[subset_train]
  subset_y = train_y[subset_train]
  subset_test_X = test_X[subset_test]
  subset_test_y = test_y[subset_test]
  return subset_X, subset_y, subset_test_X, subset_test_y

#next goal: testing light gbm trained on whites on white and other datasets
#first, run white_model_on others with model = light gbm
#next, run train_ethnic with model = light gbm-- NOTE: function needs to be edited to generate Shapley curves for light gbm

def white_model_on_others(model):
  model = lgb.LGBMClassifier(learning_rate=0.1, max_depth=-5, random_state=42)
  model.fit(train_X_white[good_cols], train_y_white)
  pred_black = model.predict(total_X_black[good_cols])
  pred_hispanic = model.predict(total_X_hispanic[good_cols])
  f1_black = f1_score(total_y_black, pred_black)
  f1_hispanic = f1_score(total_y_hispanic, pred_hispanic)
  f1_whites = []
  for i in range(100):
    test_sample = test_white_together.sample(total_X_black.shape[0])
    test_sample_X = test_sample.drop(['y'], axis=1)
    test_sample_y = test_sample['y']
    pred_white = model.predict(test_sample_X[good_cols])
    f1 = f1_score(test_sample_y, pred_white)
    f1_whites.append(f1)

  return f1_whites, f1_hispanic, f1_black

import shap
from shap import KernelExplainer
from lightgbm import LGBMClassifier
lgb_model = LGBMClassifier

[f1_white, f1_hispanic, f1_black] = white_model_on_others(lgb_model)
print([f1_white, f1_hispanic, f1_black])

print(np.mean(f1_white))
print(np.mean(f1_black))
print(np.mean(f1_hispanic))

def train_ethnic(model_type):
  white_model = model_type()
  white_model.fit(train_X_white[good_cols], train_y_white)
  pred_white = white_model.predict(test_X_white[good_cols])
  f1_white = f1_score(pred_white, test_y_white)
  pred_hw = white_model.predict(test_X_hispanic[good_cols])
  f1_h_on_w = f1_score(pred_hw, test_y_hispanic)
  pred_bw = white_model.predict(test_X_black[good_cols])
  f1_b_on_w = f1_score(pred_bw, test_y_black)




  hispanic_model = model_type()
  hispanic_model.fit(train_X_hispanic[good_cols], train_y_hispanic)
  pred_hispanic = hispanic_model.predict(test_X_hispanic[good_cols])
  f1_hispanic = f1_score(pred_hispanic, test_y_hispanic)
  pred_wh = hispanic_model.predict(test_X_white[good_cols])
  f1_w_on_h = f1_score(pred_wh, test_y_white)
  pred_bh = hispanic_model.predict(test_X_black[good_cols])
  f1_b_on_h = f1_score(pred_bh, test_y_black)



  black_model = model_type()
  black_model.fit(train_X_black[good_cols], train_y_black)
  pred_black = black_model.predict(test_X_black[good_cols])
  f1_black = f1_score(pred_black, test_y_black)
  pred_wb = black_model.predict(test_X_white[good_cols])
  f1_w_on_b = f1_score(pred_wb, test_y_white)
  pred_hb = black_model.predict(test_X_hispanic[good_cols])
  f1_h_on_b = f1_score(pred_hb, test_y_hispanic)

  return [f1_white, f1_hispanic, f1_w_on_b, f1_h_on_b, f1_w_on_h, f1_b_on_h, f1_h_on_w, f1_b_on_w]

lgb_model = LGBMClassifier

print(train_ethnic(lgb_model))

from sklearn.linear_model import LogisticRegression
print(train_ethnic(LogisticRegression))

!pip install shap

import shap
from shap import KernelExplainer
from lightgbm import LGBMClassifier
lgb_model = LGBMClassifier

print(train_ethnic(lgb_model))

from sklearn.neural_network import MLPClassifier
print(train_ethnic(MLPClassifier))
# -*- coding: utf-8 -*-
"""predicting_cross_ethnic_w_analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-8WcPfh0V3x02MrhvYrt3HFVkGHU_Sm
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

df.columns

df[['HadHeartAttack']].value_counts()

df[df['HadHeartAttack'] == "No"]

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

# df_train['ChestScan'] = (df_train["ChestScan"] == "Yes").astype(int)
# df_train['had_asthma'] = (df_train["HadAsthma"] == "Yes").astype(int)
# df_train["covid_pos"] = (df_train["CovidPos"] == "Yes").astype(int)
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

copd = df_white.value_counts(['copd'])
copd[0] / (copd[0] + copd[1])

copd_black = df_black.value_counts(['copd'])
copd_black[0] / (copd_black[0] + copd_black[1])

df_white.corrwith(df_white['y']).sort_values()

df_black.corrwith(df_black['y']).sort_values()

test_white_together.shape

from sklearn.linear_model import LinearRegression

# good_cols = ["physical_activities",
# "alcohol_drinkers",
# "covid_pos",
# "SleepHours",
# "MentalHealthDays",
# "HeightInMeters",
# "BMI",
# "WeightInKilograms",
# "copd",
# "PhysicalHealthDays",
# "had_stroke",
# "had_diabetes",
# "had_angina"]

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

#white_X, white_y, white_test_X, white_test_y = ethnic_subset(train_X, train_y, test_X, test_y, 'White only, Non-Hispanic')
#white_reg = LinearRegression()
#white_reg.fit(white_X[good_cols], white_Y)
#linear_pred = white_reg.predict(white_test_X[good_cols])
#f1 = f1_score(white_test_y, linear_pred > .5)
#f1

#hispanic_X, hispanic_y, hispanic_test_X, hispanic_test_y = ethnic_subset(train_X, train_y, test_X, test_y, 'Hispanic')
#hispanic_reg = LinearRegression()
#hispanic_reg.fit(hispanic_X[good_cols], hispanic_y)
#linear_pred = hispanic_reg.predict(hispanic_test_X[good_cols])
#f1 = f1_score(hispanic_test_y, linear_pred > .5)
#f1

#black_X, black_y, black_test_X, black_test_y = ethnic_subset(train_X, train_y, test_X, test_y, 'Black only, Non-Hispanic')
#black_reg = LinearRegression()
#black_reg.fit(black_X[good_cols], black_y)
#linear_pred = black_reg.predict(black_test_X[good_cols])
#f1 = f1_score(black_test_y, linear_pred > .5)
#f1

def white_model_on_others(model):
  model.fit(train_X_white[good_cols], train_y_white)
  pred_black = model.predict(total_X_black[good_cols])
  pred_hispanic = model.predict(total_X_hispanic[good_cols])
  f1_black = f1_score(total_y_black, pred_black)
  f1_hispanic = f1_score(total_y_hispanic, pred_hispanic)
  f1_whites = []
  for i in range(1000):
    test_sample = test_white_together.sample(total_X_black.shape[0])
    test_sample_X = test_sample.drop(['y'], axis=1)
    test_sample_y = test_sample['y']
    pred_white = model.predict(test_sample_X[good_cols])
    f1 = f1_score(test_sample_y, pred_white)
    f1_whites.append(f1)

  return f1_whites, f1_hispanic, f1_black

def train_ethnic_nn(model_type):
  white_model = model_type(random_state=1, max_iter=500, activation='logistic', hidden_layer_sizes=(100, 100))
  white_model.fit(train_X_white[good_cols], train_y_white)
  pred_white = white_model.predict(test_X_white[good_cols])
  f1_white = f1_score(pred_white, test_y_white)



  hispanic_model = model_type(random_state=1, max_iter=500, activation='logistic', hidden_layer_sizes=(100, 100))
  hispanic_model.fit(train_X_hispanic[good_cols], train_y_hispanic)
  pred_hispanic = hispanic_model.predict(test_X_hispanic[good_cols])
  f1_hispanic = f1_score(pred_hispanic, test_y_hispanic)



  black_model = model_type(random_state=1, max_iter=500, activation='logistic', hidden_layer_sizes=(100, 100))
  black_model.fit(train_X_black[good_cols], train_y_black)
  pred_black = black_model.predict(test_X_black[good_cols])
  f1_black = f1_score(pred_black, test_y_black)

  explainer_white = KernelExplainer(white_model.predict, sample(test_X_white[good_cols], 100))
  shap_white = explainer_white.shap_values(sample(test_X_white[good_cols], 100), nsamples=50)
  explainer_hispanic = KernelExplainer(hispanic_model.predict, sample(test_X_hispanic[good_cols], 100))
  shap_hispanic = explainer_hispanic.shap_values(sample(test_X_hispanic[good_cols], 100), nsamples=50)
  explainer_black = KernelExplainer(black_model.predict, sample(test_X_black[good_cols], 100))
  shap_black = explainer_black.shap_values(sample(test_X_black[good_cols], 100), nsamples=50)

  return [f1_white, f1_hispanic, f1_black], [shap_white, shap_hispanic, shap_black]

def train_ethnic_log(model_type):
  white_model = model_type()
  white_model.fit(train_X_white[good_cols], train_y_white)
  pred_white = white_model.predict(test_X_white[good_cols])
  f1_white = f1_score(pred_white, test_y_white)



  hispanic_model = model_type()
  hispanic_model.fit(train_X_hispanic[good_cols], train_y_hispanic)
  pred_hispanic = hispanic_model.predict(test_X_hispanic[good_cols])
  f1_hispanic = f1_score(pred_hispanic, test_y_hispanic)



  black_model = model_type()
  black_model.fit(train_X_black[good_cols], train_y_black)
  pred_black = black_model.predict(test_X_black[good_cols])
  f1_black = f1_score(pred_black, test_y_black)

  explainer_white = Explainer(white_model.predict, train_X_white[good_cols])
  shap_white = explainer_white(test_X_white[good_cols].iloc[:100, :])
  explainer_hispanic = Explainer(hispanic_model.predict, train_X_hispanic[good_cols])
  shap_hispanic = explainer_hispanic(test_X_hispanic[good_cols].iloc[:100, :])
  explainer_black = Explainer(black_model.predict, train_X_black[good_cols])
  shap_black = explainer_black(test_X_black[good_cols].iloc[:100, :])

  return [f1_white, f1_hispanic, f1_black], [shap_white, shap_hispanic, shap_black]

from sklearn.linear_model import LogisticRegression

clf_logreg = LogisticRegression()
clf_logreg.fit(train_X[good_cols], train_y)

from shap import Explainer
[f1_white, f1_hispanic, f1_black], [shap_white, shap_hispanic, shap_black] = train_ethnic(LogisticRegression)

from sklearn.neural_network import MLPClassifier
from shap import KernelExplainer
from shap import sample
[f1_white_nn, f1_hispanic_nn, f1_black_nn], [shap_white_nn, shap_hispanic_nn, shap_black_nn] = train_ethnic_nn(MLPClassifier)

f1_white

f1_hispanic

f1_black

from shap import summary_plot
summary_plot(shap_white, test_X_white[good_cols].iloc[:100, :], plot_type='bar')

summary_plot(shap_hispanic, test_X_hispanic[good_cols].iloc[:100, :], plot_type='bar')

summary_plot(shap_black, test_X_black[good_cols].iloc[:100, :], plot_type='bar')

f1_white_nn

f1_hispanic_nn

f1_black_nn

summary_plot(shap_white_nn, test_X_white[good_cols].iloc[:100, :], plot_type='bar')

summary_plot(shap_hispanic_nn, test_X_white[good_cols].iloc[:100, :], plot_type='bar')

summary_plot(shap_black_nn, test_X_white[good_cols].iloc[:100, :], plot_type='bar')

logreg_ethnic = LogisticRegression()
f1_whites_log, f1_hispanic_log, f1_black_log = white_model_on_others(logreg_ethnic)

len(np.where(f1_whites_log < f1_black_log)[0])

from sklearn.neighbors import KNeighborsClassifier
knn_ethnic = KNeighborsClassifier(n_neighbors=3)
f1_whites_knn, f1_hispanic_knn, f1_black_knn = white_model_on_others(knn_ethnic)

#from sklearn.neural_network import MLPClassifier

nn_ethnic = MLPClassifier(random_state=1, max_iter=300, activation='logistic', hidden_layer_sizes=(100, 100))
f1_whites_nn, f1_hispanic_nn, f1_black_nn = white_model_on_others(nn_ethnic)

len(np.where(f1_whites_nn < f1_black_nn)[0])

def z_score(f1_whites, f1_other):
  return (f1_other - np.mean(f1_whites)) / np.std(f1_whites)

z_score(f1_whites_nn, f1_black_nn)

#log_y_pred = clf_logreg.predict(test_X[good_cols])

pip install shap

from shap import KernelExplainer
from shap import Explainer



explainer_log = Explainer(clf_logreg.predict, train_X[good_cols])
shap_values = explainer_log(test_X[good_cols].iloc[:100, :])

from shap import summary_plot
summary_plot(shap_values, train_X[good_cols].iloc[:100, :], plot_type='bar')

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
clf.fit(train_X[good_cols], train_y)

rfc_test_y_pred = clf.predict(test_X[good_cols])



rfc_test_y_pred

clf2 = RandomForestClassifier(n_estimators=50)
clf2.fit(train_X[good_cols], train_y)

rfc2_test_y_pred = clf2.predict(test_X[good_cols])



!pip install lightgbm

import lightgbm

model = lightgbm.LGBMClassifier(learning_rate=0.09,max_depth=-5,random_state=42)

model.fit(train_X[good_cols],train_y,eval_set=[(test_X[good_cols],test_y)],eval_metric='r2_score')

print('Training accuracy {:.4f}'.format(model.score(train_X[good_cols],train_y)))
print('Testing accuracy {:.4f}'.format(model.score(test_X[good_cols],test_y)))

from sklearn.neural_network import MLPClassifier
clf_best = MLPClassifier(random_state=1, max_iter=300, activation='logistic', hidden_layer_sizes=(100, 100)).fit(train_X[good_cols], train_y)
#clf_best.predict_proba(test_X[good_cols])
#predictions = clf.predict(test_X[good_cols])





from shap import sample
nn_explainer = KernelExplainer(clf_best.predict, sample(test_X[good_cols], 100))
shap_nn_values = nn_explainer.shap_values(sample(test_X[good_cols], 100), nsamples=50)

summary_plot(shap_nn_values, test_X[good_cols].iloc[:100, :], plot_type='bar')



pip install shap

from shap import force_plot
shap_nn_values
#force_plot(nn_explainer.expected_value, shap_nn_values)

predictions = {}
for a in ['relu', 'logistic', 'tanh']:
  for i in [(100,), (10,), (200,), (300,)]:
    clf = MLPClassifier(hidden_layer_sizes=i, activation=a, random_state=1, max_iter=300).fit(train_X[good_cols], train_y)
    clf.predict_proba(test_X[good_cols])
    predictions[(a, i)] = clf.predict(test_X[good_cols])

predictions_multi = {}
for a in ['relu', 'logistic', 'tanh']:
  for i in [(10,10), (100,100,), (100,10,), (10,100,)]:
    clf = MLPClassifier(hidden_layer_sizes=i, activation=a, random_state=1, max_iter=300).fit(train_X[good_cols], train_y)
    clf.predict_proba(test_X[good_cols])
    predictions_multi[(a, i)] = clf.predict(test_X[good_cols])

predictions_layer = {}
for a in ['relu', 'logistic', 'tanh']:
  for i in [(100,), (100, 100), (100, 100, 100), (100, 100, 100, 100,)]:
    clf = MLPClassifier(hidden_layer_sizes=i, activation=a, random_state=1, max_iter=1000).fit(train_X[good_cols], train_y)
    clf.predict_proba(test_X[good_cols])
    predictions_layer[(a, i)] = clf.predict(test_X[good_cols])

scores_nn = {key: f1_score(predictions_layer[key], test_y) for key in predictions_layer}
scores_nn



confusion_nn = confusion_matrix(test_y, predictions)
score = clf.score(test_X[good_cols], test_y)
score

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_X[good_cols], train_y)
knn_predict = knn.predict(test_X[good_cols])

f1_knn = f1_score(knn_predict, test_y)
confusion_knn = confusion_matrix(knn_predict, test_y)
f1_knn
confusion_knn

pip install shap

from sklearn.preprocessing import StandardScaler
from shap.explainers import Linear
from shap.plots import scatter
scaler = StandardScaler()
scaler.fit(train_X[good_cols])
train_X_scaled = scaler.transform(train_X[good_cols])
scaled_reg = LinearRegression()
scaled_reg.fit(train_X_scaled, train_y)
explainer_linear = Linear(scaled_reg, train_X_scaled)
shap_values = explainer_linear(train_X_scaled)

scatter(shap_values[:, 11])
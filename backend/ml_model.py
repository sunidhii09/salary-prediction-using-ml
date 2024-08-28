import pandas as pd

df=pd.read_csv('Salary Data.csv')
df=df.dropna()
df=df.drop_duplicates()


from sklearn.preprocessing import LabelEncoder

job_title_encoder = LabelEncoder()
df['Job Title'] = job_title_encoder.fit_transform(df['Job Title'])

gender_encoder = LabelEncoder()
df['Gender'] = gender_encoder.fit_transform(df['Gender'])

education_level_encoder = LabelEncoder()
df['Education Level'] = education_level_encoder.fit_transform(df['Education Level'])

X=df.drop('Salary', axis=1)
Y=df['Salary']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.25, random_state=10)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.fit_transform(X_test)

from sklearn.linear_model import LinearRegression
mlr=LinearRegression()
mlr.fit(X_train, Y_train)

Y_pred=mlr.predict(X_test)

import joblib
joblib.dump(mlr, 'mlr_model.pkl')
joblib.dump(ss, 'standard_scaler.pkl')
joblib.dump(job_title_encoder, 'job_title_encoder.pkl')
joblib.dump(gender_encoder, 'gender_encoder.pkl')
joblib.dump(education_level_encoder, 'education_level_encoder.pkl')


print("Classes in Job Title Encoder:", job_title_encoder.classes_)
print("Classes in Gender Label Encoder:", gender_encoder.classes_)
print("Classes in Education Label Encoder:", education_level_encoder.classes_)
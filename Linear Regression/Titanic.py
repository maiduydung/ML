import streamlit as st
import pandas as pd
import random as rnd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

st.title('Titanic survivor prediction')
train_df = pd.read_csv('../datasets/titanic/train.csv')
test_df = pd.read_csv('../datasets/titanic/test.csv')
combine = [train_df, test_df]

st.write("Training data")
st.write(train_df)

st.write("Correlation graph")
corr_fig = plt.figure()
sns.heatmap(train_df.corr(),annot=True)
st.pyplot(corr_fig)



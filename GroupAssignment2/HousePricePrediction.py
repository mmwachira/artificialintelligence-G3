import pandas as pd  # data processing
import numpy as np  # working with arrays
import matplotlib.pyplot as plt  # visualization
import seaborn as sb  # visualization
from termcolor import colored as cl  # text customization
from sklearn.model_selection import train_test_split  # data split
from sklearn.linear_model import Ridge  # Ridge algorithm

sb.set_style('whitegrid')  # plot style
plt.rcParams['figure.figsize'] = (20, 10)  # plot size

# IMPORTING DATA

df = pd.read_excel('Housing.xlsx')
print(df.head(5))

# DATA VISUALIZATION
# 1. Heat Map
sb.heatmap(df.corr(), annot=True, cmap='magma')

plt.savefig('heatmap.png')
plt.show()

# 2. Distribution plot

sb.distplot(df['price'], color='r')
plt.title('Price Distribution', fontsize=16)
plt.xlabel('price', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig('displot.png')
plt.show()

# FEATURE SELECTION & DATA SPLIT

X_var = df[['lotsize', 'bedrooms', 'bathrms', 'stories', 'garagepl']].values
y_var = df['price'].values

X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size=0.2, random_state=0)

print(cl('X_train samples : ', attrs=['bold']), X_train[0:5])
print(cl('X_test samples : ', attrs=['bold']), X_test[0:5])
print(cl('y_train samples : ', attrs=['bold']), y_train[0:5])
print(cl('y_test samples : ', attrs=['bold']), y_test[0:5])

# MODELING
ridgeR = Ridge(alpha=1)
ridgeR.fit(X_train, y_train)
y_pred = ridgeR.predict(X_test)

# calculate mean square error
mean_squared_error_ridge = np.mean((y_pred - y_test) ** 2)
print("The MSE is:", mean_squared_error_ridge)



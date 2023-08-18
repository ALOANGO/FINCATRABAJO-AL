import pickle
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


datosmodelo = pd.read_csv("dataoutlier.csv")

x = datosmodelo[["aream2", "toilets", "garajes", "estrato"]]
y = datosmodelo["precio"]

estandarx = preprocessing.StandardScaler()
# estandary=preprocessing.StandardScaler()


x_estandar = estandarx.fit_transform(x)
# y_estandar=estandary.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(
    x_estandar, y, test_size=0.5, random_state=42
)

x_val, x_test, y_val, y_test = train_test_split(
    x_test, y_test, test_size=0.5, random_state=42
)

# Create a Linear regressor
lm = LinearRegression()

# Train the model using the training sets
lm.fit(x_train, y_train)


#guardar scaler
pickle.dump(estandarx, open('scalerlinear.pkl','wb'))

#guardar modelo
pickle.dump(lm, open("price.pkl", "wb"))


import xlwings as xw
from sklearn.linear_model import LinearRegression
import numpy as np

@xw.sub
def main():
    pass
#     wb = xw.Book.caller()
#     # wb.sheets[0].range("A1").value = "Hello From xlwings"

# # @xw.func
# # def hello(name):
# #     return f"Hello {name}!"

@xw.func
@xw.arg('X_train', np.array, ndim=2)
@xw.arg('y_train', np.array, ndim=2)
@xw.arg('X_new', np.array, ndim=2)
def predict_lr(X_train, y_train, X_new):
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X=X_new)

    return y_pred

if __name__ == "__main__":
    xw.Book("python_vba.xlsm").set_mock_caller()
    main()

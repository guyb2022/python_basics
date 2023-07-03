import xlwings as xw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


class ExcelBook:
    def __init__(self):
        self.caller = None
        self.xw = None

    def get_df(self, sheet):
        self.caller = xw.Book.caller()
        sht = self.caller.sheets[sheet]
        df = sht.range("A2").options(pd.DataFrame, index=False, expand='table').value
        return df

    def insert_picture_to_excel(self, sht, cell, fig, pic_name):
        for picture in sht.pictures:
            if picture.name == pic_name:
                picture.delete()
        sht.pictures.add(
            fig,
            name=pic_name,
            update=True,
            left=sht.range(cell).left,
            top=sht.range(cell).top,
            height=200,
            width=300,
        )
        return None

    def scatter_chart(self, source, target, hue, place, sheet):
        """ Plot scatter plot with seaborn"""
        self.caller = xw.Book.caller()
        sht = self.caller.sheets[sheet]
        df = self.get_df(sheet)
        fig = plt.figure()
        # plt.title(f"{target} By {source}")
        sns.scatterplot(data=df, x=source, y=target, hue=hue, style="time")
        self.insert_picture_to_excel(sht=sht, cell=place, fig=fig,
                                     pic_name=f"scatter {source} {target}")

    def bar_chart(self, source, target, place, sheet):
        """
        Plot a Bar Graph for two selected columns.
        y: target
        x: source
        place: position of the chart
        sheet: WIP drop out
        """
        self.caller = xw.Book.caller()
        sht = self.caller.sheets[sheet]
        df = self.get_df(sheet)
        fig = plt.figure()
        x = df[source]
        y = df[target]
        plt.bar(x, y)
        plt.grid(False)
        plt.ylabel("in USD")
        plt.title(f"{target} Amount By {source}")
        self.insert_picture_to_excel(sht=sht, cell=place, fig=fig,
                                     pic_name=f"bar {source} {target}")

    def predict_lr(self, X_train, y_train, X_new):
        clf = LinearRegression()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X=X_new)

        return y_pred

    def CORREL2(self, x):
        return x.corr()

    def corr_plot(self, corr, place, sheet):
        caller = xw.Book.caller()
        sht = caller.sheets[sheet]
        fig = plt.figure()
        ax = sns.heatmap(corr, cmap='coolwarm', vmin=-1, vmax=1, linewidths=.5,
                         xticklabels=True, yticklabels=True)
        ax.tick_params(left=False, bottom=False)
        plt.yticks(rotation=0)
        plt.xticks(rotation=90)
        self.insert_picture_to_excel(sht=sht, cell=place, fig=fig,
                                     pic_name=f"corr plot")

        return 'Corr Plot'

excelBook = ExcelBook()

# xlwings wrapper functions
@xw.func
@xw.arg('source')
@xw.arg('target')
@xw.arg('place')
def barChart(source, target, place):
    excelBook.bar_chart(source, target, place,'sheet3')
    return "Bar Chart"

@xw.func
@xw.arg('source')
@xw.arg('target')
@xw.arg('place')
@xw.arg('hue')
def scatterChart(source, target, hue, place):
    # sheet3 can be droped later on.
    excelBook.scatter_chart(source, target, hue, place,'sheet3')
    return "Scatter Chart"

@xw.func
@xw.arg('X_train', np.array, ndim=2)
@xw.arg('y_train', np.array, ndim=2)
@xw.arg('X_new', np.array, ndim=2)
def predictLr(X_train, y_train, X_new):
    return excelBook.predict_lr(X_train, y_train, X_new)

@xw.func
@xw.arg('x', pd.DataFrame)
def correlation(x):
    return excelBook.CORREL2(x)

@xw.func
@xw.arg('corr')
@xw.arg('place')
def CorrPlot(corr, place):
    return excelBook.corr_plot(corr, place, 'Sheet2')

@xw.func
def df_man():
    return excelBook.df_manipulation('sheet3')

if __name__ == '__main__':
    excelBook.xw.Book("python_vba.xlsm").set_mock_caller()
    ExcelBook.caller = xw.Book.caller()


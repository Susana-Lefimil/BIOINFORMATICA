from sklearn.metrics import mean_squared_error, r2_score, median_absolute_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from sklearn.metrics import roc_curve

def variables_insp(df):
    """Devuelve frecuencias de las variables de un dataframe """
    v_categoricas = []
    for n, i in enumerate(df):
        if df[i].dtypes =="object":
            #print(df[i].dtypes)
            #print(df[i])
            v_categoricas.append(i)
    for i in v_categoricas:
        print("\n",i)
        print(df[i].value_counts())

def retorna_valores(df):
    """Imprime variables discretas (números enteros) de un dataframe """
    variables_discretas = df.select_dtypes(include=['int64'])
    print("Freecuencia de variables discretas")
    for i in variables_discretas.columns:
        print(display(df[i].value_counts()))      
        
def var_categoricas(df):
    """Imprime variables categóricas de un dataframe  """
    v_cat = []
    for n, i in enumerate(df):
        if df[i].dtypes =="object":
            #print(df[i].dtypes)
            #print(df[i])
            v_cat.append(i)
    return v_cat

def variables_categoricas(df):
    """ Listado de variables categoricas"""
    list(df.select_dtypes(object).columns)
    
def df_binarizado(df,variables_categoricas):
    "Para binarizacion de variables"
    df_binarizado=(pd.get_dummies(data=df
        , columns=variables_categoricas
        , drop_first=True
        , dtype='int64'))
    return df_binarizado
       
def metricas(modelo, X_test, y_test):
    """Metricas de validacion"""
    print("Test MSE:", mean_squared_error(y_test, modelo.predict(X_test)).round(5))
    print("Test MAE:", median_absolute_error(y_test, modelo.predict(X_test)).round(5))
    print("Test R2:", r2_score(y_test, modelo.predict(X_test)).round(5))
    # Diccionario - > DataFrame
    data_d = {
        'Test_MSE': [mean_squared_error(y_test, modelo.predict(X_test)).round(5)],
        'Test_MAE': [median_absolute_error(y_test, modelo.predict(X_test)).round(5)],
        'Test_R2': [r2_score(y_test, modelo.predict(X_test)).round(5)]}  
    data_f=pd.DataFrame(data_d)
    return  data_f

def report_scores(prediction_test, vector):
    """Cálculo del error cuadratico medio y R cuadrado para un modelo de regresión lineal """
    #Realizamos métricas 
    mse=mean_squared_error(vector, prediction_test).round(3)
    r2=r2_score(vector, prediction_test).round(3)
    print(f'Error cuadrático medio: ', mse, 'R2: ', r2)
    
def fetch_features(df, vector):
        """ Listado de correlaciones con vector"""
        # nombres de las columnas 
        columnas = df.columns
        # array para nombre de la variable
        attr_name = []
        # array para correlación de pearson
        pearson_r = []
        # array para valor absoluto de la correlación
        abs_pearson_r = []
    
        for c in columnas:
        # si la columna no es la dependiente
            if c != vector:
                # adjuntar el nombre de la variable en attr_name
                attr_name.append(c)
                # adjuntar la correlación de pearson
                pearson_r.append(df[c].corr(df[vector]))
                # adjuntar el absoluto de la correlación de pearson
                abs_pearson_r.append(abs(df[c].corr(df[vector])))
            
        # El arrays se transforma en DataFrame
        features = pd.DataFrame({
        'attribute': attr_name,
        'corr':pearson_r,
        'abs_corr':abs_pearson_r
        })
        # Se crea el index con los nombres de las variables
        features = features.set_index('attribute')
        # ordenamos los valores de forma descendiente
        features=features.sort_values(by=['abs_corr'], ascending=False)
        return features
    
def grafico_atr(df):    
        """ Gráfico de atributos de un df"""
        plt.rcParams['figure.figsize']=(16, 20)
        rows = 4; cols = df.shape[1] / rows
        for index, (colname, serie) in enumerate(df.iteritems()):
            plt.subplot(rows, cols, index + 1)
            if pd.api.types.is_float_dtype(serie) is True:
                sns.distplot(serie)
                plt.axvline(np.mean(serie), color='tomato')
            elif pd.api.types.is_integer_dtype(serie) is True:
                sns.countplot(serie)
                plt.title(colname, fontsize=16)
                plt.xlabel('');plt.ylabel('');plt.tight_layout()
                
                
                
def curva_roc(model, X_test, y_test):
    "Permite graficar la curva roc para visualizar verdaderos positivos y falsos positivos"
    # reestimamos los valores predichos de nuestro modelo para obtener la probabilidad entre 0 y 1.
    yhat2 = model.predict_proba(X_test)[:, 1]

    # generamos los objetos de roc_curve
    false_positive, true_positive, threshold = roc_curve(y_test, yhat2)

    plt.rcParams['figure.figsize']=(8, 8)
    # Plot ROC curve
    plt.title('Curva ROC')
    plt.plot(false_positive, true_positive, lw=1)
    plt.plot([0, 1], ls="--", lw=1)
    plt.plot([0, 0], [1, 0] , c='limegreen', lw=3), plt.plot([1, 1] ,
    c='limegreen', lw=3)
    plt.ylabel('Verdaderos Positivos')
    plt.xlabel('Falsos Positivos');
from dash import html,dcc
import pandas as pd
import dash_bootstrap_components as dbc


class dict_list:
    def __init__(self, options):
        self.options = options
        
    def dic_op(self):
        t1=self.options.DEPARTAMENTO
        a_options=[]
        a_options.append({'label':'TODOS','value':'TODOS'})
        for i in range(t1.shape[0]):
            a_options.append({"label": str(t1.iloc[i]), "value": str(t1.iloc[i])})
        return a_options
    
    def listav(self):
        listav=list(self.options.DEPARTAMENTO)
        return listav

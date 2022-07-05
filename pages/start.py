from dash_labs.plugins import register_page
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as psx
register_page(__name__,path='/')


layout = html.Div(

    children=[dbc.Container(html.H1("Irregularity Detection in Public Procurements")),dbc.Container([html.H3('Background',style={'textAlign':'center'}),html.P(
        """Our client, Colombia Compra eficiente, is the governing body for public procurements in Colombia. They have tasked us with building a system
        that could detect anomalous contracts. We have leveraged machine learning, natural language processing and statistical analysis to fulfill this task."""
    )
    ],style={'background-color':'#DCD6F7'},className="h-100" )

    , dbc.Container([dbc.Row(html.H3('Impact',style={'textAlign':'center'})),dbc.Row(html.P(
        """Corruption and mismanagement of public funds is a longtime issue in Colombia. It costs the country around xxx billions yearly in money lost to corruption.
        It is enough to check the news to see the reach of this problem. We think this project could have a huge impact, increasing oversight in how public funds are managed
        helping fight corruption and making sure our tax money is put to good use."""
    )),
    dbc.Row(
        [dbc.Col(
        dbc.Card(
    [
        dbc.CardImg(src="/assets/news1.png", top=True),
        dbc.CardBody(
            [
               
                
                dbc.Button("Go to news Article", color="primary",href='https://www.eltiempo.com/justicia/delitos/procuraduria-inicia-juicio-disciplinario-por-contrato-con-centros-poblados-633895'),
            ]
        ),
    ],
    style={"width": "18rem"},
)),
dbc.Col(
        dbc.Card(
    [
        dbc.CardImg(src="/assets/news2.png", top=True),
        dbc.CardBody(
            [
               
                
                dbc.Button("Go to news Article", color="primary",href='https://www.semana.com/nacion/articulo/corrupcion-en-el-pae-panes-mordidos-por-ratones-alimentos-en-mal-estado-y-falta-de-cubiertos/202206/'),
            ]
        ),
    ],
    style={"width": "18rem"},
))]
    )
    ],style={'background-color':'#CACFD6'}) ,
    
    
    dbc.Container([html.H3('Our Team',style={'textAlign':'center'}),html.P(
        """We are a multidisciplinary team, including professional in varied disciplines including Computer Science, Mathematics, Engineering and Economics.
        We are extremely enthusiastic about this project both from a technical standpoint and as citizens of Colombia. To get to know our team better,visit our About us page."""
    )
    ],style={'background-color':'#DCD6F7'})
    
    
    
    
    
    ])

























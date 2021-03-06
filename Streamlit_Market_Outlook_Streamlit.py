import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
from pandas.plotting import table

############ pull back from google ############
sheet_id=st.secrets.db_credentials.password

df_indice_table   = "https://docs.google.com/spreadsheets/d/" + sheet_id +  "/gviz/tq?tqx=out:csv&sheet=" +  'df_indice_table'
df_indice_chart   = "https://docs.google.com/spreadsheets/d/" + sheet_id +  "/gviz/tq?tqx=out:csv&sheet=" +  'df_indice_chart'
indices_full_name = "https://docs.google.com/spreadsheets/d/" + sheet_id +  "/gviz/tq?tqx=out:csv&sheet=" +  'indices_full_name'


df_indice_table = pd.read_csv(df_indice_table)
df_indice_chart = pd.read_csv(df_indice_chart)
indices_full_name = pd.read_csv(indices_full_name)

#convert date to right format##
df_indice_chart['Date']       = pd.to_datetime(df_indice_chart['Date'].str[:10], errors='ignore')

#######################################

st.set_page_config(layout="wide")

##### plot graph here #######

Table_Yest_chg_col_sum = df_indice_table['Yest%color'].values.tolist()
Table_1mth_chg_col_sum = df_indice_table['1mth%color'].values.tolist()
Table_3mth_chg_col_sum = df_indice_table['3mth%color'].values.tolist()
Table_6mth_chg_col_sum = df_indice_table['6mth%color'].values.tolist()
Table_YTD_chg_col_sum  = df_indice_table['YTD%color'].values.tolist()
Table_1yr_chg_col_sum  = df_indice_table['1yr%color'].values.tolist()
Table_3yr_chg_col_sum  = df_indice_table['3yr%color'].values.tolist()

today_run_date = df_indice_table['Today'].iloc[0]

df_indice_table2 = df_indice_table.filter(['Continent','Name','Price','Yest%','1mth%','3mth%','6mth%','YTD%','1yr%','3yr%'])


plt.figure(figsize=(20,8))

########################### table #########################
ax = plt.subplot(20,2,1)
ax.set_title( today_run_date )

ax.axis('off')

tbl = table(ax, df_indice_table2,)
tbl.auto_set_font_size(False)
tbl.auto_set_column_width(col=list(range(len(df_indice_table2.columns))))
tbl.set_fontsize(10)
tbl.scale(2.5,2.5)

for y, val in enumerate(Table_Yest_chg_col_sum, start=1):
    tbl[(y,3)].get_text().set_color(val) 
    
for y, val in enumerate(Table_1mth_chg_col_sum, start=1):
    tbl[(y,4)].get_text().set_color(val) 
    
for y, val in enumerate(Table_3mth_chg_col_sum, start=1):
    tbl[(y,5)].get_text().set_color(val) 
    
for y, val in enumerate(Table_6mth_chg_col_sum, start=1):
    tbl[(y,6)].get_text().set_color(val) 
    
for y, val in enumerate(Table_YTD_chg_col_sum, start=1):
    tbl[(y,7)].get_text().set_color(val) 
    
for y, val in enumerate(Table_1yr_chg_col_sum, start=1):
    tbl[(y,8)].get_text().set_color(val) 
    
for y, val in enumerate(Table_3yr_chg_col_sum, start=1):
    tbl[(y,9)].get_text().set_color(val) 

###fill colour
for x in range (1,8):
    for y in range (0,10):
        tbl[(x, y)].set_facecolor("#87CEEB")
    
for x in range (8,11):
    for y in range (0,10):
        tbl[(x, y)].set_facecolor("#FFA07A")    
        
for x in range (11,14):
    for y in range (0,10):
        tbl[(x, y)].set_facecolor("#B0C4DE")    
 

########################### graph #########################   

st.header('Market Outlook')


# Title the app
st.subheader('World Indices') 


df_indice_chart['YTD%'] = round((((df_indice_chart['Adj Close']/df_indice_chart["_YTD_fix"])-1)*100),2)

df_indice_chart2 = df_indice_chart[df_indice_chart.Year == int(today_run_date[0:4])]

trend_ST         = df_indice_chart2[df_indice_chart2.Name == 'Straits_Time']
trend_Shanghai   = df_indice_chart2[df_indice_chart2.Name == 'Shanghai']
trend_HS         = df_indice_chart2[df_indice_chart2.Name == 'Hang_Seng']
trend_Kospi      = df_indice_chart2[df_indice_chart2.Name == 'Kospi']
trend_Nikkei     = df_indice_chart2[df_indice_chart2.Name == 'Nikkei_225']
trend_Nifty      = df_indice_chart2[df_indice_chart2.Name == 'Nifty_50']
trend_ASX        = df_indice_chart2[df_indice_chart2.Name == 'S&P/ASX_200']

trend_FTSE       = df_indice_chart2[df_indice_chart2.Name == 'FTSE_100']
trend_DAX        = df_indice_chart2[df_indice_chart2.Name == 'DAX']
trend_EURONext   = df_indice_chart2[df_indice_chart2.Name == 'EURONext_100']

trend_SandP      = df_indice_chart2[df_indice_chart2.Name == 'S&P_500']
trend_DJ         = df_indice_chart2[df_indice_chart2.Name == 'Dow_Jones']
trend_Nasdaq     = df_indice_chart2[df_indice_chart2.Name == 'Nasdaq']
   
axg = plt.subplot(122)
axg.plot(trend_ST['Date'],trend_ST['YTD%'], label = "Straits Time",linestyle="--",)
axg.plot(trend_Shanghai['Date'],trend_Shanghai['YTD%'], label = "Shanghai",)
axg.plot(trend_HS['Date'],trend_HS['YTD%'], label = "Hang Seng",)
axg.plot(trend_Nikkei['Date'],trend_Nikkei['YTD%'], label = "Nikkei",)
axg.plot(trend_FTSE['Date'],trend_FTSE['YTD%'], label = "FTSE",)
axg.plot(trend_Nasdaq['Date'],trend_Nasdaq['YTD%'], label = "Nasdaq",)
axg.plot(trend_SandP['Date'],trend_SandP['YTD%'], label = "S&P", linestyle="dashdot")

axg.legend(loc=0, prop={'size': 10}, framealpha=0.8,)
#axg.legend()
axg.grid(linestyle = 'dashed', linewidth = 0.8)

plt.gcf().autofmt_xdate()

st.pyplot(fig=plt)


def chart_stock(select_stock1, select_stock2, period, secondary):

    #YTD proxy
    YTD = df_indice_chart.loc[df_indice_chart['Name'] == 'Straits_Time'] 
    days = len(YTD[YTD.Year == YTD['Year'].max()])
    
    lists = {'1mth'  :20, 
             '2mth'  :40,
             '6mth'  :120,
             'YTD'   :days,
             '1yr'   :260,
             '3yr'   :780,
             '5yr'   :1300 }    
    

    limit1 = df_indice_chart.loc[df_indice_chart['Name'] == select_stock1] 
    period_1 = limit1.tail(lists[period])
    min1 = period_1['Adj Close'].min()
    max1 = period_1['Adj Close'].max()

    limit2 = df_indice_chart.loc[df_indice_chart['Name'] == select_stock2] 
    period_2 = limit2.tail(lists[period])
    min2 = period_2['Adj Close'].min()
    max2 = period_2['Adj Close'].max()

    stock1 =alt.Chart(period_1).mark_line().encode(
        x=alt.X('Date', axis=alt.Axis( grid=True)),
        y=alt.Y('Adj Close', axis=alt.Axis(grid=True), title=select_stock1, scale=alt.Scale(domain=[min1, max1]) ),
        color=alt.Color('Name', title=None, legend=alt.Legend(orient='none', direction='horizontal',titleAnchor='middle')),
        tooltip=['Date',alt.Tooltip('Adj Close', format=",.3f" )]).interactive() 

    stock2=alt.Chart(period_2).mark_line().encode(
        x=alt.X('Date', axis=alt.Axis( grid=True)),
        y=alt.Y('Adj Close', axis=alt.Axis(grid=True), title=select_stock2, scale=alt.Scale(domain=[min2, max2]) ),
        color=alt.Color('Name', title=None, legend=alt.Legend(orient='none', direction='horizontal',titleAnchor='middle')),
        tooltip=['Date',alt.Tooltip('Adj Close', format=",.3f" )]).interactive() 

    if secondary == 'No' :
        chart = alt.layer(stock1).resolve_scale(y='independent')
    else :
        chart = alt.layer(stock1, stock2).resolve_scale(y='independent')
    
    st.altair_chart(chart, use_container_width=True)
    #return chart
 

period_choose = ['1mth', '2mth', '6mth','YTD', '1yr', '3yr', '5yr']
stock_choose  = indices_full_name['indices_full_name'].values.tolist()

#st.sidebar.markdown('Chart')
period_selection = st.selectbox('Period',period_choose)
stock_selection1  = st.selectbox('Primary',stock_choose)
stock_selection2  = st.selectbox('Secondary',stock_choose)

axis = st.radio("Secondary Axis",('Yes', 'No' ))
    
chart_stock(stock_selection1, stock_selection2 ,period_selection, axis)

########################## SG Reits ##############

############ pull back from google ############
#sheet_id=st.secrets.db_credentials.password


df_reits_table   = "https://docs.google.com/spreadsheets/d/" + sheet_id +  "/gviz/tq?tqx=out:csv&sheet=" +  'df_reits_table'
df_reits_chart   = "https://docs.google.com/spreadsheets/d/" + sheet_id +  "/gviz/tq?tqx=out:csv&sheet=" +  'df_reits_chart'
reits_full_name  = "https://docs.google.com/spreadsheets/d/" + sheet_id +  "/gviz/tq?tqx=out:csv&sheet=" +  'reits_full_name'

df_reits_table = pd.read_csv(df_reits_table)
df_reits_chart = pd.read_csv(df_reits_chart)
reits_full_name = pd.read_csv(reits_full_name)

#convert date to right format##
df_reits_chart['Date']   = pd.to_datetime(df_reits_chart['Date'].str[:10], errors='ignore')


# Title the app
st.subheader('SG Reits') 

#### dataframe ###

#################################################################

def color_negative_red(value):
    if value < 0:
        color = 'red'
    elif value > 0:
        color = 'green'
    else:
        color = 'black'
    return 'color: %s' % color


def color_recommend(s):
    return np.where(s.eq('SELL'),'background-color: Salmon',
                    np.where(s.eq('BUY'),'background-color: YellowGreen',''))


cell_hover = {  # for row hover use <tr> instead of <td>
    'selector': 'td:hover',
    'props': [('background-color', '#ffffb3')]}

border = {'selector' : '',
           'props' : [('border', '1px solid green')]}

#header = {'selector': 'th', 'props': [('font-size', '10pt')]}
#header = {'selector': 'th', 'props': [('background-color', 'LightSalmon')]}

st.dataframe((df_reits_table.style
.applymap(color_negative_red, subset=['Yest%','Adj_Slope_6month'])
.format({'Yest%': "{:.3}",
             'Adj_Slope_6month': "{:.3}", 
             'Close': "{:.3}", 
             'Coming_Div%': "{:.3}", 
             'Collected_Div%': "{:.3}", 
             'Last_yr_Div%': "{:.3}", 
            })
.set_table_styles([border])
.hide_index()
))

st.text('*Days for Dividend refer to Ex-date')

stock_reits_choose  = reits_full_name['ticker_full_name'].values.tolist()
period_reits_choose = ['5day','7day','10day','2mth','6mth','YTD','1yr','3yr','5yr']

stock_reits_selection  = st.selectbox('Reits',stock_reits_choose)
period_reits_selection = st.selectbox('Reits_Period',period_reits_choose)


def chart_reits(reits_choose, reits_period):
    
    df_reits_chart2 = df_reits_chart.loc[df_reits_chart['Name'] == reits_choose]
    
    days = len(df_reits_chart2[df_reits_chart2.Year == df_reits_chart2['Year'].max()])
    
    lists = {'5day' :5, 
             '7day' :7,
             '10day':10,
             '2mth' :40,
             '6mth' :120,
             'YTD'  :days,
             '1yr'  :260,
             '3yr'  :780,
             '5yr'  :1300 } 
    
    df_reits_chart3 = df_reits_chart2.tail(lists[reits_period])
    
    min = df_reits_chart3['Close'].min()
    max = df_reits_chart3['Close'].max()
    
    scale  = alt.Scale(domain=['Close', 'SMA_50', 'SMA_100', 'SMA_200' ], range=['#5681c7', 'Orange', 'SkyBlue', 'DarkSeaGreen'])

    chart = alt.Chart(df_reits_chart3, title=reits_choose).mark_line(strokeDash=[5, 10]).transform_fold(
    fold=['Close', 'SMA_50', 'SMA_100', 'SMA_200'], 
    as_=['variable', 'value']
    ).encode(
    x=alt.X('Date:T',title='',  axis=alt.Axis(format='%e %b, %Y') ), 
    y=alt.Y('value:Q',title='', scale=alt.Scale(domain=[min, max]) ),
    color=alt.Color('variable:N', scale=scale, legend=alt.Legend(title='')),

    tooltip=['Date',alt.Tooltip('Close', format=",.3f" )],
    strokeDash=alt.condition(
        alt.datum.variable == 'Close',
        alt.value([0]),  # solid line
        alt.value([5,5]), )  # dashed line: 5 pixels  dash + 5 pixels space
            ).interactive()
    
    #return chart 
    st.altair_chart(chart, use_container_width=True)
    
chart_reits(stock_reits_selection, period_reits_selection)

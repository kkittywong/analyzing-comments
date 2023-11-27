import pandas as pd
from pyecharts.charts import Map, Pie, Bar, WordCloud, Page, EffectScatter
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import numpy as np
from snownlp import SnowNLP

theme_config = ThemeType.CHALK

table_color = ""
if theme_config == ThemeType.DARK:
    table_color = '#333'
elif theme_config == ThemeType.CHALK:
    table_color = '#293441'   
elif theme_config == ThemeType.PURPLE_PASSION:
    table_color = '#5B5C6E'
elif theme_config == ThemeType.ROMANTIC:
    table_color = '#F0E8CD' 
elif theme_config == ThemeType.ESSOS:
    table_color = '#FDFCF5'              
else:
    table_color = ''   

def pie2():
    df=pd.read_csv('/Users/mankiwong/Desktop/評論內容.csv')
    data=df['評論內容']
    pos_count=0   #積極
    mid_count=0   #中性
    neg_count=0   #消極
    for comment in data:
        comment=str(comment)
        sentiments_score=SnowNLP(comment).sentiments
        if sentiments_score < 0.4:
            neg_count += 1
        elif 0.4 <= sentiments_score <= 0.6:
            mid_count += 1
        else:
            pos_count += 1    

    pie = (
        Pie(init_opts=opts.InitOpts(theme=theme_config, width='450px', height='350px', chart_id=3))
            .add(series_name='評論區情感分布',
                data_pair=[['積極', pos_count], 
                           ['中性', mid_count], 
                           ['消極', neg_count]],
                rosetype='radius',
                radius=['30%', '55%'],
                )
            .set_global_opts(
            legend_opts=opts.LegendOpts(pos_left='right', orient='vertical')
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {c}')))
    
    pie.render('3.html')
    print('success')
    return pie
pie2()

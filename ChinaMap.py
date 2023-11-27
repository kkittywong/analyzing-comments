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

def map():
    df=pd.read_csv('/Users/mankiwong/Desktop/評論內容.csv')
    df['ip地址']=df['ip地址'].astype(str).str.replace('来自', '')
    df['ip地址']=df['ip地址'].astype(str).str.replace('中国', '')
    loc_grp=df.groupby('ip地址').count()['評論內容']
    address_index=loc_grp.index.tolist()
    address_values=loc_grp.values.tolist()

    c=(
        Map(init_opts=opts.InitOpts(chart_id=5,bg_color=table_color))
            .add('評論者地域分布', [list(z) for z in zip(address_index, address_values)],'china')
            .set_global_opts(
            title_opts=opts.TitleOpts(title='評論者在全国的分布图',
                                     title_textstyle_opts=opts.TextStyleOpts(font_size=25,
                                                                            color='#FFF')),
            visualmap_opts=opts.VisualMapOpts(max_=250),                                                                
        )
    )
    c.render('5.html')
    print('success')
    return c
map()

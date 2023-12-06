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

def pie():
    df = pd.read_csv('/Users/mankiwong/Desktop/評論內容.csv')
    df['ip地址'] = df['ip地址'].astype(str).str.replace('来自', '')
    df['ip地址'] = df['ip地址'].astype(str).str.replace('中国', '')
    loc_grp = df.groupby('ip地址').count()['評論內容']
    address_index = loc_grp.index.tolist()
    address_values = loc_grp.values.tolist()

    c = (
        Pie(init_opts = opts.InitOpts(chart_id = 2, bg_color = table_color, theme = ThemeType.CHALK))
        .add('', [list(z) for z in zip(address_index, address_values)])
        .set_global_opts(title_opts = opts.TitleOpts(title = '評論者在全国的分布图',
                                                    title_textstyle_opts = opts.TextStyleOpts(font_size = 25, color = '#fafaf5')),
                                    legend_opts = opts.LegendOpts(orient = 'vertical',
                                    pos_left = '5%',
                                    pos_top = '10%'))
        .set_series_opts(label_opts = opts.LabelOpts(formatter = '{b}: {c}'))                                                               
    )
    c.render('2.html')
    print('success')
    return c
if __name__ == '__main__':
    pie()

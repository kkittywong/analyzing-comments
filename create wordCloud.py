from wordcloud import WordCloud
import jieba
import numpy
import PIL.Image as Image

def cut(text):
    wordlist_jieba = jieba.cut(text)
    space_wordlist = " ".join([word for word in wordlist_jieba if len(word) > 1])
    return space_wordlist

with open("/Users/mankiwong/Desktop/簿3.txt" ,encoding="utf-16")as file:
    text=file.read()
    text=cut(text)

    font='/System/Library/Fonts/Supplemental/Songti.ttc'
    wordcloud = WordCloud(background_color='white',font_path=font,collocations=False,
    width=800,height=500,min_font_size=10,max_font_size=300).generate(text)
    image=wordcloud.to_image()
    # image.show()
    wordcloud.to_file('词云图.png')

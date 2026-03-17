from urlextract import URLExtract
import re
import pandas as pd
import string
import emoji
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

extract=URLExtract()

def fetch_stats(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]

    #Fetch the number of messages
    num_messages=df.shape[0]

    #Fetch the total number of words
    words=[]
    for message in df["message"]:
        words.extend(message.split())

    #Fetch number of media messages
    number_media_messages=df[df["message"].str.contains('<Media omitted>')].shape[0]

    #Fetch number of links shared
    links = []
    url_pattern = r'(https?://\S+|www\.\S+)'
    for message in df["message"]:
        urls = re.findall(url_pattern, message)
        links.extend(urls)

    return num_messages,len(words),number_media_messages,len(links)

def most_busy_users(df):
    x=df["user"].value_counts().head()
    df=round((df["user"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={"user":"name","count":"percent"})
    return x,df

def create_wordcloud(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color="white")
    df_wc=wc.generate(df["message"].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]


    stop_words = ['media', 'omitted', 'message', 'deleted', 'poll', 'waiting', 'this', 'was', 'for', 'the', 'and', 'that', 
              'hai', 'ki', 'ke', 'ka', 'ko', 'se', 'na', 'ne', 'mein', 'hi', 'bhi', 'tho', 'to', 're', 'oi', 'ar', 'hoy', 
              'na', 'ei', 'o', 'e', 'edited', 'joined', 'left', 'added', 'removed', 'group', 'description', 
              'tui', 'kal', 'bhai', 'ta', 'nhi', 'are', 'er', 'sir'] 

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        clean_message = emoji.replace_emoji(message, replace='')
        clean_message=re.sub(r'[^a-zA-Z\s]','',clean_message)
        clean_message = clean_message.translate(str.maketrans('', '', string.punctuation))
    
        for word in clean_message.lower().split():
            if word not in stop_words and len(word)>=2 and word.isalpha():
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def monthly_timeline(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    
    timeline=df.groupby(["year","month_num","month"]).count()["message"].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i]+"-"+str(timeline["year"][i]))
    timeline["time"]=time
    return timeline

def daily_timeline(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    daily_timeline=df.groupby("only_date").count()["message"].reset_index()
    return daily_timeline

def week_activity_map(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]

    return df["day_name"].value_counts()

def month_activity_map(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    return df["month"].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user!="Overall":
        df=df[df["user"]==selected_user]
    user_heatmap=df.pivot_table(index="day_name",columns="period",values="message",aggfunc="count").fillna(0)
    return user_heatmap
    
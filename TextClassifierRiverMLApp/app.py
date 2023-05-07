from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext


st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        if blob.sentiment.polarity<0:
             st.write('Negative')
        if blob.sentiment.polarity>0:
             st.write('Positive') 
        if blob.sentiment.polarity==0:
             st.write('Neutral')         


    pre = st.text_input('Clean Text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all= False, extra_spaces=True ,
                                 stopwords=True ,lowercase=True ,numbers=True , punct=True))

with st.expander('Analyze Toxicity'):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

#
    def analyze(x):
        if x == 0:
            return 'Neutral'
        elif  -0.1<x<0:
              return 'negetive'
       # elif  x<-0.1:
        #      return 'Toxic level'
        elif  x==-0.8:
              return 'toxic level 8'
        elif  x==-0.35000000000000003:
              return 'toxic level 3'
        elif  x==-0.15:
              return 'toxic level 1'
        elif  x==-0.6999999999999998:
              return 'toxic level 7'
        elif  x==-0.13749999999999996:
              return 'toxic level 1'
        elif  x== -0.3499999999999999:
              return 'Negetive'
        elif  x==-0.23333333333333328:
              return 'negetive'
        else:
            return 'Positive'

#
    if upl:
        df = pd.read_excel(upl)
        del df['Unnamed: 0']
        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        @st.cache
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )
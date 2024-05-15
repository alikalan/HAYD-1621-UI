import streamlit as st
import pandas as pd
import plotly.express as px

def app():

    st.markdown("<p style='text-align: left;font-size: 45px;font-weight: bold;'>HOW ARE YOU DOING, TODAY?</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: right;font-size: 24px;font-weight: bold; color: #f46524;'> - ABOUT THE DATA - </p>"
                , unsafe_allow_html=True)
    st.write('----')

    col_left2,col_cen2,col_right2 = st.columns([1.5,6,1.5])
    col_cen2.markdown('#### CLASSIFICATION TASK - SEVEN TARGETS')

    # Displaying the 7 targets
    col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,1,1])
    col1.image("data_images/angry.png", caption="Angry", use_column_width=True)
    col2.image("data_images/disgusted.png", caption="Disgusted", use_column_width=True)
    col3.image("data_images/fearful.png", caption="Fearful", use_column_width=True)
    col4.image("data_images/sad.png", caption="Sad", use_column_width=True)
    col5.image("data_images/neutral.png", caption="Neutral", use_column_width=True)
    col6.image("data_images/happy.png", caption="Happy", use_column_width=True)
    col7.image("data_images/surprised.png", caption="Surprised", use_column_width=True)

    st.write('----')

    st.markdown("<p style='text-align: center;font-size: 18px;font-weight: bold;'>To predict the emotions of different images, we trained our ResNet50 model on the 'Emotion Detection' dataset from Kaggle</p>"
                , unsafe_allow_html=True)
    #st.markdown('###### To predict the emotions of different images, we trained our ResNet50 model on the "Emotion Detection" dataset from Kaggle')
    st.markdown('')

    col_l1,col_l2,col_l3 = st.columns([0.27,0.63,0.1])
    col_l2.page_link('https://keras.io/api/applications/resnet/#resnet50-function', label='#### :computer:  :blue[- ResNet50 model function]')
    st.write('----')

    st.markdown("<p style='text-align: center;font-size: 25px;font-weight: bold;'> THE DATASET CONTAINS</p>"
                , unsafe_allow_html=True)

    col_data,col_text = st.columns([0.4,0.6])

    col_data.image('data_images/data_symbol_.png',caption='')
    col_text.markdown('')
    col_text.markdown('')
    col_text.markdown('')
    col_text.markdown("<p style='text-align: left;font-size: 18px;font-weight: bold;'>35,685 examples of 48x48 pixel gray scale images</p>"
                , unsafe_allow_html=True)
    col_text.markdown("<p style='text-align: left;font-size: 18px;font-weight: bold;'>Train and Test Set</p>"
                , unsafe_allow_html=True)
    col_text.markdown("<p style='text-align: left;font-size: 18px;font-weight: bold;'>Categorized into seven different classes</p>"
                , unsafe_allow_html=True)
    #col_text.page_link('https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer', label='##### :blue[Kaggle Emotion Detection dataset]')
    st.write('----')

    col_l12,col_l22,col_l32 = st.columns([0.20,0.7,0.1])
    col_l22.page_link('https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer', label='#### :point_right:  :blue[- Kaggle Emotion Detection dataset]')
    st.write('----')

    data_train = {
    'angry': 3995,
    'disgusted': 436,
    'fearful': 4097,
    'sad': 4830,
    'neutral': 4965,
    'happy': 7215,
    'surprised': 3171,
}
    # Create the DataFrame
    df_train = pd.DataFrame.from_dict(data_train, orient='index').reset_index()
    df_train.columns = ['emotion', 'value']

    # Create the Plotly bar chart
    fig = px.bar(df_train, x='emotion', y='value', title='Emotion Values (Train Set - 28.709 images)', color='emotion')

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    data_test = {
    'angry': 958,
    'disgusted': 111,
    'fearful': 1024,
    'sad': 1247,
    'neutral': 1233,
    'happy': 1774,
    'surprised': 831,
}

    # Create the DataFrame
    df_test = pd.DataFrame.from_dict(data_test, orient='index').reset_index()
    df_test.columns = ['emotion', 'value']

    # Create the Plotly bar chart
    fig2 = px.bar(df_test, x='emotion', y='value', title=' Emotion Values (Test Set - 7.178 images)', color='emotion')

    # Display the chart in Streamlit
    st.plotly_chart(fig2)

    st.write('----')

    st.image("data_images/confusion_matrix.png", caption="", use_column_width=True)

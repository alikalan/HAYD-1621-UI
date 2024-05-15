import streamlit as st

def app():

    st.markdown("<p style='text-align: center;font-size: 45px;font-weight: bold;'>HOW ARE YOU DOING, TODAY?</p>"
                , unsafe_allow_html=True)
    #st.title('HOW ARE YOU DOING, TODAY?')

    st.markdown("<p style='text-align: right;font-size: 24px;font-weight: bold; color: #ffd16a;'>THE PROJECT</p>"
                , unsafe_allow_html=True)

    st.write('----')

    st.markdown("<p style='text-align: center;font-size: 40px;font-weight: bold; color: #2ab09d;'>THE PROBLEM</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: center;font-size: 24px;font-weight: bold;'>Most people don’t know what they feel, can’t name their emotions in detail or can’t elaborate.</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: center;font-size: 40px;font-weight: bold; color: #ffd16a;'>THE IDEA</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: center;font-size: 24px;font-weight: bold;'>A simple gamified app to help people connect to their emotions in less than one minute.</p>"
                , unsafe_allow_html=True)



    st.write('----')


    st.markdown('###### To predict the emotions of different images, we trained our ResNet50 model on the "Emotion Detection" dataset from Kaggle')
    st.markdown('')
    st.page_link('https://keras.io/api/applications/resnet/#resnet50-function', label='##### :computer:  :blue[- ResNet50 model function]')
    st.markdown("""
        ### The dataset contains:
        ###### - 35,685 examples of 48x48 pixel gray scale images
        ###### - divided into train and test dataset
        ###### - categorized into seven different classes
        """)
    st.markdown('')
    st.page_link('https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer', label='##### :point_right:  :blue[- Kaggle Emotion Detection dataset]')
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

import pickle
import streamlit as st

pickle_in = open("predictor","rb")
predictor=pickle.load(pickle_in)
def welcome():
    return "Hello!"

def predict_AQI(PM25, PM10, NO, NO2,nox, nh3, so,so2, o3):
    prediction=predictor.predict([[ PM25, PM10, NO, NO2, nox, nh3, so,so2, o3]])
    print(prediction)
    return prediction

def main():
    st.title("Delhi AQI prediction")
    html_temp = """
    <div style="background-color:#CC99CC; padding:20px">
    <h2 style="color:white; text-align:center; ">Lets predict the AQI! </h2>
    </div>
    <br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    PM25= st.text_input("Value of PM2.5 ","Type Here")
    PM10 = st.text_input("Value of PM10 ","Type Here")
    NO2 = st.text_input("Value of NO2 ","Type Here")
    NO = st.text_input("Value of NO ","Type Here")
    nox, nh3=51.963604,38.338368
    so, o3=1.322881,41
    so2=13.852180
    result=""
    if st.button("Predict"):
        result=predict_AQI(PM25, PM10, NO, NO2, nox, nh3, so,so2, o3 )
        st.success('The AQI is {}'.format(result))

if __name__=='__main__':
    main()

import streamlit as st
from PIL import Image

def calculator(weight, height):
    try:
     BMI = weight/height**2
     st.success(BMI)
    except:
        st.error('ENTER A VALID INPUT')


def calculator2(waist, hip):
    try:
        WHR = waist / hip
        st.success(WHR)
    except:
        st.error('ENTER A VALID INPUT')

def main():
 st.header('WELCOME TO HEALTHIFY')
 img = Image.open('healthify.png')
 st.image(img)
 Tools = st.radio('TOOLS:', ['BMI', 'WAIST HIP RATIO', 'BLOOD PRESSURE'])
 if Tools == 'BMI':
    img = Image.open('BMI.jpeg')
    st.image(img)
    st.title('BMI CALCULATOR')
    unit = st.radio('SELECT UNIT OF HEIGHT: ', ['Feet', 'Centimeters', 'Meters'])
    if unit == 'Feet':
     height = st.number_input('ENTER HEIGHT(in feet) : ')
     weight = st.number_input('ENTER WEIGHT(in kg) : ')
     if st.button('submit'):
                 calculator(weight, height)
    elif unit == 'Centimeters':
     height = st.number_input('ENTER HEIGHT(in cm):')
     weight = st.number_input('ENTER WEIGHT(in ft):')
     if st.button('submit'):
                  calculator(weight, height)
    else:
        height = st.number_input('ENTER HEIGHT(in m):')
        weight = st.number_input('ENTER WEIGHT(in cm):')
        if st.button('submit'):
         calculator(weight, height)

 elif Tools == 'WAIST HIP RATIO':
  img = Image.open('WHR.jpg')
  st.image(img)
  st.title('WAIST HIP RATIO CALCULATOR')
  waist = st.number_input('ENTER WAIST CIRCUMFERENCE :')
  hip = st.number_input('ENTER HIP CIRCUMFERENCE :')
  if st.button('Calculate'):
      calculator2(waist, hip)
 else:
    img = Image.open('blood.jpg')
    st.image(img)
    st.title('BLOOD PRESSURE')
    systolic = st.number_input('ENTER SYSTOLIC PRESSURE :')
    dystolic = st.number_input('ENTER DIASTOLIC PRESSURE :')

    if st.button('submit'):
       if systolic in range(90, 120) and dystolic in range(60, 80):
        st.success('NORMAL')
       elif systolic in range(140, 159) and dystolic in range(90, 99):
        st.warning('HYPERTENSION STAGE-1')
       elif systolic in range(160, 180) and dystolic in range(100, 110):
        st.error('HYPERTENSION STAGE-2')
       elif systolic > 180 and dystolic > 110:
        st.error('HYPERTENSIVE CRISIS')
       elif systolic < 90 and dystolic < 60:
        st.error('LOW BLOOD PRESSURE')


if __name__ == '__main__' :
    main()


import streamlit as st
import time
import math as mt

st.set_page_config(
     page_title="Vintage Industrial Components Pvt. Ltd",
     page_icon=C:\Users\ypran\Downloads\logo-removebg-preview (1).png,
     layout="centered",
     menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

st.success('Successfuly loaded the page! 😊')

st.title('NutryUS')
st.image('https://www.fredhutch.org/content/dam/www/research/divisions/public-health-sciences/nutrition-assessment/nutrition-dietary-data-gfb-2.jpg')
st.header('Your new diet Dormitory Mother')
#st.text('Select your meal')
#st.write("**Open the sidebar the type of meal on your left top corner to select **")
#genre = st.sidebar.selectbox(
#     "Meal:",
#     ('None','Breakfast','Lunch','Dinner'))

tab1, tab2, tab3, tab4, tab5 = st.tabs(["BMI calculation", "Breakfast", "Lunch", "Dinner", "Summary"])

### Calculating BMI of a person
with tab1:
     weight = st.slider('Enter your weight in kg',1.0,150.0,step=0.1)
     height = st.slider('Enter your height in m',1.0,2.5,step=0.01)
     bmi = (weight)/(height**2)
### Calories based on bmi
     if bmi > 16.0 and bmi < 18.5:
          cal_1 = 3000
          st.write('Based on your BMI, you need to consume 3000 Calories per day')
     elif bmi > 18.5 and bmi < 25:
          cal_2 = 2500
          st.write('Based on your BMI, you need to consume 2500 Calories per day')
     elif bmi > 25 and bmi < 40:
          cal_3 = 2300
          st.write('Based on your BMI, you need to consume 2300 Calories per day')
     else:
          st.write('Input approriate height and weight')
     breakfast_calories, lunch_calories, dinner_calories = 0, 0, 0
#st.write('**You selected:**', genre)

with tab2:
     #if genre == 'Breakfast':
     st.title('BREAKFAST SECTION')
     breakfast_calories = 0
     st.write('Idly')
     st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
     S1=st.slider('Idly Quantity',0,5,step=1)
     calories_idly = 78
     st.write('Dosa')
     st.image('https://c.ndtvimg.com/2021-03/ka6tveng_dosa_625x300_16_March_21.jpg')
     S2=st.slider('Dosa Quantity',0,5,step=1)
     calories_dosa = 154
     st.write('Breadtoast')
     st.image('https://www.archanaskitchen.com/images/archanaskitchen/BasicRecipes_HOW_TO/Bread_toast_recipe.jpg')
     S3=st.slider('Breadtoast Quantity',0,5,step=1)
     calories_breadtoast = 97
     st.write('Poori')
     st.image('https://www.awesomecuisine.com/wp-content/uploads/2020/03/poori-masala-kizhangu.jpg')
     S4=st.slider('Poori Quantity',0,5,step=1)
     calories_poori = 134
     st.write('Omelet and Boiled Egg')
     st.image('https://cdn.pixabay.com/photo/2015/05/20/16/11/kitchen-775746__340.jpg')
     S5=st.slider('Omelet Quantity',0,5,step=1)
     st.image('https://www.thespruceeats.com/thmb/XC5U2ZiRJIy89I2PPP8aKuob86w=/3797x2848/smart/filters:no_upscale()/perfect-hard-boiled-eggs-995510-Hero_3-03d1b108d1ca489dad9e1f1d7fdba73f.jpg')
     S6=st.slider('Boiled Egg Quantity', 0,5,step=1)
     calories_omelt = 127
     calories_boiledegg = 77
     st.write('Vada')
     st.image('https://img.freepik.com/premium-photo/south-indian-vada-medu-vada-dal-vadai-plate-bowl-isolated-plain_466689-1580.jpg')
     S7=st.slider('Vada Quantity',0,5,step=1)
     calories_vada = 155
     breakfast_calories = S1*calories_idly + S2*calories_dosa + S3*calories_breadtoast + S4*calories_poori + S5*calories_omelt + S6*calories_boiledegg + S7*calories_vada
  #calories = []
  #calories.append(breakfast_calories)
     st.write('Breakfast Calories = {}'.format(breakfast_calories)) 

# LUNCH SECTION ( To be edited )


with tab3:
     #if genre == 'Lunch':
     st.title('LUNCH SECTION')
     lunch_calories = 0
     st.text('Quantity is taken in terms of Bowls')
     st.write('Chicken Biryani Bowl')
     st.image('https://thumbs.dreamstime.com/b/hyderabadi-chicken-biryani-38473399.jpg')
     S1=st.slider('Biryani Bowl Quantity',0,5,step=1)
     calories_Biryani = 389
     st.write('Rice and Dal Bowl')
     st.image('https://maninio.com/wp-content/uploads/2019/06/DSC_0870.jpg')
     S2=st.slider('Rice and Dal Bowl Quantity',0,5,step=1)
     calories_Dal = 298
     st.write('Panner Rice Bowl')
     st.image('https://chayanikarestaurant.com/wp-content/uploads/2020/07/paneer-rice-thali.jpg')
     S3=st.slider('Panner Rice Bowl Quantity',0,5,step=1)
     calories_Panner_rice = 380
     st.write('Mutton Rice Bowl')
     st.image('https://upload.wikimedia.org/wikipedia/commons/c/ca/Mutton_Curry_with_Rice.jpg')
     S4=st.slider('Mutton Rice Bowl Quantity',0,5,step=1)
     calories_Mutton = 388
     st.write('Grilled Fish')
     st.image('https://res.cloudinary.com/twenty20/private_images/t_watermark-criss-cross-10/v1650227164000/photosp/481e92a6-964f-4a9a-8f4d-c99a47060bfd/stock-photo-food-blue-plate-restaurant-sauce-fish-rice-closeup-grill-481e92a6-964f-4a9a-8f4d-c99a47060bfd.jpg')
     S5=st.slider('Grilled Fish',0,5,step=1)
     calories_Grilled_Fish = 186
     st.write('Soya Curry with Rice Bowl')
     st.image('https://thumbs.dreamstime.com/b/soyabean-rice-indian-vegetarian-soybean-peas-34588825.jpg')
     S6=st.slider('Soya Curry with Rice Bowl',0,5,step=1)
     calories_Soya = 350
     st.write('Apricot Delight for dessert')
     st.image('https://media-cdn.tripadvisor.com/media/photo-s/07/f3/1f/ff/kiva-restaurant.jpg')
     S7=st.slider('Apricot Delight Quantity', 0,5,step=1)
     calories_apricot = 97
     lunch_calories = S1*calories_Biryani + S2*calories_Dal + S3*calories_Panner_rice + S4*calories_Mutton + S5*calories_Grilled_Fish + S6*calories_Soya + S7*calories_apricot
  #calories.append(lunch_calories)
     st.write('Lunch Calories = {}'.format(lunch_calories))
     
 # DINNER SECTION  (To be edited)
  

with tab4:
     #if genre == 'Dinner':
     st.title('DINNER SECTION')
     dinner_calories = 0
     st.text('Quantity is taken in terms of Bowls')
     st.write('Jeera Rice')
     st.image('https://www.whiskaffair.com/wp-content/uploads/2021/06/Jeera-Rice-2-3-1.jpg')
     S1=st.slider('Jeera Rice Quantity',0,5,step=1)
     calories_Jeera = 296
     st.write('Curd Rice')
     st.image('https://www.vegrecipesofindia.com/wp-content/uploads/2016/07/curd-rice-2.jpg')
     S2=st.slider('Curd Rice Quantity',0,5,step=1)
     calories_Curd = 283
     st.write('Butter Naan')
     st.image('https://indianvegrecipe.com/wp-content/uploads/2019/06/butter-naan-recipe.jpg')
     S3=st.slider('Butter Naan Quantity',0,5,step=1)
     calories_Naan = 271
     st.write('Roti')
     st.image('https://www.vegrecipesofindia.com/wp-content/uploads/2015/04/tandoori-roti-recipe-1.jpg')
     S4=st.slider('Roti Quantity',0,5,step=1)
     calories_Roti = 150
     st.write('Chapati')
     st.image('https://img.onmanorama.com/content/dam/mm/en/food/features/images/2021/1/6/chapathi.jpg')
     S5=st.slider('Chapati Quantity',0,5,step=1)
  #S6=st.slider('Boiled Egg Quantity', 0,5,step=1)
     calories_Chapati = 85
  #calories_boiledegg = 1
     st.write('Panner curry')
     st.image('https://www.whiskaffair.com/wp-content/uploads/2019/05/Paneer-Masala-1-3.jpg')
     S6=st.slider('Panner curry Quantity',0,5,step=1)
     calories_Panner_curry = 205
     st.write('Chicken curry')
     st.image('https://static.onecms.io/wp-content/uploads/sites/9/2021/03/10/spicy-chicken-curry-FT-RECIPE0321.jpg')
     S7=st.slider('Chicken curry Quantity',0,5,step=1)
     calories_Chicken_curry = 271
     st.write('Mutton curry')
     st.image('https://www.whiskaffair.com/wp-content/uploads/2019/04/Punjabi-Mutton-Curry-5.jpg')
     S8=st.slider('Mutton curry Quantity',0,5,step=1)
     calories_Mutton_curry = 301
     dinner_calories = S1*calories_Jeera + S2*calories_Curd + S3*calories_Naan + S4*calories_Roti + S5*calories_Chapati + S6*calories_Panner_curry + S7*calories_Chicken_curry +S8*calories_Mutton_curry
  #calories.append(dinner_calories)
     st.write('Dinner Calories = {}'.format(dinner_calories))
     
with tab5:
     #Summary of all the data
     st.write('Breakfast Calories = {}'.format(breakfast_calories))
     st.write('Lunch Calories = {}'.format(lunch_calories))
     st.write('Dinner Calories = {}'.format(dinner_calories))
     total_calories = breakfast_calories + lunch_calories + dinner_calories
     st.write('Total calories consumed today = {}'.format(total_calories))

     if bmi > 16.0 and bmi < 18.5:
          cal_1 = 3000
          if(cal_1 > total_calories):
               diff = cal_1 - total_calories
               st.write('Calories left to be consumed: ')
               st.write(diff)
          else:
               diff = total_calories - cal_1
               st.write('Extra calories taken: ')
               st.write(diff)
     elif bmi > 18.5 and bmi < 25:
          cal_2 = 2500
          if(cal_2 > total_calories):
               diff = cal_2 - total_calories
               st.write('Calories left to be consumed: ')
               st.write(diff)
          else:
               diff = total_calories - cal_2
               st.write('Extra calories taken: ')
               st.write(diff)
     elif bmi > 25 and bmi < 40:
          cal_3 = 2300
          if(cal_3 > total_calories):
               diff = cal_3 - total_calories
               st.write('Calories left to be consumed: ')
               st.write(diff)
          else:
               diff = total_calories - cal_3
               st.write('Extra calories taken: ')
               st.write(diff)
     if st.button('Submit'):
          st.write('Successfully submitted!')
     else:
          st.write('Did not submit successfully')

import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breafast Menu')
streamlit.text('🥗Omega 3 & Bluberry oat meal')
streamlit.text('🌮🥙Kale, Spinach & Rocket smoothie')
streamlit.text('🥚🍞🥪Hard-boiled Free-Range egg')

streamlit.header('🍌🍉Buid your own fruit smoothie🍓🍍🥑')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index("Fruit")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

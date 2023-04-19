import streamlit
import pandas
import requests
import snowflake.connector

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

streamlit.header('FruityVice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?')
if fruit_choice:
  streamlit.write('The user entered ', fruit_choice)
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  streamlit.text(fruityvice_response.json())

  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # streamlit.text(fruityvice_normalized)
  streamlit.dataframe(fruityvice_normalized)

  
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

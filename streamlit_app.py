import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")    
  else:
    streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    streamlit.text(fruityvice_response.json())
    
except URLError as e:
  streamlit.error(e)
  '''
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values('from streamlit')")
'''
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # streamlit.text(fruityvice_normalized)
streamlit.dataframe(fruityvice_normalized)
 # streamlit.button('Get Fruit Load List')
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
   my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
   return my_cur.fetchall()
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

streamlit.header('FruityVice Fruit Advice')
#streamlit.button('Add a fruit to list')
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('"+new_fruit+"')")
    return "Thanks for adding "+new_fruit
  
add_my_fruit=streamlit.text_input('What fruit do you like to add: ')

if streamlit.button('Add a fruit to list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()


# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
streamlit.header("Fruit Load List")
streamlit.text(my_data_row)
fruit_list_to_add = streamlit.dataframe(my_data_row)
fruit_added = streamlit.text_input("Which fruit would you like to add: ")
streamlit.write("Thanks for adding "+fruit_added)

my_cur.execute("insert into fruit_load_list values('jackfruit'),('papaya'), ('kiwi'),('guava'),('test')")

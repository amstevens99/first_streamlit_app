import streamlit
streamlit.title('Welcome to the Healthy Diner')
streamlit.header ('Breakfast Menu')
streamlit.text ('🥣 Flaxseed & Blueberry Porridge')
streamlit.text ('🥗 Kale, Spinach and Apple Smoothie')
streamlit.text ('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

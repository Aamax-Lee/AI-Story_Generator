import streamlit as st
import base64
from food_helper import FoodNames
from food_ai_api import FoodAI
from web_search import GoogleCustomSearch 
from streamlit_navigation_bar import st_navbar
from edamam import Edamam

import os

  

page = st_navbar(["Casual", "Athletes","FAQ"])
# if page == "Casual":

OPENAI_API_KEY = os.environ['OPENAI_KEY']  
GOOGLE_SEARCH_API_KEY = os.environ['GOOGLE_SEARCH_API_KEY']
SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']
EDAMAM_APP_ID = os.environ['EDAMAM_APP_KEY']
EDAMAM_APP_KEY = os.environ['EDAMAM_APP_ID']
# OPENAI_API_KEY = st.secrets['OPENAI_KEY']
# GOOGLE_SEARCH_API_KEY = st.secrets['GOOGLE_SEARCH_API_KEY']
# SEARCH_ENGINE_ID = st.secrets['SEARCH_ENGINE_ID']
# EDAMAM_APP_KEY = st.secrets['EDAMAM_APP_KEY']
# EDAMAM_APP_ID = st.secrets['EDAMAM_APP_ID']

food_ai = FoodAI(api_key=OPENAI_API_KEY)
fn = FoodNames()
search_recipe_links = GoogleCustomSearch(api_key = GOOGLE_SEARCH_API_KEY, search_engine_id = SEARCH_ENGINE_ID)
edamam_search = Edamam(app_key = EDAMAM_APP_KEY, app_id = EDAMAM_APP_ID)



def encode_image(image_path):
    return base64.b64encode(image_path.read()).decode('utf-8')


# ---------------UI-------------------

st.title("Grandma's AI")

if page == "Athletes" or page == "Casual":
    athcol1, athcol2, athcol3 = st.columns([1, 1, 1])
    col1, col2 = st.columns([1, 1])
    col4, col5 = st.columns([1, 1])

if page == "Athletes":
    with athcol1:
        cut_bulk = st.selectbox(
            "Cut or Bulk?",
            ["Aggressive Cut", "Moderate Cut", "Maintain", "Lean Bulk", "Aggressive Bulk"],
        )

    with athcol2:
        prep_level = st.selectbox(
            "Level of Preparation",
            [
                "Easy (5-15 minutes)",
                "Moderate (15-30 minutes)",
                "Difficult (30-60 minutes)",
            ],
            key=["easy", "moderate", "difficult"],
        )


    with athcol3:
        filter_options = st.multiselect(
            "Foods to not include", fn.get_food_names()
        )

        filter_ingredient_string = ', '.join([i for i in filter_options])

if page == "Casual":
    with col1:
        prep_level = st.selectbox(
            "Level of Preparation",
            [
                "Easy (5-15 minutes)",
                "Moderate (15-30 minutes)",
                "Difficult (30-60 minutes)",
            ],
            key=["easy", "moderate", "difficult"],
        )


    with col2:
        filter_options = st.multiselect(
            "Foods to not include", fn.get_food_names()
        )

        filter_ingredient_string = ', '.join([i for i in filter_options])

if page == "Athletes" or page == "Casual":
    with col4:
        dietary_restrictions = st.selectbox(
            "Do you have any dietry restriction?",
            (
                "None",
                "Vegetarian",
                "Vegan",
                "Halal",
                "Lactose intolerant",
                "Gluten intolerant",
                "Custom Option",
            ),
        )

    with col5:
        cuisine_choices = st.selectbox(
            "Cuisine Type:",
            (
                "Any",
                "Thai",
                "Italian",
                "Japanese",
                "Korean",
                "Chinese",
                "Greek",
                "French",
                "Western",
                "Indian",
                "Spanish",
                "American",
                "Galican",
                "Anglo-Indian",
                "Vietnamese",
                "Custom Option",
            ),
        )

    if dietary_restrictions == "Custom Option":
        dietary_restrictions = st.text_input("Enter your custom dietary restriction:")
    if cuisine_choices == "Custom Option":
        cuisine_choices = st.text_input("Enter your custom cuisine type:")
    
    uploaded_file = st.file_uploader("Upload pictures of past meals (Min 3)", accept_multiple_files=True)

if page == "Casual":

    generate_recipe = st.button("Generate Recipes")
    if generate_recipe and len(uploaded_file) >= 3:
    # if uploaded_file is not None and len(uploaded_file) >= 3:
        image_lst = []
        for i in range(len(uploaded_file)):
            image_lst.append(encode_image(uploaded_file[i]))

        all_ingredients = food_ai.find_ingredients(image_lst)
        
        dietary_string = ""
        if dietary_restrictions != "None":
            f"Please return recipes that are suitable for {dietary_restrictions}"
            
        # meal suggestion for easy level
        if prep_level == "Easy (5-15 minutes)":    
            st.title("Easier Options")
            easy_meals = food_ai.meal_suggestion(all_ingredients, "easy", filter_ingredient_string, dietary_restrictions, cuisine_choices)
                                                 
            meals = easy_meals.split("Meal ")
            # st.write(meals)

            mealFull1 = meals[1][3:]           
            mealFull2 = meals[2][3:]

            meal1name = meals[1].split("\n")[0][3:]
            meal2name = meals[2].split("\n")[0][3:]

            links1 = search_recipe_links.generate_recipe_links(meal1name)
            links2 = search_recipe_links.generate_recipe_links(meal2name)

            st.header(meal1name)
            with st.expander(f"View Meal 1 Info"):
                st.write(mealFull1)

            with st.expander(f"Links to recipes and resources for: {meal1name}"):
                # st.markdown(f"<h2><b>Recipes and resources for: {meal1}</b></h2>", unsafe_allow_html=True)
                for i in range(len(links1)):
                    st.write(f'{i+1}: {links1[i]}')

            st.header(meal2name)
            with st.expander(f"View Meal 2 Info"):
                st.write(mealFull2)

            with st.expander(f"Links to recipes and resources for: {meal2name}"):

                for i in range(len(links2)):
                    st.write(f'{i+1}: {links2[i]}')
            # is_text += easy_meals

            ingredients = easy_meals.split("Ingredients:")[1].split("Recipe")[0].split("\n")[1:-1]
            # st.write(ingredients)
            new_ingredients = [i[2:].strip() for i in ingredients if i != "" or i != "**"][:-3]
            # st.write(new_ingredients)      
            complete_ingredient_list = ", ".join(new_ingredients).replace("-", "")
            # st.write(complete_ingredient_list)
            nutri_facts = edamam_search.get_nutritional_facts(complete_ingredient_list)

            st.write(nutri_facts)

    
            ingredients1 = easy_meals.split("Ingredients:")[2].split("Recipe")[0].split("\n")[1:-1]
            # st.write(ingredients)
            new_ingredients1 = [i[2:].strip() for i in ingredients1 if i != "" or i != "**"][:-3]
            # st.write(new_ingredients)      
            complete_ingredient_list1 = ", ".join(new_ingredients1).replace("-", "")
            # st.write(complete_ingredient_list)
            nutri_facts1 = edamam_search.get_nutritional_facts(complete_ingredient_list1)
    
            st.write(nutri_facts1)

            
    
        # meal suggestion for moderate level
        if prep_level == "Moderate (15-30 minutes)":
            st.title("Moderate Options")
            moderate_meals = food_ai.meal_suggestion(all_ingredients, "moderate skill level", filter_ingredient_string, dietary_restrictions, cuisine_choices)
            meals = moderate_meals.split("Meal ")
            # st.write(meals)

            mealFull1 = meals[1][3:]           
            mealFull2 = meals[2][3:]

            meal1name = meals[1].split("\n")[0][3:]
            meal2name = meals[2].split("\n")[0][3:]

            links1 = search_recipe_links.generate_recipe_links(meal1name)
            links2 = search_recipe_links.generate_recipe_links(meal2name)

            st.header(meal1name)
            with st.expander(f"View Meal 1 Info"):
                st.write(mealFull1)

            with st.expander(f"Links to recipes and resources for: {meal1name}"):
                # st.markdown(f"<h2><b>Recipes and resources for: {meal1}</b></h2>", unsafe_allow_html=True)
                for i in range(len(links1)):
                    st.write(f'{i+1}: {links1[i]}')

            st.header(meal2name)
            with st.expander(f"View Meal 2 Info"):
                st.write(mealFull2)

            with st.expander(f"Links to recipes and resources for: {meal2name}"):

                for i in range(len(links2)):
                    st.write(f'{i+1}: {links2[i]}')
            # is_text += moderate_meals
    
        # meal suggestion for hard level
        if prep_level == "Difficult (30-60 minutes)":
            st.title("Difficult Options")
            hard_meals = food_ai.meal_suggestion(all_ingredients, "higher skill level", filter_ingredient_string, dietary_restrictions, cuisine_choices)
            # st.write(hard_meals)
            meals = hard_meals.split("Meal ")
            # st.write(meals)

            mealFull1 = meals[1][3:]           
            mealFull2 = meals[2][3:]
            
            meal1name = meals[1].split("\n")[0][3:]
            meal2name = meals[2].split("\n")[0][3:]

            links1 = search_recipe_links.generate_recipe_links(meal1name)
            links2 = search_recipe_links.generate_recipe_links(meal2name)

            st.header(meal1name)
            with st.expander(f"View Meal 1 Info"):
                st.write(mealFull1)

            with st.expander(f"Links to recipes and resources for: {meal1name}"):
                # st.markdown(f"<h2><b>Recipes and resources for: {meal1}</b></h2>", unsafe_allow_html=True)
                for i in range(len(links1)):
                    st.write(f'{i+1}: {links1[i]}')
            
            st.header(meal2name)
            with st.expander(f"View Meal 2 Info"):
                st.write(mealFull2)
            
            with st.expander(f"Links to recipes and resources for: {meal2name}"):
                
                for i in range(len(links2)):
                    st.write(f'{i+1}: {links2[i]}')




# -------------FAQ-------------------
if page == "FAQ":
    with st.expander(f"What if my dietry restriction is not listed in the list?"):
        st.markdown("You may select the **Custom Option** option and enter your custom dietary restriction.")

    with st.expander(f"What is 'Athletes?'"):
        st.markdown("Athletes mode provides more tailored and personalised recipes for users who seeks to gain muscle or cut body fat through a combination of high-quality meals.")
        
    

           
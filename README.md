
# AI Story Image Generator

This project is a web application that allows users to generate detailed image prompts for movie covers based on their story ideas. The application leverages OpenAI's GPT-3.5-turbo and DALL-E 2 models to create engaging and relevant movie cover designs.


## Badges


![Python](https://a11ybadges.com/badge?logo=python)  
![Replit](https://a11ybadges.com/badge?logo=replit)  
![OpenAI](https://a11ybadges.com/badge?logo=openai)  
![Streamlit](https://a11ybadges.com/badge?logo=streamlit)


## Features

- Prompt Input: Users can input a story prompt for their movie.
- Cover Generation: The app generates a detailed image prompt based on the story and uses it to create a movie cover image.
- Image Display: The generated movie cover image is displayed on the web interface.



## Installation

Install my-project with npm

```bash
    git clone https://github.com/ak1ra14/AI-Meal-Planner.git
    cd AI-Meal-Planner
```
Install required packages

```bash
pip install -r requirements.txt
```
Set up OpenAI API key
- Add your OpenAI API key to the Streamlit secrets.
- Create a .streamlit/secrets.toml file and add:
```bash
[secrets]
OPENAI_KEY = "YOUR_OPENAI_API_KEY"
EDAMAM_APP_ID = "YOUR_EDAMAM_APP_ID"
EDAMAM_APP_KEY = "YOUR_EDAMAM_APP_KEY"
GOOGLE_SEARCH_API_KEY = "YOUR_CUSTOM_SEARCH_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE"
```

## Using the app 
Run the Streamlit App:
```bash 
streamlit run main.py
```

1) Select your dietry restrictions and filters if necessary.
2) Upload a photo of your past meals.
3) That's it! Receive meal suggestions and nutritional information based on your input.


## Demo

Demo and example use cases can be seen from the following link: https://www.youtube.com/watch?v=Teu9MsIlIt4

## Authors
- [@Akira Sato](https://github.com/ak1ra14)
- [@Harry Lee Tai Peng](https://github.com/LeeTP03)
- [@Nelson Tan Zu Xuan](https://github.com/NelsonTan02)

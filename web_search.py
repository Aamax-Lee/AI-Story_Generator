import streamlit as st
import requests
gcsapikey = st.secrets["GOOGLE_SEARCH_API_KEY"]
gcsseid = st.secrets["SEARCH_ENGINE_ID"]
class GoogleCustomSearch:

    def __init__(self, api_key, search_engine_id):
        self.api_key = api_key
        self.search_engine_id = search_engine_id

    # Web search to obtain links
    def web_search(self, query):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={self.search_engine_id}"
        print(url)
        response = requests.get(url)
        results = response.json()
        return results

    def generate_recipe_links(self, food):
        query = f"Recipe for {food}"
        search_results = self.web_search(query)
        st.write(search_results)
        recipe_links = [
            item['link'] for item in search_results.get('items', [])
        ]
        return recipe_links

if __name__ == "__main__":
    gcs = GoogleCustomSearch(api_key=gcsapikey, search_engine_id=gcsseid)
    gcs.web_search("mango")
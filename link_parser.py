import streamlit as st
from bs4 import BeautifulSoup

# Define a function to parse HTML and extract links
def parse_html_to_dict(html):
    soup = BeautifulSoup(html, 'html.parser')
    sakshi_links = {}
    
    for p in soup.find_all('p'):
        text = p.get_text()
        date, _ = text.split(': ', 1)
        links_dict = {}
        
        for a in p.find_all('a'):
            label = a.text
            url = a['href']
            links_dict[label] = url
        
        sakshi_links[date] = links_dict
    
    return sakshi_links

# Streamlit UI
st.title("Extract Links from HTML")

# Input HTML
html_input = st.text_area("Paste your HTML input here:", height=300)
# Input Dictionary Name
dict_name = st.text_input("Enter the dictionary name:", "sakshi_links")

if st.button("Parse HTML"):
    if html_input.strip() and dict_name.strip():
        # Parse the HTML and get the links dictionary
        sakshi_links = parse_html_to_dict(html_input)
        
        # Create the output string
        output_string = f"{dict_name} = {sakshi_links}"
        
        # Display the result
        st.subheader("Extracted Links:")
        st.code(output_string, language="python")
    else:
        st.error("Please provide both HTML input and dictionary name before clicking 'Parse HTML'.")


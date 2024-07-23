import streamlit as st
from bs4 import BeautifulSoup

# Define a function to parse HTML and extract links
def parse_html_to_dict(html):
    soup = BeautifulSoup(html, 'html.parser')
    sakshi_links = {}
    
    for p in soup.find_all('p'):
        text = p.get_text()
        date, links_text = text.split(': ', 1)
        links = links_text.split(' | ')
        
        links_dict = {}
        for link in links:
            label, url = link.split(' ', 1)
            url = url.replace('<a href="', '').replace('" target="_blank" rel="noopener">', ' ').replace('</a>', '')
            links_dict[label] = url
        
        sakshi_links[date] = links_dict
    
    return sakshi_links

# Streamlit UI
st.title("Extract Links from HTML")

# Input HTML
html_input = st.text_area("Paste your HTML input here:", height=300)

if st.button("Parse HTML"):
    if html_input.strip():
        # Parse the HTML and get the links dictionary
        sakshi_links = parse_html_to_dict(html_input)
        
        # Display the result
        st.subheader("Extracted Links:")
        st.json(sakshi_links)
    else:
        st.error("Please paste some HTML input before clicking 'Parse HTML'.")

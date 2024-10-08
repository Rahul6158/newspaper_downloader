# link_parser
import streamlit as st
from bs4 import BeautifulSoup
from datetime import datetime

# Define a function to parse HTML and extract links
def parse_html_to_dict(html):
    soup = BeautifulSoup(html, 'html.parser')
    sakshi_links = {}
    
    # Helper function to normalize dates
    def normalize_date(date_str):
        try:
            # Try different date formats
            date_obj = datetime.strptime(date_str, '%d %B %Y')
        except ValueError:
            try:
                date_obj = datetime.strptime(date_str, '%d %B %Y')
            except ValueError:
                try:
                    date_obj = datetime.strptime(date_str, '%d %b %Y')
                except ValueError:
                    date_obj = datetime.strptime(date_str, '%B %d, %Y')
        return date_obj.strftime('%B %d, %Y')

    for p in soup.find_all('p'):
        text = p.get_text()
        # Split text to get date and links
        try:
            date, _ = text.split(': ', 1)
            date = normalize_date(date.strip())
        except ValueError:
            continue
        
        links_dict = {}
        for a in p.find_all('a'):
            label = a.text
            url = a['href']
            links_dict[label] = url
        
        sakshi_links[date] = links_dict
    
    return sakshi_links

def format_dict_as_string(dict_name, dictionary):
    output = f"{dict_name} = {{\n"
    for date, links in dictionary.items():
        output += f'    "{date}": {{\n'
        for label, url in links.items():
            output += f'        "{label}": "{url}",\n'
        output += f'    }},\n'
    output += "}"
    return output

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
        
        # Format the output string
        output_string = format_dict_as_string(dict_name, sakshi_links)
        
        # Display the result
        st.subheader("Extracted Links:")
        st.code(output_string, language="python")
    else:
        st.error("Please provide both HTML input and dictionary name before clicking 'Parse HTML'.")

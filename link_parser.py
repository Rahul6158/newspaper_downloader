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
            date_obj = datetime.strptime(date_str, '%b %d, %Y')
        except ValueError:
            try:
                date_obj = datetime.strptime(date_str, '%d %B %Y')
            except ValueError:
                try:
                    date_obj = datetime.strptime(date_str, '%d %b %Y')
                except ValueError:
                    date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        return date_obj.strftime('%B %d, %Y')

    # Parse <p> tags
    for p in soup.find_all('p'):
        text = p.get_text()
        # Split text to get date and links
        try:
            date, links = text.split(': ', 1)
            date = normalize_date(date.strip())
        except ValueError:
            continue
        
        links_dict = {}
        for a in p.find_all('a'):
            label = a.text.strip()  # Use the label provided in the <a> tag
            url = a['href']
            links_dict[label] = url
        
        sakshi_links[date] = links_dict

    # Parse <tr> tags
    for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) >= 2:
            date = normalize_date(tds[0].get_text().strip())
            links_dict = {}
            state_labels = ["AP", "TS"]  # Example labels for states; adjust as needed
            for i, td in enumerate(tds[1:], start=0):
                url = td.get_text().strip()
                label = state_labels[i] if i < len(state_labels) else f"Link {i+1}"  # Use state names or fallback
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

# Example HTML to test:
# <p>Aug 2, 2024: <a href="https://drive.google.com/file/d/1WVch9nuWKnQBHMK_9Is1euyxrWx-UaoP/view?usp=drive_link" target="_blank" rel="noopener">AP</a> | <a href="https://drive.google.com/file/d/16Q5wQNwF9Sn7uh7LZ17WQ4jU7sudHTUx/view?usp=drive_link" target="_blank" rel="noopener">TS</a></p>
# <tr data-row_id="0" class="ninja_table_row_0 nt_row_id_0">
# <td>09-08-2024</td><td>https://drive.google.com/file/d/1P5toJgmFn7-XsDAhJ_9Pci3nkBTQhekH/view?usp=drive_link</td><td>https://drive.google.com/file/d/1oHVEcmhPI0I97ci-ynkmv3bn6XWCzzBx/view?usp=drive_link</td></tr>

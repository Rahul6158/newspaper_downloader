import streamlit as st
from newspaper_links import dates, enadu_links, sakshi_links, andhra_jyothi_links, vaartha_links, velugu_links

def main():
    st.title('Newspaper Downloader')

    # Define newspaper companies
    companies = ['Enadu', 'Sakshi', 'Andhra Jyothi', 'Vaartha', 'Velugu']

    # Create dropdowns for selecting company and date
    selected_company = st.selectbox('Select Newspaper Company', companies)
    selected_date = st.selectbox('Select Date', dates)

    # Dictionary to map company names to their respective link dictionaries
    newspaper_links = {
        'Enadu': enadu_links,
        'Sakshi': sakshi_links,
        'Andhra Jyothi': andhra_jyothi_links,
        'Vaartha': vaartha_links
        'Velugu' : velugu_links
    }

    # Determine if the selected company has multiple editions (states)
    company_links = newspaper_links.get(selected_company, {})
    has_multiple_editions = any(isinstance(link, dict) for link in company_links.values())

    if has_multiple_editions:
        states = ['AP', 'TS']
        selected_state = st.selectbox('Select State', states)
    else:
        selected_state = None

    # Get the link based on selected company, state, and date
    if has_multiple_editions:
        link = company_links.get(selected_date, {}).get(selected_state, None)
    else:
        link = company_links.get(selected_date, None)

    st.subheader("Download link : ")
    if link:
        st.markdown(f"[Open {selected_company} Newspaper for {selected_date}]({link})")
    else:
        st.write("Link not available for the selected date, company, and state.")

    st.write('<p style="line-height:1;"><br><br></p>', unsafe_allow_html=True)
    st.subheader("Selected Data : ")
    # Debugging statements to check selected values
    st.write(f"Selected Company: {selected_company}")
    if has_multiple_editions:
        st.write(f"Selected State: {selected_state}")
    st.write(f"Selected Date: {selected_date}")

if __name__ == "__main__":
    main()

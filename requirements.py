import streamlit as st
from newspaper_links import dates, enadu_links

def main():
    st.title('Newspaper Downloader')

    # Define newspaper companies and states
    companies = ['Enadu', 'Sakshi', 'Andhra Jyothi', 'Vaartha']
    states = ['AP', 'TS']

    st.write('<p style="line-height:1;"><br></p>', unsafe_allow_html=True)
    # Create dropdowns for selecting company, state, and date
    selected_company = st.selectbox('Select Newspaper Company', companies)
    selected_state = st.selectbox('Select State', states)
    selected_date = st.selectbox('Select Date', dates)

    # Define dictionary with newspaper links (sample)
    sakshi_links = {}
    andhra_jyothi_links = {}
    vaartha_links = {}

    # Dictionary to map company names to their respective link dictionaries
    newspaper_links = {
        'Enadu': enadu_links,
        'Sakshi': sakshi_links,
        'Andhra Jyothi': andhra_jyothi_links,
        'Vaartha': vaartha_links
    }

    # Get the link based on selected company, state, and date
    company_links = newspaper_links.get(selected_company, {})
    link = company_links.get(selected_date, {}).get(selected_state, None)

    st.subheader("Download link : ")
    if link:
        st.markdown(f"[Open {selected_company} Newspaper for {selected_state} on {selected_date}]({link})")
    else:
        st.write("Link not available for the selected date, company, and state.")

    st.write('<p style="line-height:1;"><br><br></p>', unsafe_allow_html=True)
    st.subheader("Selected Data : ")
    # Debugging statements to check selected values
    st.write(f"Selected Company: {selected_company}")
    st.write(f"Selected State: {selected_state}")
    st.write(f"Selected Date: {selected_date}")

if __name__ == "__main__":
    main()

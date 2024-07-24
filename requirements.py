import streamlit as st
from newspaper_links import dates, enadu_links, sakshi_links, andhra_jyothi_links, vaartha_links, velugu_links

def main():
    st.title('Newspaper Downloader')

    # Define newspaper companies and states
    companies = ['Enadu', 'Sakshi', 'Andhra Jyothi', 'Vaartha', 'Velugu']
    states = ['AP', 'TS']

    st.write('<p style="line-height:1;"><br></p>', unsafe_allow_html=True)
    
    # Create dropdowns for selecting company, state, and date
    selected_company = st.selectbox('Select Newspaper Company', companies)
    selected_date = st.selectbox('Select Date', dates)

    # Dictionary to map company names to their respective link dictionaries
    newspaper_links = {
        'Enadu': enadu_links,
        'Sakshi': sakshi_links,
        'Andhra Jyothi': andhra_jyothi_links,
        'Vaartha': vaartha_links,
        'Velugu': velugu_links
    }

    # Get the link dictionary for the selected company
    company_links = newspaper_links.get(selected_company, {})

    # Determine if the state dropdown is needed
    state_dropdown_needed = False
    if selected_date in company_links:
        # Check if there are multiple states for the selected date
        states_for_date = list(company_links[selected_date].keys())
        if len(states_for_date) > 1:
            state_dropdown_needed = True

    # Display state dropdown if needed
    if state_dropdown_needed:
        selected_state = st.selectbox('Select State', states)
    else:
        # Default to the first state if there's only one state
        selected_state = list(company_links.get(selected_date, {}).keys())[0]

    # Get the link based on selected company, state, and date
    link = company_links.get(selected_date, {}).get(selected_state, None)

    st.subheader("Download link : ")
    if link:
        st.markdown(f"[Open {selected_company} Newspaper for {selected_state} on {selected_date}]({link})")
    else:
        st.write("Link not available for the selected date, company, and state.")

    # Debugging statements to check selected values
    st.write('<p style="line-height:1;"><br><br></p>', unsafe_allow_html=True)
    st.subheader("Selected Data : ")
    st.write(f"Selected Company: {selected_company}")
    st.write(f"Selected State: {selected_state}")
    st.write(f"Selected Date: {selected_date}")

if __name__ == "__main__":
    main()

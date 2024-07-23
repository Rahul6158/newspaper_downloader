import streamlit as st

def main():
    st.title('Newspaper Links')

    # Define newspaper companies, states, and dates
    companies = ['Enadu', 'Sakshi', 'Andhra Jyothi', 'Vaartha']
    states = ['AP', 'TS']
    dates = [
        "July 23, 2024",
        "July 22, 2024",
        "July 20, 2024",
        "July 19, 2024",
        "July 18, 2024",
        "July 17, 2024",
        "July 16, 2024",
        "July 15, 2024",
        "July 14, 2024",
        "July 13, 2024",
        "July 12, 2024",
        "July 11, 2024",
        "July 10, 2024",
        "July 9, 2024",
        "July 8, 2024",
        "July 7, 2024",
        "July 6, 2024",
        "July 5, 2024",
        "July 4, 2024",
        "July 3, 2024"
    ]

    # Create dropdowns for selecting company, state, and date
    selected_company = st.selectbox('Select Newspaper Company', companies)
    selected_state = st.selectbox('Select State', states)
    selected_date = st.selectbox('Select Date', dates)

    # Debugging statements to check selected values
    st.write(f"Selected Company: {selected_company}")
    st.write(f"Selected State: {selected_state}")
    st.write(f"Selected Date: {selected_date}")

    # Define dictionary with newspaper links
    enadu_links = {
        "July 23, 2024": {
            "AP": "https://drive.google.com/file/d/1RPEq2cEtl-AkVh1_E5SIcRjosS9EL7X_/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1FGvM4xnhfZuLzPuKrKtORbiKEgRR1pC4/view?usp=drive_link",
        },
        # Add more dates and links here if available
    }

    sakshi_links = {
        "July 23, 2024": {
            "AP": "https://drive.google.com/file/d/1Jc9TSzo3eISjwaSe28MPDgMLToNqBBSW/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1QUneyxyYMN9pgY4mAL41Zc3jNekCD49Y/view?usp=drive_link"
        },
        # Add more dates and links here if available
    }

    andhra_jyothi_links = {
        "July 23, 2024": {
            "AP": "https://drive.google.com/file/d/1Jc9TSzo3eISjwaSe28MPDgMLToNqBBSW/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1QUneyxyYMN9pgY4mAL41Zc3jNekCD49Y/view?usp=drive_link",
        },
        # Add more dates and links here if available
    }

    vaartha_links = {
        "July 23, 2024": {
            "AP": "https://drive.google.com/file/d/17o7wPKPr3reiUBJBKEiIAmPgAfHmk3uV/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1gOa45CMpouE6Zi-Mq7sM6S0cNUlEWJXk/view?usp=drive_link",
        },
        # Add more dates and links here if available
    }

    # Dictionary to map company names to their respective link dictionaries
    newspaper_links = {
        'Enadu': enadu_links,
        'Sakshi': sakshi_links,
        'Andhra Jyothi': andhra_jyothi_links,
        'Vaartha': vaartha_links
    }

    # Debugging statements to check dictionary access
    st.write("Newspaper Links Dictionary Loaded")

    # Get the link based on selected company, state, and date
    company_links = newspaper_links.get(selected_company, {})
    link = company_links.get(selected_date, {}).get(selected_state, None)

    # Debugging statements to check link generation
    st.write(f"Generated Link: {link}")

    if link:
        st.markdown(f"[Open {selected_company} Newspaper for {selected_state} on {selected_date}]({link})")
    else:
        st.write("Link not available for the selected date, company, and state.")

if __name__ == "__main__":
    main()

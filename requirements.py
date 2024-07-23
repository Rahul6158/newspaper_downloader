import streamlit as st

def main():
    st.title('Newspaper Links')

    # Define newspaper companies, states, and dates
    companies = ['Enadu', 'Sakshi', 'Andhra Jyothi']
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

    # Define dictionary with newspaper links
    sakshi_links = {
    "July 23, 2024": {
        "AP": "https://drive.google.com/file/d/1Jc9TSzo3eISjwaSe28MPDgMLToNqBBSW/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1QUneyxyYMN9pgY4mAL41Zc3jNekCD49Y/view?usp=drive_link"
    },
    "July 22, 2024": {
        "AP": "https://drive.google.com/file/d/1Rh1AnfxaUqiciVwJwyHb-EOoQSWIwYOX/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1S042jX6OPPF2oN_mvyGcPbkhYOILRiYW/view?usp=drive_link"
    },
    "July 20, 2024": {
        "AP": "https://drive.google.com/file/d/1uvQTSZYD1-dgcTW5IWK4SDbPr-ki-W_r/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1uT7-V6vG1uHSw5ehLAk4GRqXgiAVG2mb/view?usp=drive_link"
    },
    "July 19, 2024": {
        "AP": "https://drive.google.com/file/d/19QSUlKvkw3Z0E03AdY_egUXI3HJrLOQH/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1WwDejTd0SGxvrF52CvAU4VndnjZT44aP/view?usp=drive_link"
    },
    "July 18, 2024": {
        "AP": "https://drive.google.com/file/d/1F29ZxO0hv8Teh4B-Z-WOX6dqAwhDOXNm/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1GifhPh6DQUx_trpZ6j3S4GMn8lBVzTMA/view?usp=drive_link"
    },
    "July 17, 2024": {
        "AP": "https://drive.google.com/file/d/1mcSpRZJ_G1nDE_KK2SKp9iPx0ad-GHcd/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1xiddIrjceCfbO7MF3WYXlEoZFD86brax/view?usp=drive_link"
    },
    "July 16, 2024": {
        "AP": "https://drive.google.com/file/d/1GiQ-SLX1FC7DTpET3-13Ajp1zrvauTC2/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1yDNppPs5Xhf5hLdZVcmrhK3T55z4QcxP/view?usp=drive_link"
    },
    "July 15, 2024": {
        "AP": "https://drive.google.com/file/d/1XWJpKepKiC_R4wcwQzqz1jI_9Ds2AiBE/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1S2q1UN8Stw9puOVj3tt63APicDe-w0gZ/view?usp=drive_link"
    },
    "July 14, 2024": {
        "AP": "https://drive.google.com/file/d/1_jpPqeYx-OdY9wKmf4bO6RBjAvxq5GiX/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1auLezQDKPzO8dUT5pXKvTGkc-cXfRLtI/view?usp=drive_link"
    },
    "July 13, 2024": {
        "AP": "https://drive.google.com/file/d/1LR1Boy3dN2Uyq-f1rbgEtU5BVt8GVdUt/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1X2mZ2jV8_mZLhYM3tjKZJeFrRwtbAUyH/view?usp=drive_link"
    },
    "July 12, 2024": {
        "AP": "https://drive.google.com/file/d/1d9NaaQI9hwaL8EUZKwcLC6GFYCuYzfLx/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1xqM0z6C3JWCv-FTMzfskT_GbS1AmzY9f/view?usp=drive_link"
    },
    "July 11, 2024": {
        "AP": "https://drive.google.com/file/d/1ZQ1l1WxAOPTLmcSJhNTPjTXeITyIPx01/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1sb5OlbCuhXicqP0cr9hZjCrLukRf1Bmw/view?usp=drive_link"
    },
    "July 10, 2024": {
        "AP": "https://drive.google.com/file/d/1xG902EH7Iz4Wg0pM_hTZEY4qpTE7lhtK/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1HNsFzUzilICqwPbVFl9-o_Lu4zBBR3wX/view?usp=drive_link"
    },
    "July 9, 2024": {
        "AP": "https://drive.google.com/file/d/1O9FWd7guBOj4TC59KSo8G9mocNzxws7V/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1Bn0okOcnc4IyKJeeafT1zod0xhi-7YBf/view?usp=drive_link"
    },
    "July 8, 2024": {
        "AP": "https://drive.google.com/file/d/1LsimarY2bT8I6QfFenN3NVg69kessT_X/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1RG9vLwWys84GBvdxCdW3OUh8VkE9C5ey/view?usp=drive_link"
    },
    "July 7, 2024": {
        "AP": "https://drive.google.com/file/d/1_8cUh2Fl9AYN-FfXEJfs3l9STcpF1gje/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1aec4RxM-P9iNnImOkyYmvmS_F51b7yj8/view?usp=drive_link"
    },
    "July 6, 2024": {
        "AP": "https://drive.google.com/file/d/1XgSSfSSfO0juE7RWUmwWQokaYgxRasw0/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1Tj7okUp2uxIZbaIbN4QK1A-Fm4GdBwqN/view?usp=drive_link"
    },
    "July 4, 2024": {
        "AP": "https://drive.google.com/file/d/161F9ynIFkJpCOYlZjmgwaEFB-XjCDsG9/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/12Bu68fLgrcQWiX7Nte_AWI0l7rOO7jJ1/view?usp=drive_link"
    },
    "July 3, 2024": {
        "AP": "https://drive.google.com/file/d/1aR2jRXZASSZ1FGmEHebtZqCiflgKpzQS/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1eRgIc2Sw48_M4gEDUy-sS0B1hdN1zu9g/view?usp=drive_link"
    },
    "July 2, 2024": {
        "AP": "https://drive.google.com/file/d/1e5Qz_LJETQN1rQWmnlKc7uN8XJX-4Mki/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1OFlZRM1fR4-k_1iHU9_fJox2-HD-e_mB/view?usp=drive_link"
    },
    "July 1, 2024": {
        "AP": "https://drive.google.com/file/d/1Yb4dwYZAUkk3W4f4fq8a7nRzqZKO3H44/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1RTch8iE-wRGa_CmfD4kHfsqKjyFQ9Dgn/view?usp=drive_link"
    },
}



    # Dictionary to map company names to their respective link dictionaries
    newspaper_links = {
        'Enadu': enadu_links,
        'Sakshi': sakshi_links,
        'Andhra Jyothi': andhra_jyothi_links
    }

    # Get the link based on selected company, state, and date
    company_links = newspaper_links.get(selected_company, {})
    link = company_links.get(selected_date, {}).get(selected_state, None)

    if link:
        st.markdown(f"[Open {selected_company} Newspaper for {selected_state} on {selected_date}]({link})")
    else:
        st.write("Link not available for the selected date, company, and state.")

if __name__ == "__main__":
    main()

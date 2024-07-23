import streamlit as st

def main():
    st.title('Newspaper Links')

    # Define newspaper companies and dates
    states = ['AP', 'TS']
    companies = ['Eenadu', 'Sakshi']
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

    # Create dropdowns for selecting state, company, and date
    selected_state = st.selectbox('Select State', states)
    selected_company = st.selectbox('Select Newspaper Company', companies)
    selected_date = st.selectbox('Select Date', dates)

    # Define dictionary with newspaper links
    newspaper_links = {
        "July 23, 2024": {
            "AP": {
                "Eenadu": "https://eenadu.net/july-23-2024-ap-eenadu",
                "Sakshi": "https://sakshi.net/july-23-2024-ap-sakshi"
            },
            "TS": {
                "Eenadu": "https://eenadu.net/july-23-2024-ts-eenadu",
                "Sakshi": "https://sakshi.net/july-23-2024-ts-sakshi"
            }
        },
        "July 22, 2024": {
            "AP": {
                "Eenadu": "https://eenadu.net/july-22-2024-ap-eenadu",
                "Sakshi": "https://sakshi.net/july-22-2024-ap-sakshi"
            },
            "TS": {
                "Eenadu": "https://eenadu.net/july-22-2024-ts-eenadu",
                "Sakshi": "https://sakshi.net/july-22-2024-ts-sakshi"
            },
        "July 18, 2024": {
            "AP": "https://drive.google.com/file/d/1OFRJe0r_zhL4dQJO_W-AE0wdDQz7HDgd/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/15TXDoNRLKaYa_pA3KCVIU_qJvCFGxG0T/view?usp=drive_link"
        },
        "July 17, 2024": {
            "AP": "https://drive.google.com/file/d/1AT7tcf7NNUVcU1soLV08V3YUlyGL1hh0/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1gDlgvoWgDDxaxNvhoyE0TnHTkAC3wROv/view?usp=drive_link"
        },
        "July 16, 2024": {
            "AP": "https://drive.google.com/file/d/1GGNzaejzsTUbMo_Pa1g1o38ZRKaUOwz_/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/110_hCVeCS-r8Efxg5et37XNInnZ2xlKm/view?usp=drive_link"
        },
        "July 15, 2024": {
            "AP": "https://drive.google.com/file/d/1jdveLGfXi_WrmNN7tonspEaPD6C74xJB/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1MZi-PPvznphUz-trVrwf_KN55vZMFmQA/view?usp=drive_link"
        },
        "July 14, 2024": {
            "AP": "https://drive.google.com/file/d/1NtboCqjjFyYUTo4h9-heL5vfNNm1he8Q/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1rW-vWSkZcWKw__0T8E_2VZiZ1tYOzQAW/view?usp=drive_link"
        },
        "July 13, 2024": {
            "AP": "https://drive.google.com/file/d/1ppsRHnfXo4KpOpG8TLgIzbooYxiut7Dc/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1_W7N21Yb8acaivULhB0CaZM9UCiNytMW/view?usp=drive_link"
        },
        "July 12, 2024": {
            "AP": "https://drive.google.com/file/d/1QduWiMdjqvuwkY1yY4uIGiY-hTV5h6nE/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1YQswJZpj-n-u0kQgoou1iISd9MR3x--K/view?usp=drive_link"
        },
        "July 11, 2024": {
            "AP": "https://drive.google.com/file/d/1pAqTnbeXw2WOSt3rwcYl5y1qkyWbM9xt/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1wQ8tZBLPXYEwdXbzvG0tzQpmBNl-hE-k/view?usp=drive_link"
        },
        "July 10, 2024": {
            "AP": "https://drive.google.com/file/d/1pzD1QVVKvquYrj9sclWNj4KF4Zrl1s5E/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1AORUfVSu6xciy6Uklseob35wtKIzKxI4/view?usp=drive_link"
        },
        "July 9, 2024": {
            "AP": "https://drive.google.com/file/d/1I-hS4l-BO6u97bdaGA47WGXqrMWckz8_/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1QlBFATS9atNYTDqB2_YhfTkvNyvw7-m6/view?usp=drive_link"
        },
        "July 8, 2024": {
            "AP": "https://drive.google.com/file/d/1wdt3PHzPnscVbT-dq3TRdo6qvRms_QrM/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1aP8POgpgraUu9C5_cPw1kWup65wGEea0/view?usp=drive_link"
        },
        "July 7, 2024": {
            "AP": "https://drive.google.com/file/d/1wj8SS5INPh1ZeT7egWAfBg6_ZsTxujSi/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1V-281WP_Nnsrmmyr3-O_kYiJwCTiLHAr/view?usp=drive_link"
        },
        "July 6, 2024": {
            "AP": "https://drive.google.com/file/d/16GKPq5sbHd6iPS91kuSBEvbSh6kiY7hD/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1VKN34guROH0tD1nRiupLW6SS07siHyrp/view?usp=drive_link"
        },
        "July 5, 2024": {
            "AP": "https://drive.google.com/file/d/19Ewozo_AvA8dpy3mgCVPbHLN1E6v38tv/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1bwvW1At3UKNe-U6mWGvVkvNW5CaaeUGR/view?usp=drive_link"
        },
        "July 4, 2024": {
            "AP": "https://drive.google.com/file/d/1y4nnw3VE8dKbXsVo3yaS8_hWpKOp60XQ/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1Y4ez42kPOdZJyxDV_puxqo1Jvgw3iTr0/view?usp=drive_link"
        },
        "July 3, 2024": {
            "AP": "https://drive.google.com/file/d/1QL4pA8u4y68TczPdwps7EjINM7M6G30x/view?usp=drive_link",
            "TS": "https://drive.google.com/file/d/1IaSC2NXyyI1dNHGzq_Sz0ogQF33wPbZR/view?usp=drive_link"
        }
    }

    # Display the selected link based on the company and date selection
    if selected_date in newspaper_links and selected_company in newspaper_links[selected_date]:
        selected_link = newspaper_links[selected_date][selected_company]
        st.markdown(f"### Link for {selected_company} on {selected_date}:")
        st.markdown(f"[Newspaper Link]({selected_link})")
    else:
        st.error("No link found for the selected date and company.")

if __name__ == '__main__':
    main()

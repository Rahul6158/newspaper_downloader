import streamlit as st

def main():
    st.title('Enadu Newspaper Links')
    
    # Define the links and dates
    newspaper_links = [
        {"date": "July 23, 2024", "AP": "https://drive.google.com/file/d/1RPEq2cEtl-AkVh1_E5SIcRjosS9EL7X_/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1FGvM4xnhfZuLzPuKrKtORbiKEgRR1pC4/view?usp=drive_link"},
        {"date": "July 22, 2024", "AP": "https://drive.google.com/file/d/11gm91EhEakpO68Bdn_k9VcR7EU5TSbs1/view?usp=sharing", "TS": "https://drive.google.com/file/d/1H4QbQXaOrTC1qHpUzVphdbHR0UqUmass/view?usp=drive_link"},
        {"date": "July 20, 2024", "AP": "https://drive.google.com/file/d/1myejG97s14gsU7uIgVMvyYV5b_-SEcUX/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1EwiyphKa74QUaSsurag_N2GLc-Kkqiz_/view?usp=drive_link"},
        {"date": "July 19, 2024", "AP": "https://drive.google.com/file/d/1VZ62M8xjjadqFGe0u9WC-xYl_mcD87T2/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1lwLXv5vGQ6oSHu24OLEzN1NDlpNaa_RG/view?usp=drive_link"},
        {"date": "July 18, 2024", "AP": "https://drive.google.com/file/d/1OFRJe0r_zhL4dQJO_W-AE0wdDQz7HDgd/view?usp=drive_link", "TS": "https://drive.google.com/file/d/15TXDoNRLKaYa_pA3KCVIU_qJvCFGxG0T/view?usp=drive_link"},
        {"date": "July 17, 2024", "AP": "https://drive.google.com/file/d/1AT7tcf7NNUVcU1soLV08V3YUlyGL1hh0/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1gDlgvoWgDDxaxNvhoyE0TnHTkAC3wROv/view?usp=drive_link"},
        {"date": "July 16, 2024", "AP": "https://drive.google.com/file/d/1GGNzaejzsTUbMo_Pa1g1o38ZRKaUOwz_/view?usp=drive_link", "TS": "https://drive.google.com/file/d/110_hCVeCS-r8Efxg5et37XNInnZ2xlKm/view?usp=drive_link"},
        {"date": "July 15, 2024", "AP": "https://drive.google.com/file/d/1jdveLGfXi_WrmNN7tonspEaPD6C74xJB/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1MZi-PPvznphUz-trVrwf_KN55vZMFmQA/view?usp=drive_link"},
        {"date": "July 14, 2024", "AP": "https://drive.google.com/file/d/1NtboCqjjFyYUTo4h9-heL5vfNNm1he8Q/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1rW-vWSkZcWKw__0T8E_2VZiZ1tYOzQAW/view?usp=drive_link"},
        {"date": "July 13, 2024", "AP": "https://drive.google.com/file/d/1ppsRHnfXo4KpOpG8TLgIzbooYxiut7Dc/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1_W7N21Yb8acaivULhB0CaZM9UCiNytMW/view?usp=drive_link"},
        {"date": "July 12, 2024", "AP": "https://drive.google.com/file/d/1QduWiMdjqvuwkY1yY4uIGiY-hTV5h6nE/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1YQswJZpj-n-u0kQgoou1iISd9MR3x--K/view?usp=drive_link"},
        {"date": "July 11, 2024", "AP": "https://drive.google.com/file/d/1pAqTnbeXw2WOSt3rwcYl5y1qkyWbM9xt/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1wQ8tZBLPXYEwdXbzvG0tzQpmBNl-hE-k/view?usp=drive_link"},
        {"date": "July 10, 2024", "AP": "https://drive.google.com/file/d/1pzD1QVVKvquYrj9sclWNj4KF4Zrl1s5E/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1AORUfVSu6xciy6Uklseob35wtKIzKxI4/view?usp=drive_link"},
        {"date": "July 9, 2024", "AP": "https://drive.google.com/file/d/1I-hS4l-BO6u97bdaGA47WGXqrMWckz8_/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1QlBFATS9atNYTDqB2_YhfTkvNyvw7-m6/view?usp=drive_link"},
        {"date": "July 8, 2024", "AP": "https://drive.google.com/file/d/1wdt3PHzPnscVbT-dq3TRdo6qvRms_QrM/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1aP8POgpgraUu9C5_cPw1kWup65wGEea0/view?usp=drive_link"},
        {"date": "July 7, 2024", "AP": "https://drive.google.com/file/d/1wj8SS5INPh1ZeT7egWAfBg6_ZsTxujSi/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1V-281WP_Nnsrmmyr3-O_kYiJwCTiLHAr/view?usp=drive_link"},
        {"date": "July 6, 2024", "AP": "https://drive.google.com/file/d/16GKPq5sbHd6iPS91kuSBEvbSh6kiY7hD/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1VKN34guROH0tD1nRiupLW6SS07siHyrp/view?usp=drive_link"},
        {"date": "July 5, 2024", "AP": "https://drive.google.com/file/d/19Ewozo_AvA8dpy3mgCVPbHLN1E6v38tv/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1bwvW1At3UKNe-U6mWGvVkvNW5CaaeUGR/view?usp=drive_link"},
        {"date": "July 4, 2024", "AP": "https://drive.google.com/file/d/1y4nnw3VE8dKbXsVo3yaS8_hWpKOp60XQ/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1Y4ez42kPOdZJyxDV_puxqo1Jvgw3iTr0/view?usp=drive_link"},
        {"date": "July 3, 2024", "AP": "https://drive.google.com/file/d/1QL4pA8u4y68TczPdwps7EjINM7M6G30z/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1ZK-6q9FZ0jESWJt5y2X3ZX9yWgqRbGmK/view?usp=drive_link"},
        {"date": "July 2, 2024", "AP": "https://drive.google.com/file/d/1Y4ez42kPOdZJyxDV_puxqo1Jvgw3iTr0/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1VA10zexXK0oJTk-9lKEL1NcMXYLkPl5t/view?usp=drive_link"},
        {"date": "July 1, 2024", "AP": "https://drive.google.com/file/d/1QlBFATS9atNYTDqB2_YhfTkvNyvw7-m6/view?usp=drive_link", "TS": "https://drive.google.com/file/d/1I-hS4l-BO6u97bdaGA47WGXqrMWckz8_/view?usp=drive_link"},
    ]
    
    # Display the links
    for newspaper in newspaper_links:
        st.subheader(newspaper['date'])
        st.write("AP: ", newspaper['AP'])
        st.write("TS: ", newspaper['TS'])
        st.markdown("---")

if __name__ == "__main__":
    main()

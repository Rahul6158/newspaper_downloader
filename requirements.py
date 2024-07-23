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

    andhra_jyothi_links = {'July 23, 2024': {'AP': 'https://drive.google.com/file/d/1Jc9TSzo3eISjwaSe28MPDgMLToNqBBSW/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1QUneyxyYMN9pgY4mAL41Zc3jNekCD49Y/view?usp=drive_link'},
                           'July 22, 2024': {'AP': 'https://drive.google.com/file/d/1Rh1AnfxaUqiciVwJwyHb-EOoQSWIwYOX/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1S042jX6OPPF2oN_mvyGcPbkhYOILRiYW/view?usp=drive_link'}, 
                           'July 20, 2024': {'AP': 'https://drive.google.com/file/d/1uvQTSZYD1-dgcTW5IWK4SDbPr-ki-W_r/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1uT7-V6vG1uHSw5ehLAk4GRqXgiAVG2mb/view?usp=drive_link'}, 
                           'July 19, 2024': {'AP': 'https://drive.google.com/file/d/19QSUlKvkw3Z0E03AdY_egUXI3HJrLOQH/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1WwDejTd0SGxvrF52CvAU4VndnjZT44aP/view?usp=drive_link'}, 
                           'July 18, 2024': {'AP': 'https://drive.google.com/file/d/1F29ZxO0hv8Teh4B-Z-WOX6dqAwhDOXNm/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1GifhPh6DQUx_trpZ6j3S4GMn8lBVzTMA/view?usp=drive_link'}, 
                           'July 17, 2024': {'AP': 'https://drive.google.com/file/d/1mcSpRZJ_G1nDE_KK2SKp9iPx0ad-GHcd/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1xiddIrjceCfbO7MF3WYXlEoZFD86brax/view?usp=drive_link'}, 
                           'July 16, 2024': {'AP': 'https://drive.google.com/file/d/1GiQ-SLX1FC7DTpET3-13Ajp1zrvauTC2/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1yDNppPs5Xhf5hLdZVcmrhK3T55z4QcxP/view?usp=drive_link'}, 
                           'July 15, 2024': {'AP': 'https://drive.google.com/file/d/1XWJpKepKiC_R4wcwQzqz1jI_9Ds2AiBE/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1S2q1UN8Stw9puOVj3tt63APicDe-w0gZ/view?usp=drive_link'}, 
                           'July 14, 2024': {'AP': 'https://drive.google.com/file/d/1_jpPqeYx-OdY9wKmf4bO6RBjAvxq5GiX/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1auLezQDKPzO8dUT5pXKvTGkc-cXfRLtI/view?usp=drive_link'}, 
                           'July 13, 2024': {'AP': 'https://drive.google.com/file/d/1LR1Boy3dN2Uyq-f1rbgEtU5BVt8GVdUt/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1X2mZ2jV8_mZLhYM3tjKZJeFrRwtbAUyH/view?usp=drive_link'}, 
                           'July 12, 2024': {'AP': 'https://drive.google.com/file/d/1d9NaaQI9hwaL8EUZKwcLC6GFYCuYzfLx/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1xqM0z6C3JWCv-FTMzfskT_GbS1AmzY9f/view?usp=drive_link'}, 
                           'July 11, 2024': {'AP': 'https://drive.google.com/file/d/1ZQ1l1WxAOPTLmcSJhNTPjTXeITyIPx01/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1sb5OlbCuhXicqP0cr9hZjCrLukRf1Bmw/view?usp=drive_link'}, 
                           'July 10, 2024': {'AP': 'https://drive.google.com/file/d/1xG902EH7Iz4Wg0pM_hTZEY4qpTE7lhtK/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1HNsFzUzilICqwPbVFl9-o_Lu4zBBR3wX/view?usp=drive_link'}, 
                           'July 9, 2024': {'AP': 'https://drive.google.com/file/d/1O9FWd7guBOj4TC59KSo8G9mocNzxws7V/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1Bn0okOcnc4IyKJeeafT1zod0xhi-7YBf/view?usp=drive_link'}, 
                           'July 8, 2024': {'AP': 'https://drive.google.com/file/d/1LsimarY2bT8I6QfFenN3NVg69kessT_X/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1RG9vLwWys84GBvdxCdW3OUh8VkE9C5ey/view?usp=drive_link'},
                           'July 7, 2024': {'AP': 'https://drive.google.com/file/d/1_8cUh2Fl9AYN-FfXEJfs3l9STcpF1gje/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1aec4RxM-P9iNnImOkyYmvmS_F51b7yj8/view?usp=drive_link'},
                           'July 6, 2024': {'AP': 'https://drive.google.com/file/d/1XgSSfSSfO0juE7RWUmwWQokaYgxRasw0/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1Tj7okUp2uxIZbaIbN4QK1A-Fm4GdBwqN/view?usp=drive_link'},
                           'July 4, 2024': {'AP': 'https://drive.google.com/file/d/161F9ynIFkJpCOYlZjmgwaEFB-XjCDsG9/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/12Bu68fLgrcQWiX7Nte_AWI0l7rOO7jJ1/view?usp=drive_link'},
                           '03 July 2024': {'AP': 'https://drive.google.com/file/d/1aR2jRXZASSZ1FGmEHebtZqCiflgKpzQS/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1eRgIc2Sw48_M4gEDUy-sS0B1hdN1zu9g/view?usp=drive_link'}, 
                           '02 July 2024': {'AP': 'https://drive.google.com/file/d/1e5Qz_LJETQN1rQWmnlKc7uN8XJX-4Mki/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1OFlZRM1fR4-k_1iHU9_fJox2-HD-e_mB/view?usp=drive_link'}, '01 July 2024': {' AP': 'https://drive.google.com/file/d/1Yb4dwYZAUkkmzSqsJHw7AxwHe3dEsDqs/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1OEaSTyi7W31Yg25rhjg8a8JqfuDmxgu-/view?usp=drive_link'}, '30 June 2024': {'AP': 'https://drive.google.com/file/d/1tp4PrBzr9OWPYjHOXFmsg-94uHJf2xjz/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1x9w6N6rTc-USdoQD9ZkzgmPQmHuuGlq6/view?usp=drive_link'}, '29 June 2024': {'AP': 'https://drive.google.com/file/d/1iPR-mH2vrCqDkysSRtjHvgtuHEAJaD-X/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1cks6ECqPCT04hcclyKIUVkeTlPHkEyZ3/view?usp=drive_link'}, '28 June 2024': {'AP': 'https://drive.google.com/file/d/1M-Wl3vTNwuuv1SjFR8fGYjttsNpRe89g/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1Q73BNhYnXwPgKaOsCBcIkBJe9vxgPdyC/view?usp=drive_link'}, '27 June 2024': {'AP': 'https://drive.google.com/file/d/1JDEeCu8Ee2WE3mlUukyW8zXvXN9WhYHp/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1G8wXhKc53-goZ6A3w0iWlJ2YRfghk_vg/view?usp=drive_link'}, '26 June 2024': {'AP': 'https://drive.google.com/file/d/1hnI8QuP7w3JWIPivdoIvJcmjYi0858RE/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1k6hud1PZroMuVzJGppSkocJfVM9SZgdi/view?usp=drive_link'}, '25 June 2024': {'AP': 'https://drive.google.com/file/d/1CYpDfg-0y1-8XMxaXZ2MYNjE_2sD2ri_/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/11D7iYNdkzZKEFDJhxl9QNfts5ag09omt/view?usp=drive_link'}, '24 June 2024': {'AP': 'https://drive.google.com/file/d/1_a105MOqsF4XYgHdWJ3jfjQbdKwNxydZ/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1KeroOhJhCviB9Dcc0qTzspvxzNx0iIof/view?usp=drive_link'}, '23 June 2024': {'AP': 'https://drive.google.com/file/d/10XIp2qll06XY_-OfVDi38QNAAtgXZiCe/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1ZWN-RTAbtsJnb6AO9_EK9YN0iZ_rb8NF/view?usp=drive_link'}, '22 June 2024': {'AP': 'https://drive.google.com/file/d/1ZkRhVYlAcwDSjhpYBpBv0QWZ_ScS1VR4/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/18RUlomsaAAO2yHo8m04Y9CjxZxC7kN_s/view?usp=drive_link'}, '21 June 2024': {'AP': 'https://drive.google.com/file/d/1ATkWtqgflIrRuVE_88m9cndET7kxWO9P/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/14btoi1IjEYPp4Cqs0YANr7-Ev9V0Lg8b/view?usp=drive_link'}, '20 June 2024': {'AP': 'https://drive.google.com/file/d/1ObUe-8VQ8sx9zb29XzrFfeUhgwwDA7eX/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1zcG3QMcdg8xFz2IVYOhoDBfxaHERRelz/view?usp=drive_link'}, '19 June 2024': {'AP': 'https://drive.google.com/file/d/1BHhuPkHlx8IPLz8v75Z8nwstWRMNl-xz/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1apHY22bcZBwCSi0Zn6-GZVc3uHZEtzOH/view?usp=drive_link'}, '18 June 2024': {'AP': 'https://drive.google.com/file/d/1KIWeE-aDT8EVq80y9HZ8-qiM3asYxP-m/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/15imQ99mLQL4mwxBWlxy4gTVaB1VeZhOr/view?usp=drive_link'}, '17 June 2024': {'AP': 'https://drive.google.com/file/d/1sdkknGTfPgmyW93IYc_R28QXWgEQRj9g/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1XAnRslr2LuQKxtp1T7JksXYl9Y51_qPk/view?usp=drive_link'}, '16 June 2024': {'AP': 'https://drive.google.com/file/d/1SDzL2-S9yKySRFiq43bmEO1krcv2987g/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1oEEvXfxNgACh2u5vOADgaYvAZaqJyEhX/view?usp=drive_link'}, '15 June 2024': {'AP': 'https://drive.google.com/file/d/1qDE1a7BfcN7ST2NirVIoyIG772GI8cRG/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1weuBOjSAY9bzrjv04M0YVcbGTN_K3FXf/view?usp=drive_link'}, '14 June 2024': {'AP': 'https://drive.google.com/file/d/1Rto60NPkf6Woi2g7T197vPSDlNoMRREY/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/10aTTKQ21uKSaf5vopZUIyjrg45k3sV_m/view?usp=drive_link'}, '13 June 2024': {'AP': 'https://drive.google.com/file/d/1f4NTdUvpxLBrg5ZXENMMeNGQRtsfyJGc/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1kjut_325iHH53TaWeFoasBnTCBTk-uWb/view?usp=drive_link'}, '12 June 2024': {'AP': 'https://drive.google.com/file/d/1bHiZh8qNqms8pU1oOyhnGkCvVNIl68iQ/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1w-7JfeAnRhGnkSEc_XWmG-4yV1cRPFf3/view?usp=drive_link'}, '11 June 2024': {'AP': 'https://drive.google.com/file/d/1678Q5tmUv8VFnfzxvuXT8shMAjwSR_5m/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1dv6KX7-XxmFlDXM0V0M46kZSHkt4GSxd/view?usp=drive_link'}, '10 June 2024': {'AP': 'https://drive.google.com/file/d/1qZw4tgFxYn6CHw83atoeS5Te_dLt--dq/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1mDomTD8StKAksq4n_Urv6_AfiixrGNON/view?usp=drive_link'}, '09 June 2024': {'AP': 'https://drive.google.com/file/d/1ZvO1wOT-AO8Fpp5tiu5KhhjmBz1y23d8/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1K1Iv2AaUJhhLJTmmms6CXBauhhp8g3dh/view?usp=drive_link'}, '08 June 2024': {'AP': 'https://drive.google.com/file/d/1WWoNv4apnuqLhUfN8zH4GF5dZ3nX7irr/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1_Agp2spOXXbEz1JtosVbkql14AOlATR1/view?usp=drive_link'}, '07 June 2024': {'AP': 'https://drive.google.com/file/d/1qjDOf2vAJinyBzWUq8nw8uPGWXsN_NhJ/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1laGPXBB_XzMIhzXelEcZvbPk7RgJbbUx/view?usp=drive_link'}, '06 June 2024': {'AP': 'https://drive.google.com/file/d/1c7fXupnFYtO98KaBgzGjZ43G5vKuHAW0/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1c7fXupnFYtO98KaBgzGjZ43G5vKuHAW0/view?usp=drive_link'}, 'June 5, 2024': {'AP': 'https://drive.google.com/file/d/1CsFJKdMmoEOxcw9B_XZyJ5aFWDkxQydf/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1K5oX4lT4zGMqpzhRIDwMr3gvvTxf7SXp/view?usp=drive_link'}, '04 June 2024': {'AP': 'https://drive.google.com/file/d/1uZGwjhzZq_lrzqvQPh8REC0fql-423vQ/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1a-xauI2orA_bI2VLJYDAXw3X01XArK-9/view?usp=drive_link'}, '03 June 2024': {'AP': 'https://drive.google.com/file/d/1Ly3zvoB1mgFqMex8aEficPLosPAl0wVv/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1nBBWJJzV_bp3GmckaMK45cxF96EtQo6k/view?usp=drive_link'}, '02 June 2024': {'AP ': 'https://drive.google.com/file/d/1_Q-8CydsYErKnuQUbZVj6Y2gVji7v2ji/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1dHWzm4Tdpz21kF2D0XmK19c8H_w7YRwv/view?usp=drive_link'}, '31 May 2024': {'AP': 'https://drive.google.com/file/d/1SZpIAhdVhegvj-9e8VJ0OJw8vHt78t4K/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1A5mBwCft5fL6oOFr9mkStbX7Tqe-6hLB/view?usp=drive_link'}, '30 May 2024': {'AP ': 'https://drive.google.com/file/d/16KnamKFL7hFl76kEO85DHv_QOg810FIa/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/10lvc0hfuu7OEbcsB67ObUnSSzGwCQUwi/view?usp=drive_link'}, '29 May 2024': {'AP': 'https://drive.google.com/file/d/1BhEjrbbDamp0lSSPuuldpSS56IgsT_m1/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1sJz6xw_LaA8cLPeULlhLKGvsUQKNKL4n/view?usp=drive_link'}, '28 May 2024': {'AP': 'https://drive.google.com/file/d/1141OvsHuE5MP3jhafhXfN_F6DVzkFWAY/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1NlEiO92K9WUSYnN8eevYA0ORpi6UFct1/view?usp=drive_link'}, '27 May 2024': {'AP': 'https://drive.google.com/file/d/1iKM2gH6ySUDYnca4SMEhqYmZlSPQdFq4/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1AVA8DSpk7fj1MJiMaXHSvCTYOkbboamu/view?usp=drive_link'}, '26 May 2024': {'AP': 'https://drive.google.com/file/d/1iY2vEtLrTPL3aFL3pf_-Su4mpywZ5qkt/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1pdn7MQN2PiiFBQQWBt8mLHAQ1yr5PVUP/view?usp=drive_link'}, '25 May 2024': {'AP': 'https://drive.google.com/file/d/1WsRVrtFSI2C0Jg8JioqQDu-gWspptKm4/view?usp=drive_link', 'TS': 'https://drive.google.com/file/d/1f3Dxu2Gai6WS0SJmY-spLuodwCXWUMDq/view?usp=drive_link'}}


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

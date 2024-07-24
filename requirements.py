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
    "July 3, 2024",
    "July 2, 2024",
    "July 1, 2024",
    "June 30, 2024",
    "June 29, 2024",
    "June 28, 2024",
    "June 27, 2024",
    "June 26, 2024",
    "June 25, 2024",
    "June 24, 2024",
    "June 23, 2024",
    "June 22, 2024",
    "June 21, 2024",
    "June 20, 2024",
    "June 19, 2024",
    "June 18, 2024",
    "June 17, 2024",
    "June 16, 2024",
    "June 15, 2024",
    "June 14, 2024",
    "June 13, 2024",
    "June 12, 2024",
    "June 11, 2024",
    "June 10, 2024",
    "June 9, 2024",
    "June 8, 2024",
    "June 7, 2024",
    "June 6, 2024",
    "June 5, 2024",
    "June 4, 2024"
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
    "July 24, 2024": {
        "AP": "https://drive.google.com/file/d/126iB7bjmEIypSt2t4YSgK8VK51btwGxs/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1AeURgnafRGKTw-E8qg6SGtkqAksDJFDi/view?usp=drive_link",
    },
    "July 23, 2024": {
        "AP": "https://drive.google.com/file/d/1RPEq2cEtl-AkVh1_E5SIcRjosS9EL7X_/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1FGvM4xnhfZuLzPuKrKtORbiKEgRR1pC4/view?usp=drive_link",
    },
    "July 22, 2024": {
        "AP": "https://drive.google.com/file/d/11gm91EhEakpO68Bdn_k9VcR7EU5TSbs1/view?usp=sharing",
        "TS": "https://drive.google.com/file/d/1H4QbQXaOrTC1qHpUzVphdbHR0UqUmass/view?usp=drive_link",
    },
    "July 20, 2024": {
        "AP": "https://drive.google.com/file/d/1myejG97s14gsU7uIgVMvyYV5b_-SEcUX/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1EwiyphKa74QUaSsurag_N2GLc-Kkqiz_/view?usp=drive_link",
    },
    "July 19, 2024": {
        "AP": "https://drive.google.com/file/d/1VZ62M8xjjadqFGe0u9WC-xYl_mcD87T2/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1lwLXv5vGQ6oSHu24OLEzN1NDlpNaa_RG/view?usp=drive_link",
    },
    "July 18, 2024": {
        "AP": "https://drive.google.com/file/d/1OFRJe0r_zhL4dQJO_W-AE0wdDQz7HDgd/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/15TXDoNRLKaYa_pA3KCVIU_qJvCFGxG0T/view?usp=drive_link",
    },
    "July 17, 2024": {
        "AP": "https://drive.google.com/file/d/1AT7tcf7NNUVcU1soLV08V3YUlyGL1hh0/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1gDlgvoWgDDxaxNvhoyE0TnHTkAC3wROv/view?usp=drive_link",
    },
    "July 16, 2024": {
        "AP": "https://drive.google.com/file/d/1GGNzaejzsTUbMo_Pa1g1o38ZRKaUOwz_/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/110_hCVeCS-r8Efxg5et37XNInnZ2xlKm/view?usp=drive_link",
    },
    "July 15, 2024": {
        "AP": "https://drive.google.com/file/d/1jdveLGfXi_WrmNN7tonspEaPD6C74xJB/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1MZi-PPvznphUz-trVrwf_KN55vZMFmQA/view?usp=drive_link",
    },
    "July 14, 2024": {
        "AP": "https://drive.google.com/file/d/1NtboCqjjFyYUTo4h9-heL5vfNNm1he8Q/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1rW-vWSkZcWKw__0T8E_2VZiZ1tYOzQAW/view?usp=drive_link",
    },
    "July 13, 2024": {
        "AP": "https://drive.google.com/file/d/1ppsRHnfXo4KpOpG8TLgIzbooYxiut7Dc/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1_W7N21Yb8acaivULhB0CaZM9UCiNytMW/view?usp=drive_link",
    },
    "July 12, 2024": {
        "AP": "https://drive.google.com/file/d/1QduWiMdjqvuwkY1yY4uIGiY-hTV5h6nE/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1YQswJZpj-n-u0kQgoou1iISd9MR3x--K/view?usp=drive_link",
    },
    "July 11, 2024": {
        "AP": "https://drive.google.com/file/d/1pAqTnbeXw2WOSt3rwcYl5y1qkyWbM9xt/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1wQ8tZBLPXYEwdXbzvG0tzQpmBNl-hE-k/view?usp=drive_link",
    },
    "July 10, 2024": {
        "AP": "https://drive.google.com/file/d/1pzD1QVVKvquYrj9sclWNj4KF4Zrl1s5E/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1AORUfVSu6xciy6Uklseob35wtKIzKxI4/view?usp=drive_link",
    },
    "July 09, 2024": {
        "AP": "https://drive.google.com/file/d/1I-hS4l-BO6u97bdaGA47WGXqrMWckz8_/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1QlBFATS9atNYTDqB2_YhfTkvNyvw7-m6/view?usp=drive_link",
    },
    "July 08, 2024": {
        "AP": "https://drive.google.com/file/d/1wdt3PHzPnscVbT-dq3TRdo6qvRms_QrM/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1aP8POgpgraUu9C5_cPw1kWup65wGEea0/view?usp=drive_link",
    },
    "July 07, 2024": {
        "AP": "https://drive.google.com/file/d/1wj8SS5INPh1ZeT7egWAfBg6_ZsTxujSi/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1V-281WP_Nnsrmmyr3-O_kYiJwCTiLHAr/view?usp=drive_link",
    },
    "July 06, 2024": {
        "AP": "https://drive.google.com/file/d/16GKPq5sbHd6iPS91kuSBEvbSh6kiY7hD/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1VKN34guROH0tD1nRiupLW6SS07siHyrp/view?usp=drive_link",
    },
    "July 05, 2024": {
        "AP": "https://drive.google.com/file/d/19Ewozo_AvA8dpy3mgCVPbHLN1E6v38tv/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1bwvW1At3UKNe-U6mWGvVkvNW5CaaeUGR/view?usp=drive_link",
    },
    "July 04, 2024": {
        "AP": "https://drive.google.com/file/d/1y4nnw3VE8dKbXsVo3yaS8_hWpKOp60XQ/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1Y4ez42kPOdZJyxDV_puxqo1Jvgw3iTr0/view?usp=drive_link",
    },
    "July 03, 2024": {
        "AP": "https://drive.google.com/file/d/1QL4pA8u4yH6HJsItRUfaH9MYYXP1Ce55/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1ypme4YoxOnZ4WOUII8elmR2Ml4X_kLMJ/view?usp=drive_link",
    },
    "July 02, 2024": {
        "AP": "https://drive.google.com/file/d/1ho71GEsiVaByhMANfASvTrg38IsXhPv-/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1vxKBsIA2PdCt3Oz_aWTiDFbF73tdetQw/view?usp=drive_link",
    },
    "July 01, 2024": {
        "AP": "https://drive.google.com/file/d/1_tlLJhS91e473wnxG30-qIxXg3bWoifu/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1TcP8BTk6o69JltxUBINCZucmjgGVKfS0/view?usp=drive_link",
    },
    "June 30, 2024": {
        "AP": "https://drive.google.com/file/d/1PgIhUeRSWWyG8FrXrIKPoe0TDHeX-xiO/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/11fO1XLZydAEtnp6Z6UokFYk9Rc-6lH45/view?usp=drive_link",
    },
    "June 29, 2024": {
        "AP": "https://drive.google.com/file/d/1HC7YCMUNZ3q261qXg7BId_hKJUIPmCPu/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1rw8d5ktWovACVMmXlAdJzsqRJF5VwMhm/view?usp=drive_link",
    },
    "June 28, 2024": {
        "AP": "https://drive.google.com/file/d/1p-KBtGyXazIpFdgFy83adhlT8NajBWq7/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1WYGD1f6mUCsXdcGZbMOUnTVb32_7fi-H/view?usp=drive_link",
    },
    "June 27, 2024": {
        "AP": "https://drive.google.com/file/d/1j9xmIpdvJJwUtPMXmnPRfcFPsoUf3nw8/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1gRhCL4BuQMSkznhytPItdpUALrSjZIAy/view?usp=drive_link",
    },
    "June 26, 2024": {
        "AP": "https://drive.google.com/file/d/1OXd63ZXGFkuf1khpFlovqcqYXBgXx4d6/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1GGkfdIuG37N8vjr-9c0_FLUNwwDmYgOJ/view?usp=drive_link",
    },
    "June 25, 2024": {
        "AP": "https://drive.google.com/file/d/1mcAKvrg-geUehDgxdNaPIZ45NQtlMbsi/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1zJ94AzDjqTGtDJGdEV5GYCWaOydIJzZR/view?usp=drive_link",
    },
    "June 24, 2024": {
        "AP": "https://drive.google.com/file/d/1tMW798FHXhPL19737ZQ9N1UYe4UwVKam/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/14D3Tsy6UFGrGQwkLFtLhDg3LUePj1_l2/view?usp=drive_link",
    },
    "June 23, 2024": {
        "AP": "https://drive.google.com/file/d/1YTfBuMiA9vGSN7Wzo_YiyXq9tgZkXF3B/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1WYoBuaHerQgsaDEAotBw6tNRmhLxcIDG/view?usp=drive_link",
    },
    "June 22, 2024": {
        "AP": "https://drive.google.com/file/d/1mu1eZ1NOI7pUjwrgg5NrfNFhV_D0JZWd/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/11T_3T7u_uV05E6WmaEA2WA9sfgsV-bSW/view?usp=drive_link",
    },
    "June 21, 2024": {
        "AP": "https://drive.google.com/file/d/12z-BBBgQVJx7kYCgGUOsSiznEBeNsixA/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1vcCkBGWb-mebFuAEs9X0X-eL3A7vD3Io/view?usp=drive_link",
    },
    "June 20, 2024": {
        "AP": "https://drive.google.com/file/d/1KwOQyrl4h6vcaydLyOzJGS4wUWY9utNi/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/18oaK10RfwenlFfDiwCjmzysZQj9v6aWH/view?usp=drive_link",
    },
    "June 19, 2024": {
        "AP": "https://drive.google.com/file/d/1VHmXa7SvNGByRP1yZsLT6QO7BZL-cglJ/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1XTRClSOVLwuadw2AvT0ch2VK7Rrd9Kje/view?usp=drive_link",
    },
    "June 18, 2024": {
        "AP": "https://drive.google.com/file/d/1CqKOnbhSH4ceKgFnKO9rc_izvEQAc5Kx/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1mP6vfJSJVpdqucW5vAxwEAPKTNvjFyCl/view?usp=drive_link",
    },
    "June 17, 2024": {
        "AP": "https://drive.google.com/file/d/1uDCFl_mufQny4rO7yKwN1emFNBxZYv6W/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1QBKur0x_H83dVD10nm5U1A5oxciOxaa8/view?usp=drive_link",
    },
    "June 16, 2024": {
        "AP": "https://drive.google.com/file/d/1wVPn2DHdgmCEPrWAh1QV2KfxQDzW23uh/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1oKlxCvVk0erLabNrcgGXq-yUx-gZ9DvL/view?usp=drive_link",
    },
    "June 15, 2024": {
        "AP": "https://drive.google.com/file/d/1tU3ONXrtjuPgtltfaTn5HkG65Cjr02C7/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/15-YPONLDskMzuy2OCaPR9AlIUCDuozM8/view?usp=drive_link",
    },
    "June 14, 2024": {
        "AP": "https://drive.google.com/file/d/1P-V9gdsSDh4YSipbGwFiFYNWBeIlLhWf/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1OeErGVMhUjjmTiCFW2DWvxu1Ep8Aj2Ww/view?usp=drive_link",
    },
    "June 13, 2024": {
        "AP": "https://drive.google.com/file/d/1hWcey8btWHPQx3YVB030U0jidgz8Y1Vr/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/164UssxFGvuje5Oe8SHT5IKXFHYpcJdCk/view?usp=drive_link",
    },
    "June 12, 2024": {
        "AP": "https://drive.google.com/file/d/1KCWIxfwyeZuj1UxAy39LaqPkB6J72Bnj/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/14LFGEpcEm0FvXpdZVgsZZNAGt72dIy48/view?usp=drive_link",
    },
    "June 11, 2024": {
        "AP": "https://drive.google.com/file/d/1TzGKJ7v3jt5gD_QV1XBbYD66XM7igS6S/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/10VOmANJCcMo7x19r0CcgKBJgNFSxLpsD/view?usp=drive_link",
    },
    "June 10, 2024": {
        "AP": "https://drive.google.com/file/d/1gN9EAlSaeVDcEeI1BkC7vzCIhP-yeeNU/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1XoYfgi5pIetefVmKVdV3pyxCn_4ipNKg/view?usp=drive_link",
    },
    "June 09, 2024": {
        "AP": "https://drive.google.com/file/d/1LyR0lUy9hsCgMSozIbu4S7JOH2X-2BMw/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1kRL7BXdQzrhoGvIxVjttKc5aCLBmlE_z/view?usp=drive_link",
    },
    "June 08, 2024": {
        "AP": "https://drive.google.com/file/d/1Texh2-fwYWtvyzc22l1oCYXTBu3qCHJi/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/10YnRIh9hfgCUXduN6GkiYMdV_dyQTOro/view?usp=drive_link",
    },
    "June 07, 2024": {
        "AP": "https://drive.google.com/file/d/1uonQe-Ej5Rw2MXpkfklAmC1g82YcMOMc/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1WyP1lshmB-_8BrFMByrNs0Gbx2z3YsqH/view?usp=drive_link",
    },
    "June 06, 2024": {
        "AP": "https://drive.google.com/file/d/1nczadMUEhn3iWonkcJ12QuECORiN7NSp/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1UzUQcChj-t7gMwTAOz-F16RYH6jReZGW/view?usp=drive_link",
    },
    "June 05, 2024": {
        "AP": "https://drive.google.com/file/d/1MUao_2L5QbO9BgTwTsioH97hqGonPXQW/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1nOeJsuWuxTJUmnQOucNuDuHGw_JeaYxh/view?usp=drive_link",
    },
    "June 04, 2024": {
        "AP": "https://drive.google.com/file/d/1uAZN-n89GgI6u95DZ8txfUpupbKWSX-m/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/16Ip-jiiLo7XqGqx55L1aZEas143x10ED/view?usp=drive_link",
    },
}

    sakshi_links = {
    "July 24, 2024": {
        "AP": "https://drive.google.com/file/d/1ObRi9eB8GRV6yHwS-USKfFRVNg3jB2eZ/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1fF9JH4PfJ4PQ88vUcMz7SRN0YAZW2AUu/view?usp=drive_link",
    },
    "July 23, 2024": {
        "AP": "https://drive.google.com/file/d/1Jc9TSzo3eISjwaSe28MPDgMLToNqBBSW/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1QUneyxyYMN9pgY4mAL41Zc3jNekCD49Y/view?usp=drive_link",
    },
    "July 22, 2024": {
        "AP": "https://drive.google.com/file/d/1Rh1AnfxaUqiciVwJwyHb-EOoQSWIwYOX/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1S042jX6OPPF2oN_mvyGcPbkhYOILRiYW/view?usp=drive_link",
    },
    "July 20, 2024": {
        "AP": "https://drive.google.com/file/d/1uvQTSZYD1-dgcTW5IWK4SDbPr-ki-W_r/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1uT7-V6vG1uHSw5ehLAk4GRqXgiAVG2mb/view?usp=drive_link",
    },
    "July 19, 2024": {
        "AP": "https://drive.google.com/file/d/19QSUlKvkw3Z0E03AdY_egUXI3HJrLOQH/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1WwDejTd0SGxvrF52CvAU4VndnjZT44aP/view?usp=drive_link",
    },
    "July 18, 2024": {
        "AP": "https://drive.google.com/file/d/1F29ZxO0hv8Teh4B-Z-WOX6dqAwhDOXNm/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1GifhPh6DQUx_trpZ6j3S4GMn8lBVzTMA/view?usp=drive_link",
    },
    "July 17, 2024": {
        "AP": "https://drive.google.com/file/d/1mcSpRZJ_G1nDE_KK2SKp9iPx0ad-GHcd/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1xiddIrjceCfbO7MF3WYXlEoZFD86brax/view?usp=drive_link",
    },
    "July 16, 2024": {
        "AP": "https://drive.google.com/file/d/1GiQ-SLX1FC7DTpET3-13Ajp1zrvauTC2/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1yDNppPs5Xhf5hLdZVcmrhK3T55z4QcxP/view?usp=drive_link",
    },
    "July 15, 2024": {
        "AP": "https://drive.google.com/file/d/1XWJpKepKiC_R4wcwQzqz1jI_9Ds2AiBE/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1S2q1UN8Stw9puOVj3tt63APicDe-w0gZ/view?usp=drive_link",
    },
    "July 14, 2024": {
        "AP": "https://drive.google.com/file/d/1_jpPqeYx-OdY9wKmf4bO6RBjAvxq5GiX/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1auLezQDKPzO8dUT5pXKvTGkc-cXfRLtI/view?usp=drive_link",
    },
    "July 13, 2024": {
        "AP": "https://drive.google.com/file/d/1LR1Boy3dN2Uyq-f1rbgEtU5BVt8GVdUt/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1X2mZ2jV8_mZLhYM3tjKZJeFrRwtbAUyH/view?usp=drive_link",
    },
    "July 12, 2024": {
        "AP": "https://drive.google.com/file/d/1d9NaaQI9hwaL8EUZKwcLC6GFYCuYzfLx/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1xqM0z6C3JWCv-FTMzfskT_GbS1AmzY9f/view?usp=drive_link",
    },
    "July 11, 2024": {
        "AP": "https://drive.google.com/file/d/1ZQ1l1WxAOPTLmcSJhNTPjTXeITyIPx01/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1sb5OlbCuhXicqP0cr9hZjCrLukRf1Bmw/view?usp=drive_link",
    },
    "July 10, 2024": {
        "AP": "https://drive.google.com/file/d/1xG902EH7Iz4Wg0pM_hTZEY4qpTE7lhtK/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1HNsFzUzilICqwPbVFl9-o_Lu4zBBR3wX/view?usp=drive_link",
    },
    "July 09, 2024": {
        "AP": "https://drive.google.com/file/d/1O9FWd7guBOj4TC59KSo8G9mocNzxws7V/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1Bn0okOcnc4IyKJeeafT1zod0xhi-7YBf/view?usp=drive_link",
    },
    "July 08, 2024": {
        "AP": "https://drive.google.com/file/d/1LsimarY2bT8I6QfFenN3NVg69kessT_X/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1RG9vLwWys84GBvdxCdW3OUh8VkE9C5ey/view?usp=drive_link",
    },
    "July 07, 2024": {
        "AP": "https://drive.google.com/file/d/1_8cUh2Fl9AYN-FfXEJfs3l9STcpF1gje/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1aec4RxM-P9iNnImOkyYmvmS_F51b7yj8/view?usp=drive_link",
    },
    "July 06, 2024": {
        "AP": "https://drive.google.com/file/d/1XgSSfSSfO0juE7RWUmwWQokaYgxRasw0/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1Tj7okUp2uxIZbaIbN4QK1A-Fm4GdBwqN/view?usp=drive_link",
    },
    "July 04, 2024": {
        "AP": "https://drive.google.com/file/d/161F9ynIFkJpCOYlZjmgwaEFB-XjCDsG9/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/12Bu68fLgrcQWiX7Nte_AWI0l7rOO7jJ1/view?usp=drive_link",
    },
    "July 03, 2024": {
        "AP": "https://drive.google.com/file/d/1aR2jRXZASSZ1FGmEHebtZqCiflgKpzQS/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1eRgIc2Sw48_M4gEDUy-sS0B1hdN1zu9g/view?usp=drive_link",
    },
    "July 02, 2024": {
        "AP": "https://drive.google.com/file/d/1e5Qz_LJETQN1rQWmnlKc7uN8XJX-4Mki/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1OFlZRM1fR4-k_1iHU9_fJox2-HD-e_mB/view?usp=drive_link",
    },
    "July 01, 2024": {
        " AP": "https://drive.google.com/file/d/1Yb4dwYZAUkkmzSqsJHw7AxwHe3dEsDqs/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1OEaSTyi7W31Yg25rhjg8a8JqfuDmxgu-/view?usp=drive_link",
    },
    "June 30, 2024": {
        "AP": "https://drive.google.com/file/d/1tp4PrBzr9OWPYjHOXFmsg-94uHJf2xjz/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1x9w6N6rTc-USdoQD9ZkzgmPQmHuuGlq6/view?usp=drive_link",
    },
    "June 29, 2024": {
        "AP": "https://drive.google.com/file/d/1iPR-mH2vrCqDkysSRtjHvgtuHEAJaD-X/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1cks6ECqPCT04hcclyKIUVkeTlPHkEyZ3/view?usp=drive_link",
    },
    "June 28, 2024": {
        "AP": "https://drive.google.com/file/d/1M-Wl3vTNwuuv1SjFR8fGYjttsNpRe89g/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1Q73BNhYnXwPgKaOsCBcIkBJe9vxgPdyC/view?usp=drive_link",
    },
    "June 27, 2024": {
        "AP": "https://drive.google.com/file/d/1JDEeCu8Ee2WE3mlUukyW8zXvXN9WhYHp/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1G8wXhKc53-goZ6A3w0iWlJ2YRfghk_vg/view?usp=drive_link",
    },
    "June 26, 2024": {
        "AP": "https://drive.google.com/file/d/1hnI8QuP7w3JWIPivdoIvJcmjYi0858RE/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1k6hud1PZroMuVzJGppSkocJfVM9SZgdi/view?usp=drive_link",
    },
    "June 25, 2024": {
        "AP": "https://drive.google.com/file/d/1CYpDfg-0y1-8XMxaXZ2MYNjE_2sD2ri_/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/11D7iYNdkzZKEFDJhxl9QNfts5ag09omt/view?usp=drive_link",
    },
    "June 24, 2024": {
        "AP": "https://drive.google.com/file/d/1_a105MOqsF4XYgHdWJ3jfjQbdKwNxydZ/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1KeroOhJhCviB9Dcc0qTzspvxzNx0iIof/view?usp=drive_link",
    },
    "June 23, 2024": {
        "AP": "https://drive.google.com/file/d/10XIp2qll06XY_-OfVDi38QNAAtgXZiCe/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1ZWN-RTAbtsJnb6AO9_EK9YN0iZ_rb8NF/view?usp=drive_link",
    },
    "June 22, 2024": {
        "AP": "https://drive.google.com/file/d/1ZkRhVYlAcwDSjhpYBpBv0QWZ_ScS1VR4/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/18RUlomsaAAO2yHo8m04Y9CjxZxC7kN_s/view?usp=drive_link",
    },
    "June 21, 2024": {
        "AP": "https://drive.google.com/file/d/1ATkWtqgflIrRuVE_88m9cndET7kxWO9P/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/14btoi1IjEYPp4Cqs0YANr7-Ev9V0Lg8b/view?usp=drive_link",
    },
    "June 20, 2024": {
        "AP": "https://drive.google.com/file/d/1ObUe-8VQ8sx9zb29XzrFfeUhgwwDA7eX/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1zcG3QMcdg8xFz2IVYOhoDBfxaHERRelz/view?usp=drive_link",
    },
    "June 19, 2024": {
        "AP": "https://drive.google.com/file/d/1BHhuPkHlx8IPLz8v75Z8nwstWRMNl-xz/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1apHY22bcZBwCSi0Zn6-GZVc3uHZEtzOH/view?usp=drive_link",
    },
    "June 18, 2024": {
        "AP": "https://drive.google.com/file/d/1KIWeE-aDT8EVq80y9HZ8-qiM3asYxP-m/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/15imQ99mLQL4mwxBWlxy4gTVaB1VeZhOr/view?usp=drive_link",
    },
    "June 17, 2024": {
        "AP": "https://drive.google.com/file/d/1sdkknGTfPgmyW93IYc_R28QXWgEQRj9g/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1XAnRslr2LuQKxtp1T7JksXYl9Y51_qPk/view?usp=drive_link",
    },
    "June 16, 2024": {
        "AP": "https://drive.google.com/file/d/1SDzL2-S9yKySRFiq43bmEO1krcv2987g/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1oEEvXfxNgACh2u5vOADgaYvAZaqJyEhX/view?usp=drive_link",
    },
    "June 15, 2024": {
        "AP": "https://drive.google.com/file/d/1qDE1a7BfcN7ST2NirVIoyIG772GI8cRG/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1weuBOjSAY9bzrjv04M0YVcbGTN_K3FXf/view?usp=drive_link",
    },
    "June 14, 2024": {
        "AP": "https://drive.google.com/file/d/1Rto60NPkf6Woi2g7T197vPSDlNoMRREY/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/10aTTKQ21uKSaf5vopZUIyjrg45k3sV_m/view?usp=drive_link",
    },
    "June 13, 2024": {
        "AP": "https://drive.google.com/file/d/1f4NTdUvpxLBrg5ZXENMMeNGQRtsfyJGc/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1kjut_325iHH53TaWeFoasBnTCBTk-uWb/view?usp=drive_link",
    },
    "June 12, 2024": {
        "AP": "https://drive.google.com/file/d/1bHiZh8qNqms8pU1oOyhnGkCvVNIl68iQ/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1w-7JfeAnRhGnkSEc_XWmG-4yV1cRPFf3/view?usp=drive_link",
    },
    "June 11, 2024": {
        "AP": "https://drive.google.com/file/d/1678Q5tmUv8VFnfzxvuXT8shMAjwSR_5m/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1dv6KX7-XxmFlDXM0V0M46kZSHkt4GSxd/view?usp=drive_link",
    },
    "June 10, 2024": {
        "AP": "https://drive.google.com/file/d/1qZw4tgFxYn6CHw83atoeS5Te_dLt--dq/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1mDomTD8StKAksq4n_Urv6_AfiixrGNON/view?usp=drive_link",
    },
    "June 09, 2024": {
        "AP": "https://drive.google.com/file/d/1ZvO1wOT-AO8Fpp5tiu5KhhjmBz1y23d8/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1K1Iv2AaUJhhLJTmmms6CXBauhhp8g3dh/view?usp=drive_link",
    },
    "June 08, 2024": {
        "AP": "https://drive.google.com/file/d/1WWoNv4apnuqLhUfN8zH4GF5dZ3nX7irr/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1_Agp2spOXXbEz1JtosVbkql14AOlATR1/view?usp=drive_link",
    },
    "June 07, 2024": {
        "AP": "https://drive.google.com/file/d/1qjDOf2vAJinyBzWUq8nw8uPGWXsN_NhJ/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1laGPXBB_XzMIhzXelEcZvbPk7RgJbbUx/view?usp=drive_link",
    },
    "June 06, 2024": {
        "AP": "https://drive.google.com/file/d/1c7fXupnFYtO98KaBgzGjZ43G5vKuHAW0/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1c7fXupnFYtO98KaBgzGjZ43G5vKuHAW0/view?usp=drive_link",
    },
    "June 05, 2024": {
        "AP": "https://drive.google.com/file/d/1CsFJKdMmoEOxcw9B_XZyJ5aFWDkxQydf/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1K5oX4lT4zGMqpzhRIDwMr3gvvTxf7SXp/view?usp=drive_link",
    },
    "June 04, 2024": {
        "AP": "https://drive.google.com/file/d/1uZGwjhzZq_lrzqvQPh8REC0fql-423vQ/view?usp=drive_link",
        "TS": "https://drive.google.com/file/d/1a-xauI2orA_bI2VLJYDAXw3X01XArK-9/view?usp=drive_link",
    },
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

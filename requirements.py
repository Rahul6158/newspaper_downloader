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
    newspaper_links = {
        "July 23, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1RPEq2cEtl-AkVh1_E5SIcRjosS9EL7X_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1FGvM4xnhfZuLzPuKrKtORbiKEgRR1pC4/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1RPEq2cEtl-AkVh1_E5SIcRjosS9EL7X_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1FGvM4xnhfZuLzPuKrKtORbiKEgRR1pC4/view?usp=drive_link"
            },
            "Andhra Jyothi": {
                "AP": "https://drive.google.com/file/d/1QKbSX-ZT0YbvFN7pY6b3jfLrV3AJuAJQ/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/12bb1gcn8pHrruV7EOjv3E6XlIgAVtu4w/view?usp=drive_link"
            }
        },
        "July 22, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/11gm91EhEakpO68Bdn_k9VcR7EU5TSbs1/view?usp=sharing",
                "TS": "https://drive.google.com/file/d/1H4QbQXaOrTC1qHpUzVphdbHR0UqUmass/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/11gm91EhEakpO68Bdn_k9VcR7EU5TSbs1/view?usp=sharing",
                "TS": "https://drive.google.com/file/d/1H4QbQXaOrTC1qHpUzVphdbHR0UqUmass/view?usp=drive_link"
            },
            "Andhra Jyothi": {
                "AP": "https://drive.google.com/file/d/1bqZuI6h2HYu2eMDnmhjqR2NuXcbt1r2x/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1QDSFyXHUNkYeZfFA-vk-6i1p1hdfuZXP/view?usp=drive_link"
            }
        },
        "July 20, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1myejG97s14gsU7uIgVMvyYV5b_-SEcUX/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1EwiyphKa74QUaSsurag_N2GLc-Kkqiz_/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1myejG97s14gsU7uIgVMvyYV5b_-SEcUX/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1EwiyphKa74QUaSsurag_N2GLc-Kkqiz_/view?usp=drive_link"
            },
            "Andhra Jyothi": {
                "AP": "https://drive.google.com/file/d/1TzuREH-p5kekPmXo1jBFVCE4ICnKrCpa/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1b6Tz63hsXYD1PpdiHgnz9uA6eOH9p8D6/view?usp=drive_link"
            }
        },
        "July 19, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1VZ62M8xjjadqFGe0u9WC-xYl_mcD87T2/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1lwLXv5vGQ6oSHu24OLEzN1NDlpNaa_RG/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1VZ62M8xjjadqFGe0u9WC-xYl_mcD87T2/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1lwLXv5vGQ6oSHu24OLEzN1NDlpNaa_RG/view?usp=drive_link"
            },
            "Andhra Jyothi": {
                "AP": "https://drive.google.com/file/d/1NchMnl9LVR9HzSh8B29BsoLfCgfrO_Hb/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1drkRmRrJfx_PPrHb8G-KoxY3iCFA3K7p/view?usp=drive_link"
            }
        },
        "July 18, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1OFRJe0r_zhL4dQJO_W-AE0wdDQz7HDgd/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/15TXDoNRLKaYa_pA3KCVIU_qJvCFGxG0T/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1OFRJe0r_zhL4dQJO_W-AE0wdDQz7HDgd/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/15TXDoNRLKaYa_pA3KCVIU_qJvCFGxG0T/view?usp=drive_link"
            },
            "Andhra Jyothi": {
                "AP": "https://drive.google.com/file/d/1vX8l7QHsHqlrw20QjTtb7-07vMbPbyi8/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1dtzYfcb_kT3NcJtMxPdoGzUbQvLgZG5O/view?usp=drive_link"
            }
        },
        "July 17, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1AT7tcf7NNUVcU1soLV08V3YUlyGL1hh0/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1gDlgvoWgDDxaxNvhoyE0TnHTkAC3wROv/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1AT7tcf7NNUVcU1soLV08V3YUlyGL1hh0/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1gDlgvoWgDDxaxNvhoyE0TnHTkAC3wROv/view?usp=drive_link"
            },
            "Andhra Jyothi": {
                "AP": "https://drive.google.com/file/d/1GHTH0uKOse_GotDP9B2pTslz6BFySw4N/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1ZcZ_FZmhCjZ74bbxi6JdWtDk5m6_3Uhz/view?usp=drive_link"
            }
        }
        # Continue with the remaining dates and links similarly
    }

    # Get the link based on selected company, state, and date
    link = newspaper_links.get(selected_date, {}).get(selected_company, {}).get(selected_state, None)

    if link:
        st.markdown(f"[Open {selected_company} Newspaper for {selected_state} on {selected_date}]({link})")
    else:
        st.write("Link not available for the selected date, company, and state.")

if __name__ == "__main__":
    main()

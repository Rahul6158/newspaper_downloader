import streamlit as st

def main():
    st.title('Newspaper Links')

    # Define newspaper companies and dates
    companies = ['Enadu', 'Sakshi']
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

    # Create dropdowns for selecting company, state and date
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
            }
        },
        "July 16, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1GGNzaejzsTUbMo_Pa1g1o38ZRKaUOwz_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/110_hCVeCS-r8Efxg5et37XNInnZ2xlKm/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1GGNzaejzsTUbMo_Pa1g1o38ZRKaUOwz_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/110_hCVeCS-r8Efxg5et37XNInnZ2xlKm/view?usp=drive_link"
            }
        },
        "July 15, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1jdveLGfXi_WrmNN7tonspEaPD6C74xJB/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1MZi-PPvznphUz-trVrwf_KN55vZMFmQA/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1jdveLGfXi_WrmNN7tonspEaPD6C74xJB/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1MZi-PPvznphUz-trVrwf_KN55vZMFmQA/view?usp=drive_link"
            }
        },
        "July 14, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1Wj4qXgTb0V-8g8ovZ--_Ea-vl87yBPMF/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1nbj5Uz3fFh7ZB1HdmHvotBQ2DQ1yboFw/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1Wj4qXgTb0V-8g8ovZ--_Ea-vl87yBPMF/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1nbj5Uz3fFh7ZB1HdmHvotBQ2DQ1yboFw/view?usp=drive_link"
            }
        },
        "July 13, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1BtzkI8y8a79MLV3pb2j3kpT5I4YQeKdK/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1A7RoGmEbrinldMnVYNUUg6xKZ6mjIEtR/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1BtzkI8y8a79MLV3pb2j3kpT5I4YQeKdK/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1A7RoGmEbrinldMnVYNUUg6xKZ6mjIEtR/view?usp=drive_link"
            }
        },
        "July 12, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1b5wn1TC7wBtH28Mr_k2A0c8mWm2f6r3e/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1bg8hK0-tgj-5rYjQIotxh6A1RXmNlM7l/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1b5wn1TC7wBtH28Mr_k2A0c8mWm2f6r3e/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1bg8hK0-tgj-5rYjQIotxh6A1RXmNlM7l/view?usp=drive_link"
            }
        },
        "July 11, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1zOu1ovWcZmZ6Xux2X3cddnv0I-FV-F43/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1lHjP1I1mKb6UWh7yHIB3xg-D2hLExfQD/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1zOu1ovWcZmZ6Xux2X3cddnv0I-FV-F43/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1lHjP1I1mKb6UWh7yHIB3xg-D2hLExfQD/view?usp=drive_link"
            }
        },
        "July 10, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1zrMgUy1jH9tA9M8Y8cZxMC4-QnUVbDVo/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1V_9c6R_WIscQZ-5YrEPrd1ogT8mYPz2b/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1zrMgUy1jH9tA9M8Y8cZxMC4-QnUVbDVo/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1V_9c6R_WIscQZ-5YrEPrd1ogT8mYPz2b/view?usp=drive_link"
            }
        },
        "July 9, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1WOSgYXu3OGY0VwOoTnPS3js1mm5NLQu_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1WOSgYXu3OGY0VwOoTnPS3js1mm5NLQu_/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1WOSgYXu3OGY0VwOoTnPS3js1mm5NLQu_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1WOSgYXu3OGY0VwOoTnPS3js1mm5NLQu_/view?usp=drive_link"
            }
        },
        "July 8, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1XtqGLnNnciJpL6Mz90F1pEZMoSAC7fWE/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1i0xg3cp7pejFJjvjMJcS55wUcr5Lxcxm/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1XtqGLnNnciJpL6Mz90F1pEZMoSAC7fWE/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1i0xg3cp7pejFJjvjMJcS55wUcr5Lxcxm/view?usp=drive_link"
            }
        },
        "July 7, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1X6AQK2U3ZatUOvXHK7nmK9G1sDhLkH5H/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1XuH6PZ0dSFO0yexGcJgkUZatBfD7K7DI/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1X6AQK2U3ZatUOvXHK7nmK9G1sDhLkH5H/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1XuH6PZ0dSFO0yexGcJgkUZatBfD7K7DI/view?usp=drive_link"
            }
        },
        "July 6, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1YN06MkJ5LrsX2cKk_3bs3y-sAdINv25B/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1Y0vToO8IM0T4DfNT2vBlKn2RJ0Znp1V3/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1YN06MkJ5LrsX2cKk_3bs3y-sAdINv25B/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1Y0vToO8IM0T4DfNT2vBlKn2RJ0Znp1V3/view?usp=drive_link"
            }
        },
        "July 5, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1Yh4Xy7lMbnzZZwP9tFTuY1rOC9a0sPO_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1YdjV2SxYIcECmNkl9nDVZ2PMUisrJIS7/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1Yh4Xy7lMbnzZZwP9tFTuY1rOC9a0sPO_/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1YdjV2SxYIcECmNkl9nDVZ2PMUisrJIS7/view?usp=drive_link"
            }
        },
        "July 4, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1a5O97aUuBZzz5hQ3cE5eNcDWghbGB8ez/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1a7klC9b1eZ8gUoF3LD2R91Vt5tLBD0Dy/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1a5O97aUuBZzz5hQ3cE5eNcDWghbGB8ez/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1a7klC9b1eZ8gUoF3LD2R91Vt5tLBD0Dy/view?usp=drive_link"
            }
        },
        "July 3, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1G6Y7QG6e1vA7FDc1x0EZz8W2u2H7TeZr/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1FGoEhGLJW4k3M4f4UC1u4MyiRFFm-XAl/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1G6Y7QG6e1vA7FDc1x0EZz8W2u2H7TeZr/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1FGoEhGLJW4k3M4f4UC1u4MyiRFFm-XAl/view?usp=drive_link"
            }
        }
    }

    # Display the selected link based on the company, state, and date selection
    if selected_date in newspaper_links and selected_company in newspaper_links[selected_date] and selected_state in newspaper_links[selected_date][selected_company]:
        selected_link = newspaper_links[selected_date][selected_company][selected_state]
        st.markdown(f"### Link for {selected_company} in {selected_state} on {selected_date}:")
        st.markdown(f"[Newspaper Link]({selected_link})")
    else:
        st.error("No link found for the selected date, company, and state.")

if __name__ == '__main__':
    main()

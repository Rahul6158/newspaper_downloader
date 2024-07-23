import streamlit as st

def main():
    st.title('Newspaper Links')

    # Define newspaper companies, states, and dates
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
                "TS": "https://drive.google.com/file/d/1nbj5Uz3fFh7ZB1HdmHvotBQ2DQ1y34oK/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1Wj4qXgTb0V-8g8ovZ--_Ea-vl87yBPMF/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1nbj5Uz3fFh7ZB1HdmHvotBQ2DQ1y34oK/view?usp=drive_link"
            }
        },
        "July 13, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1ctOT6gW4MPA9DQs9Y3-aV43TIwbBHPzO/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1k5zmO7tm-DHeX5yFbKnEuZQY66QsJMPz/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1ctOT6gW4MPA9DQs9Y3-aV43TIwbBHPzO/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1k5zmO7tm-DHeX5yFbKnEuZQY66QsJMPz/view?usp=drive_link"
            }
        },
        "July 12, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1JPqlbCEv5sl5cfHe_sR7niBQbmE5l1Vd/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1icDKiW45kTKP3MfDSDyeQSHWBvQ76-GH/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1JPqlbCEv5sl5cfHe_sR7niBQbmE5l1Vd/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1icDKiW45kTKP3MfDSDyeQSHWBvQ76-GH/view?usp=drive_link"
            }
        },
        "July 11, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1dtMLZKZ2YAr_fXphZLTNR8D-E4hVJxNw/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1LUF2_Hy2-bUXHHG1CX-MC7A4MVPkW-Lz/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1dtMLZKZ2YAr_fXphZLTNR8D-E4hVJxNw/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1LUF2_Hy2-bUXHHG1CX-MC7A4MVPkW-Lz/view?usp=drive_link"
            }
        },
        "July 10, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1r9yKX5UBg_D0rh-4so_KZRI8lj5DRVCX/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1zMmGyDSmQ9nZsBhFZqToGuij26pUK7FS/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1r9yKX5UBg_D0rh-4so_KZRI8lj5DRVCX/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1zMmGyDSmQ9nZsBhFZqToGuij26pUK7FS/view?usp=drive_link"
            }
        },
        "July 9, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/10OWKDiCPNNjOiZ_GV1PlEYI82hStdtT3/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1KShYyS4otg2PrDmlLF7nff0nH9XPu7fV/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/10OWKDiCPNNjOiZ_GV1PlEYI82hStdtT3/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1KShYyS4otg2PrDmlLF7nff0nH9XPu7fV/view?usp=drive_link"
            }
        },
        "July 8, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1h7SUQQep8gfp2UDNCC2Rsm6H-R8oixHS/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1BWOB5jO3Xs2Cr9Me9M4S7YelW0rxAE00/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1h7SUQQep8gfp2UDNCC2Rsm6H-R8oixHS/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1BWOB5jO3Xs2Cr9Me9M4S7YelW0rxAE00/view?usp=drive_link"
            }
        },
        "July 7, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1iJsvHgWn4tmO2t7XSVtlkaDDksX98tPR/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1a7EL93YweYHlLBnK6qJWazNiHZ-_2lmh/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1iJsvHgWn4tmO2t7XSVtlkaDDksX98tPR/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1a7EL93YweYHlLBnK6qJWazNiHZ-_2lmh/view?usp=drive_link"
            }
        },
        "July 6, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1VVtt4NglPHzOrE_0kHQnG3usDOmvb9y3/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1hGCFeQuw5P8eu5eF63VYZAz1xf6VOjYM/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1VVtt4NglPHzOrE_0kHQnG3usDOmvb9y3/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1hGCFeQuw5P8eu5eF63VYZAz1xf6VOjYM/view?usp=drive_link"
            }
        },
        "July 5, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1nvWwWws5e27pDaK3FQOFAxVpucf17gD7/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1ZzLBu3nkl2-ncIXjxAJ7PBxjYbUbSSKx/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1nvWwWws5e27pDaK3FQOFAxVpucf17gD7/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1ZzLBu3nkl2-ncIXjxAJ7PBxjYbUbSSKx/view?usp=drive_link"
            }
        },
        "July 4, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1bEV0pNr9uuyikXnVWeXoV_Y0f2-20ftG/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1vlS7_0jWVHp9ROsWXyAesFPmx8cM5gZT/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1bEV0pNr9uuyikXnVWeXoV_Y0f2-20ftG/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1vlS7_0jWVHp9ROsWXyAesFPmx8cM5gZT/view?usp=drive_link"
            }
        },
        "July 3, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1YtdhRaMjaH7a2bnhNJWEKPOU3tK_d78Y/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1Xq5fbKTgMHb5DPJ8sFBMMcNK_0EpL8eH/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1YtdhRaMjaH7a2bnhNJWEKPOU3tK_d78Y/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1Xq5fbKTgMHb5DPJ8sFBMMcNK_0EpL8eH/view?usp=drive_link"
            }
        },
        "July 2, 2024": {
            "Enadu": {
                "AP": "https://drive.google.com/file/d/1bFO4MTVBa3_4Gz9ffF8FOmle6NRKsxH6/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1UowduP0o0E2Zx5iPV7nG9PA9jjKrfyNS/view?usp=drive_link"
            },
            "Sakshi": {
                "AP": "https://drive.google.com/file/d/1bFO4MTVBa3_4Gz9ffF8FOmle6NRKsxH6/view?usp=drive_link",
                "TS": "https://drive.google.com/file/d/1UowduP0o0E2Zx5iPV7nG9PA9jjKrfyNS/view?usp=drive_link"
            }
        }
    }
}
s

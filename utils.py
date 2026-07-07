import streamlit as st


def add_footer():

    st.markdown(
        """
        <style>

        .footer {

            position: fixed;

            left: 0;

            bottom: 0;

            width: 100%;

            text-align: center;

            padding: 8px;

            font-size: 13px;

            color: #777;

            background-color: white;

            border-top: 1px solid #eee;

            z-index: 999;

        }

        </style>


        <div class="footer">
            Pulmonolgy Unit · UCH Ibadan
        </div>

        """,
        unsafe_allow_html=True
    )

from constants import profile, links
import streamlit as st

def sidebar():
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align:center;">
            <img src="{profile['image_path']}"
                 style="border-radius:50%; width:160px; height:160px;
                        object-fit:cover; margin-bottom:1rem;">
            <h2>{profile['name']}</h2>
            <p style="color:var(--secondary-color)">
                {profile['title']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📫 Contact", expanded=True):
            st.markdown(f"""
            {profile['location']}  
            {profile['phone']}  
            {profile['email']}
            """)

        social_links()

def social_links():
    st.markdown(
            '<link rel="stylesheet" '
            'href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">',
            unsafe_allow_html=True
        )
    link_html = "".join(
        f"""
        <a href="{link['url']}" target="_blank"
           style="margin:0 12px; font-size:2rem; text-decoration:none;">
            <i class="{link['icon']}"></i>
        </a>
        """
        for link in links
    )

    st.markdown(
        f"""
        <div style="text-align:center; margin:2rem; display: flex; flex-wrap:nowrap;">
            {link_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
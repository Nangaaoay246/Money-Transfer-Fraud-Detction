from constants import profile, links
import streamlit as st

def sidebar():
    with st.sidebar:
        # Profile
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="{profile['image_path']}" style="border-radius: 50%; width: 160px; height: 160px; object-fit: cover; margin-bottom: 1rem;">
                <h2>{profile['name']}</h2>
                <p style="color: var(--secondary-color)">{profile['title']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        #Contact
        with st.expander("📫 Contact ", expanded=True):
            st.html(f"""
                <p>{profile['location']}</p>
                <p>{profile['phone']}</p>
                <p>{profile['email']}</p>
            """)

        social_links()

def social_links():
    link_html = "".join(
        f"""
        <a href="{link['url']}" target="_blank" style="margin: 0 12px; font-size: 2rem; text-decoration: none;">
            <i class="{link['icon']}"></i>
        </a>
        """
        for link in links)

    st.markdown(
        f"""
        <div style="text-align:center; margin:2rem 2rem; ">
            {link_html}
        </div>
        """, unsafe_allow_html=True,
    )
from constants import profile, links
import streamlit as st

def sidebar():
    create_page = st.Page(
        "1_main.py",
        title="Create Entry",
        icon=":material/add_circle:"
    )

    delete_page = st.Page(
        "2_model.py",
        title="Delete Entry",
        icon=":material/delete:"
    )

    # Sidebar
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

    # Run the selected page
    # Navigation
    pg = st.navigation([create_page, delete_page])
    pg.run()


def social_links():
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
        <div style="text-align:center; margin:2rem;">
            {link_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
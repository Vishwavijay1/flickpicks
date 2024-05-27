import streamlit as st

st.set_page_config(page_title='FlickPicks Homepage', layout='wide')

def main():
    st.title('Welcome to FlickPicks!')
    st.write('Use the navigation on the left to explore different features.')

    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'Explore Similar Movies', 'User Recommendations'])

    if page == 'Explore Similar Movies':
        explore_page()
    elif page == 'User Recommendations':
        user_page()

def explore_page():
    from explore import main as explore_main
    explore_main()

def user_page():
    from user import main as user_main
    user_main()

if __name__ == "__main__":
    main()

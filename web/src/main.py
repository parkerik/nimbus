import streamlit as st
import utils


def main():
    utils.set_up()

    if not utils.check_password():
        st.stop()
    st.sidebar.caption(f'Logged in as: {st.session_state["user"]}')

    pg = st.navigation(
        [
            st.Page("views/nimbus.py", title="Nimbus"),
            st.Page("views/settings.py", title="Settings"),
        ]
    )
    pg.run()


if __name__ == "__main__":
    main()

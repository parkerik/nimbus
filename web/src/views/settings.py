import service
import streamlit as st


def main():

    st.title("Settings")

    st.header("Albums")
    albums = service.get_albums()
    st.write(albums)

    st.subheader("Create")
    album = st.text_input("Album")
    if st.button("Create Album", disabled=not bool(album)):
        service.create_album(album.lower())
        st.success("Album successfully created")

    st.subheader("Delete")
    album = st.selectbox("Album", albums)
    if st.button("Delete Album"):
        service.delete_album(album)

    if st.session_state["user"] == "admin":
        st.header("Users")
        users = service.get_users()
        st.write(users)

        st.subheader("Create")
        col1, col2 = st.columns(2)
        username = col1.text_input("Username")
        password = col2.text_input("Password", type="password")
        if st.button("Create User", disabled=not (bool(username) and bool(password))):
            if username in users:
                st.warning("Username not available")
                st.stop()
            service.create_user(username, password)
            st.success("New User successfully created")

        st.subheader("Delete")
        username = st.selectbox("Username", users)
        if st.button("Delete User"):
            service.delete_user(username)


if __name__ == "__page__":
    main()

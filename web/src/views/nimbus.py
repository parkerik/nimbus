import service
import streamlit as st


def main():

    st.title("Nimbus")
    albums = service.get_albums()

    image = st.sidebar.file_uploader("Upload", type=["jpeg", "png"])
    album_upload = st.sidebar.selectbox(
        "Album", albums, format_func=lambda x: x.title(), key="album_upload"
    )
    if st.sidebar.button("Upload"):
        service.upload_image(album_upload, st.session_state["user"], image.getvalue())

    col1, col2, col3 = st.columns(3)
    album = col1.selectbox("Album", albums, format_func=lambda x: x.title())
    sort_type = col2.selectbox("Sort", ["Newest to Oldest", "Oldest to Newest"])
    num_images = col3.selectbox("Images per Page", [25, 50, 100])

    page = 0
    images = service.get_images(album, sort_type, num_images, page * num_images)
    if not images:
        st.stop()

    grid = st.columns(5)
    col = 0
    for image in images:
        grid[col].image(image, width=220)
        col = (col + 1) % 5


if __name__ == "__page__":
    main()

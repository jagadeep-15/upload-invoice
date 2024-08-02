def main():
    # Retrieve query parameters
    query_params = st.experimental_get_query_params()

    # Determine which page to display based on query parameters
    if "page" in query_params and query_params["page"][0] == "invoice_uploader":
        if st.session_state.logged_in:
            invoice_uploader()
        else:
            st.write("You need to log in first.")
            login_form()
    else:
        if not st.session_state.logged_in:
            st.title("Welcome! Please log in or register to continue.")

            # Sidebar branding (optional)
            logo_path = r"C:\Users\SBAL036\Pictures\SBA LOGO.png"  # Use raw string for the file path
            try:
                st.sidebar.image(logo_path, use_column_width=True)
            except Exception as e:
                st.sidebar.write("Logo not found.")

            st.sidebar.markdown("### SBA")

            # Tabs for login and register
            tab_login, tab_register = st.tabs(["Login", "Register"])

            with tab_login:
                login_form()

            with tab_register:
                register_form()
        else:
            # Use URL manipulation to handle redirection
            st.experimental_set_query_params(page="invoice_uploader")

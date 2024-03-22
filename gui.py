import streamlit as st

# Streamlit app
def main():
    st.title("Placed Your Product Automate")

    # Input link
    input_link = st.text_input("Enter Product Link:")

    # Size dropdown
    selected_size = st.selectbox("Select Size:", list(range(6, 46)))

    # Price input
    price_input = st.number_input("Enter Bid Price:", min_value=0.0, value=00.0, step=1.0)

    # Output
    if st.button("Submit"):
        st.write("Your product is placed ")

if __name__ == "__main__":
    main()

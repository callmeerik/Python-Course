# import streamlit framework
import streamlit as st

def main():
    st.title("Introduction to Streamlit")   # Like a h1
    st.header("A Python framework")     # h2
    st.subheader("For web apps")        # h3

    st.text("This is a simple text")
    name = "Erik"
    st.write(f"My name is {name}")  # p in html

    st.markdown("# This is a title with markdown")

    # formated messages
    st.success("Connected")
    st.warning("⚠ Caution. Learn Python before this!!")
    st.info("Tomorrow is Wednesday")
    st.error("❌ Database not founded")

if __name__ == "__main__":
    main()
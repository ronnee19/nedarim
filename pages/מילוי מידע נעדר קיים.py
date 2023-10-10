import streamlit as st

st.markdown("""
<style>
body {
  unicode-bidi:bidi-override;
  direction: RTL;
}
[data-testid=column] [data-testid=stVerticalBlock]{
    height: 20px;
}
</style>
    """, unsafe_allow_html=True)


st.title('מילוי מידע נעדר קיים')

# c1, c2 = st.columns(2)

full_name = st.selectbox(label='בחר שם', options=st.session_state['uni_data']["שם מלא"])
# c2.button('הצג פרטים')

st.subheader('פרטים אישיים')

filled_info, not_filled_info = st.tabs(['מידע קיים', 'מידע חסר'])

idx = st.session_state['uni_data'][st.session_state['uni_data']['שם מלא'] == full_name].index[0]

def saveToState():
    for i in st.session_state['uni_data'].columns:
        if st.session_state['uni_data'].loc[idx, i] != '':
            st.session_state['uni_data'].loc[idx, i] = st.session_state[i]

with filled_info:
    for i in st.session_state['uni_data'].columns:
        if st.session_state['uni_data'].loc[idx, i] != '':
            input_value = st.session_state['uni_data'].loc[idx, i]
            user_input = st.text_input(i, input_value, key=i)

    st.button("שמירה", on_click=saveToState, key="save_filled")
    
with not_filled_info:
    for i in st.session_state['uni_data'].columns:
        if st.session_state['uni_data'].loc[idx, i] == '':
            input_value = st.session_state['uni_data'].loc[idx, i]
            user_input = st.text_input(i, input_value, key=i)

    st.button("שמירה", on_click=saveToState, key="save_unfilled")
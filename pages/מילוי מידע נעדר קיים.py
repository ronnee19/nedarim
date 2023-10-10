import streamlit as st

st.title('מילוי מידע נעדר קיים')

c1, c2 = st.columns(2)

full_name = c1.selectbox(label= 'בחר שם', options=st.session_state['uni_data']["שם מלא"])
# c2.button('הצג פרטים')

st.subheader('פרטים אישיים')
not_filled_info, filled_info = st.tabs(['מידע חסר', 'מידע קיים'])
idx = st.session_state['uni_data'][st.session_state['uni_data']['שם מלא'] == full_name].index[0]

with filled_info:   
    c1, c2, c3 = st.columns(3)
    for i in st.session_state['uni_data'].columns:
        if st.session_state['uni_data'].loc[idx, i] != '':
            c1.text(i + ': ' + str(st.session_state['uni_data'].loc[idx, i]))
    
with not_filled_info:
    st.text('hdfdg')


# st.text_input('שם פרטי')
# st.text_input('שם משפחה')

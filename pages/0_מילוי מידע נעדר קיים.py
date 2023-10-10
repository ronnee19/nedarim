import streamlit as st
import pandas as pd

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


import streamlit as st
import pandas as pd

st.title('מילוי מידע נעדר קיים')

c2, c1 = st.columns(2)

full_name = c2.selectbox(label= 'בחר שם', options=st.session_state['uni_data']["שם מלא"])
idx = st.session_state['uni_data'][st.session_state['uni_data']['שם מלא'] == full_name].index[0]

c2, z, c1 = st.columns([5,1,5])
with c2:
    for col in ['מין', 'גיל', 'סטטוס עדכני', 'מיקום אחרון', 'טלפון 1 של הנעדר/ת', 'שם באנגלית', 'מקור מידע']:
        a1, a2 = st.columns([1, 3])
        a2.text_input(label=col, value=st.session_state['uni_data'].loc[idx, col], key=col + '_input')
        if a1.button(label='עדכן', key=col):
            st.session_state['uni_data'].loc[idx, col] = st.session_state[col + '_input']
            # save the data to csv file
            st.session_state['uni_data'].to_csv('data/unified.csv', encoding='utf-8', index=False)
                    
    

with c1:
    for col in ['אינסטגראם', 'טיקטוק', 'פייסבוק']:
        a1, a2 = st.columns([1, 3])
        a2.text_input(label=col, value=st.session_state['uni_data'].loc[idx, col], key=col + '_input')
        if a1.button(label='עדכן', key=col):
            st.session_state['uni_data'].loc[idx, col] = st.session_state[col + '_input']
            # save the data to csv file
            st.session_state['uni_data'].to_csv('data/unified.csv', encoding='utf-8', index=False)
            
# add a save button to all the inputs
# if st.button(label='שמור', key='save'):
    



# st.subheader('פרטים אישיים')
# not_filled_info, filled_info = st.tabs(['מידע חסר', 'מידע קיים'])
# idx = st.session_state['uni_data'][st.session_state['uni_data']['שם מלא'] == full_name].index[0]

# with filled_info:   
#     c1, c2, c3 = st.columns(3)
#     for i in st.session_state['uni_data'].columns:
#         if st.session_state['uni_data'].loc[idx, i] != '':
#             c1.text(i + ': ' + str(st.session_state['uni_data'].loc[idx, i]))
    
# with not_filled_info:
#     st.text('hdfdg')


# st.text_input('שם פרטי')
# st.text_input('שם משפחה')


# st.title('מילוי מידע נעדר קיים')

# # c1, c2 = st.columns(2)

# full_name = st.selectbox(label='בחר שם', options=st.session_state['uni_data']["שם מלא"])
# # c2.button('הצג פרטים')

# st.subheader('פרטים אישיים')

# filled_info, not_filled_info = st.tabs(['מידע קיים', 'מידע חסר'])

# idx = st.session_state['uni_data'][st.session_state['uni_data']['שם מלא'] == full_name].index[0]

# def saveToState():
#     for i in st.session_state['uni_data'].columns:
#         if st.session_state['uni_data'].loc[idx, i] != '':
#             st.session_state['uni_data'].loc[idx, i] = st.session_state[i]

# with filled_info:
#     for i in st.session_state['uni_data'].columns:
#         if st.session_state['uni_data'].loc[idx, i] != '':
#             input_value = st.session_state['uni_data'].loc[idx, i]
#             user_input = st.text_input(i, input_value, key=i)

#     st.button("שמירה", on_click=saveToState, key="save_filled")
    
# with not_filled_info:
#     for i in st.session_state['uni_data'].columns:
#         if st.session_state['uni_data'].loc[idx, i] == '':
#             input_value = st.session_state['uni_data'].loc[idx, i]
#             user_input = st.text_input(i, input_value, key=i)

#     st.button("שמירה", on_click=saveToState, key="save_unfilled")
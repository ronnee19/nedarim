import streamlit as st
import pandas as pd
from funcs.utils import upload_dataframe_to_drive


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

a1, a2 = st.columns([1, 1])
full_name = a1.selectbox(label= 'בחר שם', options=st.session_state['uni_data']["שם מלא"])
idx = st.session_state['uni_data'][st.session_state['uni_data']['שם מלא'] == full_name].index[0]
# a2.button('שמור פרטים', key='save_btn')
st.markdown("--------")

c2, c1 = st.columns([2,3])
with c2:
    # Input widgets for editing
    new_data = {'מין': st.text_input('מין', value=st.session_state['uni_data'].loc[idx, 'מין']),
                'גיל': st.text_input('גיל', value=st.session_state['uni_data'].loc[idx, 'גיל']),
                'סטטוס עדכני': st.text_input('סטטוס עדכני', value=st.session_state['uni_data'].loc[idx, 'סטטוס עדכני']),
                'מיקום אחרון': st.text_input('מיקום אחרון', value=st.session_state['uni_data'].loc[idx, 'מיקום אחרון']),
                'טלפון 1 של הנעדר/ת': st.text_input('טלפון 1 של הנעדר/ת', value=st.session_state['uni_data'].loc[idx, 'טלפון 1 של הנעדר/ת']),
                'שם באנגלית': st.text_input('שם באנגלית', value=st.session_state['uni_data'].loc[idx, 'שם באנגלית']),
                'מקור מידע': st.text_input('מקור מידע', value=st.session_state['uni_data'].loc[idx, 'מקור מידע']),
    }
with c1:
    new_data_to_append = {'אינסטגראם': st.text_input('אינסטגראם', value=st.session_state['uni_data'].loc[idx, 'אינסטגראם']),
                          'טיקטוק': st.text_input('טיקטוק', value=st.session_state['uni_data'].loc[idx, 'טיקטוק']),
                          'פייסבוק': st.text_input('פייסבוק', value=st.session_state['uni_data'].loc[idx, 'פייסבוק']),
    }
if a2.button('שמור פרטים', key='save_btn'):
    for col in new_data:
        st.session_state['uni_data'].loc[idx, col] = new_data[col]
    for col in new_data_to_append:
        st.session_state['uni_data'].loc[idx, col] = new_data_to_append[col]
    # save the data to csv file
    with st.spinner('מעדכן טבלה...'):
        upload_dataframe_to_drive(st.session_state['uni_data'])    
    a2.success('הטבלה נשמרה בהצלחה')


# c2, z, c1 = st.columns([5,1,5])
# with c2:
#     for col in ['מין', 'גיל', 'סטטוס עדכני', 'מיקום אחרון', 'טלפון 1 של הנעדר/ת', 'שם באנגלית', 'מקור מידע']:
#         a1, a2 = st.columns([1, 3])
#         a2.text_input(label=col, value=st.session_state['uni_data'].loc[idx, col], key=col + '_input')
#         if a1.button(label='עדכן', key=col):
#             st.session_state['uni_data'].loc[idx, col] = st.session_state[col + '_input']
#             # save the data to csv file
#             st.session_state['uni_data'].to_csv('data/unified.csv', encoding='utf-8', index=False)
                    
    

# with c1:
#     for col in ['אינסטגראם', 'טיקטוק', 'פייסבוק']:
#         a1, a2 = st.columns([1, 3])
#         a2.text_input(label=col, value=st.session_state['uni_data'].loc[idx, col], key=col + '_input')
#         if a1.button(label='עדכן', key=col):
#             st.session_state['uni_data'].loc[idx, col] = st.session_state[col + '_input']
#             # save the data to csv file
#             st.session_state['uni_data'].to_csv('data/unified.csv', encoding='utf-8', index=False)
            
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
import streamlit as st
import spreadsheet as s


st.title('Winding Trails Boat Pass Applet')

"""
st.text('Select a button for function')
newAccount = st.button('New Account')
purchaseRequest = st.button('Submit Purchase Request')
if newAccount:
    newName = st.text_input('Account Name')
if newName != '':
    st.text(newName)
    actIndex = s.get_account_index(newName)
    if s.account_found(actIndex):
        st.text('Account already found. Printing information...')
    else:
        s.new_account(newName)
        st.text('Added new account.')
"""

newAccount = st.text_input('Account Name')
passType = st.slider('New Pass Type', 20, 50, step=30)
confirmAdd = st.button('SUBMIT')
if confirmAdd:
    actIndex = s.get_account_index(newAccount)
    if not s.account_found(actIndex):
        s.new_account(newAccount)
        if passType == 20:
            s.add_20_pass(len(s.names)+1)
        else:
            s.add_50_pass(len(s.names)+1)
    else:
        if passType == 20:
            s.add_20_pass(actIndex)
        else:
            s.add_50_pass(actIndex)
    s.sort_sheet_by_name()
    s.update_global_variables()
import streamlit as st
import spreadsheet as s


st.title('Winding Trails Boat Pass Applet')

st.header('Add New Pass')
newAccount = st.text_input('New Account Name')
passType = st.slider('New Pass Type', 20, 50, step=30)
confirmAdd = st.button('ADD PASS')
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

st.header('Submit Purchase Request')
accountName = st.text_input('Account Name')
price = int(st.number_input('Amount Charged'))
confirmPurchase = st.button('CONFIRM PURCHASE')
if confirmPurchase:
    actIndex = s.get_account_index(accountName)
    if s.account_found(actIndex):
        if not s.make_purchase(price, actIndex):
            st.text('Purchase failed: Not enough money in account.')
        else:
            st.text('Purchase successful.')
    else:
        st.text('Purchase failed: Account not found.')

st.header('Account Lookup')
accountForLookup = st.text_input('Account for Lookup')
lookUp = st.button('LOOK UP')
if lookUp:
    actIndex = s.get_account_index(accountForLookup)
    if s.account_found(actIndex):
        txt = 'Account Name: ' + s.sh.cell(actIndex, 1).value
        st.text(txt)
        txt = 'Amount Remaining: $' + s.sh.cell(actIndex, 7).value
        st.text(txt)
        txt = 'Date added: ' + s.sh.cell(actIndex, 8).value
        st.text(txt)
    else:
        st.text('Account not found.')
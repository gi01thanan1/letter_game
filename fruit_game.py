import streamlit as st
import random

def word(data):

    def play_no():
        col1, col2 ,col3= st.columns([1,1,1])
        with col2:
            st.button('play again', on_click=clearing, key='play_button')
        with col3:
            st.button('NO, Thanks', on_click=stopping, key='no_button')
    
    def clearing():
        for key in st.session_state.keys():
            del st.session_state[key]
    def stopping():
        st.stop()
        
    hide_streamlit_style = """

    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{ display: none; } #MainMenu{ visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }
    
    
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

   

    with open('test_css.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    if 'my_word' not in st.session_state:
        st.session_state['my_word'] = random.choice(data)
    
    
    n= len(st.session_state['my_word'])

    if 't' not in st.session_state:
        st.session_state['t'] = n+3

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    def submit():
        st.session_state.user_input = st.session_state.widget
        st.session_state.widget = ""
    st.markdown("<h1 style='color:red;text-align:center;'>Welcome to the fruit game</h1>", unsafe_allow_html=True)
    #st.image("fruits.jpeg")
    col1, col2 , col3= st.columns(3)
    
    with col2:
        st.image("fruits3.jpeg")

    
    # st.markdown(n)
    #st.subheader(f"Guess the fruit name , the word is: {n} characters",help="Enter only one character then press add  , continue entering and pressing to get the complete word")
    st.markdown(f'<p class="custom-markdown">Guess the fruit name , the word is: {n} characters</p>', unsafe_allow_html=True,help="Enter only one character then press add  , continue entering and pressing to get the complete word")
    st.text_input("Enter one character :", key="widget" , on_change=submit)
    
    if 'my_lst' not in st.session_state:
        st.session_state['my_lst'] = []
        
    for i in range(len(st.session_state['my_word'])):
        st.session_state['my_lst'].append('-')
    #st.session_state['my_lst']
    #st.text(f"the word is {''.join(st.session_state['my_lst'][:n])}")
    
    user_input = st.session_state.user_input
    add_button = st.button("Add", key='add_button')
    if add_button:
        #ts = st.session_state.t
        #st.markdown(f'<p class="center-text">{ts}</p>', unsafe_allow_html=True)
        for j in range(len(st.session_state['my_word'])):
                if st.session_state['my_word'][j]==user_input.lower():
                    st.session_state['my_lst'][j]=user_input.lower()
        #st.text(''.join(st.session_state['my_lst'][:n]))
        st.markdown(f'<p class="user-word"> {"".join(st.session_state["my_lst"][:n])} </p>', unsafe_allow_html=True)

        if (st.session_state.t== 0) and (''.join(st.session_state['my_lst'][:n]) == st.session_state['my_word']):# for last trial
            st.success("you win 👍👏", icon="✅")
            play_no()
            # col1, col2 = st.columns([1,1])
            # with col1:
            #     st.button('play again', on_click=clearing)
            # with col2:
            #     st.button('NO, Thanks', on_click=stopping)
        elif(st.session_state.t== 0) and (''.join(st.session_state['my_lst'][:n]) != st.session_state['my_word']):# only case to loose
            st.error(f"you loose 😌.. the word is:     {st.session_state['my_word']}")
            play_no()
            # col1, col2 = st.columns([1,1])
            # with col1:
            #     st.button('play again', on_click=clearing)
            # with col2:
            #     st.button('NO, Thanks', on_click=stopping)
        if st.session_state.t > 0:
            # if st.session_state.t in [1,2,3]:
            #     st.warning(f"you have {st.session_state.t} trials")
            
        
            if ''.join(st.session_state['my_lst'][:n]) == st.session_state['my_word']:
                st.success("you win 👍👏", icon="✅")
                st.session_state.t=0 # to stop compare
                play_no()
            if st.session_state.t in [1,2,3]:
                st.warning(f"you have {st.session_state.t} trials")
        st.session_state.t= st.session_state.t-1
                

                
        
    

if __name__ == '__main__':
    data=['orange' , 'banana' , 'apple', 'watermelon','mango','apricot','cherry','strawberry','dates','pears','fig','grapes']
    word(data)
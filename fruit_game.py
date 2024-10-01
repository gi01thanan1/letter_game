import streamlit as st
import random
def word(data):
    
    def clearing():
        for key in st.session_state.keys():
            del st.session_state[key]
    def stopping():
        st.stop()
    #data=['orange' , 'banana' , 'apple', 'watermelon','mango','apricot','cherry','strawberry','dates','pears','fig','grapes']
    #my_word=random.choice(data)
    if 'my_word' not in st.session_state:
        st.session_state['my_word'] = random.choice(data)
    
    if 'my_counter' not in st.session_state:
        st.session_state['my_counter'] = 0
    
    n= len(st.session_state['my_word'])
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    def submit():
        st.session_state.user_input = st.session_state.widget
        st.session_state.widget = ""
    st.markdown("<h1 style='color:red;text-align:center;'>Welcome to the fruit game</h1>", unsafe_allow_html=True)
    #st.image("fruits.jpeg")
    col1, col2 = st.columns(2)
    with col1:
        st.image("fruits.jpeg")
    with col2:
        st.image("fruits.jpeg")

    #col1, col2 , col3= st.columns([0.7,0.1,0.2])
    # col1, col2, col3 = st.columns([0.7, 0.05, 0.25])
    # with col1:
    #     st.markdown("<span style='font-size:18px;font-weight:bold;text-align:left;'>Guess the fruit name , the word is:</span>", unsafe_allow_html=True)
    # with col2:
    #     st.markdown(n)

    # with col3:
    #     st.markdown("<span style='font-size:18px;font-weight:bold;align:center'>characters</span>", unsafe_allow_html=True)


    
    # st.markdown(n)
    st.subheader(f"Guess the fruit name , the word is: {n} characters")
    st.text_input("Enter a character", key="widget" , on_change=submit)
    #st.text_input("Enter a charcter", key="user_input")
    #user_input = st.text_input("Enter a charcter", key="<uniquevalueofsomesort>") 
    if 'my_lst' not in st.session_state:
        st.session_state['my_lst'] = []
        
    for i in range(len(st.session_state['my_word'])):
        st.session_state['my_lst'].append('-')
    #st.session_state['my_lst']
    #st.text(f"the word is {''.join(st.session_state['my_lst'][:n])}")
    
    user_input = st.session_state.user_input
    add_button = st.button("Add", key='add_button')
    if add_button:
        st.session_state['my_counter'] = st.session_state['my_counter']+1
        if len(user_input) > 0:
            for j in range(len(st.session_state['my_word'])):
                if st.session_state['my_word'][j]==user_input.lower():
                    st.session_state['my_lst'][j]=user_input.lower()
            st.text(''.join(st.session_state['my_lst'][:n]))
        
            
        else:
            st.warning("Enter text")
        if st.session_state['my_counter'] <= n+3:

            if ''.join(st.session_state['my_lst'][:n]) == st.session_state['my_word']:
                st.success("you win 👍👏", icon="✅")
                col1, col2 = st.columns([1,1])

                with col1:
                    st.button('play again', on_click=clearing)
                with col2:
                    st.button('NO, Thanks', on_click=stopping)
                

                #st.text(st.session_state['my_counter'])
        else:
            st.error(f"you loose 😌.. the word is:     {st.session_state['my_word']}")
            col1, col2 = st.columns([1,1])

            with col1:
                st.button('play again', on_click=clearing)
            with col2:
                st.button('NO, Thanks', on_click=stopping)

    

if __name__ == '__main__':
    data=['orange' , 'banana' , 'apple', 'watermelon','mango','apricot','cherry','strawberry','dates','pears','fig','grapes']
    word(data)

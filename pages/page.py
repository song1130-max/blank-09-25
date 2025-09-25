import streamlit as st
import random

def main():
    st.title("간단한 곱셈 게임")
    
    if 'a' not in st.session_state or 'b' not in st.session_state:
        st.session_state['a'] = random.randint(2, 9)
        st.session_state['b'] = random.randint(2, 9)
        st.session_state['answered'] = False
        st.session_state['result'] = None
        st.session_state['problem_id'] = 0

    a = st.session_state['a']
    b = st.session_state['b']
    problem_id = st.session_state.get('problem_id', 0)
    st.write(f"{a} × {b} = ?")

    answer = st.number_input("정답을 입력하세요", min_value=0, step=1, key=f"answer_input_{problem_id}")

    if st.button("제출"):
        if answer == a * b:
            st.session_state['result'] = "정답입니다!"
        else:
            st.session_state['result'] = f"오답입니다. 정답은 {a * b}입니다."
        st.session_state['answered'] = True

    if st.session_state.get('answered', False):
        st.success(st.session_state['result'])
        if st.button("다음 문제"):
            st.session_state['a'] = random.randint(2, 9)
            st.session_state['b'] = random.randint(2, 9)
            st.session_state['answered'] = False
            st.session_state['result'] = None
            st.session_state['problem_id'] = st.session_state.get('problem_id', 0) + 1

if __name__ == "__main__":
    main()

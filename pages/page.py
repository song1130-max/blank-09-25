import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 앱 설정
st.set_page_config(page_title="함수 그래프", page_icon="📈")
st.title("📈 함수 그래프 놀이터")
st.markdown("함수를 선택하거나 직접 입력해서 그래프를 확인해요!")

# 기본 함수 목록 (절댓값 포함)
default_functions = {
    "사인": "sin(x)",
    "코사인": "cos(x)",
    "탄젠트": "tan(x)",
    "역사인": "asin(x)",
    "역코사인": "acos(x)",
    "역탄젠트": "atan(x)",
    "쌍곡사인": "sinh(x)",
    "쌍곡코사인": "cosh(x)",
    "쌍곡탄젠트": "tanh(x)",
    "절댓값": "Abs(x)",
    "1차 함수": "x",
    "2차 함수": "x**2",
    "지수 함수": "exp(x)",
    "로그 함수": "log(x)"
}

# 사이드바에서 기본 함수 선택
st.sidebar.header("기본 함수")
selected_name = st.sidebar.selectbox("함수를 골라보세요", list(default_functions.keys()))
selected_expr = default_functions[selected_name]

# 사용자 함수 입력
st.subheader("직접 함수 입력")
user_input = st.text_input("예: x**2 + 2*x - 3", value=selected_expr)

# x 범위 설정
if any(func in user_input for func in ["log", "asin", "acos"]):
    x_vals = np.linspace(0.1, 10, 400)
else:
    x_vals = np.linspace(-10, 10, 400)

x = sp.Symbol('x')
try:
    expr = sp.sympify(user_input)
    f_np = sp.lambdify(x, expr, modules=["numpy"])
    y_vals = f_np(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, color="#FF69B4", linewidth=2)
    ax.grid(True)
    ax.set_title("함수 그래프", fontsize=14)
    st.pyplot(fig)

except Exception as e:
    st.error("함수 입력이 잘못됐어요. 예: x**2 + 2*x")

# 마무리
st.markdown("---")
st.markdown("그래프 잘 나왔나요? 다른 함수도 입력해보세요!")
import streamlit as st

# 용어 설명 데이터
math_terms = {
    "벡터 공간": "벡터의 덧셈과 스칼라 곱이 정의된 집합.",
    "행렬": "숫자나 수식을 직사각형 배열로 표현한 것.",
    "고유값": "행렬의 변환에서 크기만 변하고 방향은 유지되는 값.",
    "고유벡터": "행렬에 의해 방향이 변하지 않는 벡터.",
    "역행렬": "행렬 곱셈에서 항등행렬을 만드는 행렬.",
    "행렬식": "행렬의 특성을 나타내는 수치. 선형 독립성과 관련됨.",
    "랭크": "행렬의 선형 독립한 행 또는 열의 최대 개수.",
    "선형 독립": "벡터들이 서로 중복되지 않고 독립적인 성질.",
    "기저": "벡터 공간을 생성하는 최소한의 벡터 집합.",
    "선형 변환": "벡터 공간에서 구조를 보존하는 함수.",
}

# 예제 문제 데이터
example_problems = {
    "벡터 공간": {
        "question": "다음 중 벡터 공간의 조건으로 옳지 않은 것은?",
        "options": [
            "벡터 덧셈이 닫혀 있어야 한다.",
            "스칼라 곱이 분배법칙을 만족해야 한다.",
            "벡터 곱이 정의되어 있어야 한다.",
            "0벡터가 존재해야 한다."
        ],
        "answer": 2,
        "explanation": "벡터 공간에서는 벡터 곱이 필수 조건이 아닙니다. 이는 외적 개념으로 별도입니다."
    },
    "행렬": {
        "question": "2×2 단위 행렬의 행렬식은 얼마인가요?",
        "options": ["0", "1", "2", "없다"],
        "answer": 1,
        "explanation": "단위 행렬의 행렬식은 항상 1입니다."
    },
    # 나머지 용어들도 같은 형식으로 추가 가능
}

# 앱 제목
st.title("📘 수학 용어 사전")

# 용어 선택
selected_term = st.selectbox("용어를 선택하세요:", list(math_terms.keys()))

# 용어 설명 출력
st.subheader(f"🔍 {selected_term}")
st.write(math_terms[selected_term])

# 예제 문제 출력 (해당 용어에 예제가 있을 경우)
if selected_term in example_problems:
    problem = example_problems[selected_term]
    st.subheader("🧪 예제 문제")
    st.write(problem["question"])
    user_answer = st.radio("답을 선택하세요:", problem["options"])

    if st.button("채점하기"):
        if problem["options"].index(user_answer) == problem["answer"]:
            st.success("정답입니다! 🎉")
        else:
            st.error("오답입니다 😢")
        st.info(f"해설: {problem['explanation']}")
        
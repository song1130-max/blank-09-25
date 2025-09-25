# 예시 데이터 구조 (subjects_terms.py)
subjects_terms = {
    "선형대수": [
        {
            "term": "벡터 공간",
            "definition": "벡터 공간은 벡터의 덧셈과 스칼라 곱이 정의된 집합입니다.",
            "example": {
                "question": "다음 중 벡터 공간의 조건으로 옳지 않은 것은?",
                "options": [
                    "벡터 덧셈이 닫혀 있어야 한다.",
                    "스칼라 곱이 분배법칙을 만족해야 한다.",
                    "벡터 곱이 정의되어 있어야 한다.",
                    "0벡터가 존재해야 한다."
                ],
                "answer": 2,
                "explanation": "벡터 공간에서는 벡터 곱이 필수 조건이 아닙니다. 이는 외적 개념으로 별도입니다."
            }
        },
        {
            "term": "행렬",
            "definition": "행과 열로 이루어진 수 또는 수식의 배열.",
            "example": {
                "question": "2×2 단위 행렬의 행렬식은 얼마인가요?",
                "options": ["0", "1", "2", "없다"],
                "answer": 1,
                "explanation": "단위 행렬의 행렬식은 항상 1입니다."
            }
        },
    ],
    "미적분": [
        {
            "term": "미분",
            "definition": "함수의 변화율을 나타내는 개념.",
            "example": {
                "question": "y = x^2의 도함수는?",
                "options": ["2x", "x", "x^2", "1"],
                "answer": 0,
                "explanation": "x^2을 미분하면 2x가 됩니다."
            }
        },

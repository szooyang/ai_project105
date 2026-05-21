import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

# -----------------------------
# 한글 폰트 설정
# -----------------------------
system_name = platform.system()

if system_name == "Windows":
    plt.rc("font", family="Malgun Gothic")
elif system_name == "Darwin":
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="NanumGothic")

plt.rcParams["axes.unicode_minus"] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("population.csv", encoding="utf-8")

# -----------------------------
# 데이터 전처리
# -----------------------------
# 행정구 이름 컬럼
district_col = df.columns[0]

# 전체 서울 제외
df = df[df[district_col] != "서울특별시"]

# 숫자형 변환
for col in df.columns[1:]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

# 연령 컬럼 추출
age_columns = df.columns[2:]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="서울시 행정구별 인구수", layout="centered")

st.title("서울시 행정구별 인구수")

# 행정구 선택
districts = df[district_col].tolist()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택 데이터
selected_data = df[df[district_col] == selected_district]

# 연령별 인구수
population_values = selected_data.iloc[0, 2:].values

# 나이 라벨
age_labels = [col.replace("계_", "").replace("세", "") for col in age_columns]

# -----------------------------
# 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

# 회색 배경
fig.patch.set_facecolor("#d9d9d9")
ax.set_facecolor("#d9d9d9")

# 빨간색 꺾은선 그래프
ax.plot(
    age_labels,
    population_values,
    color="red",
    linewidth=2.5,
    marker="o"
)

# 제목
ax.set_title(
    "서울시 행정구별 인구수",
    fontsize=18,
    fontweight="bold"
)

# 축 제목
ax.set_xlabel("나이", fontsize=13)
ax.set_ylabel("인구수", fontsize=13)

# x축 라벨 회전
plt.xticks(rotation=45)

# 격자
ax.grid(True, linestyle="--", alpha=0.5)

# Streamlit 출력
st.pyplot(fig)

# -----------------------------
# 데이터 표 출력
# -----------------------------
st.subheader(f"{selected_district} 연령별 인구 데이터")

chart_df = pd.DataFrame({
    "나이": age_labels,
    "인구수": population_values
})

st.dataframe(chart_df, use_container_width=True)

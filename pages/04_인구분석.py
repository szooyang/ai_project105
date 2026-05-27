import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title="행정구별 인구수",
    layout="wide"
)

st.title("행정구별 인구수")

# -------------------------------------------------
# CSV 파일 불러오기
# -------------------------------------------------
df = pd.read_csv("population.csv", encoding="cp949")

# -------------------------------------------------
# 행정구 컬럼
# -------------------------------------------------
district_col = df.columns[0]

# 서울특별시 전체 제외
df = df[df[district_col] != "서울특별시"]

# -------------------------------------------------
# 연령 컬럼 자동 찾기
# -------------------------------------------------
age_columns = []

for col in df.columns:
    if "세" in col or "~" in col:
        age_columns.append(col)

# -------------------------------------------------
# 숫자형 변환
# -------------------------------------------------
for col in age_columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

# -------------------------------------------------
# 행정구 선택
# -------------------------------------------------
districts = df[district_col].tolist()

selected_district = st.selectbox(
    "Select District",
    districts
)

# -------------------------------------------------
# 선택 데이터
# -------------------------------------------------
selected_data = df[df[district_col] == selected_district]

# 연령별 인구수
population_values = selected_data[age_columns].iloc[0].values

# -------------------------------------------------
# 나이 라벨 정리
# -------------------------------------------------
age_labels = []

for col in age_columns:
    label = (
        col.replace("계_", "")
        .replace("세", "")
        .replace(" 이상", "+")
    )
    age_labels.append(label)

# -------------------------------------------------
# 그래프 생성
# -------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 7))

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

# 축 이름
ax.set_xlabel("age", fontsize=14)
ax.set_ylabel("population", fontsize=14)

# x축 회전
plt.xticks(rotation=45)

# 격자
ax.grid(True, linestyle="--", alpha=0.5)

# Streamlit 출력
st.pyplot(fig)

# -------------------------------------------------
# 데이터 테이블
# -------------------------------------------------
chart_df = pd.DataFrame({
    "age": age_labels,
    "population": population_values
})

st.dataframe(chart_df, use_container_width=True)

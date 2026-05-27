import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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

# 서울특별시 제외
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
# Plotly 그래프
# -------------------------------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=age_labels,
        y=population_values,
        mode="lines+markers",
        line=dict(color="red", width=3),
        marker=dict(size=7),
        hovertemplate=
        "<b>Age:</b> %{x}<br>" +
        "<b>Population:</b> %{y:,}<extra></extra>"
    )
)

# 배경색 회색
fig.update_layout(
    paper_bgcolor="#d9d9d9",
    plot_bgcolor="#d9d9d9",

    xaxis_title="age",
    yaxis_title="population",

    height=650
)

# 출력
st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# 데이터 테이블
# -------------------------------------------------
chart_df = pd.DataFrame({
    "age": age_labels,
    "population": population_values
})

st.dataframe(chart_df, use_container_width=True)

# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(
    page_title="🌍 국가별 MBTI 분석",
    page_icon="🧠",
    layout="wide"
)

# 제목
st.title("🧠 국가별 MBTI 비율 분석기")
st.markdown("국가를 선택하면 MBTI 유형 비율을 인터랙티브하게 확인할 수 있어요!")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "🌏 국가를 선택하세요",
    countries
)

# 선택 국가 데이터 추출
country_data = df[df["Country"] == selected_country].iloc[0]

# MBTI 컬럼만 추출
mbti_columns = [col for col in df.columns if col != "Country"]

mbti_values = country_data[mbti_columns].sort_values(ascending=False)

# 색상 설정
colors = []

for i in range(len(mbti_values)):
    if i == 0:
        colors.append("red")
    else:
        # 파란색 그라데이션 느낌
        opacity = 1 - (i * 0.04)
        opacity = max(opacity, 0.3)
        colors.append(f"rgba(30, 144, 255, {opacity})")

# Plotly 그래프
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=mbti_values.index,
        y=mbti_values.values,
        marker_color=colors,
        text=[f"{v:.1%}" for v in mbti_values.values],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

# 레이아웃 설정
fig.update_layout(
    title=f"📊 {selected_country}의 MBTI 유형 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="plotly_white",
    height=650,
    hovermode="x unified",
    font=dict(
        size=15
    )
)

# y축 퍼센트 표시
fig.update_yaxes(
    tickformat=".0%"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 가장 높은 MBTI
top_mbti = mbti_values.idxmax()
top_value = mbti_values.max()

st.success(
    f"🏆 {selected_country}에서 가장 높은 MBTI는 "
    f"**{top_mbti}** ({top_value:.1%}) 입니다!"
)

# 데이터 테이블
with st.expander("📋 데이터 보기"):
    display_df = pd.DataFrame({
        "MBTI": mbti_values.index,
        "비율": [f"{v:.2%}" for v in mbti_values.values]
    })

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

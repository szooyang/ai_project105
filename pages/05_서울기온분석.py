import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# 페이지 설정
st.set_page_config(
    page_title="날짜별 기온 분석",
    layout="wide"
)

st.title("📈 날짜별 기온 분석")

# 현재 파일 기준 상위 폴더 경로
BASE_DIR = Path(__file__).resolve().parent.parent

# CSV 경로
csv_path = BASE_DIR / "seoul.csv"

# 데이터 불러오기
df = pd.read_csv(csv_path, encoding="cp949")

# 날짜 변환
df["날짜"] = pd.to_datetime(df["날짜"])

# 연도 / 월 / 일 컬럼 생성
df["연도"] = df["날짜"].dt.year
df["월"] = df["날짜"].dt.month
df["일"] = df["날짜"].dt.day

# 월 선택
col1, col2 = st.columns(2)

with col1:
    selected_month = st.selectbox(
        "월 선택",
        sorted(df["월"].unique())
    )

# 해당 월에 존재하는 일만 표시
available_days = sorted(
    df[df["월"] == selected_month]["일"].unique()
)

with col2:
    selected_day = st.selectbox(
        "일 선택",
        available_days
    )

# 선택 날짜 필터링
filtered_df = df[
    (df["월"] == selected_month) &
    (df["일"] == selected_day)
].copy()

# 결측치 제거
filtered_df = filtered_df.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

# 연도 정렬
filtered_df = filtered_df.sort_values("연도")

# 그래프 생성
fig = go.Figure()

# 최고기온
fig.add_trace(
    go.Scatter(
        x=filtered_df["연도"],
        y=filtered_df["최고기온(℃)"],
        mode="lines+markers",
        name="최고기온",
        line=dict(
            color="hotpink",
            width=3
        ),
        marker=dict(size=6),
        hovertemplate=
        "연도: %{x}<br>" +
        "최고기온: %{y}℃<extra></extra>"
    )
)

# 최저기온
fig.add_trace(
    go.Scatter(
        x=filtered_df["연도"],
        y=filtered_df["최저기온(℃)"],
        mode="lines+markers",
        name="최저기온",
        line=dict(
            color="#87CEFA",
            width=3
        ),
        marker=dict(size=6),
        hovertemplate=
        "연도: %{x}<br>" +
        "최저기온: %{y}℃<extra></extra>"
    )
)

# 레이아웃
fig.update_layout(
    title=f"{selected_month}월 {selected_day}일 연도별 기온 변화",
    xaxis_title="연도",
    yaxis_title="기온(℃)",
    template="plotly_white",
    hovermode="x unified",
    height=650,
    legend=dict(
        orientation="h",
        y=1.05,
        x=1
    )
)

# 그래프 출력
st.plotly_chart(
    fig,
    use_container_width=True
)

# 데이터 테이블
with st.expander("📋 데이터 보기"):
    st.dataframe(
        filtered_df[
            ["연도", "최고기온(℃)", "최저기온(℃)"]
        ],
        use_container_width=True
    )

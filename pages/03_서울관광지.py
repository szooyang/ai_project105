# app.py

import streamlit as st
import folium
from streamlit.components.v1 import html
from folium.features import CustomIcon

st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("지도에서 관광지를 클릭해보세요! 👇")

# 관광지 데이터
tour_places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역(3호선)",
        "fun": "한복 체험, 궁궐 산책, 국립민속박물관",
        "emoji": "🏯"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "subway": "명동역(4호선)",
        "fun": "길거리 음식, 쇼핑, 야간 산책",
        "emoji": "🛍️"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "subway": "명동역(4호선)",
        "fun": "야경 감상, 케이블카, 사랑의 자물쇠",
        "emoji": "🌃"
    },
    {
        "name": "홍대거리",
        "lat": 37.556355,
        "lon": 126.922852,
        "subway": "홍대입구역(2호선)",
        "fun": "버스킹, 카페 투어, 쇼핑",
        "emoji": "🎵"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "subway": "안국역(3호선)",
        "fun": "한옥 골목 산책, 전통 체험, 사진 촬영",
        "emoji": "🏡"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.513068,
        "lon": 127.102486,
        "subway": "잠실역(2호선)",
        "fun": "서울스카이 전망대, 쇼핑몰, 아쿠아리움",
        "emoji": "🏙️"
    },
    {
        "name": "동대문디자인플라자(DDP)",
        "lat": 37.566526,
        "lon": 127.009224,
        "subway": "동대문역사문화공원역",
        "fun": "야경, 전시회, 디자인 쇼핑",
        "emoji": "🎨"
    },
    {
        "name": "광장시장",
        "lat": 37.570028,
        "lon": 126.999669,
        "subway": "종로5가역(1호선)",
        "fun": "빈대떡, 육회, 먹거리 탐방",
        "emoji": "🍜"
    },
    {
        "name": "코엑스",
        "lat": 37.512524,
        "lon": 127.058819,
        "subway": "삼성역(2호선)",
        "fun": "별마당도서관, 쇼핑, 아쿠아리움",
        "emoji": "📚"
    },
    {
        "name": "한강공원",
        "lat": 37.520694,
        "lon": 126.939239,
        "subway": "여의나루역(5호선)",
        "fun": "치킨 먹방, 자전거, 야경 피크닉",
        "emoji": "🚴"
    }
]

# 세션 상태 초기화
if "selected_place" not in st.session_state:
    st.session_state.selected_place = None

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    width="100%",
    height="500px"
)

# 마커 추가
for place in tour_places:
    popup_html = f"""
    <div style="width:200px">
        <h4>{place['emoji']} {place['name']}</h4>
        <p><b>가까운 지하철:</b><br>{place['subway']}</p>
        <p><b>놀거리:</b><br>{place['fun']}</p>
    </div>
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_html,
        tooltip=place["name"],
        icon=folium.Icon(
            color="red",
            icon="star"
        )
    ).add_to(m)

# 지도 출력
map_html = m._repr_html_()
html(map_html, height=520)

st.markdown("---")
st.subheader("📍 관광지 정보 한줄 요약")

# 버튼으로 선택
cols = st.columns(5)

for idx, place in enumerate(tour_places):
    with cols[idx % 5]:
        if st.button(f"{place['emoji']} {place['name']}"):
            st.session_state.selected_place = place

# 선택 결과 출력
if st.session_state.selected_place:
    selected = st.session_state.selected_place

    st.success(
        f"""
📌 **{selected['name']}**

🚇 가까운 지하철역: {selected['subway']}  
🎉 놀거리: {selected['fun']}
"""
    )

else:
    st.info("위 버튼이나 지도 팝업을 참고해서 관광지를 선택해보세요!")ㄴ

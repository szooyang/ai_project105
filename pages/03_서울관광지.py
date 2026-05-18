import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(
    page_title="서울 관광지 TOP10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ 외국인들이 좋아하는 서울 관광지 TOP10")
st.markdown("관광지를 클릭해보세요! 👇")

# 관광지 데이터
tour_places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역(3호선)",
        "fun": "한복 체험, 궁궐 산책",
        "emoji": "🏯"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.985302,
        "subway": "명동역(4호선)",
        "fun": "길거리 음식, 쇼핑",
        "emoji": "🛍️"
    },
    {
        "name": "남산서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "subway": "명동역(4호선)",
        "fun": "야경 감상, 케이블카",
        "emoji": "🌃"
    },
    {
        "name": "홍대거리",
        "lat": 37.556355,
        "lon": 126.922852,
        "subway": "홍대입구역(2호선)",
        "fun": "버스킹, 카페 투어",
        "emoji": "🎵"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.582604,
        "lon": 126.983998,
        "subway": "안국역(3호선)",
        "fun": "한옥 골목 산책",
        "emoji": "🏡"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.513068,
        "lon": 127.102486,
        "subway": "잠실역(2호선)",
        "fun": "전망대, 쇼핑몰",
        "emoji": "🏙️"
    },
    {
        "name": "DDP",
        "lat": 37.566526,
        "lon": 127.009224,
        "subway": "동대문역사문화공원역",
        "fun": "야경, 전시회",
        "emoji": "🎨"
    },
    {
        "name": "광장시장",
        "lat": 37.570028,
        "lon": 126.999669,
        "subway": "종로5가역(1호선)",
        "fun": "빈대떡, 육회",
        "emoji": "🍜"
    },
    {
        "name": "코엑스",
        "lat": 37.512524,
        "lon": 127.058819,
        "subway": "삼성역(2호선)",
        "fun": "별마당도서관, 쇼핑",
        "emoji": "📚"
    },
    {
        "name": "한강공원",
        "lat": 37.520694,
        "lon": 126.939239,
        "subway": "여의나루역(5호선)",
        "fun": "자전거, 야경 피크닉",
        "emoji": "🚴"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 마커 추가
for place in tour_places:

    popup_text = f"""
    <b>{place['emoji']} {place['name']}</b><br>
    🚇 {place['subway']}<br>
    🎉 {place['fun']}
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_text,
        tooltip=place["name"],
        icon=folium.Icon(color="red", icon="star")
    ).add_to(m)

# 지도 출력
html(m._repr_html_(), height=500)

st.markdown("---")
st.subheader("📍 관광지 정보")

selected_place = st.selectbox(
    "관광지를 선택하세요",
    [place["name"] for place in tour_places]
)

# 선택된 관광지 정보 출력
for place in tour_places:
    if place["name"] == selected_place:
        st.success(
            f"🚇 가까운 지하철역: {place['subway']} | 🎉 놀거리: {place['fun']}"
        )

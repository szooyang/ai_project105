import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="💼",
    layout="centered"
)

# MBTI별 데이터
career_data = {
    "INTJ": [
        {
            "career": "데이터 과학자",
            "major": "인공지능학과, 컴퓨터공학과, 통계학과",
            "personality": "논리적이고 전략적으로 사고하는 사람",
            "salary": "평균 연봉 약 6,500만 원"
        },
        {
            "career": "연구원",
            "major": "자연과학계열, 공학계열",
            "personality": "깊이 탐구하고 분석하는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만 원"
        }
    ],
    "INTP": [
        {
            "career": "프로그래머",
            "major": "소프트웨어학과, 컴퓨터공학과",
            "personality": "아이디어가 많고 문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 5,800만 원"
        },
        {
            "career": "게임 개발자",
            "major": "게임공학과, 컴퓨터공학과",
            "personality": "창의적이며 새로운 기술을 탐구하는 사람",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],
    "ENTJ": [
        {
            "career": "기업 경영인",
            "major": "경영학과, 경제학과",
            "personality": "리더십이 강하고 목표 지향적인 사람",
            "salary": "평균 연봉 약 7,000만 원"
        },
        {
            "career": "프로젝트 매니저",
            "major": "경영학과, 산업공학과",
            "personality": "조직 관리와 추진력이 뛰어난 사람",
            "salary": "평균 연봉 약 6,200만 원"
        }
    ],
    "ENTP": [
        {
            "career": "창업가",
            "major": "경영학과, 창업학과",
            "personality": "도전 정신이 강하고 아이디어가 풍부한 사람",
            "salary": "평균 연봉 약 6,000만 원"
        },
        {
            "career": "마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "새로운 아이디어를 잘 내는 사람",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ],
    "INFJ": [
        {
            "career": "상담교사",
            "major": "교육학과, 심리학과",
            "personality": "공감 능력이 뛰어나고 배려심이 깊은 사람",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "career": "작가",
            "major": "국문학과, 문예창작학과",
            "personality": "상상력이 풍부하고 감수성이 높은 사람",
            "salary": "평균 연봉 약 4,000만 원"
        }
    ],
    "INFP": [
        {
            "career": "웹툰 작가",
            "major": "만화애니메이션학과, 디자인학과",
            "personality": "창의적이고 감성이 풍부한 사람",
            "salary": "평균 연봉 약 4,200만 원"
        },
        {
            "career": "심리상담사",
            "major": "심리학과, 상담학과",
            "personality": "타인의 감정을 잘 이해하는 사람",
            "salary": "평균 연봉 약 4,300만 원"
        }
    ],
    "ENFJ": [
        {
            "career": "교사",
            "major": "사범대학, 교육학과",
            "personality": "사람을 이끄는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,200만 원"
        },
        {
            "career": "HR 전문가",
            "major": "경영학과, 심리학과",
            "personality": "소통 능력이 뛰어나고 친화력이 좋은 사람",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],
    "ENFP": [
        {
            "career": "유튜브 크리에이터",
            "major": "미디어학과, 영상학과",
            "personality": "에너지가 넘치고 표현력이 좋은 사람",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "career": "광고 기획자",
            "major": "광고홍보학과",
            "personality": "창의적인 아이디어를 잘 내는 사람",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ],
    "ISTJ": [
        {
            "career": "회계사",
            "major": "회계학과, 경영학과",
            "personality": "꼼꼼하고 책임감이 강한 사람",
            "salary": "평균 연봉 약 7,000만 원"
        },
        {
            "career": "공무원",
            "major": "행정학과",
            "personality": "성실하고 체계적인 사람",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],
    "ISFJ": [
        {
            "career": "간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 책임감 있는 사람",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "사회복지사",
            "major": "사회복지학과",
            "personality": "도움을 주는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 3,800만 원"
        }
    ],
    "ESTJ": [
        {
            "career": "경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "관리자",
            "major": "경영학과",
            "personality": "조직 관리 능력이 뛰어난 사람",
            "salary": "평균 연봉 약 6,000만 원"
        }
    ],
    "ESFJ": [
        {
            "career": "승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 사람 만나는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 4,800만 원"
        },
        {
            "career": "유치원 교사",
            "major": "유아교육과",
            "personality": "따뜻하고 배려심 있는 사람",
            "salary": "평균 연봉 약 3,800만 원"
        }
    ],
    "ISTP": [
        {
            "career": "자동차 엔지니어",
            "major": "기계공학과, 자동차공학과",
            "personality": "손으로 직접 만드는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,800만 원"
        },
        {
            "career": "드론 전문가",
            "major": "항공우주공학과",
            "personality": "기계를 다루는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만 원"
        }
    ],
    "ISFP": [
        {
            "career": "디자이너",
            "major": "시각디자인학과",
            "personality": "감각적이고 창의적인 사람",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "career": "플로리스트",
            "major": "원예학과",
            "personality": "섬세하고 예술 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 3,500만 원"
        }
    ],
    "ESTP": [
        {
            "career": "영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 사람들과 소통을 잘하는 사람",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "스포츠 마케터",
            "major": "스포츠산업학과",
            "personality": "도전적이고 에너지가 넘치는 사람",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ],
    "ESFP": [
        {
            "career": "방송인",
            "major": "방송연예과",
            "personality": "사람들 앞에서 표현하는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "이벤트 기획자",
            "major": "관광경영학과",
            "personality": "밝고 활발한 성격의 사람",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ]
}

# 화면 제목
st.title("💼 MBTI 진로 추천 프로그램")
st.write("나의 MBTI에 어울리는 진로를 알아보세요!")

# MBTI 선택
mbti = st.selectbox(
    "📌 MBTI를 선택하세요",
    list(career_data.keys())
)

st.divider()

# 결과 출력
st.subheader(f"✨ {mbti} 유형 추천 진로")

for idx, item in enumerate(career_data[mbti], start=1):
    st.markdown(f"## {idx}. {item['career']}")
    st.write(f"🎓 **추천 학과:** {item['major']}")
    st.write(f"🧠 **어울리는 성격:** {item['personality']}")
    st.write(f"💰 **평균 연봉:** {item['salary']}")
    st.divider()

st.caption("※ 연봉 정보는 분야·경력·회사 규모에 따라 달라질 수 있습니다.")

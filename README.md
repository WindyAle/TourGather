# ✈️ TourGather (투개더)

**TourGather**는 사용자의 기분과 상황에 딱 맞는 여행지를 추천해주는 AI 기반 웹 서비스입니다.
"회사에서 탈출하고 싶어!", "조용한 곳에서 힐링하고 싶어"와 같이 텍스트로 상황을 입력하면, AI 가이드가 적절한 여행지를 추천해 줍니다.

## 주요 기능
- **AI 여행지 추천**: 사용자의 입력(기분, 예산, 동행 등)을 분석하여 최적의 도시/국가를 추천
- **이미지 미리보기**: 추천된 여행지의 이미지를 함께 시각적으로 제공

## 기술 스택 (Tech Stack)
- **Backend**: Python, Django
- **AI & Data**: OpenAI API (GPT-4o-mini), Tavily API (Image Search)
- **Frontend**: HTML5, CSS3 (MVP.css 활용), Django Template

## 사용 방법
1. 메인 화면에서 '여행지 추천 받기' 버튼을 클릭합니다.
2. 입력 폼에 현재 기분이나 원하는 여행 스타일을 자유롭게 적습니다.
   - 예: "너무 지쳤어. 아무 생각 없이 쉴 수 있는 따뜻한 바닷가 없을까?"
3. '추천 받기' 버튼을 누르면 AI가 분석한 여행지와 사진이 결과 페이지에 표시됩니다.

## 프로젝트 구조
```
TourGather/
├── practice/           # 프로젝트 설정 디렉토리
├── traveler/           # 여행 추천 앱 (App)
│   ├── templates/      # HTML 템플릿
│   ├── static/         # CSS, 이미지 등 정적 파일
│   └── views.py        # 로직 처리 (OpenAI, Tavily 연동)
├── templates/          # 공통 템플릿 (base.html)
└── manage.py
```

---
Running on **Django** & Powered by **OpenAI**

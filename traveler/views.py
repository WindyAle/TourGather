from django.shortcuts import render, redirect
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.
SYSTEM_PROMPT = """
당신은 세계 최고의 여행 가이드입니다.
사용자의 기분에 맞는 여행지를 추천하는 것이 당신의 업무입니다.
최대한 친절하고 전문적인 톤으로 답변하세요.

[대화 지침]
1. 여행지를 추천한 이유를 함께 제시하세요.
2. 여행지에 대한 주요 정보를 제시하세요.
"""

PROMPT_TEMPLATE = """
사용자 상황/기분: "{user_mood}"
    
위 상황에 가장 적절한 여행지(도시, 국가)를 하나 추천해주세요.
답변은 반드시 다음 형식을 지켜주세요:

추천 여행지: [국가] [도시]
추천 활동: [구체적인 활동 1가지]
추천 이유: [감성적이고 설득력 있는 이유 3문장 이내]
"""

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def index(request):
    return render(request, 'traveler/index.html')

def form(request):
    return render(request, 'traveler/form.html')

def result(request):
    # 기능 강제: 주소창에 직접 result 치고 들어오는 경우 방지
    if request.method != 'POST':
        return redirect('traveler:index')

    user_mood = request.POST.get('user_mood')

    if not user_mood.strip():
        return render(request, 'traveler/form.html', {'error': "내용을 입력해주세요!"})

    system_instruction = SYSTEM_PROMPT
    user_prompt = PROMPT_TEMPLATE.format(user_mood=user_mood)

    context = {}

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
        )
        
        context = {
            'user_mood': user_mood,
            'result': response.choices[0].message.content
        }

    except Exception as e:
        print(f"Error: {e}")
        context = {
            'user_mood': user_mood,
            'result': "죄송합니다. 여행 가이드가 잠시 길을 잃었네요. 이런 것도 여행의 묘미죠!."
        }

    return render(request, 'traveler/result.html', context)
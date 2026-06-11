import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_code(diff: str, language: str = "unknown", context: str = "") -> str:
    prompt = f"""
당신은 시니어 백엔드 엔지니어입니다. 아래 코드 변경사항을 엄격하게 리뷰해주세요.

언어: {language}
컨텍스트: {context}

리뷰 항목:
1. 버그 & 논리 오류
2. 보안 취약점
3. 성능 이슈
4. 코드 품질 (네이밍, 중복, 단일책임)
5. 에러 핸들링

각 문제는 [🔴 심각] [🟠 경고] [🟡 개선] [🟢 제안] 으로 분류해주세요.

코드:
{diff}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    import sys
    diff = sys.stdin.read()
    print(review_code(diff))
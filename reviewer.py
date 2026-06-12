import os
import sys
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

diff = sys.stdin.read()

if not diff.strip():
    print("변경된 코드가 없습니다.")
    sys.exit(0)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"""다음 PR 코드 변경사항을 리뷰해줘.

리뷰 항목:
1. 버그 가능성
2. 코드 품질 및 가독성
3. 보안 문제
4. 개선 제안

코드 변경사항:
{diff}"""
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

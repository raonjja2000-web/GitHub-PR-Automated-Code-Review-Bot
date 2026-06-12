import anthropic
import sys

client = anthropic.Anthropic()

diff = sys.stdin.read()

if not diff.strip():
    print("변경된 코드가 없습니다.")
    sys.exit(0)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
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
    ]
)

print(message.content[0].text)

# GitHub PR Automated Code Review Bot

GitHub Actions와 LLM API를 활용해 코드 변경 사항을 자동으로 분석하고, AI 기반 코드 리뷰 결과를 출력하는 프로젝트입니다.

## 프로젝트 개요

이 프로젝트는 GitHub 저장소에서 `main` 브랜치를 제외한 브랜치에 push가 발생했을 때 GitHub Actions가 실행되도록 구성되어 있습니다.

GitHub Actions는 최근 커밋 간의 코드 변경 사항을 `git diff`로 가져오고, 해당 내용을 Python 스크립트인 `reviewer.py`에 전달합니다.  
`reviewer.py`는 전달받은 변경 코드를 Groq API로 전송하여 AI 코드 리뷰 결과를 생성하고, 그 결과를 GitHub Actions 실행 로그에 출력합니다.

## 주요 기능

- `main` 브랜치를 제외한 브랜치 push 이벤트 감지
- 최근 커밋 간 코드 변경 사항 추출
- 변경된 코드 내용을 LLM API로 전달
- AI 기반 코드 리뷰 결과 생성
- GitHub Actions 실행 로그에 리뷰 결과 출력

## 동작 방식

1. `main` 브랜치가 아닌 브랜치에 코드가 push됩니다.
2. GitHub Actions workflow가 실행됩니다.
3. 저장소 코드를 checkout합니다.
4. Python 3.11 환경을 설정합니다.
5. `requirements.txt`에 작성된 의존성을 설치합니다.
6. `git diff HEAD~1 HEAD` 명령어로 최근 변경 사항을 가져옵니다.
7. 변경 내용을 `reviewer.py`에 전달합니다.
8. Groq API를 통해 AI 코드 리뷰를 생성합니다.
9. 생성된 리뷰 결과를 GitHub Actions 로그에 출력합니다.

## 기술 스택

- Python
- GitHub Actions
- Groq API
- LLM
- Prompt Engineering

## 사용 모델

```txt
llama-3.3-70b-versatile

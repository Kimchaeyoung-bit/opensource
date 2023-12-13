
import openai

# OpenAI API 키 설정
openai.api_key = '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'

# GPT-3 엔진 사용
engine = "text-davinci-003"

# 생성할 텍스트의 프롬프트
prompt = "Translate the following English text to French:"

# OpenAI API 호출
response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    max_tokens=100  # 생성할 최대 토큰 수
)

# 생성된 텍스트 출력
generated_text = response.choices[0].text.strip()
print("Generated Text:", generated_text)




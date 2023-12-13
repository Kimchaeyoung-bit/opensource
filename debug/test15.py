import os
import openai

openai.api_key ="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"
question = input("무엇을 물어볼까요?: ")

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
        ]
    )

print(completion.choices[0].message.content)

import openai

# OpenAI API 키 설정
openai.api_key = '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'  # 여기에 본인의 API 키를 넣어주세요

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # ChatGPT engine 선택
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    # ChatGPT에 대화 시작
    conversation_history = ""

    while True:
        user_input = input("You: ")
        conversation_history += f"You: {user_input}\n"

        # 사용자 입력과 대화 기록을 사용하여 ChatGPT에 쿼리
        response = chat_with_gpt(conversation_history)

        # ChatGPT의 응답 출력
        print(f"ChatGPT: {response}\n")

        # 대화 기록 업데이트
        conversation_history += f"ChatGPT: {response}\n"


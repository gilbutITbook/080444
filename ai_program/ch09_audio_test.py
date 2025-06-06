from openai import OpenAI

# (1) OpenAI 클라이언트 생성
OPENAI_API_KEY = "API_Key_입력" 
client = OpenAI(api_key=OPENAI_API_KEY)

# (2) 음성 파일 경로 설정
speech_file_path = "AI음성.mp3"

def text_to_speech(text):
    # (3) API 요청 및 응답
    response = client.audio.speech.create(
	    model="tts-1", 	# TTS 모델 설정
	    voice="alloy", 		# 음성 종류 선택
	    input=text, 		# 변환할 텍스트 입력
    )
    # (4) 음성 파일 저장
    with open(speech_file_path, "wb") as audio_file:
	    audio_file.write(response.content)

# (6) 텍스트-음성 변환 함수 호출
text_to_speech("파이썬의 세계에 오신 것을 환영해요!")
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import wave

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def make_tts(text):
    """
    문자열을 음성(wav) 파일로 저장한다.
    """

    response = client.models.generate_content(
        model="models/gemini-3.1-flash-tts-preview",
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Kore"
            )
        )
    )
)
    )

    audio = (
        response.candidates[0]
        .content.parts[0]
        .inline_data.data
    )

    with wave.open("news.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(audio)


make_tts("안녕하세요. 오늘 AI 뉴스 브리핑입니다.")

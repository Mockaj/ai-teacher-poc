from openai_client import client


def tts(text, filename='output_audio.mp3'):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    # Save the audio data to a file
    with open(filename, 'wb') as audio_file:
        audio_file.write(response.content)
    return filename

import time
from openai_client import client


def stream(model, prompt, box, history):
    msg = {'role': 'user', 'content': prompt}
    history.append(msg)
    response = client.chat.completions.create(
        model=model,
        messages=history,
        temperature=0.7,
        stream=True
    )
    if response:
        s = ''
        for chunk in response:
            if chunk.choices[0].finish_reason == "stop":
                history.append(
                    {'role': 'assistant', 'content': s})
                return s
            for c in chunk.choices[0].delta.content:
                s += c
                time.sleep(.002)
                box.write(s)

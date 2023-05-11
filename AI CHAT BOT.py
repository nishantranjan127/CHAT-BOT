import openai
import gradio

openai.api_key="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"

messages=[{"role":"system","content":"what can we make with open ai api "}]

def CustomChatGPT(user_input):
    messages.append({"role":"user","content":user_input})
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",messages=messages
        )
    ChatGPT_reply=response["choices"][0]["message"]["content"]
    messages.append({"role":"assistant","content":"ChatGPT_reply"})
    return ChatGPT_reply

demo=gradio.Interface(fn=CustomChatGPT,inputs="text",outputs="text",title="AI CHAT BOT")

demo.launch(share=True)
import requests
#1.配置我的APi KEY
api_key = "sk-5143380f900940089a189b5fa19b0a1a"
#2.配置请求的URL和请求头
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
#3.构造发送给AI的数据
data = {
    "model": "deepseek-chat",
    "messages":[
        {"role": "system","content":"你是个专业的AI导师"},
        {"role":"user","content":"请你用一句话来鼓励一下正在学习python的我"}
    ]
}
#4.发送网络请求
print("正在呼叫大模型，请稍后...")
responce = requests.post(url,headers=headers,json=data)

#5.解析并打印Ai返回的结果
result = responce.json()
ai_reply = result["choices"][0]["message"]["content"]
print("/n  AI回复:")
print(ai_reply)
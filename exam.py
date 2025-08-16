from google import genai
import os
import sys

# 解决 Windows 控制台输出中文或非 ASCII 的问题
sys.stdout.reconfigure(encoding='utf-8')

# Proxy settings if needed
os.environ["HTTP_PROXY"] = "http://127.0.0.1:40008"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:40008"

client = genai.Client(api_key="AIzaSyD-ihDC5GPsXWsdq9h4Nbl_o7ZEKyp7img")

try:
    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents="Hello, can you hear me?"
    )
    print("✅ Call succeeded. Gemini's response:")
    print(response.text)

except Exception as e:
    print("❌ Call failed:", e)

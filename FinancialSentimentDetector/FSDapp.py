import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import pandas as pd
import altair as alt

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 模型路径（替换成你自己保存模型的路径）
model_path = "FinSent_Detector"

# 加载 tokenizer 和模型
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(
    model_path,
    device_map={"": device}
)
model.eval()

# 标签映射（要和训练时顺序一致）
label_map = {
    0: "negative",
    1: "neutral",
    2: "positive"
}

def predict_sentiment(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128, padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=-1)
    return probs.squeeze().cpu().numpy()

# 页面设置
st.set_page_config(page_title="Financial Sentiment Detector", layout="wide")

if "text_input" not in st.session_state:
    st.session_state.text_input = ""

def on_click_set_text(text):
    st.session_state.text_input = text

# 标题样式
st.markdown(
    """
    <style>
    .title {font-size: 48px; font-weight: bold; color: #0a4c93;}
    .subtitle {font-size: 20px; color: #333333;}
    </style>
    """, unsafe_allow_html=True
)
st.markdown('<div class="title">Financial Sentiment Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect sentiments in tweets and financial texts.</div>', unsafe_allow_html=True)

# 两列布局
col1, col2 = st.columns([3, 2])

with col1:
    text_input = st.text_area("Enter a financial or social media sentence:", height=140, key="text_input")

if st.button("Analyze"):
    if text_input.strip():
        probs = predict_sentiment(text_input, tokenizer, model)
        pred_label = label_map[np.argmax(probs)]
        conf = max(probs) * 100

        st.markdown(f"### Model Prediction: **{pred_label.capitalize()}**")
        st.markdown(f"**Confidence:** {conf:.2f}%")

        data = [{"Sentiment": label_map[i].capitalize(), "Probability": float(probs[i])} for i in range(len(probs))]
        df = pd.DataFrame(data)

        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('Sentiment:N', sort=None),
            y=alt.Y('Probability:Q'),
            color=alt.Color('Sentiment:N', scale=alt.Scale(scheme='set1'))
        ).properties(width=400, height=300)
        st.altair_chart(chart)
    else:
        st.warning("Please enter some text to analyze.")

with col2:
    st.markdown("### Try Example Sentences")
    examples = [
        # Positive exaggeration
        "🚀 This stock is going to the moon! I'm ALL IN!!",
        "Absolutely phenomenal earnings! Best company ever!",

        # Neutral / hard-to-judge
        "Market remains uncertain after the Fed's announcement.",
        "Tesla shares closed slightly higher today.",

        # Negative exaggeration
        "This is a disaster. The CEO is totally incompetent!",
        "Sell everything now. We're heading for a crash."
    ]
    for ex in examples:
        st.button(ex[:40] + "...", on_click=on_click_set_text, args=(ex,))

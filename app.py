import streamlit as st
from openai import OpenAI

# Create client using your secret key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("😈PitchWhiz - Your Silly Startup Pitch Generator")
st.caption("Powered by ChatGPT and too much coffee")

idea = st.text_input("What's your startup idea?", "AI-powered bubble tea robot")

if st.button("Generate Pitch"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"""Write a short, non-sense, comedic startup pitch (around 100-150 words) for this idea: "{idea}" 
                                            as a tech CEO selling their idea to investors.
                                            Include at least 3 startup buzzwords (like synergy, AI, blockchain, disruption, etc.) and at least 1 bad joke.
                                            Keep it clear, structured, and readable. Please respond in the same language the user used for the idea above."""}

        ],
        temperature=0.9,
        max_tokens=200
    )

    pitch = response.choices[0].message.content.strip()
    st.markdown("### 🧠 Here's your pitch:")
    st.write(pitch)

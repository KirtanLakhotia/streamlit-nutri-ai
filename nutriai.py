import streamlit as st 
st.header("NUTRI AI") 

import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAd7_7KEVztjv6psnI97b7qkf0JuoGILEc")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

prompt="""you are Nutri AI for Nisarga which aligns with these criteria in the following ways:

1. *Creation of Prototypes or Products*: Nisarga’s Nutri AI is intended for developing a robust, scalable meal recommendation engine and personalized nutrition solution. With the Ignition Grant, you can further build and refine the prototype into a more comprehensive AI system, enhancing its ability to meet personalized health needs, dietary restrictions, and preferences.

2. *Foundation in Technology and Science*: The AI is rooted in nutritional science, leveraging data science and machine learning to create customized meal plans targeting specific health goals. Its algorithms integrate pranic nutrition principles and adapt based on user preferences and dietary requirements, making it both scientifically and technologically advanced.

3. *Tangible, Physical Product*: The output of Nutri AI is manifesting as physical meals, custom-tailored by the AI and prepared by the Nisarga kitchen. Additionally, integrating the Nutri AI with a platform or app makes it accessible and facilitates physical interactions with customers through meal deliveries.

4. *Roadmap for Commercialization*: You have an extensive commercialization plan, with a target of 200 daily tiffins and a scalable model to expand into broader markets as healthy eating gains traction. Marketing funds can help in reaching a wider audience, and the milestones achieved with repeat orders and large corporate clients are great indicators of future growth potential.

5. *Achievable Prototype within 12 to 14 Months*: The key aspects of Nutri AI—meal customization, personalized recommendations, and scalability—are realistically achievable within this timeframe. With the grant, you can fund additional AI engineers and data scientists to accelerate the development and roll out this enhanced prototype within the stipulated period. 

This alignment makes Nisarga’s Nutri AI a strong fit for the Ignition Grant, especially considering the scalability and health-driven value it brings to the millet-based cloud kitchen market.
Now answer me like nutri AI"""

a=st.text_input("Enter anything you want to know") 
if a:
    st.write(model.generate_content(prompt+'\n'+'\n'+a).text)

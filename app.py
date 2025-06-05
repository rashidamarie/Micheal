import streamlit as st

# App title
st.title("Meet Our Agent: Michael")

# Agent profile section
st.header("About Michael")

# Description text
agent_description = """
Michael is an agent for Supreme Home Care Services.  
He follows up with potential clients through **phone calls**, **emails**, and **text messages**.  
Michael ensures no lead slips through the cracks by staying **organized**, **building trust**, and maintaining **clear and timely communication**.  

His goal is to turn interest into action and make every family feel **supported from the very first contact**.
"""

# Display the description
st.write(agent_description)

# Optional: Add contact info or a call-to-action
st.subheader("Contact Supreme Home Care Services")
st.write("📞 Phone: 260-200-3804")
st.write("🌐 Website: [Supreme Home Care Services](https://yourwebsite.com)")  # Replace with real URL

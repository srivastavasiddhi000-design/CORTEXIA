import streamlit as st
import sys
import os


# NEXORA PROJECT PATH
sys.path.append(
    os.path.join(
        os.getcwd(),
        "NEXORA-Multi-AI-Agent"
    )
)

from nexora_agents import (
    research_agent,
    knowledge_agent,
    planner_agent,
    code_agent
)


class NexoraAgent:

    def run(self, query):

        # simple routing
        q = query.lower()

        if "research" in q:
            return research_agent(query)

        elif "plan" in q:
            return planner_agent(query)

        elif "code" in q:
            return code_agent(query)

        else:
            return knowledge_agent(query)



# initialize agent once
if "nexora_agent" not in st.session_state:

    st.session_state.nexora_agent = NexoraAgent()



def show_nexora():


    st.markdown(
    """
    <style>

    .nexora-title{
        color:rgba(255,255,255,.85);
        letter-spacing:4px;
        font-size:38px;
        font-weight:800;
        text-shadow:none;
    }

    .nexora-sub{
        color:#B8C5D3;
    }

    </style>
    """,
    unsafe_allow_html=True
    )


    col1,col2 = st.columns([1,5])


    with col1:
        st.markdown("🤖")


    with col2:

        st.markdown(
        """
        <div class="nexora-title">
        NEXORA AI ClinIQ
        </div>

        <div class="nexora-sub">
        Intelligent Health Assistant
        </div>
        """,
        unsafe_allow_html=True
        )


    question = st.text_input(
        "",
        placeholder="Ask your health question...",
        key="nexora_input"
    )


    if st.button(
        "ASK NEXORA",
        key="nexora_btn"
    ):

        if question:

            with st.spinner(
                "NEXORA AI THINKING..."
            ):

                response = (
                    st.session_state
                    .nexora_agent
                    .run(question)
                )


            st.success(response)


        else:

            st.warning(
                "Enter your question"
            )
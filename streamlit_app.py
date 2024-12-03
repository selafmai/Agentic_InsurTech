import streamlit as st
from src.agent import InsuranceAgent
from src.utils.stripe_handler import create_checkout_session
from src.utils.document_generator import generate_policy_document

def create_streamlit_app(agent: InsuranceAgent):
    st.title("InsurTech Agent")
    st.write("Dobrodošli v pametnem zavarovalnem agentu")
    
    with st.form("insurance_form"):
        uploaded_image = st.file_uploader("Naložite sliko predmetov za zavarovanje", type=["jpg", "png"])
        location = st.text_input("Vnesite lokacijo")
        coverage_type = st.selectbox(
            "Izberite vrsto zavarovanja",
            ["Stanovanjsko", "Avtomobilsko", "Potovalno"]
        )
        
        submit_button = st.form_submit_button("Analiziraj")
        
        if submit_button and uploaded_image is not None:
            with st.spinner("Analiziram..."):
                result = agent.process_insurance_request(uploaded_image, location, coverage_type)
                
                st.json(result)
                
                if st.button("Skleni zavarovanje"):
                    checkout_session = create_checkout_session(result["premium"])
                    st.markdown(f"[Nadaljuj na plačilo]({checkout_session.url})") 
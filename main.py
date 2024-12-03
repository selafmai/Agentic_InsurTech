import os
from dotenv import load_dotenv
from src.agent import InsuranceAgent
from src.gradio_app import create_gradio_interface
from src.streamlit_app import create_streamlit_app

load_dotenv()

def main():
    # Inicializacija agenta
    agent = InsuranceAgent()
    
    # Izbira vmesnika (Gradio ali Streamlit)
    interface_type = os.getenv("INTERFACE_TYPE", "gradio")
    
    if interface_type == "gradio":
        app = create_gradio_interface(agent)
        app.launch()
    else:
        create_streamlit_app(agent)

if __name__ == "__main__":
    main() 
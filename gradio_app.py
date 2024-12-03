import gradio as gr
from src.agent import InsuranceAgent

def create_gradio_interface(agent: InsuranceAgent):
    def process_request(image, location, coverage_type):
        result = agent.process_insurance_request(image, location, coverage_type)
        return result
    
    interface = gr.Interface(
        fn=process_request,
        inputs=[
            gr.Image(label="Naložite sliko predmetov za zavarovanje"),
            gr.Textbox(label="Lokacija"),
            gr.Dropdown(choices=["Stanovanjsko", "Avtomobilsko", "Potovalno"], label="Vrsta zavarovanja")
        ],
        outputs=[
            gr.JSON(label="Rezultati analize")
        ],
        title="InsurTech Agent",
        description="Pametni zavarovalni agent za oceno tveganja in izdajo police"
    )
    
    return interface 
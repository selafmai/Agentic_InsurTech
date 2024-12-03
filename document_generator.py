import os
from datetime import datetime
from typing import Dict, Any
from fpdf import FPDF
import qrcode

class PolicyDocument:
    def __init__(self):
        self.pdf = FPDF()
        
    def generate_policy_document(self, policy_data: Dict[str, Any]) -> str:
        """Generira PDF dokument zavarovalne police."""
        self.pdf.add_page()
        self._add_header()
        self._add_policy_details(policy_data)
        self._add_coverage_details(policy_data)
        self._add_qr_code(policy_data)
        
        filename = f"policy_{policy_data['policy_number']}.pdf"
        self.pdf.output(filename)
        return filename
    
    def _add_header(self):
        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.cell(0, 10, 'Zavarovalna polica', 0, 1, 'C')
        self.pdf.ln(10)
        
    def _add_policy_details(self, data: Dict[str, Any]):
        self.pdf.set_font('Arial', '', 12)
        self.pdf.cell(0, 10, f"Številka police: {data['policy_number']}", 0, 1)
        self.pdf.cell(0, 10, f"Datum izdaje: {datetime.now().strftime('%d.%m.%Y')}", 0, 1)
        self.pdf.cell(0, 10, f"Zavarovanec: {data['insured_name']}", 0, 1)
        
    def _add_coverage_details(self, data: Dict[str, Any]):
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.cell(0, 10, 'Obseg kritja', 0, 1)
        self.pdf.set_font('Arial', '', 12)
        
        for coverage in data['coverages']:
            self.pdf.cell(0, 10, f"- {coverage['type']}: {coverage['amount']}€", 0, 1)
            
    def _add_qr_code(self, data: Dict[str, Any]):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data['policy_number'])
        qr.make(fit=True)
        
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("policy_qr.png")
        
        self.pdf.image("policy_qr.png", x=10, y=self.pdf.get_y() + 10, w=30)
        os.remove("policy_qr.png") 
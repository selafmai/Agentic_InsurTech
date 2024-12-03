# InsurTech Agent

Inteligentni zavarovalni agent z uporabo računalniškega vida in strojnega učenja.

## Funkcionalnosti

- Analiza slik za identifikacijo predmetov
- Ocena tveganja na podlagi zaznanih predmetov
- Vremenska analiza lokacije
- Avtomatski izračun zavarovalne premije
- Integracija s Stripe za plačila
- Generiranje zavarovalnih dokumentov

  #
insurtech_agent/
├── .env
├── requirements.txt
├── README.md
├── app.py
├── Dockerfile
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   ├── gradio_app.py
│   ├── streamlit_app.py
│   ├── tools.py
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       ├── image_processor.py
│       ├── weather_api.py
│       ├── stripe_handler.py
│       └── document_generator.py
├── config/
│   └── config.yaml
└── tests/
    └── __init__.py
  

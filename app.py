import gradio as gr
from transformers import pipeline


context = "The Greater Mexico City has a gross domestic product (GDP) of US$411 billion in 2011, making Mexico City urban agglomeration one of the economically largest metropolitan areas in the world. The city was responsible for generating 15.8% of Mexico's Gross Domestic Product and the metropolitan area accounted for about 22% of total national GDP. As a stand-alone country, in 2013, Mexico City would be the fifth-largest economy in Latin America—five times as large as Costa Rica's and about the same size as Peru's."
question = "What percent of the Mexican GDP is the metropolitan area of Mexico City responsible for?"

question_answer = pipeline("question-answering", model = "Kaludi/eurekaQA-model")


interface = gr.Interface.from_pipeline(question_answer,
    title = "eurekaQA - Question & Answering Model",
    description = "eurekaQA is a Question & Answering Model that has been trained by <strong><a href='https://huggingface.co/Kaludi'>Kaludi</a></strong> that uses advanced machine learning algorithms to analyze text data and automatically answer questions based on the information contained within. EurekaQA is an extractive model, meaning it selects the relevant information from a given text document to present as the answer to the question. This model can be used in a variety of applications, including customer service, virtual assistants, and information retrieval systems.",
    article = "<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>",
    theme = "peach",
    examples = [[context, question]]).launch()



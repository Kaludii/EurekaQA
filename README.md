
## EurekaQA - Question & Answering Model

EurekaQA is a Question & Answering Model that has been trained by [Kaludi](https://huggingface.co/Kaludi) to analyze text data and automatically answer questions based on the information contained within. The model uses advanced machine learning algorithms to perform extractive question-answering, meaning it selects the relevant information from a given text document to present as the answer to the question.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/EurekaQA) To View This App Online!

![Image](https://github.com/Kaludii/EurekaQA/blob/main/images/QA.png?raw=true)

The model is trained on the [EurekaQA dataset](https://huggingface.co/datasets/Kaludi/data-eurekaQA) and the model can be found on [Hugging Face](https://huggingface.co/Kaludi/eurekaQA-model).

EurekaQA can be used in a variety of applications, including customer service, virtual assistants, and information retrieval systems.

## How to use EurekaQA

You can use EurekaQA by importing the `pipeline` method from the `transformers` library and setting the task to "question-answering" and the model to "Kaludi/eurekaQA-model". You can then pass in a context and a question as a list to the `pipeline` method to receive the answer.

`from transformers import pipeline

context = "The Greater Mexico City has a gross domestic product (GDP) of US$411 billion in 2011, making Mexico City urban agglomeration one of the economically largest metropolitan areas in the world. The city was responsible for generating 15.8% of Mexico's Gross Domestic Product and the metropolitan area accounted for about 22% of total national GDP. As a stand-alone country, in 2013, Mexico City would be the fifth-largest economy in Latin America—five times as large as Costa Rica's and about the same size as Peru's."
question = "What percent of the Mexican GDP is the metropolitan area of Mexico City responsible for?"

question_answer = pipeline("question-answering", model = "Kaludi/eurekaQA-model")

answer = question_answer([context, question], top_k=1)
print(answer)`

## Download and Use EurekaQA on App

1.  Clone or download the repository.
2.  Install the required libraries by running `pip install -r requirements.txt`.
3.  Run the script using `python app.py`.
4.  Input a customer review in the textbox and click on "Run".
5.  The output will show the sentiment prediction of the review as either Positive or Negative along with the respective confidence score.

## Libraries Used

-   Gradio
-   Transformers

## Contributor

-   [Kaludi](https://github.com/Kaludii)

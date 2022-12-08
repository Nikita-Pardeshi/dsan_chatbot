The current system at Georgetown DSAN program has to answer any question that prospective students and new admits have is a manual one. Students have the option to either find answers from the FAQ section or if their question is not covered in the FAQ , they can send questions via email and wait for the student ambassadors to answer them. This process is time consuming and on average takes 2-3 days. Time to get clarity impacts students' decision making especially when deadlines are close by. Our program could end up losing prospective students and also cause anxiety to new admits especially if they have questions that are time sensitive.


<b>Solution:</b> We believe an automated chatbot can help solve the above problem and help provide answers to most of their questions in a much quicker way.

Our idea is to leverage NLP principles to study the most popular questions and choose the best answer from a predefined set of answers. This reduces the workload on students and helps provide instant responses to 80% of the questions.


This is a task-oriented/ retrieval chatbot which is trained to provide the best possible response from a database of predefined responses. Retrieval-based chatbots use techniques like keywords matching, machine learning or deep learning to identify the most appropriate response. We intend to look at two different models to build the chatbot and select the one with higher accuracy. 

<h4>Model 1: The Sequential Model - Keras </h4>

To implement this model we first need to tokenize the data and then use lemmatization to create a bag of words. We then pass the bag of words to a deep neural network built using Keras sequential. The neural network predicts the ‘ID’ of the input which can be then used to locate the response. The benefit of using this method is that the neural network can be customized to change the number of layers, number of neurons and activation functions to get better accuracy.

<h4>Model 2: BERT (base uncased)</h4>

One of the important reasons to use BERT is its capability to understand the full context of a word by looking at the words that come before and after it, which helps to understand the intent behind the query asked. The BERT base uncased model is primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked) to make decisions, such as sequence classification, token classification or question answering. More details about this model can be found here: https://huggingface.co/bert-base-uncased


<h4>Results</h4>

We decided to choose the Keras model in this scenario for 2 major reasons: 

* The model outputs a very satisfactory/ desirable answer since it picks random choices from the dataset for a particular question and intent. 

* In BERT, a context was must even for prediction. For predicting an answer to a question asked without a context, further steps need to be taken such as predicting the tag as well and then selecting the best answer. 

<i>A web interface was created using Flask which can be run using the command `python run app.py`



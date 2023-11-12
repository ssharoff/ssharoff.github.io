# SAINT

Modern methods of Natural Language Processing (NLP) rely on Deep Learning models, which emerged as winners in a number of NLP tasks. However, their empirical success is often difficult to interpret because they operate by optimising millions (more recently billions) of parameters. While their use can result in superior performance in comparison to classical feature-based machine learning models, the Deep Learning models can lead to biases, for example, towards race, gender or political figures, so that a book review containing /an interesting book about Hitler/ is treated as negative, because of a strong negative association of the political figure, while disregarding its more relevant text properties. It has been also shown that such models are not always reliable, for example, adding an unrelated word like /sometimes/ can flip their predictions. The impact of biases and unreliable predictions are even stronger for lesser-resourced languages since their models have been trained on far less data, so the statistical estimates for the million-parameter models are based on much less evidence. In this study, we will specifically focus on interpreting the predictions of Sentiment Analysis (SA) models. Better understanding of the SA models has an impact on both theoretical linguistic research for expressing evaluation and appraisal and practical outcomes, for example, detection of negative mentions of products and services on the Web. For the theory of computational linguistics, this will provide the first comprehensive benchmark for interpretability research covering three languages, namely English, German and Amharic, thus ranging from the most to some of the lesser-resourced languages.

We will also plan testing for Yoruba and Igbo, thus covering zero-shot transfer to more languages.

The directories:
 
 - [Tasks](./progress/tasks.org)
 - [Source texts](./texts)
 - [Annotation guidelines](./annotation)
 - [Prediction models](./prediction)
 

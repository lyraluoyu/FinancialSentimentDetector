##### **FinSent Detector**

FinSent Detector is a model fusion system for detecting sentiment in financial texts. It combines multiple financial sentiment analysis models (FinBERT and Twitter-RoBERTa), providing more robust and fine-grained sentiment classification for financial news, tweets, and other texts.

###### **Features**

* Combines multiple sentiment recognition models to improve robustness and accuracy  
* Specifically designed for the financial domain, supporting both formal financial texts and social media language  
* Visual sentiment detection via a Streamlit web interface  

###### **Project Structure**

├── FSDapp.py                             # Streamlit frontend entry point  
├── FinSent_Detector.ipynb       # Notebook for model training and fusion development  
├── requirements.txt                   # Dependency list  
├── .gitignore                               # Git ignore configuration  
├── data.csv                                 # Dataset  
└── README.md                         # Project documentation  

###### **Model Description**

This project uses the following models for sentiment analysis:

* FinBERT  
* Twitter-RoBERTa  

Fusion strategies include:

* Softmax probability fusion  
* Custom rule-based pseudo-sentiment detection  

###### **Installation**

Clone the project:

* git clone https://github.com/lyraluoyu/FinancialSentimentDetector.git  
* cd FinancialSentimentDetector  

Create a virtual environment (optional) and install dependencies:

* pip install -r requirements.txt  

Prepare model files:

* The FinSent_Detector fusion model code is complete and will automatically download the required model files from an online repository at runtime  
* No need to manually download or place model files; as long as your network connection is active, the code will run directly  

###### **Launch Application**

Run the Streamlit app:

* streamlit run app.py  

###### **Contact**

For any questions, please contact the author: lyraly34\_@outlook.com  

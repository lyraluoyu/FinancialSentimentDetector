##### **FinSent Detector**

FinSent Detector 是一个用于检测金融文本情绪的模型融合系统。它结合了多个金融情绪分析模型（FinBERT 和 Twitter-RoBERTa），能对财经新闻、推文等文本进行更稳健、更精细的情绪判断。



###### **功能特色**

* 融合多个情绪识别模型，提高鲁棒性和识别准确度
* 专为金融领域设计，支持识别正式财经文本与社交媒体语言
* 可通过 Streamlit 页面进行可视化情绪检测



###### **项目结构**

├── FSDapp.py                             # Streamlit 前端入口

├── FinSent\_Detector.ipynb       # 模型训练与融合开发笔记

├── requirements.txt                   # 依赖列表

├── .gitignore                               # 忽略文件配置

├── data.csv                                 # 数据集

└── README.md                         # 项目说明



###### **模型说明**

本项目使用以下模型进行情绪识别：

* FinBERT
* Twitter-RoBERTa

融合策略包括：

* softmax 概率融合
* 自定义规则判断伪情绪



###### **安装方法**

克隆项目:

* git clone https://github.com/lyraluoyu/FinancialSentimentDetector.git
* cd FinancialSentimentDetector

创建虚拟环境（可选）并安装依赖：

* pip install -r requirements.txt

准备模型文件：

* 本项目的 FinSent\_Detector 融合模型代码完整，运行时会自动从线上仓库下载所需模型文件
* 无需手动下载或放置模型文件，只要确保网络连接正常，代码即可直接运行



###### **启动应用**

运行 Streamlit 页面：

* streamlit run app.py



###### **联系方式**

如有其他问题，请联系作者：lyraly34\_@outlook.com


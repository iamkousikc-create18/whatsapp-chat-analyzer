📊 WhatsApp Chat Analyzer (Streamlit)

An interactive web application that analyzes WhatsApp chat data and provides meaningful insights using data visualization and text analysis techniques.

🚀 Features

📈 Top Statistics

Total messages

Total words

Media shared

Links shared

📅 Timelines

Monthly message activity

Daily message trends

🗓️ Activity Analysis

Most active days of the week

Most active months

Weekly activity heatmap

👥 User Insights

Most active users in group chats

☁️ Text Analysis

WordCloud visualization

Most frequently used words

🛠️ Tech Stack

Python 3.11

Streamlit

Pandas

Matplotlib

Seaborn

WordCloud

Regex & Text Processing

📂 Project Structure
app.py              # Main Streamlit application
helper.py           # Analysis functions
preprocessor.py     # Data preprocessing
requirements.txt    # Dependencies
runtime.txt         # Python version
notebook/           # Jupyter notebook (EDA & experimentation)
📓 Notebook

The project includes a Jupyter Notebook for exploratory data analysis and preprocessing.

Path:
notebook: Whatsapp_chat_analysis.ipynb

📥 How to Use

Export your WhatsApp chat:

Open chat → Click 3 dots → More → Export Chat (without media)

Upload the .txt file in the app

Select a user or choose Overall

Click Show Analysis

▶️ Run Locally
git clone https://github.com/your-username/whatsapp-chat-analyzer-streamlit.git
cd whatsapp-chat-analyzer-streamlit
pip install -r requirements.txt
streamlit run app.py

🌐 Deployment

This project can be deployed easily using Streamlit Cloud.

⚠️ Limitations

Supports only WhatsApp exported .txt format

Does not process media files

Limited language handling for text analysis

📌 Future Improvements

Sentiment analysis

Emoji-based insights

Chat comparison between users

Multi-language support

👨‍💻 Author

Kousik Chakraborty

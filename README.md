# LinkedIn Post Generator Using Generative AI

This project generates professional LinkedIn posts, articles, and engagement strategies using Generative AI. By utilizing AI-driven models, the application helps create posts in various lengths and languages (English and Hinglish) for content creators, job seekers, influencers, and marketers on LinkedIn.

The app is built using **Streamlit**, **LangChain**, **Groq**, and other essential libraries to interact with AI models, process data, and generate content dynamically.

## Features

- **Post Generation**: Generate LinkedIn posts based on topics, lengths, and languages.
- **Language Support**: English and Hinglish (Hindi + English).
- **Customizable Options**: Length of the post (Short, Medium, Long), Topic (Tags), and Language.
- **Integration with Few-Shot Learning**: AI uses previously processed posts as examples for content generation.

## Technologies Used

- **Streamlit** - Web framework for building the app.
- **LangChain** - A framework for language model interaction.
- **Groq API** - To interact with the language models.
- **Pandas** - For data manipulation.
- **Python-dotenv** - For managing environment variables.
- **JSON** - For storing raw and processed post data.

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Install Dependencies
Create a virtual environment and install the required dependencies.
```bash
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a .env file in the root directory and add your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Running the App
Once you have all the dependencies set up and your environment variables configured, you can run the app using Streamlit:
```bash
streamlit run main.py
```

### 5. project structure
```bash
linkedin-post-generator/
│
├── data/
│   ├── raw_posts.json         # Raw input posts data
│   └── processed_posts.json   # Processed posts with metadata
│
├── main.py                    # Main app file (Streamlit)
├── preprocess.py              # Data preprocessing and metadata extraction
├── llm_helper.py              # Integration with AI model (Groq API)
├── few_shot.py                # Class for handling few-shot learning
├── post_generator.py          # Post generation logic using AI
├── requirements.txt           # List of dependencies
└── .env                       # Environment variables for API keys
```

### 6. Contributing
Contributions are welcome! If you want to help improve the project, feel free to fork the repository, create a branch, and submit a pull request.

Steps for Contribution
Fork the repository
Create a new branch 
```bash
git checkout -b feature-branch
```
Make changes and commit them 
```bash
git commit -m 'Add new feature'
```
Push to your branch 
```bash
git push origin feature-branch
```
Submit a pull request with a detailed description of your changes.








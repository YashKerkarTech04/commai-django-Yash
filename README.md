<div align="center">

# 🧠 CommAI – AI-Powered Communication Skill Analyzer

**An AI-powered web application that analyzes a user's communication skills through text and speech interactions using Natural Language Processing (NLP) and Artificial Intelligence.**

The system evaluates communication across multiple parameters, provides detailed feedback, highlights grammar issues, generates an AI-powered summary, and recommends learning resources to help users improve their communication skills.

🚀 *Built with Django, Python, NLP, and AI to make communication skill assessment interactive, intelligent, and practical.*

</div>

---

## 🛠 Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![TextBlob](https://img.shields.io/badge/TextBlob-NLP-4B8BBE?style=for-the-badge)
![TextStat](https://img.shields.io/badge/TextStat-Readability-4B8BBE?style=for-the-badge)
![Scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![LanguageTool](https://img.shields.io/badge/LanguageTool-Grammar%20API-2E8B57?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI%20Integration-4285F4?style=for-the-badge&logo=google&logoColor=white)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI%20Whisper-Planned-6E6E6E?style=for-the-badge&logo=openai&logoColor=white)

</div>

| Category | Technologies |
|---|---|
| **Frontend** | HTML5, CSS3, Bootstrap, JavaScript |
| **Backend** | Django (Python) |
| **Database** | SQLite |
| **NLP Libraries** | TextBlob, TextStat, Scikit-learn |
| **Grammar Checking** | LanguageTool API |
| **AI Integration** | Google Gemini API *(Currently Integrated)* |
| **Speech-to-Text** | OpenAI Whisper *(Planned)* |

---

## 📸 Project Preview

### 🔐 Sign In Page
<img width="1917" height="962" alt="Login" src="https://github.com/user-attachments/assets/094a12cc-17e3-41d2-b24f-baf3c5f52898" />

### 📝 Sign Up Page
<img width="1917" height="971" alt="Registration" src="https://github.com/user-attachments/assets/8862c0a9-415d-4f83-8d31-0060a7f6b43b" />

### 🏠 Home Page
<img width="1900" height="960" alt="HomePage" src="https://github.com/user-attachments/assets/f3d10692-138f-422c-8f6e-3ec5c0953b5a" />

### 💬 Text Interaction
<img width="1897" height="972" alt="Text Interaction" src="https://github.com/user-attachments/assets/ba30c1ac-f961-44c2-84e9-48c2d6bb0e8d" />

### 🎙️ Speech Interaction
<img width="1911" height="963" alt="Speech Interaction" src="https://github.com/user-attachments/assets/e3c70e19-2d41-4842-912e-0780a8239ffe" />

### 📊 Evaluation Results
<img width="1908" height="956" alt="EP1" src="https://github.com/user-attachments/assets/fea5ba31-f95f-418b-988c-6c55a714b55a" />
<img width="1892" height="958" alt="EP2" src="https://github.com/user-attachments/assets/b1eb8e11-74f9-42ec-afef-f51e40503679" />
<img width="1912" height="968" alt="EP3" src="https://github.com/user-attachments/assets/0bb307fc-8dce-4ca4-b11f-a2aaaaceeb26" />
<img width="1890" height="962" alt="EP4" src="https://github.com/user-attachments/assets/9544b865-3912-4683-b0bc-36e103067f00" />

### 🚨 Error Detection
<img width="1907" height="962" alt="Error_Detector" src="https://github.com/user-attachments/assets/8f428bca-3d11-4626-8f5b-efc15647d84d" />

---

## ✨ Features

- 💬 Analyze communication through **text input**
- 🎤 Analyze communication through **speech input**
- 📊 Evaluate communication across **7 key parameters**
- 📝 Detect grammar and spelling mistakes with suggested corrections
- 📈 Display interactive circular progress indicators for each parameter
- 🎯 Automatically classify communication level:
  - 🔴 Poor
  - 🟡 Intermediate
  - 🟢 Excellent
- 🤖 Generate AI-powered conversation summaries
- 📚 Recommend learning resources based on communication level
- 📱 Responsive and user-friendly interface

---

## 📊 Communication Parameters Evaluated

The application evaluates communication using the following parameters:

| Parameter | Description |
|---|---|
| 📖 **Readability** | How easy the text is to read and understand |
| ✂️ **Conciseness** | Clarity and brevity of expression |
| 😊 **Tone & Sentiment** | Emotional tone and sentiment of the message |
| 🤝 **Engagement** | How engaging and interactive the communication is |
| ✍️ **Grammar & Spelling** | Accuracy of grammar and spelling |
| 📚 **Vocabulary Usage** | Richness and appropriateness of vocabulary |
| 🙏 **Politeness** | Courtesy and professionalism in tone |

Each parameter is evaluated independently and displayed with its own score and personalized improvement suggestions.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YashKerkarTech04/commai-django-Yash.git
```

### 2️⃣ Move into the Project Directory
```bash
cd commai-django-project
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations
```bash
python manage.py migrate
```

### 5️⃣ Run the Development Server
```bash
python manage.py runserver
```

Open your browser and visit:
```
http://127.0.0.1:8000/login/
```

---

## 💬 Text Communication Workflow

1. Open the **Text Interaction** page.
2. Enter your response.
3. Click **Send**.
4. Submit the conversation.
5. View detailed communication analysis.

---

## 🎤 Speech Communication Workflow

1. Open the **Speech Interaction** page.
2. Record your speech.
3. Convert speech into text.
4. Submit the conversation.
5. Receive communication analysis and personalized feedback.

---

## 📈 Evaluation Output

For every communication session, CommAI provides:

- ✅ Individual parameter scores
- ✅ Grammar and spelling corrections
- ✅ AI-generated conversation summary
- ✅ Communication level assessment
- ✅ Personalized improvement suggestions
- ✅ Recommended learning resources

---

<div align="center">

Made with ❤️ using Django, Python & AI

</div>

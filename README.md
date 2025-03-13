
---

# 📰 Delta Headlines - AI War Reporter

### An AI-powered web application that extracts text from e-newspaper images, summarizes the content, and generates a professional news report with human-like audio in multiple voice tones (Male/Female).

---

## 📌 Project Overview

Delta Headlines is an AI-based wartime reporter that leverages **LayoutLMv3**, **Tesseract OCR**, and **LLM-based text summarization** to extract and summarize news content from newspaper images. The generated report is converted into realistic audio using **Kokoro TTS**, with the ability to **switch between male and female voices**.

---

## 🎯 Key Features
✅ Extracts text from e-newspaper images  
✅ Summarizes the extracted content using LLM models like DeepSeek/Mistral/Ollama2  
✅ Generates a professional news report  
✅ Converts the text to speech with **Kokoro TTS**  
✅ Supports **voice tone switching (Male/Female)**  
✅ Interactive UI built with **HTML + Tailwind CSS**  
✅ Real-time **loading spinner** during report generation  

---

## 🛠️ Tech Stack Used

| Technology        | Purpose                  |
|----------------|----------------------------------|
| LayoutLMv3   | Document segmentation |
| Tesseract OCR | Text extraction |
| LLM Models (DeepSeek/Mistral/Ollama2) | Text summarization |
| Kokoro TTS | Text-to-Speech Conversion |
| Bootstrap CSS | Frontend Design |
| Flask | Backend API |
| JavaScript | Frontend Logic |

---

## 🚀 Project Architecture

```
delta-headlines/
├── app.py                   # Main Flask application
├── config.py                # Configuration settings
├── ocr_module.py            # Text extraction with LayoutLMv3 and Tesseract
├── summarizer.py            # Text summarization using Mistral
├── report_generator.py      # News report formatting
├── tts_module.py            # Text-to-speech using Kokoro
├── image_utils.py           # Image preprocessing utilities
├── requirements.txt         # Project dependencies
├── setup.sh                 # Setup script
├── static/                  # Static files directory
│   ├── uploads/             # Uploaded images directory
│   └── audio/               # Generated audio files directory
└── templates/               # HTML templates
    └── index.html         # Main application interface
```

---

## 🌟 Workflow Pipeline

1️⃣ **Upload newspaper image**  
2️⃣ Extract text using **Tesseract OCR**  
3️⃣ Summarize the text using **LLM-based summarization model**  
4️⃣ Generate a **news report**  
5️⃣ Convert the report into **realistic audio with Kokoro TTS**  
6️⃣ Toggle between **male and female voices**  
7️⃣ Download the audio file  

---

## 🎯 Installation Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/your_username/Delta-Headlines.git
```

### Step 2: Install the Required Packages
```bash
cd Delta-Headlines
pip install -r requirements.txt
```

### Step 3: Run the Flask Backend
```bash
python app.py
```

### Step 4: Access the Web Application
Visit **http://localhost:5000** in your browser.

---

## 🖥️ UI Demo Preview

| Feature                  | Preview |
|--------------------|-------------------------|
| Upload Image        | ✅ |
| Extracted Text      | ✅ |
| Summarized News  | ✅ |
| Generate Audio (Kokoro) | ✅ |
| Voice Switching (Male/Female) | ✅ |
| Loading Spinner | ✅ |

---



## 🛑 Handling Errors

| Error | Cause | Solution |
|-----------------|-----------------|--------------------|
| Extracted text showing `undefined` | Incorrect Tesseract path | Check installation |
| Audio not generated | Incorrect voice model | Verify Kokoro TTS pipeline |
| Loading spinner stuck | Backend timeout | Check Flask logs |

---

## 🎯 Future Enhancements
- ✅ Add **multi-language support (Ollama Multilingual Model)**  
- ✅ Add **gender-based voice tone selection (Kokoro TTS)**  
- ✅ Integrate **real-time speech-to-text feedback**  
- ✅ Deploy as a **fully functional web application**  

---

## 📂 Sample Output Files
| File            | Content |
|----------------|------------------------|
| `extracted_text.txt` | Raw text from OCR |
| `summarized_news.txt` | LLM-generated summary |
| `final_report.wav` | Kokoro-generated audio |

---

## 📌 How to Use the Voice Toggle Feature?

| Mode                | Voice Model |
|----------------|---------------------|
| Male Voice   | `am_adam` |
| Female Voice | `af_heart` |

---

## 🎯 Contributors

| Name             | Role                           |
|----------------|-----------------------------------|
| Sidharthan S | Backend + LLM Pipeline |
| Praveen S | Frontend + TTS Integration |

---

## 🔗 Useful Resources
- [LayoutLMv3 Official Documentation](https://huggingface.co/LayoutLMv3)  
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)  
- [Kokoro TTS](https://kokoro-tts.com)  
- [Ollama AI](https://ollama.ai)  

---

## 🌟 Final Output  
```
🔹 Extracted Text: ✅  
🔹 Summarized News: ✅  
🔹 News Report: ✅  
🔹 Audio File: ✅  
```

---

## 🚀 Run Locally and Report Like a Pro 🎯

---

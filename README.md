
# AI Features Project

## Features

1. **Audio Transcription with Speaker Diarization**
   - Upload an audio file (WAV/MP3)
   - Get transcript with speaker labels using AssemblyAI

2. **Blog Title Suggestions**
   - Enter blog content or upload a .txt file
   - Get 3 AI-generated blog title suggestions using a T5-based NLP model

## Tech Stack

- Django 4.2.7
- AssemblyAI API
- HuggingFace Transformers (T5)
- Bootstrap 5 (UI)

## Setup Instructions

### Prerequisites
- Python 3.9+
- AssemblyAI API key
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai_features_project.git
   cd ai_features_project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # Or
   source venv/bin/activate  # On Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your AssemblyAI API key securely:
   - Create a `.env` file in the project root:
     ```env
     ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here
     ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

### Audio Transcription
- Upload a WAV/MP3 file in the Transcribe Audio section
- Get transcript and speaker labels in the UI

### Blog Title Suggestions
- Enter blog content or upload a .txt file
- Get 3 AI-generated titles in the UI

## API Endpoints

- `/transcribe/` : POST audio file, returns transcript and speaker labels (JSON)
- `/suggest-titles/` : POST blog content, returns 3 title suggestions (JSON)

## Project Structure

- `ai_features_project/` : Main Django project
- `transcriber/` : Audio transcription app
- `blog_title_suggester/` : Blog title suggestion app
- `media/` : Uploaded files
- `requirements.txt` : Python dependencies
- `readme.md` : Project documentation

## Security Note

- **Never upload your `.env` file or API keys to GitHub.**
- Always keep your AssemblyAI API key private.

## Troubleshooting

- If transcription fails, check your AssemblyAI API key and internet connection.
- For title suggestions, ensure all model dependencies are installed and internet is available for HuggingFace downloads.

## License

MIT License

## Setup Instructions

### Prerequisites
- Python 3.9+
- Django 4.2.7
- AssemblyAI account (for transcription API key)
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai_features_project.git
   cd ai_features_project
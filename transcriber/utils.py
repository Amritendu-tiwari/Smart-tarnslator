import assemblyai as aai
from django.conf import settings

def transcribe_audio(file_path):
    aai.settings.api_key = settings.ASSEMBLYAI_API_KEY
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path, config=config)
    result = {
        "transcript_id": transcript.id,
        "status": transcript.status,
        "text": transcript.text,
        "speakers": [
            {"speaker": utterance.speaker, "text": utterance.text, "start": utterance.start, "end": utterance.end}
            for utterance in transcript.utterances
        ]
    }
    return result
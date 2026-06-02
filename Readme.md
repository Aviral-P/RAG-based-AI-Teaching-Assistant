# RAG Project

A simple pipeline for converting videos into audio, transcribing audio to structured JSON, and generating embeddings for retrieval-augmented generation (RAG).

## Project Structure

- `01_Video_To_mp3.py` - Convert videos from `videos/` into MP3 files saved in `audios/`.
- `02_mp3_To_json.py` - Transcribe MP3 files in `audios/` and write transcript segments as JSON files in `json/`.
- `03_Preprocessing_json.py` - Read the JSON transcripts, generate text embeddings, and save the result in `embeddings.joblib`.
- `04_Process_Incoming.py` - Load saved embeddings and answer user questions by finding the most similar transcript chunks.
- `audios/` - Output folder for generated MP3 audio.
- `json/` - Output folder for transcription JSON files.
- `embeddings.joblib` - Serialized DataFrame containing text chunks and embeddings.

## Requirements

- Python 3.x
- `ffmpeg` installed and available in PATH
- Python packages: `whisper`, `requests`, `pandas`, `joblib`

> If you don't already have a `requirements.txt`, install the packages directly.

## Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install whisper requests pandas joblib
```

3. Install `ffmpeg` if it is not already available on your system.

## Usage

1. Add source video files to the `videos/` directory.
2. Convert videos to MP3:

```bash
python 01_Video_To_mp3.py
```

3. Transcribe MP3 audio to JSON:

```bash
python 02_mp3_To_json.py
```

4. Generate embeddings from the JSON transcripts:

```bash
python 03_Preprocessing_json.py
```

5. Ask incoming questions against the saved embeddings:

```bash
python 04_Process_Incoming.py
```

## Notes

- `02_mp3_To_json.py` may expect audio file names in the format `NN_Title.mp3`.
- `03_Preprocessing_json.py` currently uses a local embedding endpoint at `http://localhost:11434/api/embed` and model `bge-m3`.
- `04_Process_Incoming.py` reads `embeddings.joblib`, computes similarity against the user query, and writes `prompt.txt` with the top matching chunks.
- Update the scripts if you want to use a different transcription or embedding service.

## Output

- `audios/` contains converted audio files.
- `json/` contains transcript JSON files.
- `embeddings.joblib` contains saved embeddings and metadata for later retrieval.

## License

This repository is intended for personal use and experimentation.

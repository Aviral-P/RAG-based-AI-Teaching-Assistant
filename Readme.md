# RAG Project

This repository contains a simple pipeline to convert video files into audio, transcribe the audio into JSON, and generate embeddings for retrieval-augmented generation (RAG).

## Project Structure

- `01_Video_To_mp3.py` - Converts videos in the `videos/` folder into MP3 files in `audios/`.
- `02_mp3_To_json.py` - Transcribes MP3 audio files in `audios/` and saves segmented transcript JSON files in `json/`.
- `03_Preprocessing_json.py` - Creates embeddings from text chunks in `json/` files and stores them in `embeddings.joblib`.
- `audios/` - Output folder for generated MP3 audio files.
- `json/` - Output folder for transcription JSON files.
- `embeddings.joblib` - Saved pandas DataFrame containing chunk metadata and embeddings.

## Requirements

- Python 3.x
- `ffmpeg` installed and available in PATH
- `whisper` Python package
- `requests`, `pandas`, `joblib`

## Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt`, install directly:

```bash
pip install whisper requests pandas joblib
```

3. Install `ffmpeg` if not already available.

## Usage

1. Place input video files into the `videos/` directory.
2. Run video-to-audio conversion:

```bash
python 01_Video_To_mp3.py
```

3. Run transcription:

```bash
python 02_mp3_To_json.py
```

4. Run embedding preprocessing:

```bash
python 03_Preprocessing_json.py
```

## Notes

- `02_mp3_To_json.py` expects audio file names in the format `NN_Title.mp3`.
- `03_Preprocessing_json.py` sends a request to a local embedding service at `http://localhost:11434/api/embed` using model `bge-m3`.
- You may need to adapt the transcription and embedding scripts for your chosen model or API.

## License

This project is for personal use and experimentation.

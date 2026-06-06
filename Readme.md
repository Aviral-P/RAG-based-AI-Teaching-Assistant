# RAG Project

A simple pipeline for converting videos into audio, transcribing audio to structured JSON, optionally merging transcript chunks, and generating embeddings for retrieval-augmented generation (RAG).

## Project Structure

- `01_Video_To_mp3.py` - Convert videos from `videos/` into MP3 files saved in `audios/`.
- `02_mp3_To_json.py` - Transcribe MP3 files in `audios/` and write transcript segments as JSON files in `json/`.
- `03_Preprocessing_json.py` - Read the JSON transcripts, generate text embeddings, and save the result in `embeddings.joblib`.
- `05_Merge_chunks.py` - Merge every 5 transcript chunks from `json/` into larger chunks and write merged files into `newjsons/`.
- `04_Process_Incoming.py` - Load saved embeddings and answer user questions by retrieving the most similar transcript chunks from `embeddings.joblib`.
- `audios/` - Output folder for generated MP3 audio.
- `json/` - Output folder for original transcript JSON files.
- `newjsons/` - Output folder for merged transcript JSON files.
- `embeddings.joblib` - Serialized DataFrame containing text chunks and embeddings.

## Requirements

- Python 3.x
- `ffmpeg` installed and available in PATH
- Python packages: `whisper`, `requests`, `pandas`, `joblib`, `numpy`, `scikit-learn`

> If you don't already have a `requirements.txt`, install the packages directly.

## Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install whisper requests pandas joblib numpy scikit-learn
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

4. (Optional) Merge transcript chunks into larger chunks for easier retrieval:

```bash
python 05_Merge_chunks.py
```

5. Generate embeddings from the JSON transcripts:

```bash
python 03_Preprocessing_json.py
```

6. Ask incoming questions against the saved embeddings:

```bash
python 04_Process_Incoming.py
```

## Notes

- `05_Merge_chunks.py` groups every 5 consecutive transcript chunks from files in `json/` and writes merged results to `newjsons/`.
- `04_Process_Incoming.py` calls a local embedding endpoint at `http://localhost:11434/api/embed` with model `bge-m3` to embed the incoming query.
- `04_Process_Incoming.py` also calls a local generation endpoint at `http://localhost:11434/api/generate` with model `qwen3:8b` to generate a human-readable answer.
- The script writes the retrieval prompt to `prompt.txt` and the generated response to `response.txt`.
- If the incoming question is unrelated, the model is instructed to reply that it can only answer questions related to the transcript data.

## Output

- `audios/` contains converted audio files.
- `json/` contains original transcription chunks.
- `newjsons/` contains merged transcript chunks.
- `embeddings.joblib` contains saved embeddings and metadata for retrieval.
- `prompt.txt` contains the assembled prompt used by the generation model.
- `response.txt` contains the generated answer to the user query.

## License

This repository is intended for personal use and experimentation.

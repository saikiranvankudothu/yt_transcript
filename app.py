from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/transcript")
def transcript(video_id: str):
    try:
        yt = YouTubeTranscriptApi()
        transcript_list = yt.fetch(video_id)

        text = " ".join(item.text for item in transcript_list)

        return {
            "video_id": video_id,
            "transcript": text
        }

    except Exception as e:
        return {"error": str(e)}

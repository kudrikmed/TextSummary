import pytube as pt
import whisper


class YoutubeTranscriber:
    def __init__(self):
        self.model = whisper.load_model("large")

    def transcribe_youtube(self, yt_url, audio_filename='audio.mp3'):
        yt = pt.YouTube(yt_url)
        stream = yt.streams.filter(only_audio=True)[0]
        stream.download(filename=audio_filename)

        result = self.model.transcribe(audio_filename)
        return result["text"]

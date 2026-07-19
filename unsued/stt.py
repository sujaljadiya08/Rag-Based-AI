import whisper 
import json

model = whisper.load_model("base")

result= model.transcribe( audio="audios/12_Exercise 1 - Pure HTML Media Player.mp3",
                         language='hi',
                         task="translate"
                         )
#create chunks
chunks= []

for segment in result['segments']:
    chunks.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
                        })
#save chunks to json
with open ("output.json","w", encoding='utf-8') as f:
    json.dump(chunks , f, ensure_ascii=False, indent=4)
    print("json created successfully")
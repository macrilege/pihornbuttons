import boto3
import sys
import os
#import ffmpeg
from ffmpy import FFmpeg

s = sys.argv[1]
polly_client = boto3.Session(
aws_access_key_id='AKIAQ6FRTC2TA2WT7N6X', 
aws_secret_access_key='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', 
region_name='us-east-1').client('polly')

response = polly_client.synthesize_speech(VoiceId='Salli', 
    OutputFormat='mp3', 
    Text = s)

file = open('speech.mp3', 'wb')

file.write(response['AudioStream'].read())
file.close()
command = f"ffmpeg -i speech.mp3 -af 'volume=3.5' speech2.mp3 -y"
print(command)
os.system(command)
#ffmpeg -i speech.mp3 -af 'volume=1.7' speech2.mp3
os.system("mpg321 speech2.mp3")

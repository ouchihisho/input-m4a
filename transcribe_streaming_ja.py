#!/usr/bin/env python

import argparse
import io
from convert_audio import convert_audio
from convert_audio import remove_tmp_file

def transcribe_streaming_ja(stream_file):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    with io.open(stream_file, 'rb') as audio_file:
        content = audio_file.read()

    stream = [content]
    requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                for chunk in stream)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ja-JP')
    streaming_config = types.StreamingRecognitionConfig(config=config)

    responses = client.streaming_recognize(streaming_config, requests)

    ret = ''.encode('utf-8')

    for response in responses:
        for result in response.results:
            print('Finished: {}'.format(result.is_final))
            print('Stability: {}'.format(result.stability))
            alternatives = result.alternatives
            for alternative in alternatives:
                transcript = alternative.transcript.encode('utf_8')
                print('Confidence: {}'.format(alternative.confidence))
                print('Transcript: {}'.format(transcript))
                ret = ret + transcript

    print('ret : '.encode('utf-8') + ret)
    return ret
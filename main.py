#!/usr/bin/env python

import argparse
import io
from transcribe_streaming_ja import transcribe_streaming_ja
from convert_audio import convert_audio
from convert_audio import remove_tmp_file

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('stream', help='File to stream to the API')
    args = parser.parse_args()
    tmp_wav_name = '16000.wav'
    tmp_raw_name = '16000.raw'

    transcribe_streaming_ja(convert_audio(args.stream, tmp_wav_name, tmp_raw_name))
    remove_tmp_file(tmp_wav_name, tmp_raw_name)

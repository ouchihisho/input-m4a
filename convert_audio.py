#!/usr/bin/env python

import argparse
import io
import commands
import ConfigParser

def convert_audio(m4a_file_name, tmp_wav_name, tmp_raw_name):
    command_str = ('ffmpeg -i %s -ar 16000 %s ; sox %s %s' % (m4a_file_name, tmp_wav_name, tmp_wav_name, tmp_raw_name))
    commands.getstatusoutput(command_str)
    return tmp_raw_name

def remove_tmp_file(tmp_wav_name, tmp_raw_name):
    commands.getstatusoutput('rm ' + tmp_wav_name)
    commands.getstatusoutput('rm ' + tmp_raw_name)

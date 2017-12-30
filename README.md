# 使い方

```
$ python main.py hoge.m4a
```

# 事前準備

## soxのインストール

```
$ brew install lame
$ brew install sox
```

## ffmpegのインストール

```
$ brew install ffmpeg
```

## pipenvのインストールと実行

```
$ pip install pipenv
$ pipenv install
```

## google speech apiの連携

Googleのドキュメントをもとに進める。
https://cloud.google.com/speech/docs/streaming-recognize?hl=ja

2017/12/30時点のおおまかの流れは以下。

1. gcloudのインストール
    1. `google-cloud-sdk` の取得
    1. `./google-cloud-sdk/install.sh` を実行
    1. `gcloud init` 
    1. ブラウザ上で個人のgoogleアカウントで認証
1. クライアントライブラリのインストール ※ pipenvを実行しておけば不要
```
$ pip install --upgrade google-cloud-speech
```
1. クライアントライブラリの認証
```
$ gcloud auth application-default login
```

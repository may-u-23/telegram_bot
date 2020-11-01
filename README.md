# telegram_bot

# repeat_bot

# 概要
- オウム返しするBotサンプル

![repeat_bot](https://user-images.githubusercontent.com/56919784/97782479-1046ee00-1bd5-11eb-82e5-a3ab49346562.gif)

# 動作確認環境
```
ProductName:	Mac OS X
ProductVersion:	10.15.6
BuildVersion:	19G73

python-telegram-bot: 12.8
```

# 事前作業
## Telegram APIsのインストール
API仕様変更により、最新バージョンだと動作しない。下記の通り、バージョン指定してインストールする
```
❯ pip3 install python-telegram-bot==12.8
```

## Telegram Bot用アクセストークンの取得
下記リンク参照
https://core.telegram.org/bots#6-botfather

# 実行方法
## 実行権限付与
```
chmod u+x echo_system.py
```

## 実行
```
❯ ./mecab-python3_sample.py
```
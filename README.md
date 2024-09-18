# Notifier Bot

`notifier-bot` は、指定された日時や条件に基づいて、LINE Notify を通じて通知を送信する自動化ツールです。本ツールを使用することで、特定のスケジュールに基づいてリマインダーや通知をLINEに送ることができます。  
デフォルトでは、ゴミの回収日を通知しますが、カスタマイズして他のリマインダー用途にも使用可能です。

## 機能

- LINE Notify を使用して通知を送信
- 指定された曜日・時間に自動的にメッセージを送信
- GitHub Actionsを利用して定期的なジョブ実行が可能
- 簡単にカスタマイズして、他の通知用途に対応

## 使い方

### 1. LINE Notify トークンの取得

1. [LINE Notify](https://notify-bot.line.me/ja/) からLINE Notifyトークンを取得します。
2. GitHubリポジトリのシークレットに、`LINE_NOTIFY_TOKEN` としてトークンを保存します。

### 2. GitHub Actions の設定

このリポジトリには、通知を定期的に送信するためのGitHub Actions設定が含まれています。特定のスケジュールで通知を送信するには、`.github/workflows/line_notify.yml` ファイルの `cron` 部分を修正します。

#### スケジュール設定例

```yaml
on:
  schedule:
    # 毎週金曜日 9:00 JST
    - cron: '0 0 * * 5'
    # 毎週火曜日 9:00 JST
    - cron: '0 0 * * 2'
    # 毎週水曜日と土曜日 9:00 JST
    - cron: '0 0 * * 3'
    - cron: '0 0 * * 6'
    # 第1・第3木曜日 9:00 JST
    - cron: '0 0 1-7,15-21 * 4'
```

### 3. カスタマイズ方法

通知する内容やスケジュールを変更したい場合は、`line_notify.yml` 内のPythonスクリプト部分を修正します。  
例えば、異なるメッセージを送信したり、別の曜日に通知することができます。

#### 例: カスタマイズされたPythonコード

```python
# 曜日ごとのメッセージを送信
today = datetime.today()
weekday = today.weekday()

if weekday == 4:  # 金曜日
    send_line_notify('金曜日の特別なリマインダーです！')
elif weekday == 1:  # 火曜日
    send_line_notify('火曜日のタスク確認をお願いします。')
```

## インストール

このリポジトリはGitHub Actions上で動作するため、ローカルでのインストールは不要です。  
ただし、ローカルでテストしたい場合は以下の手順でセットアップできます。

1. リポジトリをクローンします。

```bash
git clone https://github.com/your-username/notifier-bot.git
cd notifier-bot
```

2. 必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

3. LINE Notify トークンを環境変数として設定します。

```bash
export LINE_NOTIFY_TOKEN=YOUR_LINE_NOTIFY_TOKEN
```

4. Python スクリプトを実行します。

```bash
python notify.py
```

## ライセンス

このプロジェクトは [MIT License](LICENSE) に基づいています。

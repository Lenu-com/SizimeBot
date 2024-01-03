
# chatGPT×Discord 概要
当プログラムはDiscordAPIとOpenAIAPIを使用し、<br>
Discord内でのBOTへのメッセージをプロンプトとして<br>
chatGPTへリクエストを送信し、レスポンスをBOTが送信する事で<br>
Discord内でのchatGPTの使用を可能にします。

# 使用方法
1. app.pyにDiscord Botのトークンを設定します。<br>
   ```
   TOKEN: Final[str] = 'YOUR_DISCORD_BOT_TOKEN'
   ```

2. OpenAIConnector.pyにOpenAIのAPIキーを設定します。<br>
    ```
    API_KEY: Final[str] = 'YOUR_OPENAI_API_KEY'
    ```

3. config.ymlに事前情報を設定します。
    ```
    content:
        ここにキャラ設定や制約などを記載する。
    
    ng_words:
        - ここに禁止ワードを記載する。(頭に- を付ける。)
    ```

4. app.pyを実行し、本ツールを起動します。
5. BOT宛にメンションを付け、メッセージを送信します。


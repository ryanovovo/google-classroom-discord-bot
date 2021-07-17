# Google Classroom discord Bot

## 簡介
使用discord bot同步Google Classroom中的公告和作業

## 可使用指令
`/stop` 停止伺服器

`/listcourses` 列出所有已經加入的課程

## **使用方法**
### 1.下載所需程式碼
https://github.com/ryanovovo/google-classroom-discord-bot/archive/refs/heads/master.zip

#### 1.1 解壓縮檔案

#### 1.2 重新命名檔案
將資料夾中的`setting_copy.json`重新命名為`setting.json`


### 2.建立OAuth同意畫面
#### 2.1至下列網址並登入google帳號
https://console.cloud.google.com

#### 2.2進入API資訊主頁


#### 2.3 建立OAuth 2.0同意畫面

#### 2.4 填入所需資訊

#### 2.5 新增所需權限
在手動新增範圍處填入以下網址：
`https://www.googleapis.com/auth/classroom.courses.readonly,https://www.googleapis.com/auth/classroom.coursework.me.readonly,https://www.googleapis.com/auth/classroom.announcements.readonly,https://www.googleapis.com/auth/classroom.coursework.students.readonly,https://www.googleapis.com/auth/classroom.coursework.students,https://www.googleapis.com/auth/classroom.coursework.me`

#### 2.6 發布應用程式


### 3 建立OAuth用戶端ID

#### 3.1 點選建立憑證,OAuth


#### 3.2 url處填入`http://localhost:8080/`



#### 3.3 下載金鑰檔案
下載完成後將檔案放入一開始解壓縮的資料夾並將檔案重新命名為`credentials.json`

### 4. 建立discord bot

#### 4.1 至以下網址並登入discord帳號
https://discord.com/developers/applications
建立discord bot並邀請至伺服器

#### 4.2複製bot token
將複製好的bot token替換掉 `setting.json`中的`YOUR_DISCORD_BOT_TOKEN`

### 5. 建立頻道
#### 5.1 建立頻道"公告"
右鍵複製頻道ID並將複製好的ID替換掉`setting.json`中的`ANNOUNCEMENT_CHANNEL_ID`

#### 5.2 建立頻道"作業"
右鍵複製頻道ID並將複製好的ID替換掉`setting.json`中的`HOMEWORK_CHANNEL_ID`

#### 5.3 建立頻道"command line"
右鍵複製頻道ID並將複製好的ID替換掉`setting.json`中的`COMMAND_LINE_CHANNEL_ID`

### 6. 下載所需函式庫
`pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib httplib2 oauth2client`

### 7. 啟動bot
輸入指令 `python3 bot.py`
若在discord中有跳出通知及代表建立成功

## 碰到問題？
* 在github上發Issue
* 在github上發Pull Request
















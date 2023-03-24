# 交通部運輸資料流通服務平臺TDX-簡易JSON查詢

## 程式功能
1. 查詢TDX API的JSON內容
2. 複製輸出的JSON資料

## 使用方式
1. 註冊TDX帳號([交通部運輸資料流通服務平臺TDX](https://tdx.transportdata.tw/))
2. 編輯TDX.py檔案，在Line 5.6輸入自己的TDX-Client Id及Client Secret
3. 安裝requirements.txt
    ```
    pip install -r requirements.txt
    ```
4. 執行TDX.py
5. 輸入Request URL後Enter
6. 即可顯示此API的JSON資料，並且程式會自動複製輸出內容

## 套件需求
1. requests
2. json
3. pyperclip

## 程式截圖
![](https://i.imgur.com/t84iHzj.png)

![](https://i.imgur.com/GUUngab.png)
## 資料來源
此程式參考官方提供之[參考程式碼](https://github.com/tdxmotc/SampleCode)




# Programs running on Raspberry Pi that connects to IoT Platform
     
## 【 Overview 】
           
* 物聯網架構與應用
 
![Imgur](http://i.imgur.com/pZykKHV.png)

* 通訊協定與網路服務提供商

| 通訊協定 | 網路服務提供商 |
|---|---|
| HTTP | ThingSpeak、MediaTek Cloud Sandbox (MCS)、Google Firebase |
| MQTT | MediaTek Cloud Sandbox (MCS)、AWS IoT、IBM Bluemix IoT Platform |
| WebSocket | WoT.City |

## 【 檔案說明 】

| 編號 | 資料夾 |  檔案名稱 |
|---|---|---|
| 1 | get_data_from_MCS.py | 從 MCS 取得溫濕度資料 |
| 2 | get_data_from_WoTCity.py | 從 WoT.City 取得溫濕度資料 |
| 3 | raspberryPi_dht_AWS_IoT.py | 將溫濕度資料傳送到 AWS IoT |
| 4 | raspberryPi_dht_Firebase.py | 將溫濕度資料傳送到 Google Firebase |
| 5 | raspberryPi_dht_IBM_Bluemix_Publish.py | 將溫濕度資料傳送到 IBM Bluemix |
| 6 | raspberryPi_dht_IBM_Bluemix_Subscribe.py | 從 IBM Bluemix 取得溫濕度資料 |
| 7 | raspberryPi_dht_MCS_API.py | 將溫濕度資料透過 API 傳送到 MCS |
| 8 | raspberryPi_dht_MCS_MQTT.py | 將溫濕度資料透過 MQTT 傳送到 MCS |
| 9 | raspberryPi_dht_ThingSpeak.py | 將溫濕度資料傳送到 ThingSpeak |
| 10 | raspberryPi_dht_WoTCity.py | 將溫濕度資料傳送到 WoT.City |
| 11 | raspberryPi_dht_lcd.py | 將溫濕度資料顯示於 LCD |

## 【 Board and Sensor 】

* [Raspberry Pi 3 Model B](https://www.seeedstudio.com/Raspberry-Pi-3-Model-B-p-2625.html)
* [GrovePi+ ](https://www.seeedstudio.com/GrovePi%2B-p-2241.html)
* [Grove - Temperature & Humidity Sensor](https://www.seeedstudio.com/Grove-Temp%26Humi-Sensor-p-745.html)
* [Grove - LCD RGB Backlight](https://www.seeedstudio.com/Grove-LCD-RGB-Backlight-p-1643.html)

## 【 Integrated Development Environment - IDE 】

 * Python
   * [Sublime Text](https://www.sublimetext.com/)
   * [Visual Studio Code](https://code.visualstudio.com/b?utm_expid=101350005-27.GqBWbOBuSRqlazQC_nNSRg.1&utm_referrer=https%3A%2F%2Fwww.google.com.tw%2F)
   * [Jupyter](http://jupyter.org/)
     * Command: ipython notebook

## 【 Service 】

* [WoT.City](https://wotcity.com/)
* [Amazon Web Services Cloud](https://aws.amazon.com/tw/)
* [Google Firebase](https://firebase.google.com/)
* [IBM Bluemix](https://console.ng.bluemix.net/)
* [MediaTek Cloud Sandbox](https://mcs.mediatek.com)
* [ThingSpeak](https://thingspeak.com/)
* [ThinkSpeak Data Visualization](nrl.iis.sinica.edu.tw/LASS/PM25.php?site=III&city=台北市&district=信義區&channel=152239&apikey=9ND1FVDPKLQGPDRI)

## 【 Reference 】

* [MediaTek Cloud Sandbox (MCS)](https://mcs.mediatek.com/resources/zh-TW/latest/api_references/)

## 【 Tools 】
 * Windows 作業系統
   *  登入
      * Windows 端
        * [Putty](https://the.earth.li/~sgtatham/putty/latest/x86/putty.exe)
   *  傳送檔案 
      * Windows 端
        * [FileZilla Client](https://filezilla-project.org/)

 * macOS 作業系統
   *  登入 / 傳送檔案（本地端到 Raspberry Pi 端）- 終端機
      * 登入（在本地端電腦的終端機執行） ➙ ```ssh root@Raspberry Pi 的IP```
      * 傳送檔案（在本地端電腦的終端機執行） ➙ ```scp 在電腦中的檔案位置 root@Raspberry Pi 的IP:要傳送到 Raspberry Pi 中的位置```

## 【 Execute】

 * execute Python Code
```bash
$ python Python-Name-Here.py
```

 * execute Shell Script
```bash
$ sh Script-Name-Here.sh
$ ./Script-Name-Here.sh
```

## 【 JSON Tools 】
 * [JSON Lint](http://jsonlint.com/)
 * [JSON Editor Online](http://www.jsoneditoronline.org/)

## 【 Troubleshooting 】
 * 如果在瀏覽器輸入所設定的 local domain ( 預設為 ```http://mylinkit.local``` ) 後無法顯示設定頁時
   *  請安裝 [Bonjour Print Services](https://support.apple.com/kb/dl999?locale=zh_TW)
   *  再重新在瀏覽器輸入所設定的 local domain 
 * 當登入時發生 ```WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!``` 錯誤
   * 於終端機輸入 ```ssh-keygen -R IP位置 ```
   * 再重新 Login
   
## 【 Blog 】
* [Archer @ 部落格](https://github.com/ArcherHuang/MyBlog/blob/master/README.md)

## 【 License 】

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



 



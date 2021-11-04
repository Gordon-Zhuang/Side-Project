# C語言KNN程式碼(predict)(STM32專案)

## Environment
```
STM32 G474
language : C
IDE : Cube IDE
```
## Get Start

`*此專案僅有預測功能`

>A. 直接使用專案
>>step1. 將訓練完的model編寫成model.h

>>step2. 編寫main.c，需要使用預測功能時，呼叫kNN函數即可

>B. 將kNN.c導入個人專案
>>step1. 將kNN.h, dangerous_type.h放入include資料夾

>>step2. 將kNN.c 放入src資料夾

>>step3. 將個人model編寫成model.h

>>step4. 編寫main.h 將以上幾個.h檔案加入

## Parameter
```
兩個input參數:
1 為陣列，輸入需要被預測的資料
2 可以調整K的數量選擇，太小可能會過擬和，太大則有可能被無關的點所影響
```
```
partition函式
閹割版的快排，誤了找出最近K個資料
```





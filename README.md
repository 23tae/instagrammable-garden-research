# Instagrammable Garden Research

## Overview

인스타그램에서 태그(garden, travel, cafe, food, book)별 이미지를 수집하여 사용자의 활동 유형별 이용행태를 분석한다.  
인스타그램 이미지에서 인식된 레이블을 막대그래프와 워드클라우드를 사용하여 시각화한다.

## Features

### 레이블 인식

[Google Cloud Vision API](https://cloud.google.com/vision)를 활용하여 수집한 이미지의 레이블을 인식한다. (`.txt` 형식으로 저장한다.)

- 방법

```bash
python3 main.py
```

- 결과 예시

```
  Labels:
  Font
  Material property
  Rectangle
  Wood
  Art
  Paper
  Publication
  Paper product
  Pattern
  Illustration
```

### 시각화

`.txt` 형식의 파일로 저장된 레이블 데이터를 막대그래프와 워드클라우드로 시각화한다.

- 막대그래프
  ![barchart](/assets/barchart_travel.png)

- 워드클라우드
  ![wordcloud](/assets/wordcloud_travel.png)

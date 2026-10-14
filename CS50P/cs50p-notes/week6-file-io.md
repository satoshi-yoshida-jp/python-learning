# Week 6: File I/O

## 1. 概要

ファイル操作（File I/O）は、プログラムが外部のデータを読み込み、加工し、再出力するための基本技術。Python では `open()` を使ってファイルを開き、`with` 文と組み合わせることで自動で閉じられるようにするのが基本。

week6では、テキストファイル、CSV、画像ファイルを扱いながら、データを読み取る方法と保存する方法を学習。

## 2. ファイルを開く・読む

```python
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
```

- `open("filename")` でファイルを開く
- `"r"` は読み取りモード（省略可能）
- `for line in file` で1行ずつ読み込める
- `rstrip()` を使って改行文字を取り除く
- `sorted(names, reverse=True)` のように、読み込んだデータを並べ替えて処理できる

この考え方は、テキストデータを順番に処理する典型的なファイル入出力

## 3. ファイルを書き出す

```python
with open("alice.txt", "r") as f:
    contents = f.readlines()

chapter1 = contents[52:208]
with open("chapter1.txt", "w") as f:
    f.writelines(chapter1)
```

- `readlines()` で複数行をリストとして読み込む
- 取得したデータの一部をスライスして取り出す
- `"w"` は書き込みモードで、新しいファイルを作成・上書きする
- `writelines()` で文字列や行をまとめて書き込む

ここでは、元のファイルから必要な部分だけを抽出して、新しいファイルに保存する例を学習

## 4. CSV を扱う

```python
import csv

name = input("Whats your name? ")
country = input("Whats your country? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "country"])
    writer.writerow({"name": name, "country": country})
```

CSV は、表形式のデータを保存するための標準的なファイル形式です。

- `csv.DictReader` は列名付きでデータを読む
- `csv.DictWriter` は列名付きでデータを書き出す
- `"a"` は追記モードで、既存ファイルに新しい行を追加する
- `fieldnames` で表の列名を定義する

CSV はデータ分析やデータ収集の際によく使われる

## 5. CSV と画像を組み合わせる

```python
import csv
import numpy as np
from PIL import Image

with (
    open("./data-csv/views.csv", "r") as views,
    open("analysis.csv", "w") as analysis,
):
    reader = csv.DictReader(views)
    writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
    writer.writeheader()

    for row in reader:
        row["brightness"] = round(
            calculate_brightness(f"./data-csv/{row['id']}.jpeg"), 2
        )
        writer.writerow(row)
```

- CSV の各行を読み込みながら、画像ファイルの情報を計算する
- 画像の明るさ（brightness）を計算して、CSV に追記する
- `Image.open()` で画像を開き、`convert("L")` でグレースケール化する
- `numpy` を使って画像の平均値を計算し、`/255` で正規化する

このような処理は、ファイル I/O とデータ処理を組み合わせた典型例

## 6. 画像の編集

```python
from PIL import Image, ImageFilter

with Image.open("in.jpeg") as img:
    img = img.rotate(180)
    img = img.filter(ImageFilter.FIND_EDGES)
    img.save("out.jpeg")
```

- `Image.open()` で画像を開く
- `rotate()` で回転させる
- `ImageFilter` でエフェクトを追加する
- `save()` で加工済みの画像を保存する

ファイル I/O は、テキストだけでなく画像やバイナリデータにも使える

## 7. 重要ポイント

- `with open(...) as file:` はファイルを安全に扱うための基本形
- `"r"` 、`"w"` 、`"a"` の違いを理解することが重要
- 文字列データは行単位で処理することが多い
- CSV は表形式のデータを扱うのに便利
- 画像はファイルとして読み込み、加工して保存できる

## 8. まとめ

Week6では、Pythonのファイル入出力を学び、テキストファイル、CSV、画像ファイルを扱う方法を実際のコードで確認した。重要なのは、ファイルを開いてデータを読み込み、必要な加工を行い、結果を保存する一連の流れを理解すること。

この考え方は、データ分析、ログ処理、画像加工、業務自動化など、Python を使う多くの場面で活用される。

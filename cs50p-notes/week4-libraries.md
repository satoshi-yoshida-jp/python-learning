# Week4 Libraries

## Library > Package > Module

複数のコードをまとめ、特定の目的のために再利用可能とする

### Module

モジュールは関数やクラスなど再利用可能なコードが書かれたpyファイル

### Package

パッケージは複数のモジュールをまとめたもの

### Library

複数のモジュールやパッケージをまとめたもので、特定の目的のため機能するコードの集合。Pythonに始めから搭載されている標準ライブラリと、自分でインストールして使う外部ライブラリがある。

## Library introduction

### random

Generate pweudo-random numbers

- choice(seq)
- shuffle(x)
- randint(a, b)
- ...

### statistics

Mathmatical statistics functions.

Provides functions for calculating mathmatical statistics of numeric data.

### sys

Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

Unless explicitly noted otherwise, all variables are read-only

- sys.argv : argument vector
  プログラム実行時にコマンドラインから渡された引数を文字列のリストとして格納する。インデックスで特定の要素を取得できる。[0]は主に実行ファイル名
- sys.exit
  プログラムを終了させる。引数でエラーメッセージや終了コードなどを表示させ終了させることができる。

## Packages

Package repository : PyPi（外部パッケージ管理サイト）
pip : package installer for Pythonでインストールする（pip install ~）

### Package structure

package dir

- **init**.py
- module (~.py)
- module (~.py)
- ...

**init**.pyはそのディレクトリをパッケージとして定義し、初期化処理を行うファイル

## APIs : Application Programming Interface

異なるソフトウェア同士がやり取りするための仕組み

クライアントがリクエストを送り、サーバーがその結果をレスポンスとして返す

requestsなど使用

Art Institute of Chicago's APIを活用して練習した
https://api.artic.edu/docs/

### JSON : JavaScript Object Notation

計量なテキスト形式で、ブラウザとサーバー間の通信などで利用されるデータ交換フォーマット。JavaScript以外の多くのプログラミング言語で使用可能。

### API responses

API通信時に受信する情報

- HTTP status code（200 OK, 404 Not Fund, 500 Internal Server Errorなど）
  処理が成功したか、エラーだったかを示す３桁の数字
- response header
  Content-Type（データ形式）やサーバ情報などの付加情報
- response body
  クライアントに返す実データ（JSONなど）

## random module

擬似乱数を生成する標準モジュール

random.seed()
擬似乱数の開始状態を設定する関数

通常、seedを設定しないrandom関数では実行のたびに異なる乱数を出力する。
一方seedの値を設定（固定）すれば、何度実行しても同じ乱数を生成する。

random.seed(42)
print(random.choices(cards, k=2))　→ [jack, queen]
print(random.choices(cards, k=2))　→ [king, queen]

↑を実行した結果は、その後再度↓を実行した結果と同じ（再現性がある）
seed設定しないと上下は異なる出力となる（再現性はない）

random.seed(42)
print(random.choices(cards, k=2)) → [jack, queen]
print(random.choices(cards, k=2)) → [king, queen]

## style

### PEP8

pythonのコーディング（スタイル）規約

- インデント
- １行の文字数
- 空白
- インポート順序
- 変数、関数、クラス、定数の命名規則
- ...

### pylint

pythonコードの構文エラーや規約違反、バグの可能性などを検出するコード解析ツール
コードを実行せずに不適切な箇所がないか解析する

### Ruffをvscodeに導入

Rust製で高速に動作するpython向けの次世代リンタおよびコードフォーマッタ
伝統的なものはBlack

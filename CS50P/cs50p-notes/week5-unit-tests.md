# Week 5: Unit tests

## 1. 概要

Unit test（単体テスト）は、関数など小さな単位のコードが期待どおりに動くかを自動で確かめるテスト。入力と期待する出力を明示しておけば、変更後に以前の動作が壊れていないかを繰り返し確認できる。

テストでは、通常の実行結果だけでなく、境界値や不正な入力に対する振る舞いも確認する。テストは仕様を明確にする助けにもなるが、すべての不具合がないことを証明するものではないため、重要なケースを選んでテストする。

## 2. pytest

```{python}
import pytest
from calculator import square


def test_positive():
    assert square(2) == 4


def test_zero():
    assert square(0) == 0


def test_wrong_type():
    with pytest.raises(TypeError):
        square("cat")
```

`assert` は条件が偽ならテストを失敗させる。pytestでは、`test_`で始まるファイル内の`test_`で始まる関数がテストとして自動検出される。プロジェクトの対象ディレクトリで次のように実行する。

```bash
pytest test_calculator.py
```

- 正常な値、0、負の値など、入力の種類ごとにテストを分ける。
- 例外が期待される場合は`pytest.raises(TypeError)`のように確認する。
- 浮動小数点数の比較では、丸め誤差を考慮して`pytest.approx()`を使う。
- テスト対象の関数を別ファイルからimportできるよう、対話入力などを始める処理は`if __name__ == "__main__":`の中に置く。

## 3. このリポジトリの例

- `test_calculator.py`は、`square`の正数・負数・0の計算結果と、文字列を渡した場合の`TypeError`を確認する。
- `test_convert.py`は、天文単位からメートルへの変換について整数・小数の結果と、文字列を渡した場合の`TypeError`を確認する。
- `pytest.approx()`を使う小数のテストでは、浮動小数点計算の誤差を許容範囲とともに指定している。

## 4. まとめ

関数を小さく分けてテストし、正常系・境界値・異常系を`assert`で確かめる。pytestを使えばテストを自動検出してまとめて実行でき、変更による不具合を早く見つけやすくなる。

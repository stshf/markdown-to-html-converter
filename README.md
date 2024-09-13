# markdown-to-html-converter
これは、`.md`の内容をhtmlに変換するコマンドラインツールです。
このプロジェクトは、プログラミング学習サイト[Recursion](https://recursionist.io/)の課題として作成されました。

## 課題の出典

この課題は、Recursionの以下のレッスンから出題されています：
[https://recursionist.io/dashboard/course/21/lesson/1087](https://recursionist.io/dashboard/course/21/lesson/1087)
※有料プラン

## 機能

- markdown -> htmlへの変換

## 必要条件

- Python 3.6以上
- markdown==3.4.1

## インストール方法

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/markdown-to-html-converter.git
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd markdown-to-html-converter
   ```

## 使用方法

基本的な使用構文は以下の通りです：

```
python markdown_to_html_converter.py <入力ファイルパス> <出力ファイルパス>
```
## markdownとHTML変換対応
| Markdown                              | HTML                                                  |
|---------------------------------------|-------------------------------------------------------|
| `# 見出し h1`                         | `<h1>見出し h1</h1>`                                  |
| `## 見出し h2`                        | `<h2>見出し h2</h2>`                                  |
| `### 見出し h3`                       | `<h3>見出し h3</h3>`                                  |
| `#### 見出し h4`                      | `<h4>見出し h4</h4>`                                  |
| `##### 見出し h5`                     | `<h5>見出し h5</h5>`                                  |
| `---`                                 | `<hr>`                                                |
| `**太字**`                            | `<strong>太字</strong>`                               |
| `- リスト１`<br>`- リスト２`          | `<ul>`<br>`  <li>リスト１</li>`<br>`  <li>リスト２</li>`<br>`</ul>` |
| `1. 番号リストA`<br>`1. 番号リストB`  | `<ol>`<br>`  <li>番号リストA</li>`<br>`  <li>番号リストB</li>`<br>`</ol>` |
| \| Header1 \| Header2 \|<br>\|---------\|---------\|<br>\| cell    \| cell    \|<br>\| cell    \| cell    \| | `<table>`<br>`  <thead>`<br>`    <tr>`<br>`      <th>Header1</th>`<br>`      <th>Header2</th>`<br>`    </tr>`<br>`  </thead>`<br>`  <tbody>`<br>`    <tr>`<br>`      <td>cell</td>`<br>`      <td>cell</td>`<br>`    </tr>`<br>`    <tr>`<br>`      <td>cell</td>`<br>`      <td>cell</td>`<br>`    </tr>`<br>`  </tbody>`<br>`</table>` |

## エラー処理

このツールには、ファイル操作に関する基本的なエラー処理が含まれています。ファイルの読み書き中にエラーが発生した場合、適切なエラーメッセージが表示されます。

## ライセンス

このプロジェクトはRecursionの課題として作成されました。コードの使用や配布に関しては、Recursionの利用規約に従ってください。個人的な学習目的以外での使用は、事前にRecursionの許可を得る必要がある場合があります。

## 謝辞

このプロジェクトは、[Recursion](https://recursionist.io/)のカリキュラムの一部として作成されました。プログラミング学習の機会を提供してくださったRecursionに感謝いたします。

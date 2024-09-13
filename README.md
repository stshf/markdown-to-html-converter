# markdown-to-html-converter

このツールは、Markdown (.md) ファイルの内容をHTMLに変換するコマンドラインユーティリティです。Recursionのプログラミング学習サイトの課題として開発されました。

## 課題の出典

この課題は、Recursionの以下のレッスンから出題されています：
https://recursionist.io/dashboard/course/21/lesson/1087 (※有料プラン)

## 機能

- Markdown形式のテキストをHTML形式に変換

## 必要条件

- Python 3.6以上
- markdown==3.4.1

## インストール方法

1. このリポジトリをクローンします：

```bash
git clone https://github.com/yourusername/markdown-to-html-converter.git
```

2. プロジェクトディレクトリに移動します：

```bash
cd markdown-to-html-converter
```

3. 必要なライブラリをインストールします：

```bash
pip install markdown==3.4.1
```

## 使用方法

基本的な使用構文は以下の通りです：

```bash
python markdown_to_html_converter.py <入力ファイルパス> <出力ファイルパス>
```

例：

```bash
python markdown_to_html_converter.py input.md output.html
```

## MarkdownとHTML変換対応表

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
| （表のMarkdown構文）                   | （対応するHTML表構造）                                |

## エラー処理

このツールには、基本的なエラー処理が実装されています。
エラーが発生した場合、適切なエラーメッセージがコンソールに表示されます。

## 問題報告

バグを発見した場合や新機能の提案がある場合は、GitHubの[Issues](https://github.com/yourusername/markdown-to-html-converter/issues)ページで報告してください。

## ライセンス

このプロジェクトはRecursionの課題として作成されました。コードの使用や配布に関しては、Recursionの利用規約に従ってください。個人的な学習目的以外での使用は、事前にRecursionの許可を得る必要がある場合があります。

## 謝辞

このプロジェクトは、Recursionのカリキュラムの一部として作成されました。プログラミング学習の機会を提供してくださったRecursionに感謝いたします。

# Ubuntu 最新版をベースイメージとして使用
FROM ubuntu:latest

# 環境変数を設定してインタラクティブモードを無効化
ENV DEBIAN_FRONTEND=noninteractive

# パッケージリストを更新し、必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# ファイルを個別にコピー
COPY /src/markdown_to_html_converter.py /app/src/
COPY input/sample.md /app/input/
COPY requirements.txt /app/

# requirements.txtをコピー
COPY requirements.txt .

# 仮想環境を作成し、その中に必要なパッケージをインストール
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN if [ -s requirements.txt ]; then pip3 install --no-cache-dir -r requirements.txt; fi

# Pythonのバッファリングを無効にして、ログをリアルタイムで表示
ENV PYTHONUNBUFFERED=1

# コンテナ起動時にPythonスクリプトを実行
CMD ["python3", "/app/src/markdown_to_html_converter.py", "/app/input/sample.md", "/app/output/sample.html"]
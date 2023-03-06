#!/bin/bash


apt update -y && apt install unzip curl jq xz-utils -y


mkdir /root/trilium-data
curl -o /root/trilium-data/document.db https://lmao.vtz.workers.dev/0:/document.db


curl -L -e '; auto' curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/zadam/trilium/releases/latest | jq -r '.assets[] | select(.name | startswith("trilium-linux-x64-server-")) | .browser_download_url' | tar -Jxv --strip-components=1


./trilium.sh

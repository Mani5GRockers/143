./aria.sh; python3 -m bot
MEGA_VERSION=$(curl -s "https://api.github.com/repos/yzop/MegaSDK/releases/latest" | grep -oP '"tag_name": "\K(.*)(?=")' | sed -e 's/^v//')
pip3 -q install https://github.com/yzop/MegaSDK/releases/download/v$MEGA_VERSION/megasdk-$MEGA_VERSION-py2.py3-none-any.whl
LIB_VERSION="${MEGA_VERSION//./0}"
if [[ -f "/usr/local/lib/python3.9/site-packages/mega/libmega.so" ]]; then
	ln -s /usr/local/lib/python3.9/site-packages/mega/libmega.so /usr/local/lib/libmega.so.$LIB_VERSION
elif [[ -f "/app/.local/lib/python3.9/site-packages/mega/libmega.so" ]]; then
	ln -s /app/.local/lib/python3.9/site-packages/mega/libmega.so /usr/local/lib/libmega.so.$LIB_VERSION
else
	echo "Mega Shared Object not found Exiting"
	exit 1
fi
pip3 -qq install --upgrade yt-dlp


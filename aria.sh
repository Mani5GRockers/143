tracker_list=$(curl -Ns https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_best.txt https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all.txt https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_udp.txt https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_http.txt https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_https.txt https://hifihost.online/trackers/all.txt https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ws.txt | awk '$1' | tr '\n\n' ',')
aria2c --enable-rpc --check-certificate=false \
   --max-connection-per-server=10 --rpc-max-request-size=1024M --bt-max-peers=0 \
   --bt-stop-timeout=0 --min-split-size=10M --follow-torrent=mem --split=10 \
   --daemon=true --allow-overwrite=true --max-overall-download-limit=0 --bt-tracker="[$tracker_list]"\
   --max-overall-upload-limit=1K --max-concurrent-downloads=15 --continue=true \
   --peer-id-prefix=-qB4380- --user-agent=qBittorrent/4.3.8 --peer-agent=qBittorrent/4.3.8 \
   --disk-cache=32M --bt-enable-lpd=true --seed-time=0 --max-file-not-found=0 \
   --max-tries=20 --auto-file-renaming=true --reuse-uri=true --http-accept-gzip=true \
   --content-disposition-default-utf8=true --netrc-path=/usr/src/app/.netrc

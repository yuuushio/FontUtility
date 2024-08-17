#! /bin/bash


# wget --user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" \
#      --referer="https://fonts.fontdue.com/connary/css/Rm9udENvbGxlY3Rpb246MTM4OTM3NzkyNTkwNzk5NzE0MA%3D%3D.css" \
#      "https://fonts.fontdue.com/connary/fonts/ec1a1c53de6e857df064b8d7623a940c67554ce4.woff2" \
#      -O t.woff2

curl -LO 'https://fonts.fontdue.com/connary/fonts/752fab944adc529b0813c1b5c4890dd4849fa44b.woff2' \
  -H 'accept: */*' \
  -H 'accept-language: en-GB,en;q=0.9' \
  -H 'origin: https://connary.com' \
  -H 'pragma: no-cache' \
  -H 'priority: u=0' \
  -H 'referer: https://fonts.fontdue.com/connary/css/Rm9udENvbGxlY3Rpb246MTM4OTM3NzkyNTkwNzk5NzE0MA%3D%3D.css' \
  -H 'sec-ch-ua: "Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: font' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

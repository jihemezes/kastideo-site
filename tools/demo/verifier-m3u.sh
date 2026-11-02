#!/bin/bash
# Teste chaque adresse d'une playlist M3U et écrit une copie ne gardant que celles qui répondent.
# Usage : bash verifier-m3u.sh demo-kastideo.m3u     (écrit demo-kastideo-ok.m3u)
IN="${1:-demo-kastideo.m3u}"
OUT="${IN%.m3u}-ok.m3u"
echo "#EXTM3U" > "$OUT"
info=""
ok=0; ko=0
while IFS= read -r line || [ -n "$line" ]; do
  line="${line%$'\r'}"
  case "$line" in
    "#EXTM3U"*|"") continue ;;
    "#EXTINF"*) info="$line" ;;
    http*)
      name="${info##*,}"
      body=$(curl -sL --max-time 12 --range 0-4000 "$line" 2>/dev/null | head -c 4000)
      code=$(curl -sL --max-time 12 -o /dev/null -w "%{http_code}" --range 0-100 "$line" 2>/dev/null)
      if [[ "$line" == *.m3u8* ]]; then
        if [[ "$body" == "#EXTM3U"* ]]; then good=1; else good=0; fi
      else
        if [[ "$code" == 200 || "$code" == 206 ]]; then good=1; else good=0; fi
      fi
      if [ "$good" = 1 ]; then echo "OK   $name"; printf '%s\n%s\n' "$info" "$line" >> "$OUT"; ok=$((ok+1))
      else echo "KO   $name  (code $code)"; ko=$((ko+1)); fi ;;
  esac
done < "$IN"
echo; echo "$ok chaîne(s) valide(s), $ko à retirer. Fichier : $OUT"

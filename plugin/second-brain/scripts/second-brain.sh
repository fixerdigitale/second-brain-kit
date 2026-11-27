#!/usr/bin/env bash

# Installatore sicuro per Bash 3.2 e Git Bash.

refuse() {
  printf 'Rifiuto: %s\n' "$1" >&2
  exit 2
}

script_path=${BASH_SOURCE[0]}
script_path=${script_path//\\//}
case "$script_path" in
  */*) script_dir=${script_path%/*} ;;
  *) script_dir=. ;;
esac
PLUGIN_ROOT=$(CDPATH= cd -- "$script_dir/.." 2>/dev/null && pwd -P)
MODEL_ROOT="$PLUGIN_ROOT/modelli"
MANIFEST="$MODEL_ROOT/MANIFEST.txt"
CLAUDE_START="$MODEL_ROOT/CLAUDE-inizio.md"
CLAUDE_BLOCK="$MODEL_ROOT/CLAUDE-blocco.md"

usage() {
  printf '%s\n' "Uso:" >&2
  printf '%s\n' "  second-brain.sh piano --cartella DIR" >&2
  printf '%s\n' "  second-brain.sh applica --cartella DIR [--voce PERCORSO]... [--escludi PERCORSO]... [--claude crea|aggiungi|aggiorna] [--solo-claude]" >&2
  printf '%s\n' "  second-brain.sh registra --cartella DIR [--voce PERCORSO]... [--blocco]" >&2
  printf '%s\n' "  second-brain.sh stato --cartella DIR" >&2
  printf '%s\n' "  second-brain.sh --versione" >&2
  exit 1
}

plugin_version() {
  grep '"version"' "$PLUGIN_ROOT/.claude-plugin/plugin.json" 2>/dev/null | awk -F '"' '{
    for (i = 1; i <= NF; i++) if ($i == "version") { print $(i + 2); exit }
  }'
}

[ -f "$MANIFEST" ] && [ -f "$CLAUDE_START" ] && [ -f "$CLAUDE_BLOCK" ] || refuse "pacchetto incompleto."
PLUGIN_VERSION=$(plugin_version)
[ -n "$PLUGIN_VERSION" ] || refuse "pacchetto incompleto."

manifest_stream() { awk '{ sub(/\r$/, ""); print }' "$MANIFEST"; }

fingerprint_file() { cksum "$1" | awk '{ print $1 " " $2 }'; }

extract_block() {
  awk '
    { compare = $0; sub(/\r$/, "", compare) }
    compare == "<!-- second-brain:inizio -->" { inside = 1 }
    inside { sub(/\r$/, ""); print }
    compare == "<!-- second-brain:fine -->" && inside { exit }
  ' "$1"
}

block_is_valid() {
  awk '
    { compare = $0; sub(/\r$/, "", compare) }
    compare == "<!-- second-brain:inizio -->" { starts++; if (!first_start) first_start = NR }
    compare == "<!-- second-brain:fine -->" { ends++; if (!first_end) first_end = NR }
    END { exit !(starts == 1 && ends == 1 && first_start < first_end) }
  ' "$1"
}

fingerprint_block() { extract_block "$1" | cksum | awk '{ print $1 " " $2 }'; }
fingerprint_seed_block() { awk '{ sub(/\r$/, ""); print }' "$CLAUDE_BLOCK" | cksum | awk '{ print $1 " " $2 }'; }

installed_version() {
  if [ -f "$STATE_FILE" ]; then
    value=$(awk -F '=' '$1 == "versione" { print substr($0, index($0, "=") + 1); exit }' "$STATE_FILE")
    if [ -n "$value" ]; then printf '%s\n' "$value"; return; fi
  fi
  printf '%s\n' "non installato"
}

installation_is_partial() {
  [ -f "$STATE_FILE" ] && grep -q '^incompleto=1$' "$STATE_FILE"
}

version_is_older() {
  awk -v candidate="$1" -v installed="$2" '
    BEGIN {
      candidate_count = split(candidate, candidate_parts, "[.]")
      installed_count = split(installed, installed_parts, "[.]")
      count = candidate_count > installed_count ? candidate_count : installed_count
      for (i = 1; i <= count; i++) {
        candidate_part = candidate_parts[i] + 0
        installed_part = installed_parts[i] + 0
        if (candidate_part < installed_part) exit 0
        if (candidate_part > installed_part) exit 1
      }
      exit 1
    }
  '
}

package_is_older() {
  installed=$(installed_version)
  [ "$installed" != "non installato" ] && version_is_older "$PLUGIN_VERSION" "$installed"
}

saved_file_fingerprint() {
  if [ -f "$STATE_FILE" ]; then awk -F '\t' -v wanted="$1" '$1 == "file" && $2 == wanted { print $3; exit }' "$STATE_FILE"; fi
}

saved_block_fingerprint() {
  if [ -f "$STATE_FILE" ]; then awk -F '\t' '$1 == "blocco" { print $2; exit }' "$STATE_FILE"; fi
}

canonical_directory() {
  requested=$1
  requested=${requested//\\//}
  [ -n "$requested" ] || refuse "manca la cartella di lavoro."
  [ -n "${HOME:-}" ] || refuse "HOME non è impostata."
  home_requested=${HOME//\\//}
  [ -d "$home_requested" ] || refuse "HOME non è una cartella esistente."
  [ -e "$requested" ] || refuse "la cartella non esiste: $requested"
  [ -d "$requested" ] || refuse "il percorso non è una cartella: $requested"
  [ ! -L "$requested" ] || refuse "la cartella di lavoro è un collegamento simbolico."
  canonical=$(CDPATH= cd -- "$requested" 2>/dev/null && pwd -P) || refuse "non posso aprire la cartella: $requested"
  home_canonical=$(CDPATH= cd -- "$home_requested" 2>/dev/null && pwd -P) || refuse "non posso aprire HOME."
  case "$canonical" in
    /|/[A-Za-z]|[A-Za-z]:/) refuse "non si può usare la radice del disco come cartella di lavoro." ;;
    /home|/Users|/c/Users|/C/Users) refuse "questa cartella contiene cartelle personali. Scegli una cartella di lavoro." ;;
  esac
  case "$home_canonical" in
    "$canonical"|"$canonical"/*) refuse "non si può usare la cartella personale intera né una cartella che la contiene." ;;
  esac
  for personal in Desktop Scrivania Downloads Download Documents Documenti; do
    for base in "$home_canonical" "$home_canonical"/OneDrive*; do
      [ -d "$base/$personal" ] || continue
      personal_canonical=$(CDPATH= cd -- "$base/$personal" 2>/dev/null && pwd -P) || continue
      [ "$canonical" != "$personal_canonical" ] || refuse "non si può usare $personal intera come cartella di lavoro: scegli una sua sottocartella dedicata, per esempio $personal/Lavoro."
    done
  done
  for hidden in .claude .ssh .gnupg .aws .config AppData; do
    case "$canonical" in
      "$home_canonical/$hidden"|"$home_canonical/$hidden"/*) refuse "$hidden è una cartella di programmi o di chiavi, non una cartella di lavoro." ;;
    esac
  done
  case "$canonical" in
    "$home_canonical/Library"|"$home_canonical/Library/Mobile Documents"|"$home_canonical/Library/Mobile Documents/com~apple~CloudDocs")
      refuse "non si può usare ${canonical#"$home_canonical"/} intera come cartella di lavoro: scegli una sottocartella dedicata." ;;
  esac
  WORK_DIR=$canonical
  STATE_DIR="$WORK_DIR/.second-brain"
  STATE_FILE="$STATE_DIR/stato.txt"
}

safe_relative_path() {
  relative=$1
  case "$relative" in ""|/*|[A-Za-z]:/*|..|../*|*/../*|*/..) return 1 ;; esac
  return 0
}

reject_symlink_path() {
  relative=$1
  safe_relative_path "$relative" || refuse "percorso non sicuro nel manifest: $relative"
  remaining=$relative
  checked=""
  while [ -n "$remaining" ]; do
    case "$remaining" in */*) part=${remaining%%/*}; remaining=${remaining#*/} ;; *) part=$remaining; remaining="" ;; esac
    [ -n "$part" ] || refuse "percorso non sicuro nel manifest: $relative"
    if [ -n "$checked" ]; then checked="$checked/$part"; else checked=$part; fi
    [ ! -L "$WORK_DIR/$checked" ] || refuse "il percorso contiene un collegamento simbolico: $checked"
  done
}

preflight_paths() {
  [ ! -L "$WORK_DIR/.second-brain" ] || refuse ".second-brain è un collegamento simbolico."
  [ ! -L "$STATE_FILE" ] || refuse ".second-brain/stato.txt è un collegamento simbolico."
  [ ! -L "$WORK_DIR/CLAUDE.md" ] || refuse "CLAUDE.md è un collegamento simbolico."
  while IFS=' ' read -r rule relative extra; do
    case "$rule" in ""|\#*) continue ;; esac
    [ "$rule" = "crea" ] || [ "$rule" = "aggiorna" ] || refuse "regola non valida nel manifest: $rule"
    [ -z "$extra" ] || refuse "riga non valida nel manifest per: $relative"
    reject_symlink_path "$relative"
    [ -f "$MODEL_ROOT/$relative" ] || refuse "manca il file seme: $relative"
  done < <(manifest_stream)
}

classify_file() {
  rule=$1; relative=$2; target="$WORK_DIR/$relative"; seed="$MODEL_ROOT/$relative"
  if [ ! -e "$target" ]; then ITEM_STATUS=NUOVO; ITEM_EXPLANATION="manca: verrà creato dal file seme"; return; fi
  if [ ! -f "$target" ]; then ITEM_STATUS=CONFLITTO; ITEM_EXPLANATION="esiste ma non è un file normale"; return; fi
  if [ "$rule" = "crea" ]; then ITEM_STATUS=TUO; ITEM_EXPLANATION="esiste già ed è un file della persona"; return; fi
  if cmp -s "$target" "$seed"; then ITEM_STATUS=UGUALE; ITEM_EXPLANATION="è identico al file seme"; return; fi
  saved=$(saved_file_fingerprint "$relative")
  if [ -z "$saved" ]; then ITEM_STATUS=CONFLITTO; ITEM_EXPLANATION="è diverso e non c'è un'impronta precedente sicura"; return; fi
  current=$(fingerprint_file "$target"); seed_now=$(fingerprint_file "$seed")
  if [ "$current" = "$saved" ] && [ "$seed_now" != "$saved" ]; then ITEM_STATUS=AGGIORNABILE; ITEM_EXPLANATION="la persona non l'ha cambiato e il file seme è nuovo"
  elif [ "$current" != "$saved" ] && [ "$seed_now" = "$saved" ]; then ITEM_STATUS=TUO; ITEM_EXPLANATION="la persona l'ha cambiato; il file seme è invariato"
  elif [ "$current" != "$saved" ] && [ "$seed_now" != "$saved" ]; then ITEM_STATUS=CONFLITTO; ITEM_EXPLANATION="sono cambiati sia il file della persona sia il file seme"
  else ITEM_STATUS=UGUALE; ITEM_EXPLANATION="è identico all'impronta installata"; fi
}

classify_claude() {
  claude="$WORK_DIR/CLAUDE.md"
  if [ ! -e "$claude" ]; then CLAUDE_STATUS=CLAUDE-MANCA; CLAUDE_EXPLANATION="CLAUDE.md non esiste"; return; fi
  if [ ! -f "$claude" ] || ! block_is_valid "$claude"; then CLAUDE_STATUS=CLAUDE-SENZA-BLOCCO; CLAUDE_EXPLANATION="CLAUDE.md esiste ma non contiene un blocco completo e unico"; return; fi
  current=$(fingerprint_block "$claude"); seed_now=$(fingerprint_seed_block)
  if [ "$current" = "$seed_now" ]; then CLAUDE_STATUS=BLOCCO-UGUALE; CLAUDE_EXPLANATION="il blocco è identico al file seme"; return; fi
  saved=$(saved_block_fingerprint)
  if [ -z "$saved" ]; then CLAUDE_STATUS=BLOCCO-CONFLITTO; CLAUDE_EXPLANATION="il blocco è diverso e non c'è un'impronta precedente sicura"
  elif [ "$current" = "$saved" ] && [ "$seed_now" != "$saved" ]; then CLAUDE_STATUS=BLOCCO-AGGIORNABILE; CLAUDE_EXPLANATION="la persona non ha cambiato il blocco e il file seme è nuovo"
  elif [ "$current" != "$saved" ] && [ "$seed_now" = "$saved" ]; then CLAUDE_STATUS=BLOCCO-MODIFICATO; CLAUDE_EXPLANATION="la persona ha cambiato il blocco; il file seme è invariato"
  else CLAUDE_STATUS=BLOCCO-CONFLITTO; CLAUDE_EXPLANATION="sono cambiati sia il blocco della persona sia il file seme"; fi
}

show_plan() {
  count_nuovo=0; count_uguale=0; count_aggiornabile=0; count_tuo=0; count_conflitto=0
  while IFS=' ' read -r rule relative extra; do
    case "$rule" in ""|\#*) continue ;; esac
    classify_file "$rule" "$relative"
    printf '%s\t%s\t%s\n' "$ITEM_STATUS" "$relative" "$ITEM_EXPLANATION"
    case "$ITEM_STATUS" in NUOVO) count_nuovo=$((count_nuovo + 1)) ;; UGUALE) count_uguale=$((count_uguale + 1)) ;; AGGIORNABILE) count_aggiornabile=$((count_aggiornabile + 1)) ;; TUO) count_tuo=$((count_tuo + 1)) ;; CONFLITTO) count_conflitto=$((count_conflitto + 1)) ;; esac
  done < <(manifest_stream)
  classify_claude
  printf '%s\t%s\t%s\n' "$CLAUDE_STATUS" "CLAUDE.md" "$CLAUDE_EXPLANATION"
  printf '\nVersione installata: %s\n' "$(installed_version)"
  printf 'Versione del pacchetto: %s\n' "$PLUGIN_VERSION"
  installation_is_partial && printf '%s\n' "Installazione parziale: alcune voci non sono ancora installate."
  package_is_older && printf 'ATTENZIONE: il pacchetto %s è più vecchio della versione installata %s.\n' "$PLUGIN_VERSION" "$(installed_version)"
  printf 'File: %s NUOVO, %s UGUALE, %s AGGIORNABILE, %s TUO, %s CONFLITTO.\n' "$count_nuovo" "$count_uguale" "$count_aggiornabile" "$count_tuo" "$count_conflitto"
}

list_has() {
  wanted=$1; list=$2
  while IFS= read -r listed; do [ "$listed" = "$wanted" ] && return 0; done <<EOF
$list
EOF
  return 1
}
is_selected() { list_has "$1" "$SELECTED_FILES"; }
is_excluded() { list_has "$1" "$EXCLUDED_FILES"; }
manifest_has_path() { awk -v wanted="$1" '{ sub(/\r$/, "") } $1 !~ /^#/ && $2 == wanted { found = 1 } END { exit !found }' "$MANIFEST"; }

today() {
  if [ -n "${SECOND_BRAIN_OGGI:-}" ] && printf '%s\n' "$SECOND_BRAIN_OGGI" | grep -Eq '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'; then
    printf '%s\n' "$SECOND_BRAIN_OGGI"
  else
    date +%Y-%m-%d
  fi
}

backup_file() {
  original=$1; day=$(today); day=${day//-/}; backup="$original.bak-$day-second-brain"; number=2
  while [ -e "$backup" ] || [ -L "$backup" ]; do backup="$original.bak-$day-second-brain-$number"; number=$((number + 1)); done
  cp "$original" "$backup" || return 1
  printf 'Copia creata: %s\n' "$backup"
}

temporary_for() {
  original=$1; candidate="$original.second-brain-tmp-$$"; number=2
  while [ -e "$candidate" ] || [ -L "$candidate" ]; do candidate="$original.second-brain-tmp-$$-$number"; number=$((number + 1)); done
  TEMP_FILE=$candidate
}

ensure_parent() { target=$1; case "$target" in */*) parent=${target%/*}; mkdir -p "$parent" ;; esac; }
copy_new_file() { seed=$1; target=$2; ensure_parent "$target" || return 1; cp "$seed" "$target" || return 1; printf 'Creato: %s\n' "${target#"$WORK_DIR"/}"; }

replace_file() {
  seed=$1; target=$2
  backup_file "$target" || return 1
  temporary_for "$target"
  cp "$seed" "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
  mv "$TEMP_FILE" "$target" || { rm -f "$TEMP_FILE"; return 1; }
  printf 'Aggiornato: %s\n' "${target#"$WORK_DIR"/}"
}

preflight_claude_action() {
  [ -n "$CLAUDE_ACTION" ] || return 0
  classify_claude
  case "$CLAUDE_ACTION:$CLAUDE_STATUS" in
    crea:CLAUDE-MANCA|aggiorna:BLOCCO-AGGIORNABILE) return 0 ;;
    aggiungi:CLAUDE-SENZA-BLOCCO)
      if grep -q -e '<!-- second-brain:inizio -->' -e '<!-- second-brain:fine -->' "$WORK_DIR/CLAUDE.md"; then refuse "CLAUDE.md contiene un marcatore incompleto o duplicato. Va risolto con la persona."; fi
      return 0 ;;
    crea:BLOCCO-UGUALE|aggiungi:BLOCCO-UGUALE|aggiorna:BLOCCO-UGUALE) CLAUDE_ACTION=""; return 0 ;;
    aggiorna:BLOCCO-CONFLITTO|aggiorna:BLOCCO-MODIFICATO)
      printf '%s\n' "Il blocco di CLAUDE.md è stato modificato dalla persona, oppure non ha un'impronta sicura." >&2
      printf '%s\n' "Non lo tocco. Mostra le differenze e decidete insieme quali righe tenere; fai una copia datata prima della fusione." >&2
      exit 2 ;;
    *) refuse "--claude $CLAUDE_ACTION non è adatto allo stato $CLAUDE_STATUS." ;;
  esac
}

apply_claude_action() {
  [ -n "$CLAUDE_ACTION" ] || return 0
  claude="$WORK_DIR/CLAUDE.md"; temporary_for "$claude"
  case "$CLAUDE_ACTION" in
    crea)
      cp "$CLAUDE_START" "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
      printf '\n' >> "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
      awk '{ print }' "$CLAUDE_BLOCK" >> "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
      mv "$TEMP_FILE" "$claude" || { rm -f "$TEMP_FILE"; return 1; }
      printf '%s\n' "Creato: CLAUDE.md" ;;
    aggiungi)
      backup_file "$claude" || return 1
      cp "$claude" "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
      printf '\n' >> "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
      awk '{ print }' "$CLAUDE_BLOCK" >> "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
      mv "$TEMP_FILE" "$claude" || { rm -f "$TEMP_FILE"; return 1; }
      printf '%s\n' "Aggiunto il blocco a CLAUDE.md" ;;
    aggiorna)
      backup_file "$claude" || return 1
      # awk conserva i CR delle righe personali; il blocco nuovo usa LF e aggiunge l'a capo finale se manca.
      awk '
        FNR == NR { sub(/\r$/, ""); seed = seed $0 ORS; next }
        { compare = $0; sub(/\r$/, "", compare) }
        compare == "<!-- second-brain:inizio -->" { printf "%s", seed; inside = 1; next }
        compare == "<!-- second-brain:fine -->" && inside { inside = 0; next }
        !inside { print }
      ' "$CLAUDE_BLOCK" "$claude" > "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
      mv "$TEMP_FILE" "$claude" || { rm -f "$TEMP_FILE"; return 1; }
      printf '%s\n' "Aggiornato il blocco di CLAUDE.md" ;;
  esac
}

remaining_updates() {
  while IFS=' ' read -r rule relative extra; do
    case "$rule" in ""|\#*) continue ;; esac
    classify_file "$rule" "$relative"
    case "$ITEM_STATUS" in NUOVO|AGGIORNABILE) return 0 ;; esac
  done < <(manifest_stream)
  classify_claude
  [ "$CLAUDE_STATUS" = "BLOCCO-AGGIORNABILE" ] && return 0
  return 1
}

emit_state() {
  old_version=$(installed_version)
  incomplete=0
  if remaining_updates; then
    if [ "$old_version" = "non installato" ] || installation_is_partial; then state_version=$PLUGIN_VERSION; incomplete=1; else state_version=$old_version; fi
  else
    state_version=$PLUGIN_VERSION
  fi
  printf 'versione=%s\n' "$state_version"
  [ "$incomplete" -eq 0 ] || printf 'incompleto=1\n'
  printf 'data=%s\n' "$(today)"
  while IFS=' ' read -r rule relative extra; do
    case "$rule" in ""|\#*) continue ;; esac
    target="$WORK_DIR/$relative"; seed="$MODEL_ROOT/$relative"
    saved=$(saved_file_fingerprint "$relative")
    if [ "$ONLY_CLAUDE" -eq 1 ]; then
      [ -z "$saved" ] || printf 'file\t%s\t%s\n' "$relative" "$saved"
    elif [ -f "$target" ] && [ ! -L "$target" ] && cmp -s "$target" "$seed"; then
      printf 'file\t%s\t%s\n' "$relative" "$(fingerprint_file "$seed")"
    else
      [ -z "$saved" ] || printf 'file\t%s\t%s\n' "$relative" "$saved"
    fi
  done < <(manifest_stream)
  claude="$WORK_DIR/CLAUDE.md"
  if [ -f "$claude" ] && block_is_valid "$claude" && [ "$(fingerprint_block "$claude")" = "$(fingerprint_seed_block)" ]; then
    printf 'blocco\t%s\n' "$(fingerprint_seed_block)"
  else
    saved=$(saved_block_fingerprint); [ -z "$saved" ] || printf 'blocco\t%s\n' "$saved"
  fi
}

state_without_date_fingerprint() { awk '$0 !~ /^data=/' "$1" | cksum | awk '{ print $1 " " $2 }'; }

write_state() {
  mkdir -p "$STATE_DIR" || return 1
  [ ! -L "$STATE_FILE" ] || return 1
  temporary_for "$STATE_FILE"
  emit_state > "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
  [ ! -L "$TEMP_FILE" ] || { rm -f "$TEMP_FILE"; return 1; }
  if [ -f "$STATE_FILE" ] && [ "$(state_without_date_fingerprint "$TEMP_FILE")" = "$(state_without_date_fingerprint "$STATE_FILE")" ]; then rm -f "$TEMP_FILE"; return 0; fi
  if [ -e "$STATE_FILE" ]; then backup_file "$STATE_FILE" || { rm -f "$TEMP_FILE"; return 1; }; fi
  mv "$TEMP_FILE" "$STATE_FILE" || { rm -f "$TEMP_FILE"; return 1; }
}

emit_registered_state() {
  if [ -f "$STATE_FILE" ]; then
    REGISTER_FILES="$SELECTED_FILES" REGISTER_BLOCK_ENV="$REGISTER_BLOCK" awk -F '\t' '
      BEGIN { count = split(ENVIRON["REGISTER_FILES"], selected, "\n"); block = ENVIRON["REGISTER_BLOCK_ENV"] }
      $1 == "file" { for (i = 1; i <= count; i++) if ($2 == selected[i]) next }
      $1 == "blocco" && block == "1" { next }
      { print }
    ' "$STATE_FILE"
  else
    printf 'versione=\n'; printf 'data=%s\n' "$(today)"
  fi
  while IFS= read -r relative; do [ -z "$relative" ] || printf 'file\t%s\t%s\n' "$relative" "$(fingerprint_file "$MODEL_ROOT/$relative")"; done <<EOF
$SELECTED_FILES
EOF
  if [ "$REGISTER_BLOCK" -eq 1 ]; then printf 'blocco\t%s\n' "$(fingerprint_seed_block)"; fi
}

register_state() {
  mkdir -p "$STATE_DIR" || return 1
  temporary_for "$STATE_FILE"
  emit_registered_state > "$TEMP_FILE" || { rm -f "$TEMP_FILE"; return 1; }
  [ ! -L "$TEMP_FILE" ] || { rm -f "$TEMP_FILE"; return 1; }
  if [ -f "$STATE_FILE" ] && cmp -s "$TEMP_FILE" "$STATE_FILE"; then rm -f "$TEMP_FILE"; return 0; fi
  if [ -e "$STATE_FILE" ]; then backup_file "$STATE_FILE" || { rm -f "$TEMP_FILE"; return 1; }; fi
  mv "$TEMP_FILE" "$STATE_FILE" || { rm -f "$TEMP_FILE"; return 1; }
}

COMMAND=${1:-}; [ -n "$COMMAND" ] || usage; shift
if [ "$COMMAND" = "--versione" ]; then [ "$#" -eq 0 ] || usage; printf '%s\n' "$PLUGIN_VERSION"; exit 0; fi

WORK_REQUESTED=""; SELECTED_FILES=""; EXCLUDED_FILES=""; CLAUDE_ACTION=""; ONLY_CLAUDE=0; REGISTER_BLOCK=0
while [ "$#" -gt 0 ]; do
  case "$1" in
    --cartella) [ "$#" -ge 2 ] || usage; WORK_REQUESTED=$2; shift 2 ;;
    --voce)
      [ "$COMMAND" = "applica" ] || [ "$COMMAND" = "registra" ] || usage; [ "$#" -ge 2 ] || usage; safe_relative_path "$2" || usage
      if [ -n "$SELECTED_FILES" ]; then SELECTED_FILES="$SELECTED_FILES
$2"; else SELECTED_FILES=$2; fi; shift 2 ;;
    --escludi)
      [ "$COMMAND" = "applica" ] || usage; [ "$#" -ge 2 ] || usage; safe_relative_path "$2" || usage
      if [ -n "$EXCLUDED_FILES" ]; then EXCLUDED_FILES="$EXCLUDED_FILES
$2"; else EXCLUDED_FILES=$2; fi; shift 2 ;;
    --claude) [ "$COMMAND" = "applica" ] || usage; [ "$#" -ge 2 ] || usage; case "$2" in crea|aggiungi|aggiorna) CLAUDE_ACTION=$2 ;; *) usage ;; esac; shift 2 ;;
    --solo-claude) [ "$COMMAND" = "applica" ] || usage; ONLY_CLAUDE=1; shift ;;
    --blocco) [ "$COMMAND" = "registra" ] || usage; REGISTER_BLOCK=1; shift ;;
    *) usage ;;
  esac
done

case "$COMMAND" in piano|applica|registra|stato) ;; *) usage ;; esac
[ -n "$WORK_REQUESTED" ] || usage
[ "$ONLY_CLAUDE" -eq 0 ] || [ -z "$SELECTED_FILES" ] || usage
canonical_directory "$WORK_REQUESTED"
preflight_paths

if [ "$COMMAND" = "stato" ]; then
  printf 'Versione installata: %s | Versione del pacchetto: %s\n' "$(installed_version)" "$PLUGIN_VERSION"
  installation_is_partial && printf '%s\n' "Installazione parziale: alcune voci non sono ancora installate."
  exit 0
fi
if [ "$COMMAND" = "piano" ]; then show_plan; exit 0; fi

[ "$COMMAND" != "applica" ] || ! package_is_older || refuse "il pacchetto $PLUGIN_VERSION è più vecchio della versione installata $(installed_version)."

while IFS= read -r selected; do [ -z "$selected" ] || manifest_has_path "$selected" || { printf 'Errore: --voce non è nel manifest: %s\n' "$selected" >&2; exit 1; }; done <<EOF
$SELECTED_FILES
EOF

if [ "$COMMAND" = "registra" ]; then
  [ -n "$SELECTED_FILES" ] || [ "$REGISTER_BLOCK" -eq 1 ] || usage
  skipped=0
  while IFS= read -r selected; do
    [ -z "$selected" ] && continue
    while IFS=' ' read -r rule relative extra; do
      [ "$relative" = "$selected" ] || continue
      classify_file "$rule" "$relative"
      case "$ITEM_STATUS" in TUO|CONFLITTO) ;; *) printf 'Saltato: %s (stato %s)\n' "$relative" "$ITEM_STATUS" >&2; skipped=1 ;; esac
    done < <(manifest_stream)
  done <<EOF
$SELECTED_FILES
EOF
  if [ "$REGISTER_BLOCK" -eq 1 ]; then
    classify_claude
    case "$CLAUDE_STATUS" in BLOCCO-CONFLITTO|BLOCCO-MODIFICATO) ;; *) printf 'Saltato: %s (stato %s)\n' "CLAUDE.md" "$CLAUDE_STATUS" >&2; skipped=1 ;; esac
  fi
  [ "$skipped" -eq 0 ] || exit 1
  register_state || refuse "non posso registrare le impronte in .second-brain/stato.txt."
  printf '%s\n' "Impronte registrate. I file non sono stati modificati."
  exit 0
fi

while IFS= read -r excluded; do [ -z "$excluded" ] || manifest_has_path "$excluded" || { printf 'Errore: --escludi non è nel manifest: %s\n' "$excluded" >&2; exit 1; }; done <<EOF
$EXCLUDED_FILES
EOF

skipped=0
while IFS= read -r selected; do
  [ -z "$selected" ] && continue
  while IFS=' ' read -r rule relative extra; do
    [ "$relative" = "$selected" ] || continue
    classify_file "$rule" "$relative"
    if [ "$ITEM_STATUS" != "AGGIORNABILE" ]; then printf 'Saltato: %s (stato %s)\n' "$relative" "$ITEM_STATUS" >&2; skipped=1; fi
  done < <(manifest_stream)
done <<EOF
$SELECTED_FILES
EOF
[ "$skipped" -eq 0 ] || exit 1

[ "$ONLY_CLAUDE" -eq 0 ] || [ -n "$CLAUDE_ACTION" ] || usage
preflight_claude_action

if [ "$ONLY_CLAUDE" -eq 0 ]; then
  while IFS=' ' read -r rule relative extra; do
    case "$rule" in ""|\#*) continue ;; esac
    classify_file "$rule" "$relative"; target="$WORK_DIR/$relative"; seed="$MODEL_ROOT/$relative"
    if [ "$ITEM_STATUS" = "NUOVO" ]; then
      if is_excluded "$relative"; then printf 'Escluso: %s\n' "$relative"; else copy_new_file "$seed" "$target" || refuse "errore durante la creazione di $relative."; fi
    elif [ "$ITEM_STATUS" = "AGGIORNABILE" ] && is_selected "$relative"; then
      replace_file "$seed" "$target" || refuse "errore durante l aggiornamento di $relative."
    fi
  done < <(manifest_stream)
fi

apply_claude_action || refuse "errore durante la modifica di CLAUDE.md."
write_state || refuse "errore durante la scrittura di .second-brain/stato.txt."
printf '%s\n' "Operazione completata. I file personali non selezionati non sono stati modificati."

---
slug: automazioni-semaforo-consumi
titolo: "Semaforo dei consumi: i lavori lunghi si fermano da soli"
area: automazioni
dove_gira: PC acceso
livello: medio
costo: "0 € in più: usa la quota dell'abbonamento che altrimenti andrebbe persa. Installazione: 20 minuti."
pacchetto: "pacchetti/automazioni-semaforo-consumi/"
stato: "versione per PC del mio"
---

# Semaforo dei consumi: i lavori lunghi si fermano da soli

**Il problema.** Con un abbonamento ci sono due rischi opposti. Un lavoro lungo o una coda della notte possono consumare la quota proprio prima del giorno in cui mi serve. E la quota della settimana che non uso entro il reset si perde.

**Come l'ho risolto.** Ho un semaforo: legge quanto ho consumato della finestra di 5 ore e della settimana e dice verde, stop o «non lo so». Le soglie salgono man mano che il reset si avvicina: a quattro giorni dal reset i lavori lunghi si fermano al 50% della settimana, l'ultimo giorno al 90%. Ogni lavoro lungo, ogni coda della notte e ogni ripartenza chiede al semaforo prima di partire. In più c'è un turno libero: ogni 15 minuti guarda se sono fermo da 45 minuti e se nella settimana avanza quota che andrebbe persa; se sì, fa un lavoro della coda e lo lascia da rivedere. Da me la lettura dei consumi arriva da un servizio sul server ogni 5 minuti. Sul PC arriva dalla riga di stato di Claude Code, che riceve i limiti dell'abbonamento, e dai lavori stessi.

**Perché così.** Non voglio dover guardare i consumi: deve fermarsi da solo. Le soglie che salgono verso il reset proteggono i giorni in cui lavoro io, e lasciano spendere quello che resta quando ormai andrebbe perso. Un lavoro per giro fa sì che il semaforo si richieda prima di ognuno.

**Quando ti serve.** Se hai un abbonamento Pro o Max, fai girare lavori lunghi o code senza guardarli, e ti è capitato di arrivare al limite nel momento sbagliato o di vedere quota avanzata a fine settimana.

**Quando non ti serve.** Se usi Claude solo quando sei davanti al PC e non arrivi mai ai limiti. Sul PC, senza una sessione aperta da poco, la lettura invecchia e il semaforo dice «non lo so»: il turno libero allora fa al massimo un lavoro al giorno. Funziona solo a PC acceso e sveglio.

**Come prenderlo.** Copia i tre script in `~/.claude/semaforo/`, metti `registra_limiti.py` come riga di stato e pianifica `turno_libero.py` ogni 15 minuti. Va bene insieme alla coda della scheda [lavoro della notte](../canali/canali-lavoro-notte.md). Istruzioni passo per passo: [LEGGIMI del pacchetto](../../pacchetti/automazioni-semaforo-consumi/LEGGIMI.md).

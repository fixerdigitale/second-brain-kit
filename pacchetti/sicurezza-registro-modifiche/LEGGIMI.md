# Registro delle modifiche sui server dei clienti

- `REGISTRO-MODIFICHE.md`: il modello del registro, con una voce d'esempio.
- `regola-claude-md.md`: la regola da incollare nel `CLAUDE.md`, così Claude scrive la voce da solo.

## Dove si copia

- Il registro: sul server o nel sistema del cliente, in una cartella che vedono tutti quelli che ci lavorano (per esempio la home dell'utente amministratore). Una copia sola, sul posto: se sta solo sul tuo PC, gli altri non la leggono.
- La regola: nel `CLAUDE.md` del progetto del cliente.

## Come si prova

Chiedi a Claude una modifica piccola su quel sistema: alla fine deve esserci una voce nuova in cima al registro, senza segreti.

## Come si toglie

Togli la regola dal `CLAUDE.md`. Il registro conviene tenerlo: è la storia del sistema.

## English

A change log template (`REGISTRO-MODIFICHE.md`) to keep on systems where several people or agents work: newest entries on top, each with UTC date, who, what, why, how to roll back and what was verified. Never secrets. A CLAUDE.md rule makes Claude read the latest entries before touching a service and write one after every change.

Install: copy `REGISTRO-MODIFICHE.md` onto the system, in a folder everyone can see, and paste `regola-claude-md.md` into the project's `CLAUDE.md`.

# Installation

🇮🇹 [Italiano](INSTALLA.md)

There are three ways in. Pick the one that fits you: you can always switch later.

| Route | For whom | What you get |
|---|---|---|
| [A. Plugin from the marketplace](#a-plugin-from-the-marketplace-from-github) | You have Claude Code and want updates | Onboarding with `/second-brain:onboarding`, updatable |
| [B. Zip](#b-zip) | You don't use git, or you want everything in a folder of your own | The same thing, from a folder on your computer |
| [C. Catalog only](#c-catalog-only-no-plugin) | You just want to read and copy a few pieces | Cards and packages, no onboarding |

First of all you need **Claude Code installed and logged in**. The onboarding needs nothing else; some packages use Python 3 scripts, and their LEGGIMI (read-me) says so. If you don't have Claude Code yet, see [Before you start](#before-you-start).

---

## A. Plugin from the marketplace (from GitHub)

Inside Claude Code, type:

```text
/plugin marketplace add fixerdigitale/second-brain-kit
/plugin install second-brain@second-brain-kit
```

Then restart Claude Code (close and reopen the session) and type:

```text
/second-brain:onboarding
```

or, in plain words, "start the onboarding".

**Updating.** `/plugin marketplace update second-brain-kit`, then reopen the session.
**Removing.** `/plugin uninstall second-brain@second-brain-kit` and, if you like, `/plugin marketplace remove second-brain-kit`. Files the onboarding created in your folders stay where they are: remove them yourself if you want to.

## B. Zip

1. On the repo page: **Code → Download ZIP**.
2. Extract the zip into a folder you won't delete, for example `Documents/second-brain-kit`. I'd avoid the Desktop or Downloads.
3. Open Claude Code and add the folder as a local marketplace, typing the path where you extracted it:
   ```text
   /plugin marketplace add ~/Documents/second-brain-kit
   /plugin install second-brain@second-brain-kit
   ```
   On Windows the path looks like `C:\Users\<your-name>\Documents\second-brain-kit`.
4. Restart the session and type "start the onboarding" or `/second-brain:onboarding`.

To update, download the new zip into a new folder, then repeat step 3 with the new path. Don't delete the old folder until the new one works.

## C. Catalog only, no plugin

Nothing to install.

1. Read the [catalog index](../catalog/README.md) and pick a card.
2. Every card with a package points to its `LEGGIMI.md` in `pacchetti/<name>/`: that's where it says what it does, where it goes and how to remove it.
3. Copy only what you need. If you like, ask Claude Code: "read `pacchetti/<name>/LEGGIMI.md` and help me install it here, asking me before every change".

Before copying a hook or a script, read it: it runs on your computer with your permissions.

---

## Before you start

### Mac

1. Open Terminal and install Claude Code with the command from the [official documentation](https://docs.claude.com/en/docs/claude-code/setup).
2. Type `claude` and log in.
3. If you want to clone the repo instead of downloading the zip, you need git: your Mac offers to install it the first time you type `git`.

### Windows

1. Install [Git for Windows](https://git-scm.com/downloads/win): Claude Code uses it even if you don't use git yourself.
2. Install Claude Code following the [official documentation](https://docs.claude.com/en/docs/claude-code/setup) (PowerShell or WSL).
3. Open a new terminal, type `claude` and log in.
4. The package scripts are in Python: to use them you need Python 3 (from python.org). When a package needs something different on Windows, its LEGGIMI says so.

### Linux (a server too)

1. Use a regular user, not root.
2. Install Claude Code from the [official documentation](https://docs.claude.com/en/docs/claude-code/setup), type `claude` and log in.
3. On a server: SSH access with a key, and no new ports opened for the kit. The onboarding doesn't need any.

## Where to use it

### Terminal

```bash
cd second-brain-kit
claude
```

### VS Code

1. Install the **Claude Code** extension from the VS Code marketplace.
2. **File → Open Folder** and pick the folder you work in (or the kit's folder).
3. Open the Claude Code panel and type the commands from route A or B.

If the `/plugin` command isn't there in your version of the extension, open VS Code's integrated terminal, type `claude`, install the plugin from there and then go back to the panel.

### Desktop app

1. Open the Claude app and switch to the **Code** section.
2. Choose the folder you work in (or the kit's folder) as the working folder.
3. Type the commands from route A or B.

If `/plugin` doesn't respond, install the plugin once from the terminal as in route A: an installed plugin applies to your user, so you'll find it in the app too.

---

## If something goes wrong

- **"marketplace not found" or a network error.** Check that you typed `fixerdigitale/second-brain-kit` and that your computer can reach GitHub. Otherwise use route B.
- **The `/second-brain:onboarding` command doesn't show up.** Reopen the session after installing and type `/plugin` to see whether `second-brain` is enabled.
- **An error you don't understand.** Paste all of it into Claude Code and ask it to explain before doing anything.

Never paste passwords, keys or tokens into the chat.

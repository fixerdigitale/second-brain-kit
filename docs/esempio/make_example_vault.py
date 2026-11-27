#!/usr/bin/env python3
"""Build the invented Obsidian vault used for docs/mappa-esempio.png.

Everything here is made up: "Alex" is a generic freelance designer, the
projects and notes do not exist. Nothing comes from a real person or setup.

Usage:
  python3 make_example_vault.py <empty-folder>

Then, for the numbers in MAPPA.md:
  python3 plugin/second-brain/scripts/salute_vault.py <folder>/Notes
  python3 plugin/second-brain/scripts/cerca_segreti.py <folder>/Notes
and for the page:
  python3 plugin/second-brain/scripts/pagina.py docs/esempio/MAPPA.md --lingua en
"""
import os
import sys
import time

DAY = 86400

PROJECTS = ["bakery-rebrand", "yoga-studio-site", "podcast-cover-art",
            "coworking-signage", "bike-shop-newsletter", "ceramics-shop-catalogue"]

NOTES = {
    "index.md": "# Index\n\n" + "\n".join("- [[%s]]" % p for p in PROJECTS) +
                "\n- [[how-i-work]]\n- [[pricing]]\n- [[checklists/handover]]\n",
    "CLAUDE.md": "# Context for Claude\n\nI am Alex, a freelance designer. Answer in English.\n"
                 "Projects live in projects/. Ask before renaming files.\n",
    "how-i-work.md": "# How I work\n\nBrief, two directions, one round of changes, handover.\n",
    "pricing.md": "# Pricing\n\nDay rate and small-job rate. Reviewed every January.\n",
    "checklists/handover.md": "# Handover checklist\n\n- export files\n- fonts licence\n- invoice\n",
    "checklists/new-client.md": "# New client\n\n- brief call\n- quote\n- folder\n",
}


def write(path, text, age_days):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    t = time.time() - age_days * DAY
    os.utime(path, (t, t))


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    root = os.path.join(argv[0], "Notes")
    for rel, text in NOTES.items():
        write(os.path.join(root, rel), text, 3)
    n = 0
    for k, p in enumerate(PROJECTS):
        write(os.path.join(root, "projects", p + ".md"),
              "# %s\n\nStatus, next step, links to [[meetings/%s-kickoff]].\n" % (p, p), 2 + k * 9)
        write(os.path.join(root, "meetings", p + "-kickoff.md"),
              "# Kickoff %s\n\nNotes from the first call.\n" % p, 10 + k * 20)
        for j in range(18):
            n += 1
            age = (n * 7) % 330
            write(os.path.join(root, "journal", "2026-%03d.md" % n),
                  "# Day note %d\n\nWhat I did on [[%s]].\n" % (n, p), age)
    # a few loose notes nobody links to
    for j in range(14):
        write(os.path.join(root, "inbox", "idea-%02d.md" % j), "# Idea %d\n\nTo sort.\n" % j, 40 + j * 11)
    # two copies left by a sync tool
    write(os.path.join(root, "pricing (1).md"), "# Pricing\n\nold copy\n", 200)
    write(os.path.join(root, "projects", "yoga-studio-site (conflict).md"), "# old copy\n", 120)
    # an admin note that points to the password manager instead of holding secrets
    write(os.path.join(root, "admin", "hosting.md"),
          "# Hosting\n\nLogins are in the password manager, not here.\n", 60)
    # Claude Code pieces inside the vault
    write(os.path.join(root, ".claude", "skills", "write-quote", "SKILL.md"),
          "---\nname: write-quote\ndescription: Draft a quote from a brief.\n---\n", 30)
    write(os.path.join(root, ".claude", "settings.json"), "{}\n", 30)
    print(root)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# wifi-story

[![make.fun · u-xvader-tell-a-whole-story-in-32-characters-f86dd978](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/nmlyz/wifi-story/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/nmlyz/wifi-story/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

A tiny program that writes one Wi-Fi network name to a file. The name is twenty-five characters: she got the house, and the narrator got the Wi-Fi — the network you are looking at is the prize from the divorce settlement. It is the whole story of a marriage, told in the few words a phone shows in its network list.

## Run it

```sh
python3 main.py
```

It writes the name to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). Standard library only, no network, deterministic: two runs produce byte-identical output. Before writing, it checks the name is 1–32 characters with no surrounding space.

## The name

> SheGotTheHouseIGotTheWiFi

Thirty-eight candidate names were written from deliberately different angles, the stock Wi-Fi jokes were thrown out, and the survivors were judged pairwise against the brief by three readers — a deadpan comedy editor weighing freshness, a passerby weighing whether the joke lands on first sight, and a reader weighing how much story the name carries. The divorce-settlement name won the final 3-0.

---

Entered on [make.fun](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978).

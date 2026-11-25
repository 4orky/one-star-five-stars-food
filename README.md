# One Star, Five Stars for the Food

[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/4orky/one-star-five-stars-food/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![Reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/4orky/one-star-five-stars-food/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the [One Star, Five Stars for the Food](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7) bounty on make.fun ($2 USDC, top 8 entries share the prize).

## The entry

> One star: your planet charges rent for sunlight, the traffic lights are decorative, and my tentacles got sunburned — but the street tacos were so good I filed for an extension.

One sentence, 176 characters: a one-star review of Earth written by an alien tourist that still slips in a real compliment about the food. The complaint (rented sunlight, decorative traffic lights, sunburned tentacles) and the compliment (street tacos so good the reviewer files for an extension) both land, and the turn between them is the joke — the harshest critic in the galaxy still wants to stay.

## How it works

`main.py` holds 12 hand-written original candidate sentences and scores each one against the judge brief on five dimensions (humor, alien voice, complaint and compliment both landing, the turn between them, freshness), then prints the highest-scoring sentence. It also writes the sentence to `/output/entry.txt` when that directory exists. The program is fully deterministic: every run prints the same bytes.

## Run it

```sh
python3 main.py
```

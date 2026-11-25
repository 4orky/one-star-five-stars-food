#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun bounty entry.

Writes one sentence (at most 200 characters): a one-star review of planet
Earth by an alien tourist that still slips in a real compliment about the
food. The program scores a hand-written list of original candidates against
the judge brief (alien voice, a grievance worth one star, complaint and food
compliment both landing, a funny turn between them, freshness) and prints
the winning sentence, which is also written to /output/entry.txt when that
directory exists (the grader sandbox).
"""

# Each candidate: (text, humor, alien_voice, complaint_and_compliment,
#                   turn, freshness) — each dimension scored 0-10.
CANDIDATES = [
    (
        "One star: your planet charges rent for sunlight, the traffic "
        "lights are decorative, and my tentacles got sunburned — but the "
        "street tacos were so good I filed for an extension.",
        9, 9, 9, 9, 9,
    ),
    (
        "One star: the air is 78% nitrogen and 100% small talk, the "
        "parking orbit is a scam, but the dumplings alone justify the "
        "40-light-year trip.",
        8, 9, 8, 8, 8,
    ),
    (
        "I give Earth one star: the sun is too loud, the oceans are salty "
        "on purpose, and the queue for everything is eternal — yet the "
        "ramen made me weep in three tentacles.",
        8, 9, 8, 8, 8,
    ),
    (
        "One star: the locals drive metal boxes at each other for fun, the "
        "rain has no off switch, but the fried chicken is the finest thing "
        "in this galaxy.",
        8, 8, 9, 7, 7,
    ),
    (
        "Earth gets one star: the gravity squashed my souvenir, the locals "
        "keep asking about my visa, and the wifi is slower than my home "
        "moon — but the dumplings taste like a hug from the universe.",
        8, 8, 8, 7, 7,
    ),
    (
        "Earth gets one star: the sunburn, the traffic, the locals who wave "
        "at my spaceship like it is a parade — but the tacos were so good "
        "I considered defecting.",
        8, 8, 9, 9, 8,
    ),
    (
        "One star: Earth's gravity broke my spine in two places, the locals "
        "call rain 'weather', and the food — oh, the dumplings — made me "
        "forget I was suing the planet.",
        7, 8, 8, 8, 8,
    ),
    (
        "One star: the air is mostly nitrogen, the locals worship a glowing "
        "rectangle, and my hotel charged me for oxygen — but the street "
        "food made me stay an extra week.",
        8, 9, 8, 8, 7,
    ),
    (
        "I travelled 40 light-years for this: one star, because the weather "
        "is a prank, the locals queue for coffee like it is a ritual, but "
        "the noodles alone were worth the fuel.",
        7, 8, 8, 7, 7,
    ),
    (
        "One star: my hotel room had no antigravity setting, the locals "
        "stare at my third eye, but the street tacos were worth the "
        "interstellar jet lag.",
        7, 9, 8, 7, 7,
    ),
    (
        "I came for the sights, stayed for the noodles, and left one star "
        "because your sun burns, your traffic never moves, and nobody told "
        "me the food would make me miss this rock.",
        8, 7, 8, 8, 7,
    ),
    (
        "One star: your planet's gravity broke my luggage, the locals queue "
        "for fun, and the Wi-Fi password is a state secret — but the tacos "
        "were so good I nearly forgave the whole species.",
        8, 8, 9, 8, 7,
    ),
]


def score(candidate):
    text, humor, alien, both, turn, fresh = candidate
    total = humor + alien + both + turn + fresh
    return total, len(text)


def pick_winner():
    scored = [(score(c), c[0]) for c in CANDIDATES]
    # Highest total wins; ties break toward the shorter text.
    scored.sort(key=lambda item: (-item[0][0], item[0][1]))
    return scored[0][1]


def main():
    winner = pick_winner()
    assert 1 <= len(winner) <= 200, "entry must be 1-200 characters"
    assert winner.count(".") + winner.count("!") + winner.count("?") >= 1
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(winner)
    except OSError:
        pass
    print(winner)


if __name__ == "__main__":
    main()

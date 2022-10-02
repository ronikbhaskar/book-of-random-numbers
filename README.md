# Book of Random Numbers

*This article is also linked [here](https://ronikbhaskar.github.io/the-connoisseur-of-random-before-computers/)*

As we discussed last time, computers aren't great at generating truly random numbers. Can you do any better? You have plenty of practice generating random numbers, I can promise you that, as long as you've played a few board games.

Dice. Roll one to get a random number. Roll a few and add them together to get bigger numbers. So many board games rely on you generating random numbers to make the game enjoyable. Will you pass Go or will you go bankrupt on Boardwalk? Will you climb a ladder or slide down a snake? It all depends on how the dice roll.

In 1890 Francis Galton saw the power of using dice in statistics, creating a special set of dice for statistical experiments. He argued that shaking dice in a bag and taking them out with your eyes closed was sufficiently random for this random sampling technique.

Dice are great, but no one has time to sit around, rolling dice hundreds of times to get random numbers. In the early-mid 1900s, scientists began developing better mechanical techniques, like using electronic "roulette wheels." They generated some binary digits (0s and 1s) and converted the number to decimal. Using this technique, Project RAND turned into the RAND Corporation, selling books of one million random digits. The book still sells for roughly 70 USD. While their analyses of random digits looked usable for the most part, there were some issues with the odd-even distribution, and they made some strong assumptions about overcoming bias.

While I respect the RAND corporation for pioneering modern techniques, on my quest to finding the best truly random numbers, their method doesn't meet the mark. You all deserve better. To understand the nature of writing a book of random numbers, I borrowed techniques from Galton and RAND, and I wrote my own.

Rather than creating custom dice, I used existing six-sided dice. After rolling over 1000 dice, I converted from base 6 to base 10, and recorded my results. After thinking for a moment, I realized that one of the few things we need high volumes of random numbers of is dice rolls, so I saved those separately. Random coin flips would be nice too, so I did a bit more math to convert the dice rolls into coin flips. While I was at it, I converted the rolls into hexadecimal digits for the programmers out there. As of writing this, I'm only at the first volume, but if this proves useful, I will gladly create more handcrafted random numbers just for you.

Unfortunately, these random numbers aren't truly random. Humans are notoriously bad at being random, and I am human, so I likely introduced a non-random bias into the system. I don't know how to cheat with dice, nor did I try. While I made a good effort, it's hard to call these artisan "random" numbers truly random.

We'll have to push further next time.

---
## References

1. [Dice for Statistical Experiments](https://doi.org/10.1038/042013a0)
2. [RAND Corporation's History of Random Digits](https://www.rand.org/content/dam/rand/pubs/papers/2008/P113.pdf)
3. [Book of A Million Random Digits](https://www.amazon.com/Million-Random-Digits-Normal-Deviates/dp/0833030477)
4. [Random Number Circuit Using Frequencies](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjwx8Pt08D6AhU2lIkEHf8jAqcQFnoECAgQAQ&url=https%3A%2F%2Fwww.mdpi.com%2F2079-9292%2F10%2F13%2F1517%2Fpdf&usg=AOvVaw1PiU7pbgXdIviYWLFI4TgC)

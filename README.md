# flashcards
A quick-and-dirty flashcard program I made to help me study for my AWS Certification exam.

When the program is run alone, the default behavior is to run through the full set of cards once in a randomized order.

The contents of cards.txt is parsed into a set of flashcards as follows:
* Any number of consecutive lines that contain non-whitespace characters represents one side (front or back) of a flashcard.
* The delimiter between sides/cards is any number of lines that contain only white space.
* The first side the program finds will be the front of a card, the next will be the back of that card, and then the next side will begin a new card.

Check cards.txt to see an example that should help this click. :)

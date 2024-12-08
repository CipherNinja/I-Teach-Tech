# Scenario 3: Textual Data Normalization
# Story: As a data engineer at a publishing house, you're handling a list of book titles with inconsistent formatting—some are in uppercase, some in lowercase, and others have irregular spacing. Your objective is to standardize these titles to title case (where the first letter of each word is capitalized) and remove any leading or trailing whitespace.

# Challenge: Apply the map() function to clean and standardize the list of book titles.

# Hint: Combine string methods like strip() and title() within a function, and use map() to apply this function to the list of titles.

'''
This dataset contains challenging cases, such as:

1. Titles entirely in uppercase.
2. Titles entirely in lowercase.
3. Titles with irregular spacing (e.g., leading/trailing spaces, multiple spaces between words).
4. Mixed cases.

Task:
Normalize all book titles to title case (capitalize the first letter of each word).
Remove leading/trailing whitespace and fix irregular spacing.

Explanation:
strip():

Removes leading and trailing whitespace from the title.
title():

Converts the title to title case, where the first letter of each word is capitalized.
map():

Applies the cleaning function (strip() + title()) to every title in the dataset.
list():

Converts the map object into a list for further processing or display.



1. The Catcher In The Rye
2. To Kill A Mockingbird
3. 1984
4. Animal Farm
5. The Great Gatsby
6. One Hundred Years Of Solitude
7. Brave New World
8. Crime And Punishment
9. The Brothers Karamazov
10. War And Peace
...
50. The Road


'''


book_titles = [
    "  THE CATCHER IN THE RYE  ",
    "to kill a mockingbird",
    "1984   ",
    "  animal farm",
    "THE GREAT GATSBY",
    " one hundred years of solitude  ",
    "brave NEW world",
    "CRIME AND punishment",
    "the brothers karamazov",
    "WAR and peace  ",
    "   the lord of the rings",
    " the hobbit",
    "harry POTTER AND THE sorcerer's stone",
    "PRIDE AND prejudice",
    "   the alchemist ",
    "moby dick",
    "wuthering heights  ",
    "  ulysses",
    " THE odyssey",
    " great EXPECTATIONS",
    "   don quixote ",
    "   the little prince",
    "DRACULA",
    "  frankenstein ",
    " jane eyre",
    "THE CALL OF THE WILD  ",
    "The sun also rises",
    " of mice and men ",
    "THE SCARLET LETTER",
    "   gone with the wind",
    " THE GRAPES OF WRATH",
    "les miserables",
    "   anna karenina ",
    "madame bovary  ",
    " the divine comedy ",
    " THE ILIAD ",
    "   a tale of two cities",
    "THE OLD MAN AND THE SEA",
    " fahrenheit 451 ",
    "  the jungle book  ",
    "THE SECRET GARDEN",
    " charlotte's web",
    " PETER pan  ",
    " the time machine",
    " the catcher in the rye",
    " dUNE  ",
    "   the fault in our stars",
    "CLOUD ATLAS ",
    " LIFE OF PI",
    "   the road "
]

# We focus more on problem solving | here is working code you can modify it and print according to your LOU.
normalize_book_title = [print(" ".join(meta.title() for meta in title)) for title in map(lambda books:books.split(),book_titles)]

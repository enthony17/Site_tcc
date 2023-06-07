# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Enthony")

## Pessoas são a parte ruim de tudo que existe, sem serem humanos tudo seria melhor mas, tambem seria tudo ruim.
## Apenas algumas coisas que trazem felizidade e coisas boas. Então aproveita sua vida de merda, se voce ta feliz, bom... que se foda


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

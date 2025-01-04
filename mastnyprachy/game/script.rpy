# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define placeholder = Character("placeholder")


# The game starts here.

label start:

    scene bg bar-1

    show placeholder neutral

    # dialogue

    placeholder "Takže tak"

    placeholder "jsem zplozenec AI pekel, takže je čas mě odebrat co nejdříve"

    # This ends the game.

    return

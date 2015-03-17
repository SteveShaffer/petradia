# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image a n = "Sapphire_[N].png"
image a s = "Sapphire_[S].png"

image ml a = "MsLayna_[A]Scaled.png"
image ml s = "MsLayna_[S]Scaled.png"
image ml l = "MsLayna_[L]Scaled.png"
# TODO: Define image ml b = "MsLayna_[B]Scaled.png"

# Declare characters used by this game.
define a = Character('Adonia', color="#c8ffc8", image="a")
define ml = Character('Ms. Layna', color="#888888", image="ml")


# The game starts here.
label start:

    "In this world there is a force,"
    "a power so great it turns your course."
    "It comes, it goes, it reaps, it sows."
    "How it works? Nobody knows."
    "It gives, and it takes."
    "It kills, and it makes."
    "It is slow, and it is fast,"
    "It lingers, and it lasts."
    "It helps, and it hinders,"
    "It shines, and it cinders."
    "We often forget it,"
    "But we always desire it,"
    "Yet woe to the one who seeks to control it."
    "It is something you should never-ever be changing,"
    "because playing with time is a dangerous thing."

    "The morning sunlight filters into the bedroom windows rousing me from my sleep."

    show a n
    with fade

    a n "YAAAWWWN!"

    # show a s
    a "Morning already?"
    
    "Wait….sunlight??  That means…"

    show ml a
    ml a "Adoooniaaa!!  Adonia, are you awake yet?"
    ml a "Do you have any idea what time it is?!"
    
    "... ... ..."
    
    "Oh no!"
    "I slept in late again! I’m in soooo much trouble!! Ms. Layna is gonna kill me!"
    
    ml a "Adonia! How come you’re still sleeping?"
    ml s "You promised to make some deliveries this morning."

    # TODO: a s
    a "I know, I know. I’m very sorry."

    # TODO: show ml a
    ml a "Overslept eh? You do know that this is the fourth time this week!"
    ml s "There’s a lot of work to be done around here. I hope you’re not coming down with anything."

    # TODO: Should be ml n
    ml l "You’re lucky farmer Morey offered to help me today. Otherwise you’d be in a lot of trouble, Miss!"
    ml l "Maybe I will ask him to pick up some medicinal herbs for you from Madam Gia."

    ml s "I don’t want you getting sick dear."
    ml b "Oh, farmer Morey is such a nice man. *sigh*"
    
    "I chuckle inside. Old Farmer Morey and Ms. Layna have had crushes on each other for a while now."
    "So recently he has made excuses to come see her."
    "It doesn’t hurt that he is helping me out by doing some of the chores and getting me outta trouble."

    show a r
    a r "So you saw Farmer Morey this morning, huh?"
    a n "You know, Ms. Layna, Farmer Morey has been coming over here quite often these days, and I don’t think it’s because he likes making deliveries."
    a l "I think he likes you."
    
    "I give her a playful wink, trying to distract her from being angry at me."

    show ml b
    ml b "Oh Adonia, stop! You’re too much! Heeheehee."
    ml n "Anyways, it’s about time you got up and ready."
    ml n "There’s still a whole day ahead of you."

    return

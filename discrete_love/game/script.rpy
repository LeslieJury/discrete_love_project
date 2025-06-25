define j = Character("Jobs", color="#4682B4")       # Blue
define g = Character("Grace", color="#8B4513")       # Brown
define l = Character("Lovelace", color="#708090")       # Grey
define to = Character("Torvald", color="#2E8B57")       # Green
define a = Character("Anita", color="#4B0082")       # Dark Purple
define m = Character("Margaret", color="#D8BFD8")       # Light Purple
define v = Character("Von Neumann", color="#C71585")       # Dark Pink
define t = Character("Turing", color="#FFB6C1")        # Light Pink

image Jobs = "images/Jobs.png"
image Grace = "images/Grace.png"
image Lovelace = "images/Lovelace.png"
image Torvald = "images/Torvald.png"
image Anita = "images/Anita.png"
image Margaret = "images/Margaret.png"
image Von Neumann = "images/Von Neumann.png"
image Turing  = "images/Turing.png"
image Turing_Wedding = "images/Turing_Wedding.png"
image Student_Wedding = "images/Student_Wedding.jpg"

image bg classroom = "images/backgrounds/classroom.png"
image bg graph_undirected = "images/backgrounds/undirected.png"
image bg graph_directed = "images/backgrounds/directed.png"
image bg graph_tree = "images/backgrounds/tree.png"
image bg edges = "images/backgrounds/edges.png"

image logo = "transparent_logo.png"
image leslie_logo = "leslie_logo.png"
image cover = "cover.png"

label splashscreen:
    scene black 
    with Pause(1)
    
    play sound "ping.ogg"

    show logo with dissolve
    with Pause(2)
    
    scene black with dissolve
    with Pause(1)

    play sound "ping.ogg"

    show leslie_logo with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    play sound "ping.ogg"

    show cover with dissolve
    with Pause(4)

    scene black with dissolve
    with Pause(1)

    return


label start:

    scene bg classroom
    with dissolve

    show turing at center
    t "Welcome to Discrete Mathematics! Taught by your favorite Computer Science innovators, except in this world we are all cute anime girls! Please enjoy our lesson!"
    show Grace at right
    g "We will be your tutors for today! I'm Grace Hopper, I was the first to come up with the theory of machine-independent programming languages!"
    g "I even have a Women in Computer Science conference named after me! Aww so nice!"
    show Anita at left
    a "Hii I'm Anita Borg! I started that conference!"
    g "Kyaah yeah that would seem self centered if I made it haha, thank you <3"
    t "And I'm Alayna Turing! I helped win WW2 by using the Bombe (A codebreaking device! Not a real bomb haha)"
    a "Yeah who would..."
    hide turing
    show Von Neumann at center
    v "..."
    a "Oh... Sorry Von Neumann"
    v "(Pouts)"
    g "B-but she made so many theorems for the world of STEM, her wikipedia page is filled to the brim with the things she discovered! Ahh Von Neumann-Senpai is so cool <3"
    hide Von Neumann
    hide Anita 
    hide Grace
    show Turing at center
    t "Settle down girls! We all admire Von Neumann-Senpai for her contributions to Computer Science, but remember we all are pioneers here! Don't forget about your own strengths!"
    show Von Neumann at left
    v "You're right! Anyway, Student, please select which topic to study first!"
    t "And if you've already studied up on the topics you can challenge yourself with the dating quiz game!"
    v "Don't forget to come back and test your math skills and memory in the dating quiz game! Romance your favorite character and get their answers right to win!"
    t "It wouldn't be a true anime visual novel if you can't charm the characters yourself!"


    menu:
        "Graph Theory":
            jump graph_theory
        "Set Theory":
            jump set_theory
        "Dating Quiz Game":
            jump date_start



label graph_theory:

    scene bg classroom
    with dissolve

    show Margaret at left
    show Anita at right

    m "Hello! Welcome to Graph Theory: The study graphs which are comprised of nodes and edges! With graphs we can represent complex relations between objects"
    a "If you meant to select set theory, don't worry you can go back to the start in the next menu!"
    m "Please select the type of graph you would like to start with! I recommend starting with undirected graphs and working down the list (The jokes will make more sense that way)"


    menu:
        "Undirected Graphs":
            jump undirected_graph
        "Directed Graphs":
            jump directed_graph
        "Tree Graphs":
            jump tree_graph
        "Start from the beginning":
            jump start


label undirected_graph:

    scene bg classroom
    with dissolve

    show Grace at left
    show Lovelace at right
    g "Today we're exploring undirected graphs in depth."
    l "Let’s begin by defining a graph G = (V, E)."

    t "Exactly. Where V is the set of vertices, which will be us, and E is the edges, or our friendships."

    hide Grace
    hide Lovelace
    show Torvald at left
    show Anita at right

    to "For example, suppose E contains (Torvald, Anita), (Jobs, Grace), and (Margaret, Turing)."
    a "That means the graph is undirected, we can go from one node to the other and back."
    to "That's right! In our context it shows that are friendships are mutual and not one sided!"
    a "Yep! We are all interconnected because of our friendships with one another!"

    scene bg graph_undirected
    with fade

    show Jobs at left
    show Margaret at right
    j "Here's a diagram showing these undirected edges."
    m "It's a simple graph, no loops or multiple edges, and it's connected."
    show Turing at center
    t "I like how even though we aren't all directly close friends, we all have mutual friends! Since the graph is connected, everyone has a friend of a friend to everyone else!"
    t "Like how you two aren't close, but share mutual friends, meaning one can trace you to eachother using our graph"
    m "Yeah! Me and you are closer to eachother than we are to Jobs! Not to leave you out, Stevie Jobs"
    j "It's no problem, I'm more into appealing to consumers than working on theoretical computer science! I've always been a CEO type kinda like Torvald, except for our opposite approaches to our products"
    m "Yeah you have more in common with her than with us... but we still love to have you around!"
    j "Thanks! (Blushes) I look up to both of you as my senpais! I'm one of the newest here in this group, I'm pretty much a first year! so I have a lot to learn from my predecessors"
    hide Turing
    hide Jobs
    hide Maragaret
    t "Alright let's get out of the way to let our new Student-san see our graph"

    menu:
        "Directed Graphs":
            jump directed_graph
        "Tree Graphs":
            jump tree_graph
        "Finish Lesson":
            jump ending_graph

label directed_graph:

    scene bg classroom
    with dissolve

    show Lovelace at left
    show Torvald at right

    l "Now let's talk about directed graphs, or digraphs."
    to "Here, edges are ordered pairs, like (Lovelace -> Torvald), meaning her admiration is one sided."
    l "Torvald... do you not like me back?"
    to "Of course I do! It's just for the example!"
    l "Thank you Torvald-chan! I love your passion for open-source software! I think it's so cool (Blushes)"
    to "Yeah I think that open-source is absolutely necessary, I only use open-source"
    show Jobs at center
    j "That's why you won't use my revolutionary iPhone Torvald-chan (Pouts)"
    hide Jobs

    show Von Neumann at center
    v "This structure is useful for modeling connections, like who is close with who."

    scene bg graph_directed
    with fade

    show Lovelace at left
    show Torvald at right
    l "Observe how directed edges can form cycles or even become strongly connected."

    menu:
        "Tree Graphs":
            jump tree_graph
        "Go Back to Undirected":
            jump undirected_graph
        "Finish Lesson":
            jump ending_graph

label tree_graph:

    scene bg classroom
    with dissolve

    show Jobs at center
    j "Now for trees: connected acyclic graphs."

    show Turing at right
    show Von Neumann at left
    t "If Turing is the root, then every other girl has exactly one parent node above her."

    scene bg graph_tree
    with fade

    show Grace at left
    show Lovelace at right
    l "Let’s construct a tree: Turing -> Lovelace, Grace, and Jobs. Lovelace -> Anita and Margaret. Jobs -> Von Neumann. Von Neumann -> Torvald"
    g "There are no cycles, and every girl is reachable from the root, that being Turing."
    hide Lovelace
    show Torvald at right
    to "Hey why am I at the bottom of the list (pouts), and under Stevie Jobs-chan too??? I love her but be real she is not above Neumann!"
    g "My sources are telling me that the creator of that graph finished the graph before adding the names, so it's effectively random"
    hide Torvald
    show Jobs at right
    j "That's not true! I do deserve to be up that high! (Smirk)"

    menu:
        "Review Directed Graphs":
            jump directed_graph
        "Review Undirected Graphs":
            jump undirected_graph
        "Finish Lesson":
            jump ending_graph

label ending_graph:

    scene bg classroom
    with fade

    show Jobs at left
    show Torvald at right

    j "Thanks for joining us today in Graph Theory Class!"
    to "Come back next time for when we dive deeper into tree traversal, next time we'll have an accurate tree teehee"
    j "We already have an accurate one (pouts) You know how my inventions changed the climate of the tech industry forever??"
    to "They sure made an impact that's for sure, if you call privitizing everything changing it for the better?!"
    j "You don't even know what you're saying, open-sourcialist!"
    to "I'll take that title over whatever you're doing these days, I mean come on, your phones are worth nothing but you sell them for more than a whole PC?? That could've had open-source software on it??"
    show Turing
    hide Jobs
    hide Torvald
    t "Don't mind them, they're good friends, they just love to argue! Anyways! Thanks for playing our game! Have a great day!"

    return

label set_theory:

    scene bg classroom
    with dissolve
    show Turing at left
    show Von Neumann at right

    t "Welcome to Set Theory: The study of sets! These contain collections of objects."
    v "You can represent so many different things using sets, but in our case we will represent our friend group with a set!"
    t "You can even sort through sets to group things together"
    v "If you meant to pick graph theory, don't worry, you can start over clicking the last button in the upcoming menu"

    menu:
        "Set Fundamentals":
            jump set_fundamentals
        "Operations of Sets":
            jump set_operations
        "Finish Lesson":
            jump ending_sets
        "Start from the beginning":
            jump start

label set_fundamentals:

    scene bg classroom
    with dissolve

    show Margaret at left
    show Lovelace at right

    m "Hii Student! Today me and Countess: Ada Lovelace, will teach you about the fundamentals of sets!"
    l "Aww Margaret, no need to be so formal"
    m "You're literally royalty! Not to mention you created the first computer program!"
    l "Well you coined the term Software Engineering! That's impressive too! You worked at NASA, which has been explained to me as the people who go to the moon? I don't understand"
    m "You don't know what NASA is! It's been around since the late fifties"
    l "That's in the 20th century... I was born in 1815"
    m "Oh my gosh you must be the oldest of all.... I should not have said that"
    l "You calling me old!? Two seconds ago you were calling me a countess! Youngsters these days, have it too easy. I faced so much gender discrimination back in my day!"
    m "I know that must've been hard, your legacy has made a strong impact though in the world of gender equality in STEM"
    l "Stem?... Oh yeah I think I remember that gender something phrase starting to go around in my 30's, something about voting I think? That sounds so progressive and fascinating!"
    m "You were alive before the feminist movement... Okay I need to stop talking about your age before I get beat up by english royalty"
    l "That's a good choice... Student, please observe:"

    scene bg black # Replace later
    show Margaret at left
    show Lovelace at right

    l "A set is a collection of distinct, well-defined elements."
    m "You can think of a set as an array or list, but with no duplicates and no particular order."
    l "For example, the set (Margaret, Turing, Lovelace) contains exactly three elements"
    m "If you wrote (Lovelace, Turing, Margaret), that’s still the same set. Order doesn’t matter."
    l "Correct. Writing (Margaret, Turing, Turing, Lovelace) doesn’t change anything either, Turing's duplicate is ignored."
    m "We write an empty set as ∅ or just empty curly braces."
    l "Moving on, if we want to check whether an element is part of a set, we use the symbol ∈."
    m "For example, if A = (Torvald, Grace, Jobs), then Torvald ∈ A. That just means 'Torvald is in A'."
    m "Great! Now let’s talk about subsets!"
    l "A subset is a set where every element is also in another set. We write that as ⊆."
    m "It's checking if the element presented is inside the set!"
    l "Now that we have a base understanding, we can move on to operations!"

    menu:
        "Operations of Sets":
            jump set_operations
        "Finish Lesson":
            jump ending_sets

label set_operations:

    scene bg classroom
    with dissolve

    show Torvald at left
    show Anita at right

    a "Hii Student! Today me and Lina S. Torvald will teach you about the set operations!"
    t "I'm the creator of the best OS ever, Linux!"
    a "Such a cute name for you, Lina!"
    t "Awww thank youu! You're too kind Senpai!"
    a "Lina you're the youngest of all of us right?"
    t "Yeah! I'm the most modern pioneer here! I feel so honored being around such great minds!"
    a "Aww, I'm glad to be around such modern people, You're 30 years younger than me!"
    t "Aww you look great!"
    a "Thank you! You too you're so cute!"
    t "Aww You're making me blush!"

    scene bg classroom
    with dissolve

    a "Set operations time. First up: union."
    t "Union means combining two sets. Use ∪."
    a "Example: A = (Torvald, Lovelace, Grace), B = (Grace, Jobs), so A ∪ B = (Torvald, Lovelace, Grace, Jobs)."
    t "Next: intersection. That’s what both sets share."
    a "So A ∩ B = (Grace). Only the common element."
    t "Now difference. A − B means take out what B has."
    a "Like A = (1, 2, 3), B = (2, 4), then A − B = (1, 3)."
    t "Last one: complement. Everything not in the set."
    a "For this we need a universal set defined, that will be our friends here."
    t "That’s it! Know these four and you’re solid on operations."

    menu:
        "Review Set Fundamentals":
            jump set_fundamentals
        "Finish Lesson":
            jump ending_sets

label ending_sets:

    scene bg classroom
    with dissolve

    show Turing at left
    show Von Neumann at right

    t "That was a great lesson on sets, ladies, thank you for the explanations!"
    v "Yeah, we hope you paid attention, because the dialogue between them is part of the dating quiz game!"
    t "Don't worry though, you'll see if you got the problems right or wrong, so even if you mess up on dialogue you can still see how well you did in the math part!"
    v "And always feel free to review each section if you need!"
    t "All right! If you haven't done graph theory, go on ahead! If you have, then try testing your memory and math skills in the dating quiz game!"

    menu:
        "Check out Graph Theory":
            jump graph_theory
        "Go to Start":
            jump start

label date_start:

    scene bg classroom
    with dissolve

    show Turing at left
    show Von Neumann at right

    v "Hello! And welcome to the dating quiz game! Try your memory of not only the material, but also of your favorite character!"
    t "Don't worry, in this universe we are all single!"
    v "Anyone can play this game, no matter your gender or anything, we all are willing to go on a date with you IF and ONLY IF (<-> for my logic fans) you show us your math prowess!"
    t "That's right Von Neumann! Now let's get into the game!"

    jump turing_date_start

    # Make a dating quiz minigame where you need to get the questions right and when you do, the love level goes up and you can successfully date your selected character.
    # Implement not only quizzing the user but also charming the scientist you chose

label turing_date_start:

    scene bg classroom
    with dissolve

    show Turing at center

    t "Hello Student-chan, It's me Alayna! Do you want to go on a date?"
    t "Well, it's not going to be so easy, you must prove yourself as a good student and listener before that."
    t "I'm gonna call you a computer the way I hope your memory is sufficient!"

    $ turing_score = 0
    jump question1

label question1:
    show Turing at center

    t "Let's use traits of everyone to sort them!"
    t "CS = (Turing, Von Neumann, Grace, Lovelace, Torvald, Anita) (Pioneers or contributors to computer science)"
    t "TechIndustry = (Jobs, Margaret, Torvald) (Worked in applied tech or business)"

    t "What is the union of these groups?"

    menu:

        "U = (Turing, Von Neumann, Torvald, Jobs, Grace, Margaret, Anita, Lovelace)":

            t "Great job! When you take the union of two categories of the same group, you are left with the original group! "
            $ turing_score += 1
            jump question2

        "U = (Turing, Von Neumann, Torvald, Jobs, Grace, Margaret, Anita, Torvald)":

            t "Torvald appears twice, and Lovelace is missing"
            jump question2

        "U = (Turing, Von Neumann, Torvald, Jobs, Grace, Margaret, Berners-Lee)":

            t "That's a trick question! Berners-Lee is the name of the creator of the inventor of the World Wide Web, however, he is not in this game. Also Anita is missing"
            jump question2

label question2:

    show Turing at center

    t "What was the name of the machine I helped create during World War 2?"

    menu:

        "Little Boy":
            t "Sorry that's the name of one of the nuclear bombs dropped on Japan. ごめんなさい"
            jump question3
        "The Bombe":
            t "Congrats yep! It was referenced in the beginning, Anita and Von Neumann joked around about its name"
            $ turing_score += 1
            jump question3

        "Manchester Mark 1":
            t "Sorry, wrong british early computing machine"
            jump question3

label question3:
    show Turing at center
    t "People known for their work in the world of programming languages: P = (Grace, Lovelace, Turing, Anita)"
    t "People known as hardware theorists and computer architects: A = (Turing, Von Neumann, Torvald, Grace)"
    t "Now What is the intersection of these two?"

    menu:
        "Lovelace":
            "Sorry, Lovelace was the first computer programmer, she didn't have any influence in hardware theory"
            jump question4

        "Von Neumann":
            "Sorry, Von Neumann made the Von Neumann Architecture, but he wasn't as much in the programming-sphere"
            jump question4

        "Turing":

            "That's right, it's me! For programming: The Turing Machine and The Universal Computation Model. For computer architecture: ACE design and The Theoretical CPU/Memory Model"
            $ turing_score += 1
            jump question4


label question4:
    show Turing at left
    show bg edges
    t "Let's imagine a graph, who's vertices are: V(G) = (Turing, Von Neumann, Torvald, Jobs, Grace, Margaret, Anita, Lovelace)"
    t "It's edges connect people who have things in common. The edges are on screen"

    t "What is the degree of Grace?"

    menu:
        "4":
            "Nope, the answer was 3. Grace is connected to Turing, Lovelace, and Anita"
            jump turing_end

        "5":
            "Nope, the answer was 3. Grace is connected to Turing, Lovelace, and Anita"
            jump turing_end

        "2":
            "Nope, the answer was 3. Grace is connected to Turing, Lovelace, and Anita"
            jump turing_end

        "3":
            "Great Job! Grace is connected to Turing, Lovelace, and Anita"
            $ turing_score += 1
            jump turing_end

label turing_end:
    show Turing at center
    show bg classroom

    t "Moment of truth! Did you win the game?"

    if (turing_score == 4):
        jump turing_success
    else:
        jump turing_fail

label turing_success:
    hide Turing
    show Turing_Wedding at left
    show Student_Wedding at right
    t "Congrats Student-chan! I decided to skip the whole date thing and just marry you because you got a perfect score!"
    t "Love you Student Turing!!! <3"
    


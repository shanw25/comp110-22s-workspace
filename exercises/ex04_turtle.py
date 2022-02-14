"""An animation telling a little story inspired by one of the Chinese ancient Valentine's allegory.

0. Drawing functions (40 points total)
    0.0 draw_star: 44-56
    0.1 draw_half_bridge_or_birds 70-92
    0.2 draw_head_or_moon_circle 95-108
    0.3 draw_body_line 111-121
1. Main
    0.0 main: 134-217
    0.1 idiom: 220-221
2. Draw something twice
    2.0 draw_half_bridge_or_birds: 174, 175, 196, 197, 198, 199
    2.1 draw_head_or_moon_circle: 178, 179, 180, 187, 188, 189
    2.2 draw_body_line: 181, 182, 183, 184, 190, 191, 192, 193
3. Loop Usage
    3.0 51-56
    3.1 64-67
4. Fill Color
    4.0 187
    4.1 188
    4.2 189
5. Marker color
    5.1 50
    5.2 74
    5.3 115
    5.4 127
6 Types, Linting, Documentation
    this
7 Break up complex functions
    No specific function is written in the main method
8 Try something fun!
    8.0 I wrote the script using ontimer(): 201 - 217
    8.1 The shining stars appear randomly in the sky using randint(): 65
    8.2 Things drawn are cleaned using clear(): 66, 148
    8.3 I think the story is interesting
"""

__author__ = 730488727

from turtle import Turtle, done, ontimer, bgcolor
from random import randint


def draw_star(a_turtle: Turtle, x: float, y: float, length_of_segment: float) -> None:
    """Draw a star with given position and segment length."""
    a_turtle.penup() 
    a_turtle.goto(x, y)
    a_turtle.pendown()
    i: int = 0  # index counter in the loop
    a_turtle.color("yellow")  # the color of the star
    while i < 5:  # a star have five segments, therefore, i < 5
        a_turtle.begin_fill()
        a_turtle.forward(length_of_segment)
        a_turtle.right(144)
        i += 1
        a_turtle.end_fill()


def shin_star(star: Turtle) -> None:  # make the star shin in the sky

    star.speed(600)  # let it draw really fast
    star.ht()  # hide the turtle
    i: int = 0
    while i < 6:  # each star shin 6 times
        draw_star(star, randint(-400, 350), randint(100, 300), 50)  
        star.clear()  # clear the star after it's drawn so it seems shining
        i += 1


def draw_half_bridge_or_birds(bridge: Turtle, x: float, y: float, left_or_right_half: str, is_bridge: bool) -> None:
    """Draw half of the bridge, either the left bridge or right bridge. For param 'left_or_right_half', use 'left' or 'right'."""
    bridge.penup()
    bridge.home()
    bridge.color("white")
    bridge.ht()
    bridge.speed(100)
    bridge.goto(x, y)
    bridge.pendown()  # basic setups for the turtle object
    if is_bridge:  # if the 1/4 circle is for the bridge
        if left_or_right_half == "left":  # left side of the bridge
            bridge.left(180)
            bridge.circle(250, 90)
        else:
            bridge.left(180)  # right side of the bridge
            bridge.circle(250, -90)
    else:  # the 1/4 circle is for the birds
        if left_or_right_half == "left":  # left side of the birds
            bridge.left(90)
            bridge.circle(88, 90)
        else:  # right side of the birdes
            bridge.left(270)
            bridge.circle(88, -90)


def draw_head_or_moon_circle(head: Turtle, x: float, y: float, fill: bool, fill_color: str) -> None:
    """Draw a circle with color filled or not. When the color isn't filled, the param 'fill_color' is the line color."""
    head.color(fill_color)
    head.ht()
    head.speed(100)
    head.penup()
    head.goto(x, y)
    head.pendown()  # basic setups
    if fill:  # if the circle's color needs to be filled
        head.fillcolor(fill_color)
        head.begin_fill()
    head.circle(50)
    if fill:
        head.end_fill()
    

def draw_body_line(body: Turtle, x: float, y: float, length: int, direction: int) -> None:
    """Draw a line with given length and direction."""
    body.penup()
    body.home()
    body.color("white")
    body.ht()
    body.speed(100)
    body.goto(x, y)
    body.pendown()
    body.left(direction)  # pointing towards the given direction
    body.forward(length)  # forward the given length


def create_subtitle(a_turtle: Turtle, x: float, y: float, msg: str) -> None:
    """Generate subtitles with free position but fixed format."""
    a_turtle.ht()
    a_turtle.color("white")
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.write(msg, False, "left", ("Arial", 30, "normal"))  # create subtitles in the scene


def main() -> None:
    """The entrypoint of my scene."""
    # set the back ground color to black since it's evening.
    bgcolor("black")
    # creating a turtle for generating subtitles
    subtitle: Turtle = Turtle()  # the subtitle turtle
    star_one: Turtle = Turtle()  # the first star in the sky
    star_two: Turtle = Turtle()  # the second star in the sky
    bridge: Turtle = Turtle()  # the bridge the stand on
    head: Turtle = Turtle()  # their head & the moon
    body: Turtle = Turtle()  # their body
    # NOTE: The ontimer() function needs the first param to be a funciton with no arguments, therefore, the following functions are created.

    def clear_sub() -> None:  # a function to clear the subtitle. Because the ontimer function need a static function with no arguments as one of it's param, these function is created.
        subtitle.clear()

    def clear_body_and_head() -> None:  # clear the character on the screen
        body.clear()
        head.clear()

    def sub_2() -> None:  # 2ed subtitle
        create_subtitle(subtitle, -100, 320, "It's a shining night")
    
    def sub_3() -> None:  # 3rd subtitle
        create_subtitle(subtitle, -400, 320, "Mr. Python and a Mrs. Turtle was in love and they could only \nmeet each other once per year on this broken bridge")

    def sub_4() -> None:  # 4th subtitle
        create_subtitle(subtitle, -400, 320, "The birds in the sky was moved by their love. \nThey fixed the bridge using thier body.")

    def sub_5() -> None:  # 5 subtitle
        create_subtitle(subtitle, -400, 320, "Mr. Python and Mrs. Turtle finally could hug each other!")

    def sub_6() -> None:  # 6 subtitle
        create_subtitle(subtitle, -400, 200, "Happy Valentine's day!!!")

    def shin() -> None:  # shin the light
        shin_star(star_one)
        shin_star(star_two)
    
    def draw_bridge() -> None:  # draw the bridge
        draw_half_bridge_or_birds(bridge, -180, -160, "left", True)
        draw_half_bridge_or_birds(bridge, 172, -160, "right", True)

    def draw_people_and_moon() -> None:  # characters and the moon
        draw_head_or_moon_circle(head, 172, -60, False, "white")
        draw_head_or_moon_circle(head, -180, -60, False, "white")
        draw_head_or_moon_circle(head, 300, 200, True, "yellow")
        draw_body_line(body, 172, -60, 100, 270)
        draw_body_line(body, -180, -60, 100, 270)
        draw_body_line(body, 170, -60, 50, 250)
        draw_body_line(body, -180, -60, 50, 290)

    def draw_people_hug() -> None:  # draw two chars hugging
        draw_head_or_moon_circle(head, 50, -60, True, "white")
        draw_head_or_moon_circle(head, -50, -60, True, "white")
        draw_head_or_moon_circle(head, 300, 200, True, "yellow")
        draw_body_line(body, 50, -60, 100, 270)
        draw_body_line(body, -50, -60, 100, 270)
        draw_body_line(body, 50, -60, 50, 250)
        draw_body_line(body, -50, -60, 50, 290)

    def draw_birds() -> None:  # draw the birds
        draw_half_bridge_or_birds(bridge, -92, -248, "left", False)
        draw_half_bridge_or_birds(bridge, -92, -248, "right", False)
        draw_half_bridge_or_birds(bridge, 84, -248, "left", False)
        draw_half_bridge_or_birds(bridge, 84, -248, "right", False)
    # The first subtitle introducing the background of the story, it starts at 0 second thus it doesn't need ontimer() function to call.
    create_subtitle(subtitle, -380, 320, "The following story is a transformation to \none of the Ancient Chinese Valentine Allegory")
    ontimer(clear_sub, 2500)
    ontimer(sub_2, 2500)
    ontimer(shin, 3000)
    ontimer(clear_sub, 7500)
    ontimer(sub_3, 8000)
    ontimer(draw_bridge, 8500)
    ontimer(draw_people_and_moon, 8500)
    ontimer(clear_sub, 12000)
    ontimer(draw_birds, 12000)
    ontimer(sub_4, 12000)
    ontimer(clear_sub, 15500)
    ontimer(clear_body_and_head, 15500)
    ontimer(sub_5, 16000)
    ontimer(draw_people_hug, 16000)
    ontimer(sub_6, 16000)
    done()


if __name__ == "__main__":
    main()  # main method
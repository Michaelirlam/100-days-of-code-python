# 100 Days of Code - Day 22

## Pong

Day 22 is a traditional pong game. I've used classes to keep the game modular
and I put my game loop behind a function that continues to call itself until
the game over conditions are met. 

This project cemented my learning on classes from the previous projects and also
made me have to use my head a bit when it came to maths. Overall it wasnt to much
of a challenging project however there are some couple of issues that I still need
to work out. 

 1. Stuttering when player holds down a key: I've tried so many different things to
    try to fix this from messing with the ontimer to trying to simplify so movements
    and reduce the memory as much as possible but nothing has worked so far. From a
    bit of a google search I think this is a limitation with the turtle module.2.
 2. The computer AI may be a little too tough: Originally I implemented logic that
    meant that the computer paddle would follow the y pos of the ball, this proved to
    make an unbeatable opponent even as the speed of the ball increased. I've changed
    the logic a bit to make the paddle move only if its a certain distance away from
    the ball's y position that make the computer AI much more beatable but still with
    a decent challenge.
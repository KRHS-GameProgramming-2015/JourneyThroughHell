import sys, pygame, math, random
pygame.init()

ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        ballSpeed = [random.randint(-5, 5),
                     random.randint(-5, 5)]
        ballPos = [random.randint(100, width-100),
                     random.randint(100, height-100)]
        balls += [Ball(["zombie1.png",
                        "zombie2.png"],
                       ballSpeed,
                       ballPos)]

if __name__ == '__main__':
    print_hi('PyCharm')
    # seed random number generator
    seed(int(round(time.time() * 1000)))
    race_over = False
    finish_line = 200
    rounds = 0
    screen = turtle.Screen()
    screen_setup(screen)
    # create turtles
    t1 = turtle.Turtle()
    t1_id = init_turtle(t1, 0, "green", 1)
    t1_total = 0
    t2 = turtle.Turtle()
    t2_id = init_turtle(t2, 0, "red", 2)
    t2_total = 0

    # loop
    screen.update()
    screen.textinput("Turtle Race", "Ready, Set, Go!")
    while not race_over:
        rounds += 1
        # t1 turn
        move1 = randint(1, 6)
        t1_id = turn(t1, t1_id, move1)
        screen.update()
        # t2 turn
        move2 = randint(1, 6)
        t2_id = turn(t2, t2_id, move2)
        screen.update()
        # calculate position
        t1_total += move1
        t2_total += move2
        if t1_total >= finish_line or t2_total >= finish_line:
            race_over = True
            if t1_total >= finish_line and t2_total >= finish_line:
                result = "Tie in " + str(rounds) + " rounds."
            elif t1_total >= finish_line:
                result = "Green with " + str(t1_total) + " won vs " + str(t2_total) + " for Red in " + str(
                    rounds) + " rounds."
            else:
                result = "Red with " + str(t2_total) + " won vs " + str(t1_total) + " for Green in " + str(
                    rounds) + " rounds."
            screen.textinput("Game over!", result)
            exit()

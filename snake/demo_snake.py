from snake import Snake
snake = Snake()

snake.display()
actions = {'a':0, 'w':1, 'd':2, 's':3}
for i in range(60):
    action_str = raw_input('Move with: a,w,d,s + enter')
    if action_str in actions.keys():
        action = actions[action_str]
        snake.play(action)
        snake.display()
    else:
        print('Key %s not valid' % action_str)

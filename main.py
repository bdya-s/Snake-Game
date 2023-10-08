from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍😨")
screen.tracer(0)

snake = Snake()
new_food = Food()
score = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.listen()

game_on = True
score_count = 1
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(new_food) < 14:
        new_food.add_new_food()
        score.update_score(score_count)
        score_count += 1
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()

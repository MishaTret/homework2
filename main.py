import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print('Time to study!')
        self.progress += 0.15
        self.gladness -= 3

    def to_sleep(self):
        print('I am going to sleep!')
        self.gladness += 3

    def to_chill(self):
        print('Resting time!')
        self.gladness += 5
        self.money -= 10
        self.progress -= 0.2

    def to_work(self):
        print('Time to work!')
        self.money += 50
        self.gladness -= 5

    def update_student_state(self):
        if self.money < 0:
            print("I don't have enough money, I have to work!")
            self.to_work()
        elif self.progress < 0:
            print('I have problems with my progress, I have to study!')
            self.to_study()

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Passed externaly...')
            self.alive = False

    def end_of_day(self):
        print(f'Progress = {self.progress}')
        print(f'Gladness = {self.gladness}')
        print(f'Money = {self.money}')

    def live(self, day):
        day = 'Day ' + str(day) + " of " + self.name + "'s life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        else:
            self.to_work()
        self.update_student_state()
        self.is_alive()
        self.end_of_day()

nick = Student(name='Nick')
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)

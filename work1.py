import random
def test():
    user = input('請輸入你的選擇：')
    n = random.choice( ['rock', 'spock', 'paper', 'lizard', 'scissors'] )
    print('Player choose ', user,'computer choose ',n)
    if n == 'rock' and (user == 'scissors' or user == 'lizard'):
        print('computer win')
    elif n == 'rock' and user == 'rock':
        print('deuce')
    elif n == 'rock' and (user == 'Spock' or user == 'paper'):
        print('user win')
    elif n == 'spock' and (user == 'rock' or user == 'scissors'):
        print('computer win')
    elif n == 'spock' and user == 'spock':
        print('deuce')
    elif n == 'spock' and (user =='lizard' or user == 'paper'):
        print('user win')
    elif n == 'paper' and (user =='rock' or user == 'spock'):
        print('computer win')
    elif n == 'paper' and user == 'paper':
        print('deuce')
    elif n == 'paper' and (user == 'lizard' or user == 'scissors'):
        print('user win')
    elif n == 'lizard' and (user == 'paper' or user == 'spock'):
        print('computer win')
    elif n == 'lizard' and user == 'lizard':
        print('deuce')
    elif n == 'lizard' and (user == 'rock' or user == 'scissors'):
        print('user win')
    elif n == 'scissors' and (user == 'paper' or user == 'lizard'):
        print('computer win')
    elif n == 'scissors' and user == 'scissors':
        print('deuce')
    else:
        print('user win')
while(True):
    test()

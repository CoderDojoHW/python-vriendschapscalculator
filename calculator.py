#!/usr/local/bin/python3

score = 0
naam = input('Voer je naam in: ')
vriend = input('Voer de naam van vriend(in) in: ')

namen = naam + vriend

for teken in namen:
  if teken in 'aeiou':
    score += 5
  if teken in 'vriend':
    score += 10

print('je vriendschapsscore is: ', score)

if score > 100:
  print('beste vrienden!')
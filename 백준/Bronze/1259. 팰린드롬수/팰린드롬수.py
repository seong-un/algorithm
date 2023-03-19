while True:
  pelindrome=list(input())
  if pelindrome==['0']:
    break
  if pelindrome==list(reversed(pelindrome)):
    print('yes')
  else:
    print('no')
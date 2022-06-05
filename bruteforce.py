import random


words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

def generate_text(length):
  text = ''
  for i in range(0,length):
    text += random.choice(words)
  return text

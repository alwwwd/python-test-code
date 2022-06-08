def countVowels(string,flag):
   en_vowels = ['a','e','i','o','u']
   ru_vowels = []
   total = 0
   if flag == "en":
      for s in string:
         if s in en_vowels:
            total += 1
   elif flag == "ru":
      for s in string:
         if s in ru_vowels:
            total += 1
   return total


countVowels(input("введите строку:"),"en")
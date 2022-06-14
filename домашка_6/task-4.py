def countVowels(string,flag : str):
   en_vowels = ['a','e','i','o','u']
   ru_vowels = ['а','е','ё','и','у','я','ю','о','ы']
   total = 0

   if flag == 'ru':
      vowels = ru_vowels
   elif flag == 'en':
      vowels = en_vowels

   for s in string:
         if s in vowels:
            total += 1
      
   return total


print(countVowels(input("введите строку: "),"ru"))
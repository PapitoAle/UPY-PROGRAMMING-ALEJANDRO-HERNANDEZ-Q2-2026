#INPUT
verb = input("Ingrese el verbo: ")

#PROCESS
#All the pronouns
pronouns = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

#Dictionary of ending of the verbs
ending = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

#Get stem (verb minus last 3 letters) and ending (last 2 letters)
stem = verb[:-2]
ending = verb[-2:]

endings_list = terminaions[ending]

#OUTPUT
for index, pronoun in enumerate(pronouns):
    termination = endings_list[index]
    print(f"{pronoun} {stem}{terminacion}")

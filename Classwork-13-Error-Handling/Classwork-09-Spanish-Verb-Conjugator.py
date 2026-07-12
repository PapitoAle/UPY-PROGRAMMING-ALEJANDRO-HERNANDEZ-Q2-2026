#Spanish Verb Conjugator

pronouns = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

endings = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# INPUT
while True:
    try:
        action = input("Enter a verb: ").strip().lower()

        if len(action) < 3:
            raise VerboInvalidoError("The verb is too short. It must have at least 3 letters.")

        if not action.isalpha():
            raise VerboInvalidoError("The verb must contain only letters.")

        verb_type = action[-2:]

        if verb_type not in endings:
            raise VerboInvalidoError(f"'{action}' is not a valid infinitive. It must end in -ar, -er or -ir.")

        break
    except VerboInvalidoError as e:
        print(f"Invalid verb: {e}")

# PROCESS
stem = action[:-2]
selected_endings = endings[verb_type]

# OUTPUT
try:
    for index, pronoun in enumerate(pronouns):
        suffix = selected_endings[index]
        print(f"{pronoun} {stem}{suffix}")
except IndexError as e:
    raise VerboInvalidoError(f"Error generating conjugations: {e}")

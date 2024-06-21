# Major keys and their corresponding chords
major_keys = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
    "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"],
    "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
    "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
    "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
    "Db": ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"],
    "Gb": ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fdim"],
    "Cb": ["Cb", "Dbm", "Ebm", "Fb", "Gb", "Abm", "Bdim"]
}

# Minor keys dictionary
minor_keys = {}

# Function to add minor keys and their chords
def add_minor_key_chords():
    while True:
        key = input("Enter the minor key (or 'done' to finish): ").capitalize()
        if key.lower() == 'done':
            break
        chords = input(f"Enter the chords for {key} minor key, separated by commas: ").split(',')
        minor_keys[key] = [chord.strip() for chord in chords]

add_minor_key_chords()
print(minor_keys)  # To check the entered minor keys and chords

# Function for chord progression
def get_chord_progression(key, key_type="major"):
    if key_type == "major":
        chords = major_keys.get(key)
    else:
        chords = minor_keys.get(key)

    if not chords:
        return f"Chords for {key} {key_type} not found."

    # Progression [I, V, vi, IV]
    progression_indices = [0, 4, 5, 3]
    progression_chords = [chords[i] for i in progression_indices]

    return f"The chord progression for {key} {key_type} is {progression_chords}"

# Example usage
key = input("Enter the key for chord progression: ").capitalize()
key_type = input("Is it a major or minor key? ").lower()

print(get_chord_progression(key, key_type))

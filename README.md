# Dictionary-of-Chords-and-One-Popular-Progression

### Step-by-Step Implementation

1. **Create a dictionary for major keys with their corresponding chords.**
2. **Create a function to manually add minor chords to a minor key dictionary.**
3. **Create a function to get the chord progression [I, V, vi, IV] for a given key.**

### Step 1: Dictionary of Major Keys and Chords

We'll start by defining a dictionary where each major key maps to its chords.

```python
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
```

### Step 2: Function to Add Minor Keys

We'll create a function to manually add minor chords to a minor key dictionary.

```python
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
```

### Step 3: Function for Chord Progression

We'll create a function that, given a key, outputs the chord progression [I, V, vi, IV].

```python
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
```

### Complete Program

Putting it all together, here is the complete program:

```python
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
```

### Explanation

1. **Dictionary of Major Keys**: Contains chords for each major key.
2. **Function to Add Minor Keys**: Allows user input to add chords for minor keys.
3. **Function for Chord Progression**: Retrieves and displays the chord progression [I, V, vi, IV] for the specified key.

This program will guide you through creating and managing a dictionary of chords for both major and minor keys and will provide the specified chord progression upon request.

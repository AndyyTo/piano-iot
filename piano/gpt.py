import requests

key = "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"
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}


def get_chords(genre):
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are an helpful assistant."
            },
            {
                "role": "user",
                "content": f"Your job is to generate me a chord progression in the style of {genre}. The chord progression " +
                           "should be 4 bars long." +
                           "Your answer should be a list of 4 chords, each chord separated by a comma. Please only use MAJOR"
                           ", MINOR and 7TH chords. Do not use b5 chords. Makes sure to replace flat chords by their sharp equivalent, for example Bbmaj7 should be replaced by A#maj7. Do not include any other text in your response. DO NOT INCLUDE ANY TEXT IN YOUR RESPONSE."
            },

        ]
    }

    return requests.post(url, json=body, headers=headers).json()["choices"][0]["message"]["content"]


Notes = ["c4", "c#4", "d4", "d#4", "e4", "f4", "f#4", "g4", "g#4", "a4", "a#4", "b4", "c5", "c#5", "d5", "d#5", "e5",
         "f5", "f#5", "g5", "g#5", "a5", "a#5", "b5"]

Chords = {}
frequencies = {
    "c4": 261.63, #Do
    "c#4": 277.18,
    "d4": 293.66, #Re
    "d#4": 311.13,
    "e4": 329.63, #Mi
    "f4": 349.23, #Fa
    "f#4": 369.99,
    "g4": 392.00, #SOL
    "g#4": 415.30,
    "a4": 440.00, #La
    "a#4": 466.16,
    "b4": 493.88, #Si
    "c5": 523.25, #Do2
    "c#5": 554.37,
    "d5": 587.33,
    "d#5": 622.25,
    "e5": 659.26,
    "f5": 698.46,
    "f#5": 739.99,
    "g5": 783.99,
    "g#5": 830.61,
    "a5": 880.00,
    "a#5": 932.33,
    "b5": 987.77
}
cMajor = ["c4", "d4", "e4", "f4", "g4","a4", "b4", "c5"]

def convert(note):
    return frequencies[note]
cMajorFrequencies = list(map(convert, cMajor))

for i in range(12):
    Note = Notes[i][:-1]
    Chords[Note] = [Notes[i], Notes[i + 4], Notes[i + 7], Notes[i + 12]]
    Chords[Note + "7"] = [Notes[i], Notes[i + 4], Notes[i + 7], Notes[i + 10]]
    Chords[Note + "maj7"] = [Notes[i], Notes[i + 4], Notes[i + 7], Notes[i + 11]]
    Chords[Note + "m"] = [Notes[i], Notes[i + 3], Notes[i + 7], Notes[i + 12]]
    Chords[Note + "m7"] = [Notes[i], Notes[i + 3], Notes[i + 7], Notes[i + 10]]
    Chords[Note + "mmaj7"] = [Notes[i], Notes[i + 3], Notes[i + 7], Notes[i + 11]]


def flatRemover(x):
    notes = ["a", "b", "c", "d", "e", "f", "g"]
    x = [*x]
    if x[1] == "b":
        x[1] = "#"
        x[0] = notes[notes.index(x[0]) - 1]
    if x[-1] == "5" and x[-2] == "b":
        x = x[0:-2]
    new = ""
    for char in x:
        new += char
    return new


def chord_corrector(chords):
    return list(map(flatRemover, chords.lower().replace(" ", "") .split(",")))


def chord_deconstructor(chords):
    notes = []
    for chord in chords:
        notes.append(Chords[chord.lower()])
    return [note for chord in notes for note in chord]


def get_frequencie(note):
    return frequencies[note]

def generate_music(data):
    return list(map(get_frequencie, chord_deconstructor(chord_corrector(get_chords(data)))))
import pretty_midi

def basic_song_config():
    length = 30
    bpm = 120
    beat_length = 60 / bpm

    config = {
        "length": length,
        "bpm": bpm,
        "beat_length": 60 / bpm,
        "num_beats": int(length / beat_length),
    }

    return config

def create_song():
    # Create a PrettyMIDI object
    song = pretty_midi.PrettyMIDI()

    # do the same for a piano
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program, name="piano")

    # Add the instruments to the PrettyMIDI object
    song.instruments.append(piano)
    return song

def create_chord_song(chords, song_config=None):
    # TODO: add types, chords will be a list of pitch classes for now
    song = create_song()

    # TODO: grab this by name "piano"
    piano = song.instruments[0]

    if song_config is None:
        song_config = {
            "bpm": 120,
            "beat_length": 120 / 120,
        }

    notes = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
    ]

    # TODO: a class for song config seems a little more natural
    beat = 0
    for chord in chords:
        beat_length = song_config["beat_length"]
        note_start = beat * beat_length
        note_end = note_start + beat_length

        chord_notes = [notes[p] + "5" for p in chord.pitches]

        note_numbers = [pretty_midi.note_name_to_number(note_name) for note_name in chord_notes]

        for note_number in note_numbers:
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_start, end=note_end)
            piano.notes.append(note)
        beat += 1

    write_song(song)

def make_basic_song(song_config=None):
    song = create_song()

    # TODO: grab this by name "piano"
    piano = song.instruments[0]

    if song_config is None:
        song_config = basic_song_config()

    # TODO: a class for song config seems a little more natural
    for beat in range(song_config["num_beats"]):
        beat_length = song_config["beat_length"]
        if beat % 2 == 0:
            note_name = 'B5'
        else:
            note_name = 'E5'
        note_number = pretty_midi.note_name_to_number(note_name)
        note_start = beat * beat_length
        note_end = note_start + beat_length
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=note_start, end=note_end)
        piano.notes.append(note)

    write_song(song)


def write_song(song):
    # Write out the MIDI data
    song.write('midi/simple.mid')

if __name__ == "__main__":
    # make_basic_song()
    # TODO fix which module is doing the imports
    from pitch_class import PitchClass
    chords = [
        PitchClass([0, 1, 4]),
        PitchClass([2, 1, 4]),
        PitchClass([0, 1, 7]),
        PitchClass([0, 3, 4, 8]),
    ]
    create_chord_song(chords)
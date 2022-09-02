N_PITCHES = 12

class PitchClass:
    def __init__(self, pitches) -> None:
        # TODO: type check that pitches was a collection of integers
        self.pitches = self.clean_pitch_set(pitches)
        # TODO: will have to re-calc if this changes
        self.num_pitches = len(self.pitches)

    def clean_pitch_set(self, pitches):
        return sorted(list(set(pitches)))

    def pitches_to_str(self, pitches=None):
        if pitches is None:
            pitches = self.pitches
        return "".join([str(p) for p in pitches])

    def __repr__(self) -> str:
        return f"{{{self.pitches_to_str()}}}"

    def normalize(self):
        candidates = []
        for root in self.pitches:
            rerooted_pitches = [(p - root) % N_PITCHES for p in self.pitches]
            candidates.append(sorted(rerooted_pitches))

        min_width = N_PITCHES
        min_width_candidates = []
        for c in candidates:
            width = c[-1] - c[0]
            if width == min_width:
                min_width_candidates.append(c)
            if width < min_width:
                min_width = width
                min_width_candidates = [c]

        if len(min_width_candidates) == 0:
            self.pitches = min_width_candidates[0]
        else:
            intervals = []
            for candidate in min_width_candidates:
                interval = [candidate[i + 1] - candidate[i] for i in range(len(candidate) - 1)]
                intervals.append(interval)
            most_left_scrunched = min(intervals)
            candidate_index = intervals.index(most_left_scrunched)
            self.pitches = min_width_candidates[candidate_index]


if __name__ == "__main__":
    pc = PitchClass([0, 5, 7, 8])
    print(pc)
    print("normal form")
    pc.normalize()
    print(pc)
    # TODO: write some tests for the normal form
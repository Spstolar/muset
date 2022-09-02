from itertools import combinations
import math


N_PITCHES = 12

class PitchClass:
    def __init__(self, pitches) -> None:
        # TODO: type check that pitches was a collection of integers
        self.pitches = self.clean_pitch_set(pitches)
        # TODO: will have to re-calc these if the pitches change
        self.num_pitches = len(self.pitches)
        self.interval_vector = self.compute_interval_vector()

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

    def compute_interval_vector(self):
        interval_dict = {i: 0 for i in range(1, 7)}
        for p1, p2 in combinations(self.pitches, 2):
            interval = (p1 - p2) % N_PITCHES
            # TODO: generalize this (assumes N_PITCHES = 12)
            # The function is f(x) = 6 - |x - 6|
            mid = 6
            dist_from_mid = math.fabs(interval - mid)
            interval = mid - dist_from_mid
            # because the pitch class was cleaned, we know it has to be 1-6
            interval_dict[interval] += 1
        return list(interval_dict.values())

        


if __name__ == "__main__":
    example = [0, 5, 7, 8]
    print(f"Example: {example}")
    pc = PitchClass(example)
    print(pc)
    # TODO: write some tests for the normal form
    print("normal form")
    pc.normalize()
    print(pc)
    # TODO: interval vector tests, also how do we want to format this object
    print(pc.interval_vector)
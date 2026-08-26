def count_smileys(arr):
    eyes=[":", ";"]
    nose=["-", "~"]
    mouth=[")", "D"]
    def smiley(face):
        if len(face)>3 or len(face) <2:
            return False
        if len(face)==3:
            if face[0] in eyes and face[2] in mouth and face[1] in nose:
                return True
        if len(face)==2:
            if face[0] in eyes and face[1] in mouth:
                return True
        return False
    smiley_count = 0
    for face in arr:
        print(smiley(face))
        smiley_count += smiley(face)
    return smiley_count

arr=[':)',':(',':D',':O',':;']
print(count_smileys(arr))
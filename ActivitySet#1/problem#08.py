 text = "X-DSPAM-Confidence:    0.8475"
Sanjana=text.find(':')
Piece=text[Sanjana+1:]
End=float(Piece)
print(End)
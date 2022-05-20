text = "X-DSPAM-Confidence:    0.8475"
Sanjana=text.find(':')
piece=text[Sanjana+1:]
end=float(piece)
print(end)
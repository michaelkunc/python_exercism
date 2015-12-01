import itertools

def encode(string):
    counts = [[len(list(g)), k] for k,g in itertools.groupby(string)]
    return ''.join(map(str, (list(itertools.chain(*counts)))))

def decode(string):
  return 'what about this?'
# from "Effective Pandas" by Matt Harrison

series = {
  'index':[0, 1, 2, 3],
  'data':[145, 142, 38, 13],
  'name':'songs'
  }

def get(series, idx):
    value_idx = series['index'].index(idx)
    return series['data'][value_idx]

get(series, 1)

songs = {
  'index':['Paul', 'John', 'George', 'Ringo'],
  'data':[145, 142, 38, 13],
  'name':'counts'
  }

get(songs, 'John')



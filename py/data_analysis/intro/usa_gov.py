path = '../data/usagov_bitly_data2013-05-15'

# print(open(path).readline())

import json
records = [json.loads(line) for line in open(path)]
print(records[0])
print(records[0]['tz'])

# counting time zones
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10])

from collections import defaultdict


def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1

    return counts


def top_counts(count_dict, n=10):
    pairs = [(count, tz) for tz, count in count_dict.items()]
    pairs.sort()
    return pairs[-n:]

time_zone_counts = get_counts(time_zones)
print(time_zone_counts['America/New_York'])
print(len(time_zones))
print(top_counts(time_zone_counts, 5))

# built-in Counter
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))

# with pandas lib
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
print(frame[:5])

print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

# missing values
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

# plot it
import matplotlib
tz_counts[:10].plot(kind='bar', rot=0)

print(frame['a'][1])

# user agents
agents = Series([x.split()[0] for x in frame.a.dropna()])
print(agents[:5])
print(agents.value_counts()[:8])

# OS
import numpy as np
cframe = frame[frame.a.notnull()]
oses = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Non-Windows')
print(oses[:5])

# grouping
by_tz_os = cframe.groupby(['tz', oses])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])

# top overall time zones
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)
print(count_subset.plot(kind='barh', stacked=True))


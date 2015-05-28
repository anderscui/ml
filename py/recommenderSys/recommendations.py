#!/usr/bin/env python

from math import sqrt


# A dict of movie critics and their ratings of a small set of movies.
critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snake on a Plane': 3.5,
                  'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                  'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snake on a Plane': 3.5,
                     'Just My Luck': 1.5, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5,
                     'The Night Listener': 3.0},
    'Mickael Phillips': {'Lady in the Water': 2.5, 'Snake on a Plane': 3.0,
                         'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snake on a Plane': 3.5, 'Just My Luck': 3.0,
                     'Superman Returns': 4.0, 'You, Me and Dupree': 2.5,
                     'The Night Listener': 4.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snake on a Plane': 4.0,
                     'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 2.0,
                     'The Night Listener': 3.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snake on a Plane': 4.0,
                      'Superman Returns': 5.0, 'You, Me and Dupree': 3.5,
                      'The Night Listener': 3.0},
    'Toby': {'Snake on a Plane': 4.5, 'Superman Returns': 4.0,
             'You, Me and Dupree': 1.0}
}


def sim_distance(prefs, p1, p2):
    # find shared items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in si])
    return 1 / (1 + sqrt(sum_of_squares))


def sim_pearson(prefs, p1, p2):
    # find shared items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)
    if n == 0:
        return 1

    sum1 = sum([prefs[p1][item] for item in si])
    sum2 = sum([prefs[p2][item] for item in si])

    sum1_sq = sum([pow(prefs[p1][item], 2) for item in si])
    sum2_sq = sum([pow(prefs[p2][item], 2) for item in si])

    prod_sum = sum([prefs[p1][item] * prefs[p2][item] for item in si])

    num = prod_sum - (sum1*sum2/n)
    den = sqrt((sum1_sq - pow(sum1, 2)/n) * (sum2_sq - pow(sum2, 2)/n))
    if den == 0:
        return 0

    return num/den


def top_matches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[:n]


def get_recommendations(prefs, person, similarity=sim_pearson):

    totals = {}
    sim_sums = {}

    for other in prefs:
        if other == person:
            continue

        sim = similarity(prefs, person, other)
        if sim <= 0:
            continue

        for item in prefs[other]:

            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim

                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim

    # normalize scores
    rankings = [(total/sim_sums[item], item) for item, total in totals.items()]
    rankings.sort(reverse=True)
    return rankings


if __name__ == '__main__':

    # Euclidean distance
    print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
    print(sim_distance(critics, 'Lisa Rose', 'Mickael Phillips'))

    # Pearson correlation
    print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
    print(sim_pearson(critics, 'Lisa Rose', 'Mickael Phillips'))

    # find similar users
    print(top_matches(critics, 'Toby', 3))
    print(top_matches(critics, 'Toby', 3, sim_distance))

    # get recommendations for a specific user
    print(get_recommendations(critics, 'Toby'))
    print(get_recommendations(critics, 'Toby', sim_distance))
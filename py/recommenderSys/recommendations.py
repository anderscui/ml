#!/usr/bin/env python

from math import sqrt
import datetime

from common.persistence import to_pickle, from_pickle

# A dict of movie critics and their ratings of a small set of movies.
critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snake on a Plane': 3.5,
                  'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                  'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snake on a Plane': 3.5,
                     'Just My Luck': 1.5, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5,
                     'The Night Listener': 3.0},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snake on a Plane': 3.0,
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
    scores.sort(reverse=True)
    return scores[0:n]


def get_recommendations(prefs, person, similarity=sim_pearson):

    """
    Implement simple userCF.

    :param prefs: preference data including each user for each movie
    :param person:  find recommendations for
    :param similarity: similarity method
    :return: a list of recommendations
    """
    totals = {}
    sim_sums = {}

    for other in prefs:
        if other == person:
            continue

        sim = similarity(prefs, person, other)
        # if the two are not similar, ignore it.
        if sim <= 0:
            continue

        for item in prefs[other]:

            #if item not in prefs[person] or prefs[person][item] == 0:
            # has not seen or rated
            if item not in prefs[person]:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item]*sim

                sim_sums.setdefault(item, 0)
                sim_sums[item] += sim

    # normalize scores
    rankings = [(total/sim_sums[item], item) for item, total in totals.items()]
    rankings.sort(reverse=True)
    return rankings


def transform_prefs(prefs):
    result = {}
    for p in prefs:
        for item in prefs[p]:
            result.setdefault(item, {})

            result[item][p] = prefs[p][item]

    return result


def calc_similar_items(prefs, n=10):

    result = {}

    item_prefs = transform_prefs(prefs)
    c = 0
    for item in item_prefs:
        c += 1
        if c % 100 == 0:
            print('{0} / {1}'.format(c, len(item_prefs)))
        matches = top_matches(item_prefs, item, n=n, similarity=sim_distance)
        result[item] = matches
    return result


def get_recommended_items(prefs, item_match, user):
    """
    Implement simple itemCF.

    :param prefs: user preferences.
    :param item_match: similar items dataset.
    :param user: recommend for
    """
    user_ratings = prefs[user]

    scores = {}
    total_sim = {}

    for (item, rating) in user_ratings.items():
        for (similarity, item2) in item_match[item]:
            # rated before, ignore it.
            if item2 in user_ratings:
                continue

            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating

            total_sim.setdefault(item2, 0)
            total_sim[item2] += similarity

    rankings = [(score/total_sim[item], item) for item, score in scores.items()]
    rankings.sort(reverse=True)

    return rankings


def load_movie_lens():

    movies = {}
    for line in open('./data/movies.dat'):
        (mid, mtitle) = line.split('::')[0:2]
        movies[mid] = mtitle

    print(len(movies))

    prefs = {}
    for line in open('./data/ratings.dat'):
        (uid, mid, rating, ts) = line.split('::')
        prefs.setdefault(uid, {})
        prefs[uid][movies[mid]] = float(rating)

    print(len(prefs))

    return prefs


# if __name__ == '__main__':
#
#     # Euclidean distance
#     print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
#     print(sim_distance(critics, 'Lisa Rose', 'Michael Phillips'))
#
#     # Pearson correlation
#     print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
#     print(sim_pearson(critics, 'Lisa Rose', 'Michael Phillips'))
#
#     # find similar users
#     print(top_matches(critics, 'Toby', 3))
#     print(top_matches(critics, 'Toby', 3, sim_distance))
#
#     # get recommendations for a specific user
#     print(get_recommendations(critics, 'Toby'))
#     print(get_recommendations(critics, 'Toby', sim_distance))
#
#     movies = transform_prefs(critics)
#     # item similarity
#     print('item similarity')
#     print(movies)
#     print(top_matches(movies, 'Superman Returns'))
#     # print(top_matches(movies, 'Superman Returns', similarity=sim_distance))
#
#     # 'recommend' reviewers
#     print(get_recommendations(movies, 'Just My Luck'))
#
#     # itemCF
#     item_similarities = calc_similar_items(critics)
#     print(item_similarities)
#     print(get_recommended_items(critics, item_similarities, 'Toby'))


if __name__ == '__main__':
    # for MovieLens
    prefs = load_movie_lens()
    # print(prefs['87'])
    # print(len(prefs))

    # # UserCF
    # user_recommended = get_recommendations(prefs, '87')[:15]
    # print(user_recommended)
    #
    # ItemCF
    # print(datetime.datetime.now())
    # item_sim = calc_similar_items(prefs, n=50)
    # to_pickle(item_sim, 'item_sim.pkl')
    # print(datetime.datetime.now())

    item_sim = from_pickle('item_sim.pkl')
    item_recommended = get_recommended_items(prefs, item_sim, '101')[:5]
    print(item_recommended)
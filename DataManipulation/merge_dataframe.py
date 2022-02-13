# coding: utf-8
import pandas as pd


person = pd.read_csv('../data/survey_person.csv')
site = pd.read_csv('../data/survey_site.csv')
survey = pd.read_csv('../data/survey_survey.csv')
visited = pd.read_csv('../data/survey_visited.csv')
print(person)
print(site)
print(survey)
print(visited)

visited_subset = visited.loc[[0,2,6]]
print(visited_subset)

one_to_one_merge = site.merge(visited_subset, left_on='name', right_on='site')
print(one_to_one_merge)

many_to_one_merge = site.merge(visited, left_on='name', right_on='site')
print(many_to_one_merge)

person_survey = person.merge(survey, left_on='ident', right_on='person')
print(person_survey)

visited_survey = visited.merge(survey, left_on='ident', right_on='taken')
print(visited_survey)

four_way_merge = person_survey.merge(
    visited_survey,
    left_on = ['ident','taken','quant','reading'],
    right_on = ['person','ident','quant','reading']
    )

# When column names collide, pandas automatically adds suffix
# _x for left and _y for right dataframe
print(four_way_merge.head())


from random import randint
import copy

story = ("One day my {} friend and I decided to go to the {} game in {}. "+
"We really wanted to see the {} play the {}. "+
"So, we {} our {} down to the {} and bought some {}'s. "+
"We got into the game and it was a lot of fun. "+
"We ate some {} {} and drank some {} {}. "+
"We had a great time! We plan to go ahead next year.")

#creating a dictionary

word_dict = {
        'adjective':['greedy','lazy','lousy','overexcited','abrasive','rich','harsh','tasty'],
        'city name':['Chicago','New York','Delhi','Bangalore','Chennai'],
        'noun':['people','map','music','dog','circus','ball','salad'],
        'action verb':['run','fall','cry','scurry','jump','watch','hunt'],
        'sports noun':['ball','mit','puck','uniform','helmet','scoreboard','player','referee'],
        'place': ['park','desert','forest','store','restaurant','waterfall','library'],
        'edibles':['nuts','bananas','hot dogs','chips','burgers','ice creams'],
        'beverage':['beer cans','soft drinks','tea cups','coffee cups','orange juice']
}


def get_word(type, local_dict):
        words = local_dict[type]
        cnt = len(words)-1
        index = randint(0,cnt)
        return local_dict[type].pop(index)


def create_story():
        local_dict = copy.deepcopy(word_dict)
        return story.format(
                get_word('adjective',local_dict),
                get_word('sports noun',local_dict),
                get_word('city name',local_dict),
                get_word('noun',local_dict),
                get_word('sports noun',local_dict),
                get_word('action verb',local_dict),
                get_word('noun',local_dict),
                get_word('place',local_dict),
                get_word('noun',local_dict),
                get_word('adjective',local_dict),
                get_word('edibles',local_dict),
                get_word('adjective',local_dict),
                get_word('beverage',local_dict),
        )

print("Story 1: ")
print(create_story())
print("Story 2: ")
print(create_story())
print()

"""
Some basic examples for promptimize.

to run, simply execute `p9e ./examples/set_of_standard_ques.py`
"""
# Brining some "prompt generator" classes
from promptimize.prompt_cases import PromptCase

# Bringing some useful eval function that help evaluating and scoring responses
# eval functions have a handle on the prompt object and are expected
# to return a score between 0 and 1
from promptimize import evals

# Promptimize will scan the target folder and find all Prompt objects
# and derivatives that are in the python modules
simple_prompts = [
    # Prompting "hello there" and making sure there's "hi" or "hello"
    # somewhere in the answer
    PromptCase("hello on the other side!", lambda x: evals.any_word(x.response, ["heyy", "hey"])),
    PromptCase(
        "name the top 10 cricketers!",
        lambda x: evals.any_word(x.response, ["sachin", "don bradman"]),
        weight=2,
 category="cricket"
    ),
    PromptCase(
        "top 10 countries in the world by gdp",
        lambda x: evals.any_word(x.response, ["Germany", "Italy"]),
        weight=2,
 category="world"
    ),
]

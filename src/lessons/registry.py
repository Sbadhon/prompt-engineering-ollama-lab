from lessons.lesson_01_generation_parameters import LESSON as LESSON_01
from lessons.lesson_02_basic_prompt import LESSON as LESSON_02
from lessons.lesson_03_zero_shot import LESSON as LESSON_03
from lessons.lesson_04_one_shot import LESSON as LESSON_04
from lessons.lesson_05_few_shot import LESSON as LESSON_05
from lessons.lesson_06_chain_of_thought import LESSON as LESSON_06
from lessons.lesson_07_self_consistency import LESSON as LESSON_07
from lessons.lesson_08_prompt_template import LESSON as LESSON_08
from lessons.lesson_09_runnable_lambda import LESSON as LESSON_09
from lessons.lesson_10_str_output_parser import LESSON as LESSON_10
from lessons.lesson_11_lcel import LESSON as LESSON_11
from lessons.lesson_12_question_answering import LESSON as LESSON_12
from lessons.lesson_13_product_review_analyzer import LESSON as LESSON_13


LESSON_LIST = [
    LESSON_01,
    LESSON_02,
    LESSON_03,
    LESSON_04,
    LESSON_05,
    LESSON_06,
    LESSON_07,
    LESSON_08,
    LESSON_09,
    LESSON_10,
    LESSON_11,
    LESSON_12,
    LESSON_13,
]

LESSONS = {lesson["title"]: lesson for lesson in LESSON_LIST}

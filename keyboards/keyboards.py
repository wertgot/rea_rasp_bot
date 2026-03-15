from aiogram.types import(
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


# главное меню
schedule_optimization_btn = KeyboardButton(text=LEXICON_RU["schedule_optimization_btn"])
schedule_analytics_btn = KeyboardButton(text=LEXICON_RU["schedule_analytics_btn"])

main_menu_kb_builer = ReplyKeyboardBuilder()

main_menu_kb_builer.row(
    schedule_optimization_btn,
    schedule_analytics_btn,
    width=1,
)

main_menu_kb: ReplyKeyboardMarkup = main_menu_kb_builer.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)

# меню аналитики расписания
empty_rooms_btn =  KeyboardButton(text=LEXICON_RU["empty_rooms_btn"])
pairs_num_by_corpuses_btn =  KeyboardButton(text=LEXICON_RU["pairs_num_by_corpuses_btn"])

schedule_analytics_kb_builer = ReplyKeyboardBuilder()

schedule_analytics_kb_builer.row(
    empty_rooms_btn,
    pairs_num_by_corpuses_btn,
    width=1,
)

schedule_analytics_kb: ReplyKeyboardMarkup = schedule_analytics_kb_builer.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)

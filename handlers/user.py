from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

import logging

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import main_menu_kb, schedule_analytics_kb

from services.analytics import vacant_rooms, pairs_num_by_corpuses


user_router = Router()

logger = logging.getLogger(__name__)

p_by_c, all_pairs_num, max_pairs_together = pairs_num_by_corpuses()


@user_router.message(Command(commands="start"))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=main_menu_kb)


@user_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

@user_router.message(F.text == LEXICON_RU["schedule_analytics_btn"])
async def process_schedule_analytics_btn(message: Message):
    await message.answer(
        text=LEXICON_RU["schedule_analytics"],
        reply_markup=schedule_analytics_kb
    )

@user_router.message(F.text == LEXICON_RU["empty_rooms_btn"])
async def process_empty_rooms_btn(message: Message):
    await message.answer(
        text=LEXICON_RU["empty_rooms"],
    )

@user_router.message(F.text.replace(" ", "").regexp(r'^\d+-\d+$'))
async def process_empty_rooms(message: Message):
    clear_input = message.text.replace(" ", "")
    pair_num, corpus = map(int, clear_input.split('-'))
    if pair_num not in range(1, 9) or corpus not in [1,2,3,4,6,7,8,9]:
        await message.reply(text="нет такого номера пары или корпуса")
    else:
        v_rooms, rooms_num = vacant_rooms(pair_num, corpus)
        await message.answer(f"Свободно {len(v_rooms)} из {rooms_num}\n\n{', '.join(v_rooms)}")


@user_router.message(F.text == LEXICON_RU["pairs_num_by_corpuses_btn"])
async def process_pairs_num_by_corpuses_btn(message: Message):
    await message.answer(
        text=f"Всего пар сегодня: {all_pairs_num}\nМаксимум пар одновременно: {max_pairs_together}\n\n{p_by_c}",
    )

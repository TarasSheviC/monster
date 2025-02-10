import asyncio
from browser_automation.vk_actions import VKAutomation
from ai.personality_generator import PersonalityGenerator
from ai.content_generator import ContentGenerator
from database.db_manager import DBManager
from analytics.performance_analyzer import PerformanceAnalyzer

async def main():
    db_manager = DBManager()
    vk_auto = VKAutomation()
    personality_gen = PersonalityGenerator()
    content_gen = ContentGenerator()
    analyzer = PerformanceAnalyzer(db_manager)

    # Создаем новый аккаунт
    phone = "+79123456789"
    password = "securepassword"
    personality = personality_gen.generate_personality()
    db_manager.add_account(phone, personality)

    # Логинимся и выполняем действия
    await vk_auto.login(phone, password)

    # Присоединяемся к сообществам
    for interest in personality['interests']:
        community_url = f"https://vk.com/search?c[q]={interest}&c[section]=communities"
        await vk_auto.join_community(community_url)

    # Комментируем посты
    post_url = "https://vk.com/feed"
    comment = content_gen.generate_comment("Интересный пост о технологиях", personality)
    await vk_auto.comment_post(post_url, comment)

    # Закрываем браузер
    await vk_auto.close()

if __name__ == "__main__":
    asyncio.run(main())

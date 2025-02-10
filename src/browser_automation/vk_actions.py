import asyncio
from pyppeteer import launch

class VKAutomation:
    async def login(self, phone, password):
        self.browser = await launch(headless=True)
        self.page = await self.browser.newPage()
        await self.page.goto('https://vk.com')
        await self.page.type('#index_email', phone)
        await self.page.type('#index_pass', password)
        await self.page.click('#index_login_button')
        await self.page.waitForNavigation()

    async def join_community(self, community_url):
        await self.page.goto(community_url)
        await self.page.click('#join_button')

    async def comment_post(self, post_url, comment):
        await self.page.goto(post_url)
        await self.page.type('.reply_field', comment)
        await self.page.click('.reply_button')

    async def send_friend_request(self, user_url):
        await self.page.goto(user_url)
        await self.page.click('#profile_add_friend')

    async def close(self):
        await self.browser.close()

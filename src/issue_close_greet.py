import asyncio
import os
import sys
import traceback
import aiohttp
from aiohttp import web
from gidgethub import aiohttp as gh_aiohttp
from gidgethub import routing
from gidgethub import sansio
from gidgethub import apps


router = routing.Router()

############################ Issue Greetings when closed #############################################


@router.register("issues", action="closed")
async def issue_opened_event(event, gh, *args, **kwargs):

    installation_id = event.data["installation"]["id"]

    installation_access_token = await apps.get_installation_access_token(
        gh,
        installation_id=installation_id,
        app_id=os.environ.get("GH_APP_ID"),
        private_key=os.environ.get("GH_PRIVATE_KEY")
    )

    #url for the comment url
    url = event.data['issue']['comments_url']
    
    #author of the issue creater
    author = event.data['issue']['user']['login']

    # avatar = event.data['issue']['user']['avatar_url']

    #message tobe posted
    message = f"<table><tbody><tr><td>Thanks for closing this issue @{author}! We hope you loved to work with our repository 😋.</td></tr></tbody></table>"
    
    await gh.post(url, data={
        'body': message,
        },
        oauth_token=installation_access_token["token"]
                 )

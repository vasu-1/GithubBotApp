from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ pull request review_needed_pr labeler #############################################


LABEL1 = 'review_needed_pr' # label name

@router.register("pull_request", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):
    is_url = event.data['pull_request']['issue_url']
    suffix = '/labels{/name}'
    label_url = is_url + suffix


    await gh.post(label_url, data=[LABEL1]) #event post for key label
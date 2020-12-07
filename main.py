
import instapy
from instapy import InstaPy
from instapy import smart_run

GECKODRIVER_PATH = "/app/vendor/geckodriver/geckodriver"

session = InstaPy(username="pytesting01",
                  password="456852jj",
                  browser_executable_path=GECKODRIVER_PATH,
                  headless_browser=False,
                  multi_logs=True)




with smart_run(session):

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_user_interact(amount=2,
                              randomize=True,
                              percentage=100,
                              media='Photo')
    session.set_do_follow(True, percentage=80)
    session.set_do_like(True, percentage=70)
    session.set_do_comment(True, percentage=5)
    session.set_comments(["@{} buen contenido", ":heart_eyes: :heart_eyes: :heart_eyes:"],
                         media='Photo')

    session.set_quota_supervisor(enabled=True,
                                 peak_comments_daily=250,
                                 peak_comments_hourly=30,
                                 peak_likes_daily=800,
                                 peak_likes_hourly=50)

    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1500,
                                    max_following=2000,
                                    min_followers=30,
                                    min_following=30,
                                    min_posts=5)

    #session.interact_user_followers(usernames=['thekhalifaners'],amount=10, randomize=True)
    for i in range(10):
        session.follow_user_followers(['thekhalifaners'],
                                      amount=10,
                                      randomize=True,
                                      interact=True,
                                      sleep_delay=240)

    #session.interact_user_followers(usernames=["natgeo"], amount=100000)
    #session.like_by_tags(['python3', 'javascript'], amount=300)


session.end()


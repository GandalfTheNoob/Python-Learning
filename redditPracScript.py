#a simple script just to test Reddit scraping
#this script does not use Oauth

import praw
import pprint
import requests

user_agent = ("Python script for testing the reddit api by /u/Ceevu")
r = praw.Reddit(user_agent = user_agent)
v_fixed = []

subbreddit = r.get_subreddit('breathless')

for submission in subbreddit.get_hot(limit = 25):
	title = submission.title
	if " " in title.lower():
		v_fixed.append(title)
print "The following %d posts might contain ' ' ..." %(len(v_fixed))

pprint.pprint(v_fixed)

pprint.pprint(dir(subbreddit))

loggedin = r.get_me()
pprint.pprint(dir(loggedin))

#
#print dir(mysubs) -- output is below when using mysubs = r.get_subreddit('mine')
#
# ['add_ban',
#  'add_contributor',
#   'add_flair_template',
#    'add_moderator',
#     'add_mute',
#      'add_wiki_ban'
# , 'add_wiki_contributor',
#  'clear_all_flair',
#   'clear_flair_templates',
#    'configure_flair',
#     'delete_flair',
#      'delete_image',

#  'display_name',
#   'edit_wiki_page',
#    'from_api_response',
#     'fullname',
#      'get_banned',
#       'get_comments',
#        'get_contributors',
#         'get_controversial',
#          'get_controversial_from_all',
#           'get_controversial_from_day',
#            'get_controversial_from_hour',
#             'get_controversial_from_month',
#              'get_controversial_from_week',
#               'get_controversial_from_year',
#                'get_edited',
#                 'get_flair',
#                  'get_flair_choices',
#                   'get_flair_list',
#                    'get_hot',
#                     'get_mod_log',
#                      'get_mod_mail',
#                       'get_mod_queue',
#                        'get_moderators',
#                         'get_muted',

# 'get_new',
#  'get_random_submission',
#   'get_reports',
#    'get_rising',
#     'get_settings',
#      'get_spam',
#       'get_sticky',
#        'get_stylesheet',
#         'get_top',
#          'get_top_from_all',
#           'get_top_from_day',
#            'get_top_from_hour',
#             'get_top_from_month',
#              'get_top_from_week',    
# 'get_top_from_year',
#  'get_traffic',
#   'get_unmoderated',
#    'get_wiki_banned',
#     'get_wiki_contributors',
#      'get_wiki_page',
#       'get_wiki_pages',
#        'has_fetched',
#         'json_dict',
#          'leave_contributor',
#           'leave_moderator',
#            'reddit_session',
#             'refresh',
#              'remove_ban',
#               'remove_contributor',
#                'remove_moderator',
#                 'remove_mute',
#                  'remove_wiki_ban',
#                   'remove_wiki_contributor',
#                    'search',
#                     'select_flair',
#                      'send_message',
#                       'set_flair',
#                        'set_flair_csv',
#                         'set_settings',
#                          'set_stylesheet',
#                           'submit',
#                            'subscribe',
#                             'unsubscribe',
#                              'update_settings',
#                               'upload_image']

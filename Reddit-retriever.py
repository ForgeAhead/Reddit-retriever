import praw
import time
import Tkinter
import tkMessageBox

r = praw.Reddit('Keyword search in new posts per subreddit by /u/VeiledFortune')

r.login()
already_seen = []

keyword_list = ['Giveaway', 'giveaway', 'tip', 'Tip']

while True:
	subreddit = r.get_subreddit('dogecoin+Bitcoin')
	for submission in subreddit.get_new(limit=10):
		op_text = submission.title 
		has_keywords = any(word in op_text for word in keyword_list)
		if has_keywords and submission.id not in already_seen:
			msg = '[found a giveaway](%s)'% submission.short_link
			r.user.send_message('Username', msg)
			already_seen.append(submission.id)
			top = Tkinter.Tk()
			def hello():
   				tkMessageBox.showinfo("Found one", "Found one")

			B1 = Tkinter.Button(top, text = "Found one", command = hello)
			B1.pack()

			top.mainloop()
	time.sleep(900)

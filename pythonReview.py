def create_youtube_video(title,description):
	comments= {}
	youtube_dictionary = {"title" : title , "description" : description , "likes" : 0 , "dislikes" : 0 , "comments" : comments}
	return youtube_dictionary

def like (youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video


def dislike (youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1
	return youtube_video
def add_comment (youtube_video , username , comment_text):
	youtube_video["comments"][username]=comment_text
	return youtube_video

z=create_youtube_video("Carrot Cake!" , "how to bake a carrot cake")
like(z)
dislike(z)
add_comment(z,"Samar","What a great cake!")
print(z)

for i in range(495):
	like(z)

print(z)
def create_youtube_video(title,description,hashtags):
	vid = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}, "hashtags" : hashtags}
	return vid 


def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1

	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"] += 1

	return youtube_video	

def add_comment(youtube_video,username,comment_text):
	if "comments" in youtube_video:
		youtube_video["comments"][username] = comment_text
	return youtube_video

def similarity_to_video(vid1,vid2):
	y = 0
	z = 0
	if "hashtags" in vid1 and "hashtags" in vid2:
		for i in range(len(vid1["hashtags"])):
			for k in range(len(vid2["hashtags"])):
				if vid1["hashtags"][k] == vid2["hashtags"][i]:
					y += 1
				z += 1
	return str((y/z)*100) + "%"

def is_trending(vid):
	if "likes" in vid and "dislikes" in vid:
		if vid["likes"] > 20 and vid["likes"] > vid["dislikes"]:
			return "is"
		else:
			return "is not"


youtube_video = create_youtube_video("Nabih","Just nabih",[])
youtube_video = add_comment(youtube_video,"Idk23","Best Nabih video")
youtube_video = dislike(youtube_video)
youtube_video = like(youtube_video)
print("similarity to video is " + similarity_to_video(create_youtube_video("Nabih","Just nabih",["1","2"]),create_youtube_video("Nabih","Just nabih",["2","3"])))
print("the video " + is_trending(youtube_video) + " trending")






for i in range(494):
	youtube_video = like(youtube_video)	

print(youtube_video)
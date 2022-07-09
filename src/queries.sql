-- List idol's twitter metrics from most to least twitter followers 
SELECT  idols.username,
		idols.name,
		tw_metrics.author_id, 
		tw_metrics.followers_count, 
		tw_metrics.friends_count, 
		tw_metrics.tweets_count,
		tw_metrics.recorded_at
FROM twitter_metrics as tw_metrics
INNER JOIN idols
ON tw_metrics.author_id = idols.author_id
ORDER BY tw_metrics.followers_count DESC;

-- List idol's twitter posts from most to least current
SELECT idols.name, 
	   idols.username,
	   idols.author_id,
	   posts.created_at,
	   posts.twitter_post_id,
	   posts.text,
	   posts.image_path,
	   posts.youtube_link
FROM idols
INNER JOIN twitter_posts as posts
ON idols.author_id = posts.author_id
ORDER BY posts.created_at DESC;

-- List idol's YouTube subscriber count
SELECT idol.youtube_id, 
	   idol.title, 
	   yt.subscriber_count, 
	   yt.video_count, 
	   yt.view_count, 
	   yt.recorded_at
FROM youtube_idols as idol
INNER JOIN youtube_statistics as yt
ON idol.youtube_id = yt.youtube_id
ORDER BY idol.title ASC, yt.recorded_at DESC;
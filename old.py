docs = []
for post in posts:
    post_doc = Document(
        page_content=f"Title: {post['title']}"+ (f"; Content: {post['selftext']}" if len(post['selftext'])>0 else ""),
        metadata={"type":"post", "subreddit":post["subreddit"], "upvote_ratio":post["upvote_ratio"], "num_comments": post["num_comments"], "submission_flair":post["submission_flair"],"url":post["url"],},
        id=post["id"]
    )
    
    docs.append(post_doc)
    
    for comment in post['comments']:
        comment_doc = Document(page_content=f"Comment: {comment['body']}", metadata={"type":"comment"}, relationships={"node_id":post["id"]}, id= comment["id"])
        docs.append(comment_doc)
    
metadata_field_info = [
    AttributeInfo(
        name="type",
        description="The type of document, either post or comment",
        type="string",
    ),
    AttributeInfo(
        name="subreddit",
        description="The Subreddity the post is from",
        type="string",
    ),
    AttributeInfo(
        name="upvote_ratio",
        description="The post upvote ration on a scale of 0 to 1",
        type="float",
    ),
    AttributeInfo(
        name="num_comments",
        description="The number of comments on the post",
        type="int",
    ),
    AttributeInfo(
        name="submission_flair",
        description="A label of the post contents",
        type="string",
    ),
    AttributeInfo(
        name="url",
        description="The url of the post or of the referred resource",
        type="str",
    ),
]


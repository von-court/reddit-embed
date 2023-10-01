import streamlit as st
import praw

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=st.secrets["REDDIT_CLIENT_ID"],
    client_secret=st.secrets["REDDIT_CLIENT_SECRET"],
    user_agent="streamlit_app"
)

def main():
    st.title("Top 6 Listings in a Reddit Subreddit")

    # Input for subreddit name
    subreddit_name = st.text_input("Enter subreddit name:", "all")
    
    if subreddit_name:
        # Fetch top 6 listings
        subreddit = reddit.subreddit(subreddit_name)
        top_posts = list(subreddit.hot(limit=6))

        st.markdown("""
        <style>
            .post {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            .post-title {
                font-weight: bold;
                font-size: 1.2em;
                margin-bottom: 10px;
            }
            .post-stats {
                font-size: 0.9em;
                color: #888;
                margin-top: 10px;
            }
        </style>
        """, unsafe_allow_html=True)

        # Display the top 6 listings with styling
        for post in top_posts if not post.stickied:
            post_content = f"""
            <div class="post">
                <div class="post-title">{post.title}</div>
                <div>{post.selftext}</div>
                <div class="post-stats">🔼 {post.ups} | 💬 {post.num_comments}</div>
            </div>
            """
            st.markdown(post_content, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

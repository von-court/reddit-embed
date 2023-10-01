import streamlit as st
import praw

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="streamlit_app"
)

def main():
    st.title("Top 6 Listings in a Reddit Subreddit")

    # Input for subreddit name
    subreddit_name = st.text_input("Enter subreddit name:", "all")
    
    if subreddit_name:
        # Fetch top 6 listings
        subreddit = reddit.subreddit(subreddit_name)
        top_posts = list(subreddit.top(limit=6))

        # Display the top 6 listings
        for post in top_posts:
            st.write(f"**{post.title}**")
            st.write(post.selftext)
            st.write(f"🔼 {post.ups} | 💬 {post.num_comments}")
            st.write("---")

if __name__ == "__main__":
    main()

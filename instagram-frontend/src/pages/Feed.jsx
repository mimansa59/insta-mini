import { useEffect, useState } from "react";
import api from "../api/axios";
import PostCard from "/Users/mac/Desktop/insta/instagram-frontend/src/components/ PostCard.jsx";
export default function Feed() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const res = await api.get("/posts/feed");
        setPosts(res.data || []);
      } catch (error) {
        console.error("Error fetching feed:", error);
        setPosts([]);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-10 text-gray-500">
        Loading feed...
      </div>
    );
  }

  return (
    <div className="max-w-xl mx-auto mt-6 space-y-4">
      {posts.length === 0 ? (
        <p className="text-center text-gray-500">No posts found</p>
      ) : (
        posts.map((post) => (
          <PostCard key={post._id} post={post} />
        ))
      )}
    </div>
  );
}

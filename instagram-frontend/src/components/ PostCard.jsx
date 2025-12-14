// import api from "../api/axios";

// export default function PostCard({ post }) {
//   const likePost = async () => {
//     await api.post(`/posts/${post._id}/like`);
//     window.location.reload();
//   };

//   return (
//     <div className="border rounded mb-6 bg-white">
//       <img src={post.image_url} className="w-full" />

//       <div className="p-3">
//         <p className="font-semibold">
//           {post.user?.username || "User"}
//         </p>

//         <p className="text-sm">{post.caption}</p>

//         <button
//           onClick={likePost}
//           className="text-red-500 mt-2"
//         >
//           ❤️ {post.likes?.length || 0}
//         </button>
//       </div>
//     </div>
//   );
// }
import React from "react";

export default function PostCard({ post }) {
  if (!post) return null;

  return (
    <div className="border rounded-lg p-4 shadow bg-white">
      <h2 className="font-semibold text-lg">
        {post.title || "Untitled Post"}
      </h2>

      <p className="text-gray-600 text-sm mt-1">
        {post.content || "No content"}
      </p>
    </div>
  );
}

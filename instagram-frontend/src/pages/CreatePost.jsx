import { useState } from "react";
import api from "../api/axios";

export default function CreatePost() {
  const [image, setImage] = useState("");
  const [caption, setCaption] = useState("");

  const submit = async () => {
    await api.post("/posts", { image_url: image, caption });
    window.location.href = "/";
  };

  return (
    <div className="max-w-md mx-auto mt-10">
      <input className="border p-2 w-full mb-2" placeholder="Image URL"
        onChange={(e) => setImage(e.target.value)} />
      <textarea className="border p-2 w-full mb-2" placeholder="Caption"
        onChange={(e) => setCaption(e.target.value)} />
      <button onClick={submit} className="bg-purple-500 text-white w-full p-2">
        Post
      </button>
    </div>
  );
}

import { useState } from "react";
import api from "../api/axios";

export default function Signup() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });

  const submit = async () => {
    await api.post("/auth/signup", form);
    window.location.href = "/login";
  };

  return (
    <div className="flex h-screen justify-center items-center">
      <div className="w-80 p-6 border rounded">
        <h2 className="text-xl font-bold mb-4">Signup</h2>
        {["username", "email", "password"].map((f) => (
          <input key={f} className="border p-2 w-full mb-2" placeholder={f}
            onChange={(e) => setForm({ ...form, [f]: e.target.value })} />
        ))}
        <button onClick={submit} className="bg-green-500 text-white w-full p-2">
          Signup
        </button>
      </div>
    </div>
  );
}

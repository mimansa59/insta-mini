import React from "react";
import { useParams } from "react-router-dom";

export default function Profile() {
  const { id } = useParams();

  return (
    <div className="max-w-xl mx-auto mt-6">
      <h1 className="text-xl font-bold">Profile Page</h1>
      <p className="text-gray-600">User ID: {id}</p>
    </div>
  );
}

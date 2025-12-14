import { Link } from "react-router-dom";
import { logout } from "../utils/auth";

export default function Navbar() {
  return (
    <nav className="border-b bg-white sticky top-0 z-10">
      <div className="max-w-5xl mx-auto flex justify-between items-center px-4 py-3">

        {/* Logo */}
        <Link to="/" className="text-xl font-bold">
          Instagram
        </Link>

        {/* Menu */}
        <div className="flex gap-6 items-center text-sm font-medium">
          <Link to="/">Home</Link>
          <Link to="/create">Create</Link>
          <Link to="/profile/me">Profile</Link>

          <button
            onClick={logout}
            className="text-red-500 hover:underline"
          >
            Logout
          </button>
        </div>

      </div>
    </nav>
  );
}

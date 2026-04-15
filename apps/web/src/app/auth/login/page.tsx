export default function LoginPage() {
  return (
    <div className="flex flex-col min-h-screen px-4 safe-top safe-bottom">
      <div className="flex-1 flex flex-col justify-center max-w-sm mx-auto w-full py-12">
        <div className="mb-8 text-center">
          <span className="text-3xl font-bold text-indigo-600">SoberFuture</span>
          <p className="text-sm text-zinc-500 mt-2">Welcome back</p>
        </div>

        <form className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-zinc-700 mb-1.5">Email</label>
            <input
              type="email"
              autoComplete="email"
              className="w-full h-12 rounded-2xl border border-zinc-200 px-4 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              placeholder="you@example.com"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-zinc-700 mb-1.5">Password</label>
            <input
              type="password"
              autoComplete="current-password"
              className="w-full h-12 rounded-2xl border border-zinc-200 px-4 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              placeholder="••••••••"
            />
          </div>
          <button
            type="submit"
            className="w-full flex items-center justify-center h-12 rounded-2xl bg-indigo-600 text-white font-semibold text-base hover:bg-indigo-700 transition-colors"
          >
            Sign in
          </button>
        </form>

        <p className="text-center text-sm text-zinc-500 mt-6">
          No account?{" "}
          <a href="/auth/signup" className="text-indigo-600 font-medium">Create one free</a>
        </p>
      </div>
    </div>
  );
}

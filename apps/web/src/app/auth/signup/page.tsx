export default function SignupPage() {
  return (
    <div className="flex flex-col min-h-screen px-4 safe-top safe-bottom">
      <div className="flex-1 flex flex-col justify-center max-w-sm mx-auto w-full py-12">
        <div className="mb-8 text-center">
          <span className="text-3xl font-bold text-indigo-600">SoberFuture</span>
          <p className="text-sm text-zinc-500 mt-2">Start your recovery journal</p>
        </div>

        <form className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-zinc-700 mb-1.5">Name</label>
            <input
              type="text"
              autoComplete="name"
              className="w-full h-12 rounded-2xl border border-zinc-200 px-4 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              placeholder="Your first name"
            />
          </div>
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
              autoComplete="new-password"
              className="w-full h-12 rounded-2xl border border-zinc-200 px-4 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              placeholder="At least 8 characters"
            />
          </div>
          <button
            type="submit"
            className="w-full flex items-center justify-center h-12 rounded-2xl bg-indigo-600 text-white font-semibold text-base hover:bg-indigo-700 transition-colors"
          >
            Create journal
          </button>
        </form>

        <p className="text-xs text-zinc-400 text-center mt-4 leading-relaxed">
          By signing up you agree to our{" "}
          <a href="/terms" className="underline">Terms</a> and{" "}
          <a href="/privacy" className="underline">Privacy Policy</a>.
          Your journal is private and encrypted.
        </p>

        <p className="text-center text-sm text-zinc-500 mt-4">
          Already have an account?{" "}
          <a href="/auth/login" className="text-indigo-600 font-medium">Sign in</a>
        </p>
      </div>
    </div>
  );
}

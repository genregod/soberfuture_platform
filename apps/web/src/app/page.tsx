export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Nav */}
      <header className="sticky top-0 z-50 bg-white/90 backdrop-blur border-b border-zinc-100 safe-top">
        <div className="flex items-center justify-between px-4 h-14 max-w-2xl mx-auto w-full">
          <span className="text-lg font-bold text-indigo-600 tracking-tight">SoberFuture</span>
          <a
            href="/auth/login"
            className="flex items-center justify-center rounded-full bg-indigo-600 text-white text-sm font-medium px-5 h-10 hover:bg-indigo-700 transition-colors"
          >
            Sign in
          </a>
        </div>
      </header>

      <main className="flex-1">
        {/* Hero */}
        <section className="px-4 pt-12 pb-10 text-center max-w-lg mx-auto">
          <div className="inline-flex items-center gap-2 bg-indigo-50 text-indigo-700 text-xs font-semibold px-3 py-1.5 rounded-full mb-6">
            🌱 Your recovery, your story
          </div>
          <h1 className="text-4xl font-bold tracking-tight text-zinc-900 leading-tight mb-4">
            A journal that grows with your recovery
          </h1>
          <p className="text-lg text-zinc-500 leading-relaxed mb-8">
            Private, AI-assisted journaling designed for people in recovery. Reflect, track patterns, and share progress with your care team — on your terms.
          </p>
          <div className="flex flex-col gap-3 sm:flex-row sm:justify-center">
            <a
              href="/auth/signup"
              className="flex items-center justify-center h-12 rounded-2xl bg-indigo-600 text-white font-semibold text-base px-8 hover:bg-indigo-700 transition-colors"
            >
              Start journaling free
            </a>
            <a
              href="#how-it-works"
              className="flex items-center justify-center h-12 rounded-2xl border border-zinc-200 text-zinc-700 font-semibold text-base px-8 hover:bg-zinc-50 transition-colors"
            >
              How it works
            </a>
          </div>
        </section>

        {/* Feature cards */}
        <section id="how-it-works" className="px-4 pb-12 max-w-lg mx-auto">
          <div className="grid gap-4">
            {[
              { icon: "📓", title: "Daily check-ins", body: "Quick, guided prompts that take 2 minutes. Build a habit without the pressure." },
              { icon: "🔍", title: "Pattern insights", body: "AI surfaces trends in your mood, triggers, and milestones — privately, just for you." },
              { icon: "🤝", title: "Clinician sharing", body: "Optionally share summaries with your counselor or sponsor. You control what they see." },
              { icon: "🔒", title: "Private by default", body: "End-to-end encrypted. Your journal is yours. We never train AI on your entries." },
            ].map(({ icon, title, body }) => (
              <div key={title} className="flex gap-4 p-4 rounded-2xl bg-zinc-50 border border-zinc-100">
                <span className="text-2xl mt-0.5">{icon}</span>
                <div>
                  <h3 className="font-semibold text-zinc-900 mb-1">{title}</h3>
                  <p className="text-sm text-zinc-500 leading-relaxed">{body}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* CTA */}
        <section className="px-4 pb-16 max-w-lg mx-auto text-center">
          <div className="bg-indigo-600 rounded-3xl p-8">
            <h2 className="text-2xl font-bold text-white mb-2">Ready to start?</h2>
            <p className="text-indigo-200 text-sm mb-6">Free to use. No credit card required.</p>
            <a
              href="/auth/signup"
              className="inline-flex items-center justify-center h-12 rounded-2xl bg-white text-indigo-600 font-semibold text-base px-8 hover:bg-indigo-50 transition-colors"
            >
              Create your journal
            </a>
          </div>
        </section>
      </main>

      <footer className="border-t border-zinc-100 px-4 py-6 text-center text-xs text-zinc-400 safe-bottom">
        © 2026 SoberFuture · <a href="/privacy" className="underline">Privacy</a> · <a href="/terms" className="underline">Terms</a>
      </footer>
    </div>
  );
}

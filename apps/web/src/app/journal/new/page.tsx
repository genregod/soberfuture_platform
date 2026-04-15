import BottomNav from "@/components/BottomNav";

export default function NewEntryPage() {
  return (
    <div className="flex flex-col min-h-screen pb-20">
      <header className="sticky top-0 z-40 bg-white border-b border-zinc-100 safe-top">
        <div className="flex items-center gap-3 px-4 h-14 max-w-lg mx-auto">
          <a href="/journal" className="flex items-center justify-center w-9 h-9 rounded-full hover:bg-zinc-100 text-zinc-500 transition-colors">
            ←
          </a>
          <h1 className="text-base font-semibold text-zinc-900">Today&apos;s check-in</h1>
        </div>
      </header>

      <main className="flex-1 px-4 py-6 max-w-lg mx-auto w-full space-y-6">
        {/* Mood */}
        <section>
          <p className="text-sm font-medium text-zinc-700 mb-3">How are you feeling right now?</p>
          <div className="flex justify-between gap-2">
            {["😔", "😕", "😐", "🙂", "😊"].map((emoji, i) => (
              <button
                key={i}
                className="flex-1 flex flex-col items-center justify-center h-14 rounded-2xl border border-zinc-200 text-2xl hover:border-indigo-400 hover:bg-indigo-50 transition-colors"
              >
                {emoji}
              </button>
            ))}
          </div>
        </section>

        {/* Prompt */}
        <section>
          <p className="text-sm font-medium text-zinc-700 mb-2">
            What&apos;s one thing you&apos;re grateful for today?
          </p>
          <textarea
            className="w-full rounded-2xl border border-zinc-200 p-4 text-sm text-zinc-900 placeholder:text-zinc-400 resize-none focus:outline-none focus:ring-2 focus:ring-indigo-400 min-h-[120px]"
            placeholder="Write freely — this is just for you..."
          />
        </section>

        <button className="w-full flex items-center justify-center h-12 rounded-2xl bg-indigo-600 text-white font-semibold text-base hover:bg-indigo-700 transition-colors">
          Save entry
        </button>
      </main>

      <BottomNav active="/journal/new" />
    </div>
  );
}

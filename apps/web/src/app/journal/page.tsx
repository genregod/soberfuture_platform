import BottomNav from "@/components/BottomNav";

export default function JournalPage() {
  return (
    <div className="flex flex-col min-h-screen pb-20">
      <header className="sticky top-0 z-40 bg-white border-b border-zinc-100 safe-top">
        <div className="flex items-center justify-between px-4 h-14 max-w-lg mx-auto">
          <h1 className="text-base font-semibold text-zinc-900">My Journal</h1>
          <span className="text-xs text-zinc-400">Day 1</span>
        </div>
      </header>

      <main className="flex-1 px-4 py-6 max-w-lg mx-auto w-full">
        {/* Empty state */}
        <div className="flex flex-col items-center justify-center text-center py-20 gap-4">
          <span className="text-5xl">📓</span>
          <h2 className="text-lg font-semibold text-zinc-800">Your journal is empty</h2>
          <p className="text-sm text-zinc-500 max-w-xs">
            Start your first check-in. It only takes a couple of minutes.
          </p>
          <a
            href="/journal/new"
            className="flex items-center justify-center h-12 rounded-2xl bg-indigo-600 text-white font-semibold text-sm px-8 hover:bg-indigo-700 transition-colors"
          >
            Start check-in
          </a>
        </div>
      </main>

      <BottomNav active="/journal" />
    </div>
  );
}

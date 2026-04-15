/* Mobile-first bottom nav shell for the journal app */
import Link from "next/link";

const NAV = [
  { href: "/journal", label: "Journal", icon: "📓" },
  { href: "/journal/new", label: "Check in", icon: "✏️" },
  { href: "/insights", label: "Insights", icon: "🔍" },
  { href: "/profile", label: "Profile", icon: "👤" },
];

export default function BottomNav({ active }: { active: string }) {
  return (
    <nav className="fixed bottom-0 inset-x-0 bg-white border-t border-zinc-100 safe-bottom z-50">
      <div className="flex max-w-lg mx-auto">
        {NAV.map(({ href, label, icon }) => (
          <Link
            key={href}
            href={href}
            className={`flex flex-1 flex-col items-center justify-center gap-0.5 py-2 text-xs font-medium transition-colors ${
              active === href ? "text-indigo-600" : "text-zinc-400 hover:text-zinc-700"
            }`}
          >
            <span className="text-xl leading-none">{icon}</span>
            {label}
          </Link>
        ))}
      </div>
    </nav>
  );
}

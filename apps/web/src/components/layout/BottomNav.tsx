import { NavLink } from 'react-router-dom'
import { Home, LayoutGrid, Shirt, ShoppingBag, User } from 'lucide-react'
import { cn } from '@/lib/utils'

const navItems = [
  { to: '/', icon: Home, label: 'Today' },
  { to: '/closet', icon: LayoutGrid, label: 'Closet' },
  { to: '/outfits', icon: Shirt, label: 'Outfits' },
  { to: '/discover', icon: ShoppingBag, label: 'Shop' },
  { to: '/profile', icon: User, label: 'Profile' },
]

export function BottomNav() {
  return (
    <nav className="fixed bottom-0 left-0 right-0 z-50 border-t border-border bg-white/80 backdrop-blur-lg safe-area-bottom">
      <div className="mx-auto flex max-w-md items-center justify-around py-2">
        {navItems.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            className={({ isActive }) =>
              cn(
                'flex flex-col items-center gap-0.5 px-3 py-1 text-xs transition-colors',
                isActive
                  ? 'text-rose-400 font-medium'
                  : 'text-charcoal-300 hover:text-charcoal-500'
              )
            }
          >
            <Icon className="h-5 w-5" />
            <span>{label}</span>
          </NavLink>
        ))}
      </div>
    </nav>
  )
}

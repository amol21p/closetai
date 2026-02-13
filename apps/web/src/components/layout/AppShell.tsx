import { Outlet } from 'react-router-dom'
import { BottomNav } from './BottomNav'

export function AppShell() {
  return (
    <div className="mx-auto min-h-screen max-w-md bg-cream">
      <main className="pb-20">
        <Outlet />
      </main>
      <BottomNav />
    </div>
  )
}

import { useNavigate } from 'react-router-dom'
import { ChevronRight, LogOut, Settings, Palette, Ruler, ShoppingBag, Shield } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { useAuthStore } from '@/stores/auth'
import { getInitials } from '@/lib/utils'

export default function Profile() {
  const navigate = useNavigate()
  const { profile, signOut } = useAuthStore()

  const handleSignOut = async () => {
    await signOut()
    navigate('/welcome')
  }

  const menuItems = [
    { icon: Palette, label: 'Style DNA', description: 'Your evolving style profile' },
    { icon: Ruler, label: 'Body Profile', description: 'Measurements & body type' },
    { icon: ShoppingBag, label: 'Subscription', description: 'Free plan' },
    { icon: Settings, label: 'Preferences', description: 'App settings' },
    { icon: Shield, label: 'Privacy & Data', description: 'Manage your data' },
  ]

  return (
    <div className="px-4 py-6">
      {/* Profile Header */}
      <div className="mb-6 flex items-center gap-4">
        <div className="flex h-16 w-16 items-center justify-center rounded-full bg-rose-100 text-rose-400">
          <span className="text-xl font-semibold">
            {profile?.name ? getInitials(profile.name) : '?'}
          </span>
        </div>
        <div>
          <h1 className="font-heading text-xl font-bold text-charcoal">
            {profile?.name ?? 'Your Profile'}
          </h1>
          <p className="text-sm text-charcoal-400">{profile?.email ?? ''}</p>
        </div>
      </div>

      {/* Style DNA Preview */}
      <Card className="mb-6 border-gold-200 bg-gradient-to-br from-gold-50 to-cream">
        <CardContent className="py-5">
          <p className="text-xs font-medium uppercase tracking-wider text-gold-600">
            Your Style DNA
          </p>
          <p className="mt-2 font-heading text-lg font-semibold text-charcoal">
            Complete onboarding to unlock
          </p>
          <p className="mt-1 text-sm text-charcoal-400">
            Take the style quiz to discover your unique style archetype, power colors, and more.
          </p>
          <Button size="sm" className="mt-4">
            Start Style Quiz
          </Button>
        </CardContent>
      </Card>

      {/* Menu */}
      <div className="space-y-1">
        {menuItems.map(({ icon: Icon, label, description }) => (
          <button
            key={label}
            className="flex w-full items-center gap-4 rounded-xl p-3 text-left transition-colors hover:bg-white"
          >
            <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg bg-cream-200">
              <Icon className="h-5 w-5 text-charcoal-400" />
            </div>
            <div className="flex-1">
              <p className="text-sm font-medium text-charcoal">{label}</p>
              <p className="text-xs text-charcoal-300">{description}</p>
            </div>
            <ChevronRight className="h-4 w-4 text-charcoal-200" />
          </button>
        ))}
      </div>

      {/* Sign Out */}
      <Button
        variant="ghost"
        className="mt-8 w-full text-charcoal-400"
        onClick={handleSignOut}
      >
        <LogOut className="mr-2 h-4 w-4" />
        Sign Out
      </Button>
    </div>
  )
}

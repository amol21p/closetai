import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { useAuthStore } from '@/stores/auth'
import { Sun } from 'lucide-react'

export default function Home() {
  const { profile } = useAuthStore()
  const firstName = profile?.name?.split(' ')[0] ?? 'there'

  return (
    <div className="px-4 py-6">
      {/* Header */}
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="font-heading text-2xl font-bold text-charcoal">
            Good morning, {firstName}
          </h1>
          <div className="mt-1 flex items-center gap-2 text-sm text-charcoal-400">
            <Sun className="h-4 w-4 text-gold" />
            <span>28°C Mumbai</span>
          </div>
        </div>
        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-rose-100 text-rose-400">
          <span className="text-sm font-medium">
            {profile?.name?.[0]?.toUpperCase() ?? '?'}
          </span>
        </div>
      </div>

      {/* Today's Outfit - Placeholder */}
      <Card className="mb-4">
        <CardHeader>
          <CardTitle>Today's Outfit</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex h-48 items-center justify-center rounded-lg bg-cream-200 text-charcoal-300">
            <p className="text-center text-sm">
              Add items to your closet to get<br />personalized outfit suggestions
            </p>
          </div>
          <div className="mt-4 flex gap-2">
            <Button size="sm" className="flex-1">Wear This</Button>
            <Button size="sm" variant="outline" className="flex-1">Show Another</Button>
          </div>
        </CardContent>
      </Card>

      {/* Quick Stats */}
      <Card className="mb-4">
        <CardContent className="py-4">
          <div className="flex items-center justify-between text-sm">
            <span className="text-charcoal-400">Items worn this month</span>
            <span className="font-medium text-charcoal">0 / 0</span>
          </div>
          <div className="mt-2 h-2 rounded-full bg-cream-200">
            <div className="h-2 rounded-full bg-rose-300" style={{ width: '0%' }} />
          </div>
        </CardContent>
      </Card>

      {/* Style Tip */}
      <Card>
        <CardContent className="py-4">
          <p className="text-xs font-medium uppercase tracking-wider text-gold">
            Style Tip
          </p>
          <p className="mt-2 text-sm text-charcoal-500">
            Start by adding your most-worn items first. This helps the AI understand
            your actual style, not just what's in your closet.
          </p>
        </CardContent>
      </Card>
    </div>
  )
}

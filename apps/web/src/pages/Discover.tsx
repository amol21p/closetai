import { Search, Camera, Sparkles } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { Input } from '@/components/ui/input'

export default function Discover() {
  return (
    <div className="px-4 py-6">
      {/* Header */}
      <h1 className="mb-4 font-heading text-2xl font-bold text-charcoal">
        Smart Shopping
      </h1>

      {/* Search */}
      <div className="relative mb-6">
        <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-charcoal-300" />
        <Input placeholder="Search for items..." className="pl-10" />
      </div>

      {/* What's Missing */}
      <div className="mb-6">
        <h2 className="mb-3 font-heading text-lg font-semibold text-charcoal">
          What's Missing
        </h2>
        <Card className="mb-3 border-gold-200 bg-gold-50">
          <CardContent className="py-4">
            <div className="flex items-start gap-3">
              <Sparkles className="mt-0.5 h-5 w-5 text-gold" />
              <div>
                <p className="text-sm font-medium text-charcoal">
                  Add items to your closet to unlock gap analysis
                </p>
                <p className="mt-1 text-xs text-charcoal-400">
                  We'll identify what's missing and show you items that unlock the most new outfits.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Before You Buy */}
      <Card className="mb-6">
        <CardContent className="flex items-center gap-4 py-4">
          <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-rose-50">
            <Camera className="h-6 w-6 text-rose-400" />
          </div>
          <div className="flex-1">
            <p className="text-sm font-medium text-charcoal">Before You Buy</p>
            <p className="text-xs text-charcoal-400">
              About to buy something? Scan it to check if you already own something similar.
            </p>
          </div>
          <Button size="sm" variant="outline">
            Scan
          </Button>
        </CardContent>
      </Card>

      {/* Placeholder Recommendations */}
      <h2 className="mb-3 font-heading text-lg font-semibold text-charcoal">
        Recommended For You
      </h2>
      <div className="grid grid-cols-2 gap-3">
        {[1, 2, 3, 4].map((i) => (
          <Card key={i} className="overflow-hidden">
            <div className="aspect-square bg-cream-200" />
            <CardContent className="p-3">
              <div className="mb-1 h-3 w-20 rounded bg-cream-200" />
              <div className="h-3 w-14 rounded bg-cream-200" />
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}

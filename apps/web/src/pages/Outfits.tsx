import { Plus, Shuffle } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'

export default function Outfits() {
  return (
    <div className="px-4 py-6">
      {/* Header */}
      <div className="mb-6 flex items-center justify-between">
        <h1 className="font-heading text-2xl font-bold text-charcoal">Outfits</h1>
        <div className="flex gap-2">
          <Button size="icon" variant="outline" className="h-10 w-10 rounded-full">
            <Shuffle className="h-4 w-4" />
          </Button>
          <Button size="icon" className="h-10 w-10 rounded-full">
            <Plus className="h-5 w-5" />
          </Button>
        </div>
      </div>

      {/* Empty State */}
      <Card className="mt-4">
        <CardContent className="flex flex-col items-center py-12 text-center">
          <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-rose-50">
            <Shuffle className="h-8 w-8 text-rose-300" />
          </div>
          <h3 className="font-heading text-lg font-semibold text-charcoal">
            No outfits yet
          </h3>
          <p className="mt-2 max-w-xs text-sm text-charcoal-300">
            Add items to your closet first, then our AI will start creating outfit combinations for you.
          </p>
          <Button className="mt-6" size="sm">
            Create Your First Outfit
          </Button>
        </CardContent>
      </Card>
    </div>
  )
}

import { useEffect } from 'react'
import { Plus, Camera, Upload } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { useWardrobeStore } from '@/stores/wardrobe'
import { cn } from '@/lib/utils'

const categories = [
  'All', 'Tops', 'Bottoms', 'Dresses', 'Ethnic', 'Outerwear',
  'Shoes', 'Bags', 'Accessories', 'Jewelry',
]

export default function Closet() {
  const { items, selectedCategory, fetchItems, setCategory } = useWardrobeStore()

  useEffect(() => {
    fetchItems()
  }, [fetchItems])

  const filteredItems = selectedCategory && selectedCategory !== 'All'
    ? items.filter((item) => item.category.toLowerCase() === selectedCategory.toLowerCase())
    : items

  return (
    <div className="px-4 py-6">
      {/* Header */}
      <div className="mb-4 flex items-center justify-between">
        <div>
          <h1 className="font-heading text-2xl font-bold text-charcoal">My Closet</h1>
          <p className="text-sm text-charcoal-400">{items.length} items</p>
        </div>
        <Button size="icon" className="h-10 w-10 rounded-full">
          <Plus className="h-5 w-5" />
        </Button>
      </div>

      {/* Category Filter */}
      <div className="hide-scrollbar mb-4 flex gap-2 overflow-x-auto">
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setCategory(cat === 'All' ? null : cat)}
            className={cn(
              'whitespace-nowrap rounded-full px-4 py-1.5 text-sm transition-colors',
              (!selectedCategory && cat === 'All') || selectedCategory === cat
                ? 'bg-rose-300 text-white'
                : 'bg-white text-charcoal-400 border border-charcoal-100'
            )}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Items Grid or Empty State */}
      {filteredItems.length === 0 ? (
        <Card className="mt-8">
          <CardContent className="flex flex-col items-center py-12 text-center">
            <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-rose-50">
              <Camera className="h-8 w-8 text-rose-300" />
            </div>
            <h3 className="font-heading text-lg font-semibold text-charcoal">
              Add your first item!
            </h3>
            <p className="mt-2 max-w-xs text-sm text-charcoal-300">
              Take a photo or upload from your gallery. Our AI will automatically detect the category, colors, and style.
            </p>
            <div className="mt-6 flex gap-3">
              <Button size="sm">
                <Camera className="mr-2 h-4 w-4" />
                Take Photo
              </Button>
              <Button size="sm" variant="outline">
                <Upload className="mr-2 h-4 w-4" />
                Upload
              </Button>
            </div>
          </CardContent>
        </Card>
      ) : (
        <div className="grid grid-cols-2 gap-3">
          {filteredItems.map((item) => (
            <Card key={item.id} className="overflow-hidden">
              <div className="aspect-square bg-cream-200">
                <img
                  src={item.image_url}
                  alt={item.name ?? 'Wardrobe item'}
                  className="h-full w-full object-cover"
                />
              </div>
              <CardContent className="p-3">
                <p className="truncate text-sm font-medium text-charcoal">
                  {item.name ?? item.subcategory ?? item.category}
                </p>
                <p className="text-xs text-charcoal-300">
                  Worn {item.times_worn}x
                </p>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}

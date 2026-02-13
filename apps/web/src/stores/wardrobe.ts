import { create } from 'zustand'
import type { WardrobeItem } from '@/types'
import { supabase } from '@/lib/supabase'

interface WardrobeState {
  items: WardrobeItem[]
  loading: boolean
  selectedCategory: string | null
  fetchItems: () => Promise<void>
  addItem: (item: Partial<WardrobeItem> & { image_url: string; category: string }) => Promise<WardrobeItem>
  updateItem: (id: string, updates: Partial<WardrobeItem>) => Promise<void>
  deleteItem: (id: string) => Promise<void>
  setCategory: (category: string | null) => void
}

export const useWardrobeStore = create<WardrobeState>((set, get) => ({
  items: [],
  loading: false,
  selectedCategory: null,

  fetchItems: async () => {
    set({ loading: true })
    const { data, error } = await supabase
      .from('wardrobe_items')
      .select('*')
      .eq('is_archived', false)
      .order('created_at', { ascending: false })

    if (error) throw error
    set({ items: (data ?? []) as WardrobeItem[], loading: false })
  },

  addItem: async (item) => {
    const { data, error } = await supabase
      .from('wardrobe_items')
      .insert(item)
      .select()
      .single()

    if (error) throw error
    const newItem = data as WardrobeItem
    set({ items: [newItem, ...get().items] })
    return newItem
  },

  updateItem: async (id, updates) => {
    const { error } = await supabase
      .from('wardrobe_items')
      .update(updates)
      .eq('id', id)

    if (error) throw error
    set({
      items: get().items.map((item) =>
        item.id === id ? { ...item, ...updates } : item
      ),
    })
  },

  deleteItem: async (id) => {
    const { error } = await supabase
      .from('wardrobe_items')
      .update({ is_archived: true })
      .eq('id', id)

    if (error) throw error
    set({ items: get().items.filter((item) => item.id !== id) })
  },

  setCategory: (category) => set({ selectedCategory: category }),
}))

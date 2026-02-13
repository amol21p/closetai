import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { ArrowLeft } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { useAuthStore } from '@/stores/auth'

export default function Signup() {
  const navigate = useNavigate()
  const { signUpWithEmail, loading } = useAuthStore()
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    try {
      await signUpWithEmail(email, password, name)
      navigate('/onboarding')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Signup failed')
    }
  }

  return (
    <div className="min-h-screen bg-cream px-6 py-8">
      <button onClick={() => navigate(-1)} className="mb-8 text-charcoal-400">
        <ArrowLeft className="h-6 w-6" />
      </button>

      <h1 className="font-heading text-3xl font-bold text-charcoal">
        Create account
      </h1>
      <p className="mt-2 text-charcoal-400">
        Let's build your style profile
      </p>

      <form onSubmit={handleSubmit} className="mt-8 space-y-4">
        {error && (
          <div className="rounded-lg bg-red-50 p-3 text-sm text-red-600">
            {error}
          </div>
        )}
        <div>
          <label className="mb-1.5 block text-sm font-medium text-charcoal-600">
            Name
          </label>
          <Input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Your name"
            required
          />
        </div>
        <div>
          <label className="mb-1.5 block text-sm font-medium text-charcoal-600">
            Email
          </label>
          <Input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="you@example.com"
            required
          />
        </div>
        <div>
          <label className="mb-1.5 block text-sm font-medium text-charcoal-600">
            Password
          </label>
          <Input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Min 6 characters"
            minLength={6}
            required
          />
        </div>
        <Button type="submit" size="lg" className="w-full" disabled={loading}>
          {loading ? 'Creating account...' : 'Create Account'}
        </Button>
      </form>

      <p className="mt-6 text-center text-sm text-charcoal-400">
        Already have an account?{' '}
        <Link to="/login" className="font-medium text-rose-400">
          Sign in
        </Link>
      </p>
    </div>
  )
}

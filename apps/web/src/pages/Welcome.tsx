import { useNavigate } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { useAuthStore } from '@/stores/auth'

export default function Welcome() {
  const navigate = useNavigate()
  const { signInWithGoogle, loading } = useAuthStore()

  const handleGoogleLogin = async () => {
    try {
      await signInWithGoogle()
    } catch {
      // OAuth redirect will handle navigation
    }
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-between bg-cream px-6 py-12">
      {/* Hero */}
      <div className="flex flex-1 flex-col items-center justify-center text-center">
        <div className="mb-6 flex h-20 w-20 items-center justify-center rounded-2xl bg-rose-300 shadow-lg">
          <span className="text-3xl text-white font-heading font-bold">C</span>
        </div>
        <h1 className="font-heading text-4xl font-bold text-charcoal">
          ClosetAI
        </h1>
        <p className="mt-3 text-lg text-charcoal-400">
          Your closet, but smarter.
        </p>
        <p className="mt-2 max-w-xs text-sm text-charcoal-300">
          AI-powered personal styling that knows your wardrobe, your body, and your life.
        </p>
      </div>

      {/* Auth Buttons */}
      <div className="w-full max-w-sm space-y-3">
        <Button
          size="lg"
          className="w-full"
          onClick={handleGoogleLogin}
          disabled={loading}
        >
          Continue with Google
        </Button>
        <Button
          size="lg"
          variant="outline"
          className="w-full"
          onClick={() => navigate('/login')}
        >
          Continue with Email
        </Button>
        <p className="text-center text-xs text-charcoal-300">
          By continuing, you agree to our Terms of Service and Privacy Policy.
        </p>
      </div>
    </div>
  )
}

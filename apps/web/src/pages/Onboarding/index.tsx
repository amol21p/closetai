import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowLeft, ArrowRight } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { cn } from '@/lib/utils'

const steps = [
  { title: 'About You', description: 'Basic info to personalize your experience' },
  { title: 'Your Colors', description: 'Discover your power colors' },
  { title: 'Your Style', description: 'What vibes speak to you?' },
  { title: 'Your Life', description: 'Occasions that matter to you' },
  { title: 'Your Closet', description: 'Let\'s see what you\'ve got!' },
  { title: 'Style DNA', description: 'Your unique style profile' },
]

export default function Onboarding() {
  const navigate = useNavigate()
  const [currentStep, setCurrentStep] = useState(0)

  const handleNext = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1)
    } else {
      navigate('/')
    }
  }

  const handleBack = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1)
    }
  }

  return (
    <div className="flex min-h-screen flex-col bg-cream px-6 py-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        {currentStep > 0 ? (
          <button onClick={handleBack} className="text-charcoal-400">
            <ArrowLeft className="h-6 w-6" />
          </button>
        ) : (
          <div />
        )}
        <button
          onClick={() => navigate('/')}
          className="text-sm text-charcoal-300"
        >
          Skip
        </button>
      </div>

      {/* Progress */}
      <div className="mt-6 flex gap-1.5">
        {steps.map((_, i) => (
          <div
            key={i}
            className={cn(
              'h-1 flex-1 rounded-full transition-colors',
              i <= currentStep ? 'bg-rose-300' : 'bg-charcoal-100'
            )}
          />
        ))}
      </div>

      {/* Step Content */}
      <div className="mt-8 flex-1">
        <p className="text-xs font-medium uppercase tracking-wider text-rose-400">
          Step {currentStep + 1} of {steps.length}
        </p>
        <h1 className="mt-2 font-heading text-3xl font-bold text-charcoal">
          {steps[currentStep].title}
        </h1>
        <p className="mt-2 text-charcoal-400">
          {steps[currentStep].description}
        </p>

        {/* Step-specific content placeholder */}
        <div className="mt-8 flex h-64 items-center justify-center rounded-2xl bg-white text-center text-sm text-charcoal-300">
          <p>
            Step {currentStep + 1} content<br />
            (will be implemented in Phase 1)
          </p>
        </div>
      </div>

      {/* Footer */}
      <Button size="lg" className="mt-6 w-full" onClick={handleNext}>
        {currentStep < steps.length - 1 ? (
          <>
            Continue
            <ArrowRight className="ml-2 h-4 w-4" />
          </>
        ) : (
          "Let's Go!"
        )}
      </Button>
    </div>
  )
}

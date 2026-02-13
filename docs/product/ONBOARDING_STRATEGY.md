# ClosetAI - Onboarding Strategy: Solving the Closet Digitization Problem

## TL;DR

The #1 killer of wardrobe apps is onboarding friction. Photographing 50-100 items takes 3-4 hours — over 70% of users abandon before adding 15 items. We flip the model: instead of "set up your closet, then get value," we do "get value immediately, closet builds itself." The OOTD-first approach (photograph today's outfit, AI extracts 3-4 items) builds the closet passively through daily use. Target: first outfit suggestion within 3 minutes of install.

---

## The Problem: Why Wardrobe Apps Die at Onboarding

### The Math That Kills

- Average woman owns **70-100+ clothing items**
- Photographing each item individually takes **~2 minutes** (Stylebook power users confirm this)
- That's **3-4 hours** of tedious work for a 100-item closet
- Over **70% of users abandon** account creation flows that take >20 minutes (Visa research)
- Fashion apps have an average 90-day retention rate of only **28%**
- Customer acquisition costs for fashion apps are **up 35% since 2022** — costing upwards of $15/active user

### The "5-10 Item Wall"

Consistent pattern across app store reviews: users add 5-10 items, don't see enough value from outfit suggestions with so few items, and abandon. The app needs a critical mass of items to generate useful outfits, but users won't reach that mass because the process is too painful.

This is the **cold start death spiral:**
```
Few items → Bad suggestions → "This app doesn't work" → Abandon
     ↑                                                        |
     └────────────────────────────────────────────────────────┘
```

### What Existing Apps Do (And Why It Fails)

| App | Onboarding Approach | Why It Struggles |
|-----|-------------------|-----------------|
| **Stylebook** | Manual one-by-one photography + tagging | 2 min/item, 100 items = 3+ hours. Only power users survive. |
| **Acloset** | Manual photography, manual tags | Same friction. 1M+ downloads but low retention. |
| **Whering** | Manual photography + AI background removal | Caps batch uploads at 15 items. 9M+ users but reviews cite frustration with upload process. |
| **Cladwell** | AI-assisted tagging ("snap and let AI do the rest") | Better — reduces per-item time to ~15-20 seconds. Average user catalogs 125+ items (but this is survivorship bias — reflects users who stuck around, not those who churned). |

### The Stitch Fix Approach (Avoid the Problem Entirely)

Stitch Fix never asked users to digitize their closet. Their approach:

- **80-90 question style quiz** collecting 90+ data points: size, body shape (apple/pear/rectangle), waist level, style preferences, budget, lifestyle, comfort with baring certain body parts
- **Style Shuffle** ("Tinder for clothes"): swipe right/left on outfit images to train the algorithm on visual preferences
- **No closet inventory required**: infers preferences from quiz + swipe behavior, not existing wardrobe
- **5-item "Fix" shipments**: users try items at home for 3 days, keep what they want, return the rest — feedback on each item trains the model
- Users get value (curated clothing at their door) without photographing a single item

**Their lesson:** The style quiz IS the product experience, not a barrier to it. Immediate value delivery matters more than data completeness.

### Sources

- [Digital Wardrobe Management Statistics](https://bestcolorfulsocks.com/blogs/news/digital-wardrobe-management-statistics)
- [Wardrobe App Market Outlook 2025-2032](https://www.intelmarketresearch.com/wardrobe-app-2025-2032-667-1709)
- [Stylebook App Review: 10+ Years](https://www.cottoncashmerecathair.com/blog/2020/4/10/how-i-catalog-my-closet-and-track-what-i-wear-with-the-stylebook-app-review)
- [Whering UX Masterclass](https://medium.com/@HannahFberg/whering-a-masterclass-in-ux-understanding-the-5-elements-of-ux-through-this-digital-closet-app-3a1fb6663bd2)
- [How Stitch Fix Uses AI](https://roundtable.datascience.salon/how-stitch-fix-uses-ai-to-predict-what-style-a-customer-will-love)
- [How Stitch Fix Style Shuffle Works](https://qz.com/quartzy/1603872/how-stitch-fixs-style-shuffle-learns-your-style)
- [Cladwell vs Acloset](https://www.myindyx.com/versus/acloset-cladwell)

---

## Our Solution: The Closet That Builds Itself

### The Core Insight

Don't ask users to catalog their closet. Ask them to **live their life** — the closet builds passively.

```
OLD MODEL (every other wardrobe app):
  "Photograph your entire closet" → [3-4 hours of pain] → Get suggestions
  Result: 70% abandon before adding 15 items

OUR MODEL:
  "Take a photo of today's outfit" → [30 seconds] → Get tomorrow's suggestion
  Result: 15-25 items after 7 days, with zero extra effort
```

### Multiple Input Channels (All Feeding the Same Closet)

```
                        ┌─────────────────┐
                        │  Digital Closet  │
                        │   (wardrobe DB)  │
                        └────────▲────────┘
                                 │
        ┌────────────────────────┼───────────────────────────┐
        │                        │                            │
   ┌────┴────┐             ┌────┴────┐               ┌──────┴──────┐
   │  OOTD   │             │ Flatlay │               │   Import    │
   │ Selfie  │             │  Batch  │               │  Channels   │
   │(primary)│             │  Photo  │               │             │
   └─────────┘             └─────────┘               └─────────────┘
   Mirror selfie →         5 items on bed →          • Screenshot share
   AI segments 3-4         AI detects each           • Gmail receipts
   items per photo         item separately            • Myntra/Amazon
   30 sec/outfit           2 min for 5 items            order history
   Daily habit             Batch sessions             One-time imports
```

### The Minimum Viable Closet

You don't need 50 items to start giving value:

| Items | What Unlocks | How Long | Experience |
|-------|-------------|----------|------------|
| **0** | Style quiz results, inspiration feed, community browsing | Instant | "Discover your style" |
| **1** | "What goes with this?" suggestions | 30 seconds | First value moment |
| **3-5** | Basic mix-and-match outfit generation | 2 days of OOTD | "Wow, I didn't think of that combo" |
| **10** | Meaningful outfit calendar, weather-based suggestions | 4-5 days | Habit-forming value |
| **20-30** | Full capsule wardrobe management, gap analysis | 2 weeks | Power user territory |
| **50+** | Cost-per-wear tracking, seasonal rotation, full analytics | 1 month | Committed user |

**Target: first outfit suggestion within 3 minutes of install.** Spotify gets you listening in under 2 minutes. We need to be that fast.

### Sources

- [Time to Value](https://productled.com/blog/time-to-value) — ProductLed
- [Progressive Onboarding](https://userpilot.com/blog/progressive-onboarding/) — Userpilot
- [How Many Items in a Capsule Wardrobe](https://theeleganceedit.com/how-many-items-should-be-in-a-capsule-wardrobe/)
- [Cladwell Getting Started Guide](https://cladwell.com/style-tips/getting-started)

---

## Channel 1: OOTD Selfie (Primary — Day 1)

### Why This Is the Primary Path

The OOTD (outfit of the day) approach is the single most promising solution for our use case:

1. **Already a habit**: OOTD culture is massive on Instagram in India — our target demographic already takes mirror selfies daily
2. **Captures what matters**: Adds items they actually WEAR, not everything they own (including items they'll never touch)
3. **Daily value loop**: Each selfie adds items AND generates tomorrow's suggestion — it's both input and output
4. **Zero extra effort**: The selfie IS the onboarding. No "setup" step, no catalog session
5. **Natural growth**: 3-4 items per selfie × 30 days = 50-80 items, built passively

### Technical Pipeline

```
1. User takes full-body mirror selfie
         ↓
2. SegFormer B2 segments image into clothing regions
   (top, bottom, dress, outerwear, shoes, accessories, dupatta, saree)
         ↓
3. Each segment → background removal (rembg BiRefNet)
         ↓
4. Each segment → Claude Vision API for attributes:
   - Category, subcategory (kurta, blouse, jeans, saree)
   - Dominant colors, pattern, material
   - Formality level, occasion tags
   - Indian garment type detection
         ↓
5. Present extracted items to user for quick confirm
   (1 tap to confirm, swipe to adjust any field)
         ↓
6. Items saved to wardrobe with clean extracted photos
```

### Fashion Segmentation Models: Full Technical Comparison

| Model | Categories | Accuracy | Speed | Best For |
|-------|-----------|----------|-------|----------|
| **SegFormer B2 (ATR dataset)** | 18 categories | 80% mean accuracy, 69% mIoU | Fast (27.4M params) | Semantic segmentation of worn clothing |
| **SegFormer B3 (ATR dataset)** | 18 categories | Similar to B2, slightly better | Moderate | Higher quality at slight speed cost |
| **Spectrum (2025)** | Body parts + clothing | State-of-the-art | Moderate | Unified parsing, multi-person scenes |
| **YOLOv8-seg (DeepFashion2)** | 13 categories | ~70-75% mAP | Real-time | Detection + coarse segmentation |
| **DSA-YOLO (2024)** | DeepFashion2 categories | +2.6% over YOLOv8 baseline | Real-time | Multi-scale clothing detection |
| **Grounding DINO + SAM2** | Open-vocabulary | 52.5 AP zero-shot (COCO) | ~1-2s/image | Flexible detection + precise masks |

**Our recommendation: SegFormer B2** for the OOTD pipeline because:
- Best accuracy for segmenting clothing on a person (which is exactly our use case)
- 18 categories covers all Indian garment types (upper body, lower body, full body, hat, face, etc.)
- Fast enough for real-time mobile use (27.4M parameters)
- Open source, available on HuggingFace (`mattmdjaga/segformer_b2_clothes`)

### Accuracy Expectations

| Photo Quality | Item Detection Rate | Notes |
|--------------|-------------------|-------|
| Clear, well-lit mirror selfie | 85-90% | Ideal case |
| Moderate lighting, clean background | 75-85% | Most common real-world scenario |
| Dark/blurry photo | 60-70% | Prompt user to retake |
| Complex layered outfit (jacket over shirt over tee) | 70-75% | May miss inner layers |
| Full ethnic outfit (saree with blouse + petticoat) | 75-80% | Saree detected as full-body, blouse may be occluded |

### Indian Garment Handling

| Garment | How It's Segmented | Notes |
|---------|-------------------|-------|
| Saree | Full-body garment | Subcategory "saree" via Claude Vision |
| Kurta + churidar | Separate top + bottom | Standard segmentation |
| Kurta + palazzo | Separate top + bottom | Standard segmentation |
| Lehenga | Bottom segment | Subcategory "lehenga" |
| Dupatta | Accessory/overlay | May require explicit detection |
| Salwar kameez | Top + bottom + optional dupatta | 2-3 segments |
| Indo-western blazer + kurta | Outerwear + top | Layered detection |

**Training data gap:** ATR and DeepFashion2 datasets are weak on Indian clothing. We will need a small fine-tuning dataset (~500-1000 labeled images of Indian garments) to improve SegFormer's accuracy on sarees, dupattas, lehengas, and other Indian-specific categories. This can be built gradually from our own users' confirmed segmentations.

### Cost Per OOTD Selfie

| Processing Step | Cost |
|----------------|------|
| SegFormer B2 inference | ~$0.005 (GPU time on T4) |
| Background removal (rembg) per segment | $0.00 (local, free) |
| Claude Vision per segment (3-4 segments) | ~$0.009-0.012 |
| **Total per selfie** | **~$0.015-0.02** |

At $0.02/selfie × 30 selfies/month = **$0.60/user/month** for the OOTD pipeline. Well within our unit economics.

### Sources

- [SegFormer B2 Clothes on HuggingFace](https://huggingface.co/mattmdjaga/segformer_b2_clothes)
- [Cloth Segmentation Repo](https://github.com/levindabhi/cloth-segmentation)
- [DeepFashion2 Dataset](https://github.com/switchablenorms/DeepFashion2)
- [Spectrum 3D Texture-Aware Parsing (2025)](https://arxiv.org/html/2508.06032)
- [GRWM Outfit Analysis](https://www.grwm.digital/blog/computer-vision-outfit-analysis)
- [ModaNet Street Fashion Dataset](https://arxiv.org/pdf/1807.01394)
- [DSA-YOLO on DeepFashion2](https://dl.acm.org/doi/10.1145/3722405.3722419)
- [YOLOv8 Multi-scale Clothing Segmentation](https://link.springer.com/article/10.1007/s10044-025-01589-5)

---

## Channel 2: Flatlay Batch Photography (Secondary — Week 2+)

### How It Works

User lays 3-8 items on a bed or floor with some spacing. AI detects and segments each item separately. One photo → multiple items added.

### Technical Pipeline

```
1. User photographs items laid flat on contrasting surface
         ↓
2. Grounding DINO 1.5 detects individual garments
   Text prompt: "shirt, pants, dress, skirt, jacket, blouse,
   kurta, saree, dupatta, lehenga, jeans, sneakers, heels"
         ↓
3. SAM2 generates precise segmentation mask for each detection
         ↓
4. Each segment → background removal
         ↓
5. Each segment → Claude Vision for attribute extraction
         ↓
6. User reviews batch: swipe through, confirm/adjust each
```

### Detection Pipeline Deep Dive

**Why Grounding DINO + SAM2 (not just SegFormer):**

SegFormer is designed for parsing clothing ON a person. For items laid flat on a surface, we need:
- **Object detection** (find where each item is) → Grounding DINO
- **Instance segmentation** (precise mask for each item) → SAM2

**Grounding DINO 1.5 capabilities:**
- Open-vocabulary detection — can detect any object described in text
- Zero-shot: no training needed, just describe what to look for
- 52.5 AP on COCO without any training on COCO
- Text prompt is customizable, so we can add Indian garment categories

**SAM2 (Segment Anything Model 2) capabilities:**
- Given a bounding box from Grounding DINO, generates pixel-precise masks
- State-of-the-art instance segmentation
- Works on any object type without training
- Can handle partial occlusion

### User Guidance for Best Results

In-app tips shown before batch capture:

```
📸 Tips for Best Results:
• Lay items on a WHITE or LIGHT surface (bedsheet, floor)
• Leave 2-3 inches between items
• Avoid overlapping items
• 5-8 items per photo works best
• Unfold items so main features are visible
• Good lighting helps — near a window works great
```

### Accuracy Expectations

| Scenario | Detection Rate | Notes |
|----------|---------------|-------|
| 5 items, well-spaced, light background | 90-95% | Ideal case |
| 5-8 items, moderate spacing | 85-90% | Recommended max |
| 8+ items, some overlap | 70-80% | Overlap reduces accuracy significantly |
| Items on patterned surface | 75-85% | Contrasting background strongly preferred |
| Dark items on dark surface | 60-70% | Insufficient contrast |

### When to Introduce

Don't show batch mode on Day 1. Introduce it after the user has 10+ items from OOTD selfies and is engaged:

```
"Want to add items faster? Try Batch Mode!
 Lay 5 items on your bed, snap a photo, done."
```

### Cost Per Batch Photo

| Processing Step | Cost |
|----------------|------|
| Grounding DINO inference | ~$0.01 (GPU) |
| SAM2 per detection (5-8 items) | ~$0.005-0.008 |
| Background removal per item | $0.00 (local) |
| Claude Vision per item | ~$0.003 × 5-8 = $0.015-0.024 |
| **Total per batch** | **~$0.03-0.04** |

One batch photo captures 5-8 items for ~$0.04. That's ~$0.005-0.008 per item — cheaper than individual photography.

### Sources

- [Grounding DINO GitHub](https://github.com/IDEA-Research/GroundingDINO)
- [Grounded SAM Paper](https://arxiv.org/abs/2401.14159)
- [Roboflow Outfit Transformation Workflow](https://blog.roboflow.com/transforming-outfits-with-roboflow-workflows/)

---

## Channel 3: Screenshot/Share Import (Supplementary — Day 1)

### How It Works

User screenshots a product on Myntra/Ajio/Amazon/Zara, shares it to ClosetAI via the OS share sheet. AI extracts the product image and categorizes it.

### Why This Is Powerful

- **Zero photography effort** — product images are already high-quality with clean white backgrounds
- **Captures new purchases** at the moment of buying — "just bought this, adding to closet"
- **Works for wishlisted items** — browse shopping apps, share interesting items
- **Better AI accuracy** than selfies — clean product photos have 90%+ attribute detection
- **Already familiar** — sharing content between apps is a standard mobile behavior

### Technical Implementation

**Android (primary target for India):**
```kotlin
// AndroidManifest.xml - Register as share target
<intent-filter>
    <action android:name="android.intent.action.SEND" />
    <category android:name="android.intent.category.DEFAULT" />
    <data android:mimeType="image/*" />
</intent-filter>
```

**iOS:**
```swift
// Share Extension - Info.plist
// Accepts image types shared from any app
```

**Processing pipeline:**
```
1. Receive shared image via OS share intent
         ↓
2. Detect product image region
   (usually the largest image area in the screenshot)
         ↓
3. Crop to product image, remove UI elements
         ↓
4. Background removal (usually already clean, but normalize)
         ↓
5. Claude Vision: full attribute extraction
   - Category, subcategory, colors, pattern
   - Brand (OCR from screenshot text if visible)
   - Price (OCR if visible)
         ↓
6. Auto-fill item details, user confirms with 1 tap
```

### Whering's Chrome Extension (Inspiration)

Whering has the most mature implementation of screenshot/web import:
- Browser extension on desktop: click any product image on a shopping website → captured and added to wardrobe
- "Cuts upload time in half" compared to manual photography
- Also works for past purchases by visiting order history pages

**For our mobile-first approach:** Share intent is even more natural than a browser extension. Indian women shop primarily on mobile (Myntra, Ajio, Amazon apps), not desktop.

### Accuracy

| Source | Detection Rate | Notes |
|--------|---------------|-------|
| Myntra product page screenshot | 95%+ | Clean white background, single item |
| Amazon product screenshot | 90%+ | Usually clean, sometimes has lifestyle photos |
| Ajio product screenshot | 90%+ | Similar to Myntra |
| Zara product screenshot | 85-90% | Some lifestyle photos with models |
| Instagram shopping post screenshot | 75-85% | More complex layouts |
| General web/social media screenshot | 70-80% | Unpredictable layouts |

### Cost Per Screenshot Import

| Processing Step | Cost |
|----------------|------|
| Image region detection | ~$0.001 |
| Background removal | $0.00 (local) |
| Claude Vision attributes | ~$0.003 |
| **Total per screenshot** | **~$0.004** |

Cheapest channel by far, since product images are clean and don't need segmentation.

### Sources

- [Whering Chrome Extension](https://whering.co.uk/digital-wardrobe-chrome-extension)
- [What Can Whering's Chrome Extension Do](https://whering.co.uk/faq/chrome-extension-what-to-use-it-for)
- [Myntra Visual Search +35% YoY](https://rezolve.com/customers/myntra-simplifies-product-discovery-and-increases-visual-image-search-adoption-by-35-yoy/)
- [Google Vision API Style Detection](https://cloud.googleblog.com/2016/04/introducing-Style-Detection-for-Google-Cloud-Vision-API.html)

---

## Channel 4: Purchase History Import (Power Feature — Month 3+)

### How It Works

User connects Gmail (read-only OAuth). App searches for order confirmation emails from Indian e-commerce platforms. Extracts product names, images, prices, dates. Presents for batch confirmation.

### Technical Implementation

```python
# gmail_import.py

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

FASHION_RETAILERS = {
    "myntra.com": {
        "sender_filter": "noreply@myntra.com",
        "subject_keywords": ["order", "confirmation", "shipped"],
        "image_selector": "img.product-image",
        "name_selector": ".product-name",
        "price_selector": ".product-price"
    },
    "amazon.in": {
        "sender_filter": "auto-confirm@amazon.in",
        "subject_keywords": ["order", "confirmation"],
        "image_selector": "img[src*='images-amazon']",
        "name_selector": ".item-title",
        "price_selector": ".item-price"
    },
    "ajio.com": {
        "sender_filter": "orders@ajio.com",
        "subject_keywords": ["order", "confirmation"],
        # Similar parsing patterns
    },
    "nykaa.com": {
        "sender_filter": "noreply@nykaa.com",
        "subject_keywords": ["order", "shipped"],
    },
    "zara.com": {
        "sender_filter": "noreply@zara.com",
        "subject_keywords": ["order", "confirmation"],
    },
    "hm.com": {
        "sender_filter": "noreply@hm.com",
        "subject_keywords": ["order", "confirmation"],
    }
}

def search_fashion_emails(gmail_service, retailers=FASHION_RETAILERS):
    """Search Gmail for fashion purchase confirmation emails."""

    all_items = []
    for domain, config in retailers.items():
        query = f"""
            from:({config['sender_filter']})
            subject:({' OR '.join(config['subject_keywords'])})
            newer_than:2y
        """
        results = gmail_service.users().messages().list(
            userId='me', q=query
        ).execute()

        for msg in results.get('messages', []):
            email = gmail_service.users().messages().get(
                userId='me', id=msg['id'], format='full'
            ).execute()
            items = parse_order_email(email, config)
            all_items.extend(items)

    return all_items

def parse_order_email(email, config):
    """Extract product details from order confirmation HTML."""
    html_body = get_email_html(email)
    soup = BeautifulSoup(html_body, 'html.parser')

    items = []
    # Extract product images, names, prices
    # Each retailer has different HTML structure
    # Parse using retailer-specific selectors

    return items
```

### Third-Party Receipt Parsing Services

| Service | Description | Coverage | Cost |
|---------|------------|----------|------|
| **Edison (Sift) API** | Professional email parsing | 11,000+ brands | Enterprise pricing |
| **Slice API** | Consumer purchase data extraction | Major retailers | Contact for pricing |
| **DIY with Gmail API + BeautifulSoup** | Custom parsing per retailer | Build as needed | Free (dev time only) |

**Our recommendation:** Start with DIY parsing for the top 5 Indian retailers (Myntra, Amazon, Ajio, Nykaa Fashion, Zara). These 5 cover 80%+ of online fashion purchases in India.

### Privacy Considerations (Critical for India)

**Personal Data Protection Act (DPDP Act, 2023):**
- Requires **explicit consent** for processing personal data including email access
- Must provide **clear purpose limitation** — "we only read fashion purchase emails"
- **Data minimization** — only extract product info, don't store email content
- Must offer data **deletion on request**

**User trust reality:**
- Indian users are particularly sensitive about granting Gmail access to unknown apps
- Expect **<10% opt-in rate** for email scanning
- This must be positioned as an OPTIONAL power feature, never the primary onboarding

**Trust-building UX:**
```
"Import Your Purchases (Optional)"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

We can find your recent fashion purchases from:
📦 Myntra  📦 Amazon  📦 Ajio  📦 Nykaa  📦 Zara

What we do:
✅ Search ONLY for order confirmation emails
✅ Extract product photos, names, and prices
✅ You confirm which items to add

What we DON'T do:
❌ Read any other emails
❌ Store email content
❌ Share data with anyone
❌ Access your email after import

[Connect Gmail (Read-Only)]    [Skip]
```

### Expected Yield

For an active online shopper in India:
- ~2-4 fashion orders per month on average
- ~2-3 items per order
- Over 2 years: **20-50 items** auto-discovered
- These are items with clean product photos, brand names, and purchase prices — higher quality data than selfie-extracted items

### Sources

- [Gmail API in Python](https://www.geeksforgeeks.org/python/how-to-read-emails-from-gmail-using-gmail-api-in-python/)
- [Edison API](https://developer.edison.tech/)
- [Slice API](https://developer.slice.com/)
- [Myntra API Docs](https://apidocs.myntra.com/)
- [India DPDP Act 2023](https://www.meity.gov.in/data-protection-framework)

---

## Channel 5: Closet Scanning (NOT Recommended — Research Says No)

### Why We Investigated It

The dream: open your closet doors, pan your phone camera across the hangers, and AI detects every item. This would digitize 30-50 items in 2-3 minutes.

### Why It Doesn't Work (Yet)

**The technical challenges are severe:**
- **Dense occlusion**: Clothes on hangers overlap heavily — only 10-20% of each garment is visible
- **Uniform backgrounds**: All items share the same closet rod/wall background
- **Non-rigid deformation**: Hanging garments fold and drape unpredictably
- **Scale variation**: Items at back of deep closet appear much smaller

**State of the art:**
- **DeepMark / DeepMark++** (ICCV 2019, WACV 2021): One-shot clothing detection, outperforms Mask R-CNN. But designed for single items, not dense closet scenes.
- **ClothPose** (ICCV 2023): Real-world garment pose benchmark including hanging configurations. 600 garments across 10 categories. But focused on pose estimation, not identification.
- **Robotics research**: Garment recognition from single-hanging-point using Kinect depth sensors. Designed for robots, not consumer phones.

**Practical assessment:** A closet scan could identify rough garment count and major categories ("you have ~15 items hanging, mix of tops and dresses") but NOT extract individual items with enough detail for a wardrobe app. Asking users to slide hangers apart for each photo defeats the purpose.

**Decision: Do NOT build this for V1-V3.** Revisit when dense object detection improves or if depth sensors become standard on phones.

### Sources

- [DeepMark: One-Shot Clothing Detection (ICCV 2019)](https://openaccess.thecvf.com/content_ICCVW_2019/papers/CVFAD/Sidnev_DeepMark_One-Shot_Clothing_Detection_ICCVW_2019_paper.pdf)
- [ClothPose: ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/papers/Xu_ClothPose_A_Real-world_Benchmark_for_Visual_Analysis_of_Garment_Pose_ICCV_2023_paper.pdf)
- [Fashion Meets Computer Vision Survey](https://dl.acm.org/doi/fullHtml/10.1145/3447239)
- [Clarifai Apparel Detection](https://clarifai.com/clarifai/main/models/apparel-detection)

---

## Channel 6: Smart Wardrobe Hardware (RFID/NFC — Future Only)

### What Exists Today

**ThreadRobe (most ambitious attempt):**
- Automated armoire using passive UHF RFID technology
- Users attach RFID tags, take a photo (~30 seconds per item setup)
- Robotic arm hangs, steams, and dispenses complete outfits
- **Price: $3,250-$4,250** for 100-200 item capacity
- Status: announced ~2017-2018, unclear if still shipping. Luxury niche.

**DIY RFID systems:**
- UHF RFID readers mounted in closet doors
- Passive tags cost ~$0.05-0.10 each
- Can detect which items are in closet vs being worn/in laundry
- Requires manual tagging of every garment

**NFC/UHF dual-tag approach:**
- NFC readers are built into smartphones, enabling easy tag registration
- UHF provides longer read range for in-closet detection
- Tags cost ~$0.10-0.30 per dual-tag

### The Reality in 2026

- No mass-market consumer smart wardrobe product exists
- Hardware cost ($3,000+) and setup friction kills distribution for a bootstrapped startup
- Some fashion brands (Zara, Decathlon) use RFID for supply chain, but tags are removed by consumers
- The "RFID in every garment" future requires industry-wide adoption

**Decision: Not relevant for V1-V3.** If RFID becomes standard in Indian retail (Reliance, Tata CLiQ, Myntra warehouses already use it), we could offer NFC scanning of tags at purchase time as a future feature.

**Near-term alternative idea:** Laundry-basket scanning. A photo of clothes going into the laundry basket (unfolded, partially visible) could track "last worn" dates using the same batch-detection AI from Channel 2. This solves the "virtual laundry basket" problem that Virtualrobe identified as a useful feature.

### Sources

- [ThreadRobe Smart Wardrobe](https://www.digitaltrends.com/home/threadrobe-smart-wardrobe/)
- [ThreadRobe RFID Journal](https://www.rfidjournal.com/news/robotics-and-rfid-to-manage-your-wardrobe/70254/)
- [RFID Wardrobe New Application](https://rfid-sticker.com/projects/retail/rfid-wardrobe-new-application-of-smart-wardrobe/)
- [Smart Closet Revolution](https://betterwithgoodlife.com/2025/06/the-smart-closet-revolution-rfid-and-ai-powered-wardrobe-management/)

---

## The Redesigned Onboarding Flow

### Minute 0-1: Quick Start (Zero Friction)

```
Screen 1: Welcome
├── "Your closet, but smarter."
├── [Continue with Google] ← 1 tap OAuth
├── [Continue with Apple]
└── [Continue with Email]

Screen 2: Tell Us About You (15 seconds)
├── "What's your name?" → text input
├── Gender: [Female] [Male] [Non-binary] [Prefer not to say]
└── Age group: [18-24] [25-34] [35-44] [45+]

Screen 3: Style Vibe (30 seconds)
├── 3x3 grid of outfit photos (women's fashion, Indian + Western mix)
├── "Tap 2-3 outfits that feel like YOU"
├── AI computes initial style archetype from selections
└── "Your Style DNA: Modern Classic ✨" ← FIRST WOW MOMENT
```

**Time elapsed: ~1 minute. User has:**
- An account
- A style archetype
- Already feels "this app gets me"

### Minute 1-2: First Items (The Hook)

```
Screen 4: "Let's See Today's Outfit!"
├── Big camera button (exciting, not intimidating)
├── "Take a quick mirror selfie — we'll do the rest"
├── User takes selfie → loading animation (2-3 seconds)
├── "We found 4 items!" → items appear with extracted photos
│   ├── 👚 Navy blouse (top) → [✓ Looks right]
│   ├── 👖 Black jeans (bottom) → [✓ Looks right]
│   ├── 👟 White sneakers (footwear) → [✓ Looks right]
│   └── 👜 Brown bag (accessory) → [✓ Looks right]
├── Each item: 1 tap to confirm, swipe to adjust details
└── "4 items added to your closet! 🎉"
```

**Time elapsed: ~2 minutes. User has 3-4 items in their closet.**

### Minute 2-3: First Value (The Aha Moment)

```
Screen 5: "Here's What You Could Wear Tomorrow"
├── AI generates a suggestion rearranging today's items
│   OR pairs one item with a suggestion from style library
├── "Swap the sneakers for heels and this becomes date-night ready"
├── Shows the outfit with style score and reasoning
├── "Add more items anytime — the more we know, the better we get"
└── [Enable Morning Outfit Notification ☀️]
    └── "We'll have your outfit ready at 8 AM"
```

**Time elapsed: ~3 minutes. User has:**
- 3-4 items in closet
- Seen their first outfit suggestion
- Enabled the morning notification (the habit hook)
- Zero pain, zero "setup"

### Day 2-7: Daily Habit Forms

```
8:00 AM push notification:
"Your outfit for today is ready ☀️"
├── User opens app → sees suggestion from their items
├── [Wear This ✓] [Show Me Another →] [I'll Pick Myself]
├── At bottom: "📸 Log today's OOTD to grow your closet"
│   └── Camera opens → selfie → 3-4 new items extracted
├── Streak counter: "Day 3 🔥"
└── Progress: "Your closet: 12 items → 15 items"

End of Day 7:
├── User has 15-25 items (from 7 selfies)
├── Suggestions are getting noticeably better
├── "7-day streak! 🔥 Unlocked: Shopping Gap Analysis"
└── First gap insight: "You have 8 tops but only 3 bottoms"
```

### Week 2-4: Power Features Appear

```
Week 2:
├── "Want to add items faster? Try Batch Mode 📸"
│   └── Introduce flatlay photography
├── "Share a screenshot from Myntra to add it instantly"
│   └── Screenshot share feature
└── "We noticed 3 items you haven't worn — let's style them!"

Week 3:
├── Gap analysis becomes meaningful: "A white sneaker would unlock 8 new outfits"
├── Closet insights appear: color distribution, category balance
├── Style DNA starts showing personalization from accept/reject data
└── "14-day streak! 🔥🔥 Unlocked: Style DNA Insights"

Week 4:
├── 30-50 items. Full intelligence active.
├── Seasonal suggestions: "Monsoon is coming — let's review your rain-ready items"
├── Cost-per-wear tracking starts (for items with purchase price)
└── "30-day streak! ⭐ Unlocked: Full Wardrobe Analytics"
```

### Month 2+: Complete Closet

```
Optional power features for committed users:
├── Purchase history import (Gmail OAuth)
├── Seasonal wardrobe review
├── "Items you haven't worn in 60 days" insights
├── Community outfit sharing
└── User has 50-100+ items without ever "setting up" their closet
```

---

## Gamification: Making Onboarding Fun

### Research: Why Gamification Works

- Gamified onboarding can lead to **62% increase in monthly active users**
- Users at a 7-day streak are **3.6x more likely to stay long-term** (Duolingo data)
- Streak freezes reduced churn by **21%** for at-risk users (Duolingo data)
- Progress bars and checklists reduce perceived effort and create momentum
- Loss aversion kicks in around Day 7 — users don't want to "lose" their streak

### The Streak System (Duolingo-Inspired)

```
Day 1:  "📸 First OOTD logged!"
Day 3:  "🔥 3-day streak! Your closet is growing"
Day 7:  "🔥🔥 7-day streak! Unlocked: AI Outfit Suggestions"
Day 14: "🔥🔥🔥 14-day streak! Unlocked: Style DNA Insights"
Day 30: "⭐ 30-day streak! Unlocked: Full Wardrobe Analytics"
Day 100: "💎 100-day streak! You're a ClosetAI power user"
```

**Streak freeze:** One free "skip day" per week (don't break the streak). Additional freezes available for Pro subscribers.

### Closet Completeness Score

Visual progress bar by category — humans hate incomplete progress bars:

```
Your Closet: 62% Complete
━━━━━━━━━━━━━━━━━━━━░░░░░░░░

Tops:        ████████████ 89%
Bottoms:     ██████░░░░░░ 45%
Dresses:     ████░░░░░░░░ 30%
Shoes:       ███░░░░░░░░░ 22%
Ethnic:      ██░░░░░░░░░░ 15%
Accessories: █░░░░░░░░░░░  8%

"Add 3 more bottoms to unlock complete outfit planning"
```

The "completeness" score is calculated against a reference capsule wardrobe (adjusted for the user's style and occasions). A user who only wears Western casual might be "90% complete" with 20 items, while someone who needs office + ethnic + party might need 50+ items for the same score.

### Feature Unlocks (Not Paywalls)

Lock features behind closet size, not subscriptions:

| Threshold | Unlocked Feature | Psychological Effect |
|-----------|-----------------|---------------------|
| 1 item | "What goes with this?" | Immediate utility |
| 5 items | Daily outfit suggestions | Habit formation begins |
| 10 items | Outfit calendar | Planning value |
| 15 items | Weather-based suggestions | Context intelligence |
| 25 items | Gap analysis ("what's missing") | Shopping intelligence |
| 30 items | Full wardrobe analytics | Dashboard satisfaction |
| 50 items | "Before You Buy" scanner | Power user feature |

Adding items feels like **progress toward rewards**, not a chore. The subscription (Pro/Premium) unlocks limits on these features (e.g., free gets 1 daily outfit, Pro gets 5), but the features themselves are unlocked by engagement.

### Social Mechanics for India

**WhatsApp sharing (primary viral channel):**
- "Share your OOTD" generates a beautiful card image
- Card includes outfit photo + style score + "Made with ClosetAI" branding
- Friends see it → "what app is this?" → download
- WhatsApp is THE viral channel in India, not Instagram. 500M+ Indian users.

**Festival challenges:**
- "Build your Diwali outfit collection" (October, 4 weeks before)
- "Navratri 9 Looks Challenge" (9 days, 9 outfit colors)
- "Monsoon Wardrobe Ready?" (June, pre-monsoon check)
- Seasonal urgency drives item additions

**Friends rating:**
- Share OOTD with friends for quick rating/reaction
- Think BeReal but for outfits
- "3 friends rated your outfit 🔥🔥🔥"
- Social validation = motivation to keep logging

### Sources

- [Duolingo Gamification Secrets](https://www.orizon.co/blog/duolingos-gamification-secrets)
- [Duolingo Streak Psychology](https://www.justanotherpm.com/blog/the-psychology-behind-duolingos-streak-feature)
- [Duolingo Streak Freeze 21% Churn Reduction](https://blog.duolingo.com/how-duolingo-streak-builds-habit/)
- [Gamification Onboarding Examples](https://userpilot.com/blog/onboarding-gamification/) — Userpilot
- [Gamification in Fashion](https://www.listrak.com/blog/gamification-in-fashion-turning-engagement-into-experience) — Listrak

---

## Cost Analysis: Total Onboarding AI Cost Per User

### Month 1 (Building the Closet)

| Channel | Items Added | Cost Per Item | Total Cost |
|---------|------------|---------------|------------|
| OOTD selfies (12 selfies, 3-4 items each) | ~40 items | ~$0.005 | $0.20 |
| Background removal (rembg, local) | 40 items | $0.00 | $0.00 |
| Claude Vision attributes | 40 items | $0.003 | $0.12 |
| Screenshot imports | ~10 items | $0.004 | $0.04 |
| **Total Month 1** | **~50 items** | | **~$0.36** |

### Ongoing (Month 2+)

| Channel | Items Added | Cost | Total |
|---------|------------|------|-------|
| OOTD selfies (20 selfies/month) | ~15 new items | $0.005 | $0.075 |
| Claude Vision | 15 items | $0.003 | $0.045 |
| Screenshot imports | ~5 items | $0.004 | $0.02 |
| **Total Monthly** | **~20 new items** | | **~$0.14** |

### At Scale

| Users | Month 1 Onboarding Cost | Monthly Ongoing Cost | Total Year 1 |
|-------|------------------------|---------------------|--------------|
| 1,000 | $360 | $140/month | $1,900 |
| 10,000 | $3,600 | $1,400/month | $19,000 |
| 50,000 | $18,000 | $7,000/month | $95,000 |

At $0.36/user for Month 1 onboarding + $0.14/month ongoing, the AI costs are well within our unit economics ($4.99/month Pro subscription).

---

## Technical Architecture: Onboarding Pipeline

### Infrastructure Requirements

| Component | Tool | Cost |
|-----------|------|------|
| Outfit segmentation | SegFormer B2 (self-hosted) | GPU: ~$50-100/month on a T4 instance |
| Object detection (flatlay) | Grounding DINO 1.5 (self-hosted) | Same GPU instance |
| Precise masks (flatlay) | SAM2 (self-hosted) | Same GPU instance |
| Attribute extraction | Claude Vision API | Pay-per-call (~$0.003/item) |
| Background removal | rembg with BiRefNet (self-hosted) | Same GPU or CPU instance |
| Email parsing | Gmail API + BeautifulSoup | Free |
| Screenshot parsing | OS share intent + Claude Vision | ~$0.003/screenshot |

**Total infrastructure for onboarding AI: ~$100-150/month** for a GPU instance running SegFormer + Grounding DINO + SAM2 + rembg. This handles up to ~10,000 users before needing to scale.

### Data Model for Progressive Closet Building

```sql
-- Track how each item was added (for analytics and quality improvement)
ALTER TABLE wardrobe_items ADD COLUMN source TEXT DEFAULT 'manual';
  -- Values: 'ootd_selfie', 'flatlay_batch', 'screenshot_import',
  --         'email_import', 'manual', 'before_you_buy'

ALTER TABLE wardrobe_items ADD COLUMN source_confidence NUMERIC;
  -- AI confidence score for auto-detected items (0-1)
  -- Items with confidence < 0.7 get extra user confirmation prompts

ALTER TABLE wardrobe_items ADD COLUMN user_confirmed BOOLEAN DEFAULT FALSE;
  -- Whether user has explicitly confirmed AI-extracted attributes

-- Track onboarding progress
CREATE TABLE onboarding_progress (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    items_added INTEGER DEFAULT 0,
    ootd_streak INTEGER DEFAULT 0,
    longest_streak INTEGER DEFAULT 0,
    streak_freeze_used_this_week BOOLEAN DEFAULT FALSE,
    features_unlocked JSONB DEFAULT '[]',
    closet_completeness NUMERIC DEFAULT 0,
    last_ootd_date DATE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id)
);

-- Track streak and gamification
CREATE TABLE achievements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
    type TEXT NOT NULL,
    -- 'streak_3', 'streak_7', 'streak_14', 'streak_30', 'streak_100',
    -- 'first_item', 'closet_10', 'closet_25', 'closet_50',
    -- 'first_outfit_accepted', 'gap_analysis_unlocked'
    earned_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_onboarding_user ON onboarding_progress(user_id);
CREATE INDEX idx_achievements_user ON achievements(user_id);
```

---

## India-Specific Considerations

### Language Support

Support Hindi + English labels for clothing categories in the confirmation UI:

| English | Hindi | Category Code |
|---------|-------|--------------|
| Shirt | शर्ट | top |
| Kurta | कुर्ता | top (ethnic) |
| Jeans | जीन्स | bottom |
| Salwar | सलवार | bottom (ethnic) |
| Saree | साड़ी | dress (ethnic) |
| Lehenga | लहंगा | bottom (ethnic) |
| Dupatta | दुपट्टा | accessory (ethnic) |
| Churidar | चूड़ीदार | bottom (ethnic) |
| Palazzo | पलाज़ो | bottom |
| Kurti | कुर्ती | top (ethnic) |

### Market Context

- India Fashion E-commerce market: **USD 21.6B (2025)**, growing at **24.2% CAGR** to USD 98.5B by 2032
- Myntra alone has **55M active users**
- The wardrobe management layer on top of this ecosystem is **wide open**
- No dominant wardrobe app exists for the Indian market
- LimeRoad has a "scrapbook" feature but no true closet management
- Whering, Cladwell, Indyx are all Western-focused

### Sources

- [India Fashion Ecommerce Market](https://www.coherentmi.com/industry-reports/india-fashion-ecommerce-market)
- [Myntra AI Features](https://news.microsoft.com/source/asia/features/indias-myntra-innovates-with-generative-ai-to-help-shoppers-put-the-right-look-together/)
- [Wardrobe Management Apps Research (MDPI)](https://www.mdpi.com/2071-1050/17/9/4159)

---

## Implementation Priority

### Phase 1 (MVP, Months 1-3)

| Priority | Channel | Effort | Impact |
|----------|---------|--------|--------|
| **P0** | OOTD selfie (SegFormer B2 + Claude Vision) | 2-3 weeks | Core onboarding, daily habit |
| **P0** | Style quiz (5 visual questions) | 1 week | Instant value, zero items needed |
| **P0** | Streak system + notifications | 1 week | Retention, habit formation |
| **P1** | Screenshot share import | 1 week | Captures purchases, low effort |
| **P1** | Feature unlock progression | 1 week | Gamification, motivation |
| **P2** | Closet completeness score | 3 days | Progress visualization |

### Phase 2 (Months 3-6)

| Priority | Channel | Effort | Impact |
|----------|---------|--------|--------|
| **P1** | Flatlay batch photography (Grounding DINO + SAM2) | 2 weeks | Faster item addition |
| **P1** | Gmail purchase import | 2 weeks | Power users, 20-50 items |
| **P2** | WhatsApp OOTD sharing | 1 week | Viral growth |
| **P2** | Festival challenges | 1 week per challenge | Seasonal engagement |

### Phase 3 (Months 6+)

| Priority | Channel | Effort | Impact |
|----------|---------|--------|--------|
| **P2** | Social OOTD rating (friends) | 2 weeks | Community, engagement |
| **P3** | Laundry basket scanning | 1 week | Track item availability |
| **P3** | SegFormer fine-tuning on Indian garments | 2-3 weeks | Improved accuracy |

### Do NOT Build (V1-V3)

| Feature | Reason |
|---------|--------|
| Closet scanning (open wardrobe photo) | Accuracy too low (60-70%), dense occlusion problem unsolved |
| RFID/NFC hardware integration | Kills distribution, $3000+ hardware, no consumer adoption |
| Full 80-question style quiz | Too much friction. 5 visual questions max. |
| Desktop browser extension | India is mobile-first. Mobile share intent covers this. |

---

## Success Metrics

### Onboarding Funnel

| Stage | Target | Measurement |
|-------|--------|-------------|
| Sign up → first selfie | 70%+ | Users who take OOTD photo on Day 1 |
| First selfie → confirm items | 85%+ | Users who confirm AI-extracted items |
| Day 1 → Day 2 return | 50%+ | Users who open app on Day 2 |
| Day 1 → Day 7 streak | 30%+ | Users who log 7 consecutive OOTDs |
| 10+ items threshold | 60%+ by Day 7 | Users with meaningful closet size |
| 30+ items threshold | 40%+ by Day 30 | Users with full outfit intelligence |

### Quality Metrics

| Metric | Target | Why It Matters |
|--------|--------|---------------|
| AI item detection accuracy | 85%+ | Users shouldn't have to correct most items |
| User confirmation rate | 80%+ | High = AI is getting it right |
| Average items per OOTD selfie | 3-4 | Lower = segmentation missing items |
| Time from selfie → items confirmed | <30 seconds | Speed is critical for daily habit |
| Selfie retake rate | <15% | Low = most photos work first try |

### Growth Metrics

| Metric | Target | Timeline |
|--------|--------|----------|
| Items added per user per week | 8-12 | Week 1-4 |
| Morning notification open rate | 30%+ | Ongoing |
| OOTD streak average length | 12+ days | Month 2+ |
| Screenshot imports per user per month | 3-5 | Month 1+ |
| WhatsApp shares per user per month | 2-3 | Month 2+ |

---

## Summary

The closet digitization problem is the #1 killer of wardrobe apps. Every competitor asks users to photograph 50-100 items upfront — a 3-4 hour chore that 70%+ abandon.

Our approach:
1. **OOTD-first**: Mirror selfie → AI extracts 3-4 items → 30 seconds → done
2. **Progressive building**: Closet grows through daily use, not setup sessions
3. **Multiple channels**: OOTD selfies + screenshot imports + batch photos + email import
4. **Gamification**: Streaks, completeness scores, feature unlocks make adding items feel like progress
5. **Immediate value**: First outfit suggestion within 3 minutes, before closet is "complete"

The result: users get a complete digital wardrobe of 50-100 items within a month — and they never "set up" anything. It just happened.

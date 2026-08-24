---
name: geo-schema
description: Schema.org structured data audit and generation for rich results and entity clarity — detect, validate, and generate JSON-LD markup. Schema is NOT an AI-citation lever (Ahrefs controlled study, May 2026); it earns rich results and keeps entity data unambiguous.
metadata:
  version: "1.0.0"
  author: geo-seo-claude
  tags: [geo, schema, structured-data, json-ld, entity-recognition, ai-discoverability]
---

# GEO Schema & Structured Data

## Purpose

Structured data does two jobs well: **earning Google rich results** and **keeping entity data unambiguous** (who the organization is, what it offers, which profiles belong to it). That is the scope of this skill.

**What schema does NOT do: lift AI citations.** In the Ahrefs controlled study (1,885 pages that added JSON-LD, reported May 2026 via Search Engine Journal), citation rates moved ChatGPT +2.2%, AI Mode +2.4%, AIO -4.6% — all within noise. Adding markup alone produced no citation lift on any platform. Do not sell schema as a GEO tactic.

**The nuance worth keeping** (SSRN, Feb 2026): schema that carries concrete, extractable facts (dates, prices, locations, specs) can still correlate with citation — but the lift comes from the quotable data, not the markup itself. Put the facts in visible, well-structured page content first; schema is the machine-readable echo, not the signal.

With that framing, complete and accurate structured data remains worthwhile: rich results still win SERP real estate, and clean entity data (Organization, sameAs, contactPoint) removes ambiguity for every system — search engines, knowledge graphs, and AI platforms alike.

## How to Use This Skill

1. Fetch the target page HTML using curl or WebFetch
2. Detect all existing structured data (JSON-LD, Microdata, RDFa)
3. Validate detected schemas against Schema.org specifications
4. Identify missing recommended schemas based on business type
5. Generate ready-to-use JSON-LD code blocks
6. Output GEO-SCHEMA-REPORT.md

---

## Step 1: Detection

### Scan for JSON-LD
Look for `<script type="application/ld+json">` blocks in the HTML. Parse each block as JSON. A page may contain multiple JSON-LD blocks — collect all of them.

### Scan for Microdata
Look for elements with `itemscope`, `itemtype`, and `itemprop` attributes. Map the hierarchy of nested items. Note: Microdata is harder for AI crawlers to parse than JSON-LD. Flag a recommendation to migrate to JSON-LD if Microdata is the only format found.

### Scan for RDFa
Look for elements with `typeof`, `property`, and `vocab` attributes. Similar to Microdata — recommend migration to JSON-LD.

### Priority Order
JSON-LD is the **strongly recommended format** for GEO. Google, Bing, and AI platforms all process JSON-LD most reliably. If the site uses Microdata or RDFa exclusively, flag this as a high-priority migration.

---

## Step 2: Validation

For each detected schema block, validate:

1. **Valid JSON**: Is the JSON-LD syntactically valid? Check for trailing commas, unquoted keys, malformed strings.
2. **Valid @type**: Does the `@type` match a recognized Schema.org type? Check against https://schema.org/docs/full.html.
3. **Required Properties**: Does the schema include all required properties for its type? (See per-type requirements below.)
4. **Recommended Properties**: Does the schema include recommended properties that improve rich-result eligibility and entity clarity?
5. **sameAs Links**: Does the schema include `sameAs` properties linking to other platform presences?
6. **URL Validity**: Do all URLs in the schema resolve (not 404)?
7. **Nesting**: Is the schema properly nested (e.g., author inside Article, address inside Organization)?
8. **Rendering Method**: Is the JSON-LD in the server-rendered HTML or injected via JavaScript? Per Google's December 2025 guidance, **JavaScript-injected structured data may face delayed processing**. Flag any schema that requires JS execution.

---

## Step 3: Schema Types for GEO

### Organization (CRITICAL — every business site)
The backbone of unambiguous entity data: it states WHAT the business is in a form every search engine and knowledge graph can parse without inference.

**Required properties:**
- `@type`: "Organization" (or subtype: Corporation, LocalBusiness, etc.)
- `name`: Official business name
- `url`: Official website URL
- `logo`: URL to logo image (ImageObject preferred)

**Recommended properties for GEO:**
- `sameAs`: Array of ALL platform URLs (see sameAs strategy below)
- `description`: 1-2 sentence description of the organization
- `foundingDate`: ISO 8601 date
- `founder`: Person schema
- `address`: PostalAddress schema
- `contactPoint`: ContactPoint with telephone, email, contactType
- `areaServed`: Geographic area
- `numberOfEmployees`: QuantitativeValue
- `industry`: Text or DefinedTerm
- `award`: Array of awards received
- `knowsAbout`: Array of topics the organization is expert in (entity clarity signal)

### LocalBusiness (for businesses with physical locations)
Extends Organization. Critical for local AI search results and Google Gemini.

**Additional required properties:**
- `address`: Full PostalAddress
- `telephone`: Phone number
- `openingHoursSpecification`: Operating hours

**Recommended for GEO:**
- `geo`: GeoCoordinates (latitude, longitude)
- `priceRange`: Price indicator
- `aggregateRating`: AggregateRating schema
- `review`: Array of Review schemas
- `hasMap`: URL to Google Maps

### Article + Author (CRITICAL for publishers)
Author markup supports E-E-A-T presentation and article rich results; it also keeps byline facts consistent for any system parsing the page.

**Article required:**
- `@type`: "Article" (or NewsArticle, BlogPosting, TechArticle)
- `headline`: Article title
- `datePublished`: ISO 8601
- `dateModified`: ISO 8601 (critical for freshness signals)
- `author`: Person or Organization schema
- `publisher`: Organization schema with logo
- `image`: Representative image

**Author (Person) required for GEO:**
- `name`: Full name
- `url`: Author page URL on the site
- `sameAs`: LinkedIn, Twitter, personal site, Google Scholar, ORCID
- `jobTitle`: Professional title
- `worksFor`: Organization schema
- `knowsAbout`: Array of expertise areas
- `alumniOf`: Educational institutions
- `award`: Professional awards

### Product (for e-commerce)
**Required:**
- `name`, `description`, `image`
- `offers`: Offer with price, priceCurrency, availability
- `brand`: Brand schema
- `sku` or `gtin`/`mpn`

**Recommended for GEO:**
- `aggregateRating`: AggregateRating
- `review`: Array of individual reviews
- `category`: Product category
- `material`, `weight`, `width`, `height` (where applicable)

### FAQPage
**Status as of 2024**: Google restricts FAQ rich results to government and health sites. FAQPage schema still makes Q&A pairs trivially machine-readable, but treat it as a parsability convenience, not a citation play — the Ahrefs controlled study (May 2026) found no AI-citation lift from adding JSON-LD. Implement it where Q&A content exists; expect clean extraction, not a visibility bump.

**Structure:**
- `@type`: "FAQPage"
- `mainEntity`: Array of Question schemas, each with `acceptedAnswer` containing an Answer schema

### SoftwareApplication (for SaaS)
**Required:**
- `name`, `description`
- `applicationCategory`: e.g., "BusinessApplication"
- `operatingSystem`: Supported platforms
- `offers`: Pricing

**Recommended for GEO:**
- `aggregateRating`: User ratings
- `featureList`: Array of features (concrete extractable facts — remember the lift comes from the data, not the markup)
- `screenshot`: Screenshots
- `softwareVersion`: Current version
- `releaseNotes`: Link to changelog

### WebSite + SearchAction (for sitelinks search box)
**Structure:**
```json
{
  "@type": "WebSite",
  "name": "Site Name",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

### Person (standalone — for personal brands, authors, thought leaders)
Use as a standalone schema on About/Bio pages. This builds the entity graph for individual expertise.

**Required:** `name`, `url`
**Recommended for GEO:** `sameAs`, `jobTitle`, `worksFor`, `knowsAbout`, `alumniOf`, `award`, `description`, `image`

### speakable Property (for voice/AI assistants)
The `speakable` property marks specific sections of content as particularly suitable for voice and AI assistant consumption. Add to Article or WebPage schemas.

```json
{
  "@type": "Article",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".article-summary", ".key-takeaway"]
  }
}
```
This marks which passages are intended for text-to-speech and assistant consumption. Treat it as a hint for voice surfaces; there is no controlled evidence it changes AI citation behavior.

---

## Step 4: Deprecated/Changed Schemas to Flag

| Schema | Status | Note |
|---|---|---|
| HowTo | Rich results deprecated Aug 2023 | Still useful for AI parsing, but do not promise rich results |
| FAQPage | Restricted to govt/health Aug 2023 | Still useful for AI parsing (see above) |
| SpecialAnnouncement | Deprecated 2023 | Was for COVID; remove if still present |
| CourseInfo | Replaced by Course updates 2024 | Use updated Course schema properties |
| VideoObject `contentUrl` | Changed behavior 2024 | Must point to actual video file, not page URL |
| Review snippet | Stricter enforcement 2024 | Self-serving reviews on product pages may not display |

Flag any deprecated schemas found and recommend replacements.

---

## Step 5: sameAs Strategy (CRITICAL for Entity Clarity)

The `sameAs` property is the highest-value structured data property for entity clarity. It tells every consuming system: "This entity on my website is the SAME entity as these profiles elsewhere." That removes ambiguity across search engines, knowledge graphs, and AI platforms — consistent entity data is a prerequisite for being recognized at all, even though (per the Ahrefs May 2026 controlled study) the markup alone does not lift citations.

### Recommended sameAs Links (in priority order)

1. **Wikipedia article** — highest authority entity link
2. **Wikidata item** — machine-readable entity identifier (e.g., `https://www.wikidata.org/wiki/Q12345`)
3. **LinkedIn** — company page or personal profile
4. **YouTube** — channel URL
5. **Twitter/X** — profile URL
6. **Facebook** — page URL
7. **Crunchbase** — company profile (for startups/tech)
8. **GitHub** — organization or personal profile (for tech)
9. **Google Scholar** — author profile (for researchers/academics)
10. **ORCID** — researcher identifier (for academics)
11. **Instagram** — profile URL
12. **Apple App Store / Google Play** — app listings (for software)
13. **BBB** — Better Business Bureau listing (for US businesses)
14. **Industry directories** — relevant vertical directories

### sameAs Audit Process
1. Collect all known web presences for the entity
2. Check that each URL resolves (not 404 or redirected)
3. Verify the Organization/Person schema includes ALL of them
4. Check that the information on each platform is consistent (name, description, founding date, etc.)
5. Flag any platforms where the entity should have a presence but does not

---

## Step 6: JSON-LD Generation

Based on the detected business type, generate ready-to-paste JSON-LD blocks. Always generate:

1. **Organization or Person** (depending on entity type) — always
2. **WebSite with SearchAction** — always for the homepage
3. **Business-type-specific** — Article for publishers, Product for e-commerce, LocalBusiness for local, SoftwareApplication for SaaS
4. **BreadcrumbList** — for any page deeper than homepage

### Generation Rules
- Use the `@graph` pattern to include multiple schemas in one JSON-LD block
- All URLs must be absolute (not relative)
- Include `@id` properties for cross-referencing between schemas
- Use ISO 8601 for all dates
- Include `speakable` on Article schemas with CSS selectors pointing to key content sections
- Place JSON-LD in `<head>` section — NOT injected via JavaScript

### Template: Organization with Full GEO Signals
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 600,
    "height": 60
  },
  "description": "Concise description of what the company does.",
  "foundingDate": "2020-01-15",
  "founder": {
    "@type": "Person",
    "name": "Founder Name",
    "sameAs": "https://www.linkedin.com/in/founder"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-555-5555",
    "contactType": "customer service",
    "email": "support@example.com"
  },
  "sameAs": [
    "https://en.wikipedia.org/wiki/Company_Name",
    "https://www.wikidata.org/wiki/Q12345",
    "https://www.linkedin.com/company/company-name",
    "https://www.youtube.com/@companyname",
    "https://twitter.com/companyname",
    "https://github.com/companyname",
    "https://www.crunchbase.com/organization/company-name"
  ],
  "knowsAbout": [
    "Topic 1",
    "Topic 2",
    "Topic 3"
  ]
}
```

---

## Scoring Rubric (0-100)

| Criterion | Points | How to Score |
|---|---|---|
| Organization/Person schema present and complete | 15 | 15 if full, 10 if basic, 0 if none |
| sameAs links (5+ platforms) | 15 | 3 per valid sameAs link, max 15 |
| Article schema with author details | 10 | 10 if full author schema, 5 if name only, 0 if none |
| Business-type-specific schema present | 10 | 10 if complete, 5 if partial, 0 if missing |
| WebSite + SearchAction | 5 | 5 if present, 0 if not |
| BreadcrumbList on inner pages | 5 | 5 if present, 0 if not |
| JSON-LD format (not Microdata/RDFa) | 5 | 5 if JSON-LD, 3 if mixed, 0 if only Microdata/RDFa |
| Server-rendered (not JS-injected) | 10 | 10 if in HTML source, 5 if JS but in head, 0 if dynamic JS |
| speakable property on articles | 5 | 5 if present, 0 if not |
| Valid JSON + valid Schema.org types | 10 | 10 if no errors, 5 if minor issues, 0 if major errors |
| knowsAbout property on Organization/Person | 5 | 5 if present with 3+ topics, 0 if missing |
| No deprecated schemas present | 5 | 5 if clean, 0 if deprecated schemas found |

---

## Output Format

Generate **GEO-SCHEMA-REPORT.md** with:

```markdown
# GEO Schema & Structured Data Report — [Domain]
Date: [Date]

## Schema Score: XX/100

## Detected Schemas
| Page | Schema Type | Format | Status | Issues |
|---|---|---|---|---|
| / | Organization | JSON-LD | Valid | Missing sameAs |
| /blog/post-1 | Article | JSON-LD | Valid | No author schema |

## Validation Results
[List each schema with pass/fail per property]

## Missing Recommended Schemas
[List schemas that should be present based on business type but are not]

## sameAs Audit
| Platform | URL | Status |
|---|---|---|
| Wikipedia | [URL or "Not found"] | Present/Missing |
| LinkedIn | [URL or "Not found"] | Present/Missing |
[Continue for all recommended platforms]

## Generated JSON-LD Code
[Ready-to-paste JSON-LD blocks for each missing or incomplete schema]

## Implementation Notes
- Where to place each JSON-LD block
- Server-rendering requirements
- Testing with Google Rich Results Test and Schema.org Validator
```

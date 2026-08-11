---
name: generacia-cinu-content
version: 1.0.0
description: "Generates social media, email, and marketing content in the Generácia Činu brand voice. Use when creating posts, emails, landing pages, or any content for the Prime Agent Masterclass under the Generácia Činu movement."
arguments:
  type: object
  properties:
    content_type:
      type: string
      description: "Type of content to generate (social_post, email, landing_page_text, thread, speech)"
      enum: ["social_post", "email", "landing_page_text", "thread", "speech"]
    platform:
      type: string
      description: "Target platform (TikTok, Instagram, YouTube, Facebook, Twitter, LinkedIn)"
    topic:
      type: string
      description: "Main topic of the content"
    pillar:
      type: string
      description: "Generácia Činu pillar (Veriť, Milovať, Budovať)"
      enum: ["Veriť", "Milovať", "Budovať"]
  required: [content_type, topic]

---

# 👑 Generácia Činu — Content Generation Skill

## Brand Voice Rules

### Always use:
- "Veriť. Milovať. Budovať." as signature or slogan
- ✦ symbol (stars) as visual separator
- #002147 (Polárna modrá) and #CD7F32 (Kybernetická bronzová) as primary colors
- References to Štefánik as the original technologist
- Constructive, forward-looking language
- Technical metaphors from aviation, space, code, and cybernetics

### Never use:
- Victim rhetoric ("ukradli nám", "ublížili nám")
- Political attacks on specific parties
- Folklore or archaic nationalist symbols
- Corporate buzzwords or generic marketing fluff

## Content Pillars

### ⭐ Veriť (Believe)
- Štefánik parallels and historical vision
- Technological capability and vision
- "Slovensko nie je montážna dielňa"
- Building trust in AI and autonomous systems

### 💙 Milovať (Love)
- Practical AI agent use cases
- Community building and collaboration
- "Reverzný brain-drain" — bringing talent back
- Passion for technology and building

### 🔧 Budovať (Build)
- Concrete how-to content
- Production deployment and real results
- "Koniec rétoriky obete. Začiatok algoritmu činu."
- Call to action: join and build

## Output Formats

### Social Post (TikTok/IG/Reels)
- 30-second script format
- Epická synťáková hudba
- Focus: fascination with technology
- CTA: "Pridaj sa do Generácie Činu"

### Email
- Subject: starts with ✦ or ⚡
- Opens with: "Hey {{name}},"
- Closes with: "Veriť. Milovať. Budovať."
- Tone: direct, personal, without fluff

### Twitter/X Thread
- First tweet: hook with Štefánik parallel
- Middle tweets: 3-5 technical points
- Last tweet: CTA + ✦✦✦

### Speech / Script
- "Máme pred sebou zadanie." as opener
- Use aviation metaphors ("odlepenie sa od zeme")
- Never use victim language
- End with: "Veriť. Milovať. Budovať."

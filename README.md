<div align="center">

# 👋 Hey there, I'm zylcold

iOS Developer · Swift / SwiftUI · AI-assisted development

<a href="https://github.com/zylcold"><img src="https://img.shields.io/github/followers/zylcold?label=Follow&style=social" alt="GitHub followers" loading="lazy" /></a>

</div>

---

## 🚀 About Me

<img align="right" alt="Coding" width="400" src="https://raw.githubusercontent.com/devSouvik/devSouvik/master/gif3.gif" loading="lazy">

```swift
class Developer {
    let name = "zylcold"
    let role = "iOS Developer"
    let language_spoken = ["zh_CN", "en_US"]
    
    func getCurrentFocus() -> [String] {
        return [
            "SwiftUI & Combine",
            "iOS Architecture",
            "Open Source"
        ]
    }
    
    func getFutureGoals() -> [String] {
        return [
            "Master ARKit",
            "Contribute to Swift",
            "Build Amazing Apps"
        ]
    }
}
```
<br clear="both"/>

## 🧑‍💻 Tech Stack & Tools

<div align="center">

### 💻 Languages
![Swift](https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white)
![Objective-C](https://img.shields.io/badge/Objective--C-3A95E3?style=for-the-badge&logo=apple&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### 📱 Frameworks & Libraries
![SwiftUI](https://img.shields.io/badge/SwiftUI-0D96F6?style=for-the-badge&logo=swift&logoColor=white)
![UIKit](https://img.shields.io/badge/UIKit-2396F3?style=for-the-badge&logo=uikit&logoColor=white)
![Combine](https://img.shields.io/badge/Combine-FF6B35?style=for-the-badge&logo=swift&logoColor=white)
![CoreData](https://img.shields.io/badge/CoreData-1575F9?style=for-the-badge&logo=coredata&logoColor=white)

### 🛠️ Development Tools
![Xcode](https://img.shields.io/badge/Xcode-007ACC?style=for-the-badge&logo=Xcode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Fastlane](https://img.shields.io/badge/Fastlane-00F200?style=for-the-badge&logo=fastlane&logoColor=white)
![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-000000?style=for-the-badge&logo=githubcopilot&logoColor=white)
![Cursor](https://img.shields.io/badge/Cursor-222222?style=for-the-badge&logo=cursor&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-8C5A3C?style=for-the-badge&logo=anthropic&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-74AA9C?style=for-the-badge&logo=openai&logoColor=white)

### 📊 Databases & Backend
![Firebase](https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white)
![Realm](https://img.shields.io/badge/Realm-39477F?style=for-the-badge&logo=realm&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

</div>

## 📊 GitHub Analytics

Public GitHub activity snapshot. Private work and offline contributions are not fully represented here.

<div align="center">
  <img height="165em" src="https://github-readme-stats.vercel.app/api?username=zylcold&show_icons=true&rank_icon=github&theme=tokyonight&include_all_commits=true&hide_border=true" alt="GitHub Stats" loading="lazy"/>
  <img height="165em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=zylcold&layout=compact&langs_count=6&theme=tokyonight&hide_border=true&hide=html,css" alt="Top Languages" loading="lazy"/>
</div>

## 🛠 Featured Projects

| Project | Focus | Stack |
|---------|-------|-------|
| [DriftBuild](https://github.com/zylcold/DriftBuild) | Swift build tooling and developer workflow experiments. | `Swift` |
| [XcodeBar](https://github.com/zylcold/XcodeBar) | Xcode-focused utility work for day-to-day iOS development. | `Swift` |
| [owl-skills](https://github.com/zylcold/owl-skills) | Reusable skills and conventions for agent-assisted engineering. | `Python` `Agents` |
| [daily_stock_analysis](https://github.com/zylcold/daily_stock_analysis) | LLM-driven market analysis workflow with data, news, dashboard, and notifications. | `AI` `Automation` |

## 📚 Learning & Growth Journey

<div align="center">

```mermaid
flowchart LR
    Start([iOS Foundations])

    subgraph Core["Core iOS Engineering"]
        Swift["Swift Language"]
        UIKit["UIKit / Auto Layout"]
        SwiftUI["SwiftUI"]
        Concurrency["Swift Concurrency"]
        Combine["Combine / Reactive Streams"]
    end

    subgraph Architecture["Architecture & App Quality"]
        MVVM["MVVM / MVVM-C"]
        Clean["Clean Architecture"]
        Modular["Modularization"]
        Testing["Unit / UI Testing"]
        Performance["Launch, Memory, Rendering"]
    end

    subgraph Tooling["Developer Tooling"]
        Xcode["Xcode Workflows"]
        CI["GitHub Actions / Fastlane"]
        BuildTools["Build Automation"]
        Debugging["LLDB / Instruments"]
    end

    subgraph Product["Product Delivery"]
        UX["Interaction Polish"]
        Release["Release Discipline"]
        Observability["Crash / Metrics Feedback"]
        Docs["Technical Writing"]
    end

    subgraph AI["AI-Assisted Engineering"]
        Prompting["Prompt Design"]
        Agents["Agent Workflows"]
        Validation["Tool-driven Validation"]
        Templates["Reusable Coding Templates"]
    end

    subgraph Output["Open Source & Shipping"]
        OSS["Open Source Projects"]
        Apps["Launch iOS Apps"]
        Community["Share / Write / Speak"]
    end

    Start --> Swift --> UIKit --> SwiftUI
    Swift --> Concurrency
    SwiftUI --> Combine
    UIKit --> MVVM
    SwiftUI --> MVVM
    MVVM --> Clean --> Modular
    Modular --> Testing --> Performance
    Performance --> Release
    Xcode --> BuildTools --> CI
    Debugging --> Performance
    CI --> Release
    UX --> Release
    Release --> Observability --> Docs
    Prompting --> Agents --> Validation --> Templates
    Templates --> BuildTools
    Validation --> Testing
    Docs --> OSS
    Templates --> OSS
    OSS --> Apps
    Apps --> Community

    classDef foundation fill:#e1f5fe,stroke:#0288d1,color:#0d47a1
    classDef quality fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20
    classDef tooling fill:#fff3e0,stroke:#ef6c00,color:#e65100
    classDef ai fill:#f3e5f5,stroke:#7b1fa2,color:#4a148c
    classDef output fill:#fce4ec,stroke:#c2185b,color:#880e4f

    class Start,Swift,UIKit,SwiftUI,Concurrency,Combine foundation
    class MVVM,Clean,Modular,Testing,Performance,UX,Release,Observability,Docs quality
    class Xcode,CI,BuildTools,Debugging tooling
    class Prompting,Agents,Validation,Templates ai
    class OSS,Apps,Community output
```

</div>

### 🎯 Current Focus
```swift
let currentFocus: [String: [String]] = [
    "iOS Architecture": [
        "modular feature boundaries",
        "testable MVVM / coordinator flows",
        "clean dependency direction"
    ],
    "SwiftUI": [
        "advanced animations",
        "state management",
        "UIKit interoperability"
    ],
    "Performance": [
        "startup time",
        "memory pressure",
        "scrolling and rendering smoothness"
    ],
    "AI Workflow": [
        "agent planning",
        "tool-driven validation",
        "repeatable coding templates"
    ]
]
```

### 🚀 2026 Goals
- [ ] Ship reusable AI-assisted iOS developer workflow templates
- [ ] Build a tighter local loop for plan -> edit -> test -> review
- [ ] Launch 2 iOS apps or polished prototypes
- [ ] Publish technical notes about Swift, iOS architecture, and AI-assisted engineering
- [ ] Share practical lessons through open source, writing, or community talks

## 🤖 Agent Engineering Notes (2026)

### 🧠 Agent Knowledge Map
- **Planning**: Break tasks into verifiable checkpoints before coding
- **Tool Use**: Prefer deterministic tools (search, tests, CI logs) over guesswork
- **Memory**: Persist stable conventions and avoid session-only assumptions
- **Validation**: Run review/security checks before final output
- **Feedback Loop**: Use comment-driven iteration to refine small PRs quickly

### 🧰 Agent Workflow I Use
```text
Intent -> Plan -> Search -> Edit -> Validate -> Review -> Ship
```

### ⭐ Agent Projects (Recent Star References)
- [microsoft/autogen](https://github.com/microsoft/autogen) - Multi-agent orchestration patterns
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) - Role-based collaborative agents
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) - Stateful agent graphs
- [OpenInterpreter/open-interpreter](https://github.com/OpenInterpreter/open-interpreter) - Local tool-using code agent
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) - Software engineering agent runtime

## 🛡 Developer Philosophy

<div align="center">

| Principle | Description |
|-----------|-------------|
| 🧹 **Clean Code** | *"Code is read more often than it is written"* |
| 🚀 **Performance** | *"Premature optimization is the root of all evil"* |
| 🤝 **Collaboration** | *"Alone we can do so little; together we can do so much"* |
| 📚 **Learning** | *"Stay hungry, stay foolish"* |

</div>

## 📫 Let's Connect & Collaborate

<div align="center">

<p>
<a href="https://github.com/zylcold">
  <img src="https://img.shields.io/badge/GitHub-zylcold-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>
</p>

For project discussions, please open an issue in the relevant repository.

</div>

## 🖖 Fun Facts & Terminal

<div align="center">

```bash
$ whoami
zylcold

$ cat interests.txt
🔍 Reverse engineering iOS apps
🤖 Automation enthusiast - "If it can be automated, it will be"
🕶️ AR/VR exploration
🔧 Raspberry Pi tinkering
☕ Coffee-driven development

$ uptime
iOS development since 2018 📱

$ ps aux | grep passion
swift      1337  0.1  0.2  building_amazing_apps
automation 2022  0.0  0.1  scripting_everything  
learning   2024  1.0  0.5  exploring_new_tech
vibe      2026  1.0  0.6  ai_pair_programming
```

</div>

---

> "Code is like humor. When you have to explain it, it’s bad." – Cory House

<div align="center">

<img src="https://raw.githubusercontent.com/zylcold/zylcold/output/github-contribution-grid-snake.svg" alt="Snake animation" loading="lazy" />

**Thanks for visiting! 🚀**

*Made with ❤️ and lots of ☕*

</div>

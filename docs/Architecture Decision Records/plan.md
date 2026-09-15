ADR-003: Why Redis?

Context:
Weather data is requested frequently.

Options:
1. PostgreSQL
2. Redis
3. No caching

Decision:
Redis

Reason:
Weather data does not need second-level freshness,
and caching reduces external API requests.

Trade-offs:
Additional infrastructure and cache invalidation complexity.









                    GardenOps
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     Frontend       Backend        Database
     React/TS       Django         PostgreSQL
        │           DRF
        │              │
        │        Authentication
        │        Authorization
        │              │
        │        Business Logic
        │              │
        │       Transactions
        │              │
        │         Redis Cache
        │              │
        │      Background Jobs
        │              │
        └──────────────┼──────────────┘
                       │
                    Docker
                       │
                  GitHub Actions
                       │
                     AWS
                       │
             Monitoring / Logging



additionally:
    Tests
    Security
    OpenAPI
    Load Testing
    Architecture Docs
    GitHub Issues / PRs

AI:
    plant search by photo/text
    AI chatbot/recommendations
    weather-aware recommendations



///////
Django
PostgreSQL
REST API
Auth
Permissions
Tests
Docker
CI/CD
AWS
Redis
Background jobs
Observability

AI layer:
Garden data
     +
Weather
     +
Plant information
     ↓
Recommendation Service
     ↓
LLM
     ↓
"Your tomatoes may need..."






.//
GardenOps
     ↓
좋은 프로젝트 만들기
     ↓
GitHub에 공개
     ↓
README / Demo / Architecture
     ↓
Resume에 3~4 strong bullets
     ↓
Application
     ↓
Networking
     ↓
Interview


///////
19. 네 상황에서 내가 가장 걱정하는 부분

솔직히 말하면:

인턴십 없음
Co-op 없음
동아리 경험 없음
GPA 낮음

이것들이 모두 사실이라면, 프로젝트 하나가 모든 걸 해결해주지는 못해.

하지만 그렇다고 네가 방법이 하나밖에 없는 것도 아니야.

너에게는:

① GardenOps

→ 깊은 engineering evidence

② UniConnect

→ AWS/serverless + hackathon + event-driven architecture

③ 기존 프로젝트들

→ breadth

④ VCN volunteer

→ 실제 team experience가 생기면 매우 중요

⑤ GitHub Issues/PR

→ collaboration-like evidence

⑥ LeetCode/interview prep

→ technical interview 대비

가 있어.

특히 VCN 같은 실제 조직에서 코드/기술 업무를 경험할 기회가 생기면 GardenOps를 계속 혼자 만드는 것보다 interview signal 측면에서 굉장히 가치가 커질 수 있어.


20. 그리고 GardenOps의 최종 목표를 이렇게 정의하자

나는 지금부터 curriculum을 조금 수정해서:

"A student building a Django app"

가 아니라

"A new-grad engineer who designed, tested, deployed, monitored, and documented a production-minded web application."

으로 보이게 만들고 싶어.

그리고 senior engineer가 봤을 때 가장 좋은 반응은:

"This isn't production scale, obviously. But this person understands what production problems look like."








Phase 4  DRF / REST APIs             ← 현재
   ↓
Phase 5  React + TypeScript
   ↓
Phase 6  Authentication & Authorization
   ↓
Phase 7  Testing / QA
   ↓
Phase 8  Docker / Full-stack containerization
   ↓
Phase 9  CI/CD / GitHub Actions
   ↓
Phase 10 AWS / Deployment / Security
   ↓
⭐ Phase 11 Production Engineering
      ├── Error handling
      ├── Validation
      ├── Transactions
      ├── Concurrency
      ├── Query optimization
      ├── Redis
      ├── Background jobs
      ├── Observability
      ├── API documentation
      └── Load testing
   ↓
⭐ Phase 12 Engineering Simulation
      ├── Issues
      ├── Branches
      ├── PRs
      ├── Code review
      ├── ADRs
      └── Incident/debugging exercise
   ↓
⭐ Phase 13 AI / Smart Garden Features
      ├── Weather integration
      ├── AI recommendations
      ├── Plant search
      └── AI-assisted garden insights
   ↓
⭐ Phase 14 Final Production Polish
      ├── README
      ├── Architecture diagram
      ├── Demo
      ├── Security review
      ├── Performance report
      └── Resume-ready project
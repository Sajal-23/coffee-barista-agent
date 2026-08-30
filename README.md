# AI Coffee Barista — RAG Agent POC

## Grounded AI Agent using Google ADK, Gemini, RAG, Streamlit & Cloud Run

A proof of concept demonstrating how a conversational AI agent can use a structured business knowledge source to provide grounded recommendations through a user-facing application.

The POC uses a coffee-shop scenario to demonstrate an **AI Barista** that understands customer preferences, retrieves relevant menu information, and provides recommendations grounded in the available menu rather than inventing products.

---

## Objective

The objective of this POC was to explore a practical architecture for moving from:

**Structured Business Knowledge → Retrieval → AI Agent → User Interaction → Cloud Deployment**

The coffee-shop scenario provides a simple but useful demonstration of concepts that can be extended to other business domains where an AI agent needs access to controlled organizational knowledge.

---

## What the POC Demonstrates

The solution demonstrates several key capabilities:

* Conversational AI interaction
* AI agent development using Google ADK
* Gemini-powered reasoning
* Retrieval-Augmented Generation (RAG)
* Grounding responses in a structured menu
* Preference-based recommendations
* Allergen-aware responses
* Streamlit-based user interface
* Cloud Run deployment
* Cloud-based AI application architecture
* Foundation for evolving from static knowledge to dynamic retrieval

---

## High-Level Architecture

```text
                         CUSTOMER
                            │
                            ▼
                    ┌───────────────┐
                    │   Streamlit   │
                    │  Chat UI      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Google ADK   │
                    │  AI Agent     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Retrieval /   │
                    │ Menu Tool     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Menu /        │
                    │ Knowledge     │
                    │ Source        │
                    └───────┬───────┘
                            │
                            ▼
                    Grounded Context
                            │
                            ▼
                    ┌───────────────┐
                    │ Gemini Model  │
                    │ + Agent Logic │
                    └───────┬───────┘
                            │
                            ▼
                       AI Response
                            │
                            ▼
                       CUSTOMER
```
<img width="2918" height="1608" alt="image" src="https://github.com/user-attachments/assets/3c6a1f51-2b30-4115-a90a-69be89106754" />

---

## Agent Behavior

The AI Barista is designed to:

1. Understand the customer's preference.
2. Retrieve available menu information.
3. Ground recommendations in the available menu.
4. Consider relevant attributes such as strength, temperature, sweetness, dietary requirements, and allergens.
5. Ask for clarification when the customer's request is ambiguous.
6. Avoid recommending items that are not available in the knowledge source.

This demonstrates an important principle for enterprise AI applications:

> **The agent should be grounded in controlled business knowledge rather than relying solely on the model's general knowledge.**

---

## RAG and Grounding

The initial POC uses a structured menu data source containing information such as:

* Item name
* Description
* Price
* Tags
* Allergens

The agent accesses this information through a retrieval/tool layer before generating recommendations.

This provides a simple example of how organizational knowledge can be connected to an AI agent.

For a larger production knowledge base, the same architectural concept can evolve toward a managed retrieval layer and semantic/vector search.

---

## Example Interactions

The POC can be evaluated using scenarios such as:

### Preference-based recommendation

**Customer:**
"I want something strong and cold."

**Expected behavior:**
The agent identifies appropriate items from the available menu.

### Out-of-knowledge request

**Customer:**
"Do you have a matcha frappuccino?"

**Expected behavior:**
The agent should recognize that the requested item is not present in the available menu rather than inventing a product.

### Dietary / allergen-aware request

**Customer:**
"I'm looking for a dairy-free option."

**Expected behavior:**
The agent should use the menu's dietary and allergen information when making recommendations.

These scenarios demonstrate the importance of **grounding and controlled knowledge retrieval** in conversational AI.

---

## Technology Stack

The POC explores the following technologies:

* **Google ADK** — agent development framework
* **Gemini** — generative AI model
* **Streamlit** — conversational application interface
* **Google Cloud Run** — application deployment
* **Structured menu data** — initial knowledge source
* **Cloud Firestore / Vector Search** — potential evolution for dynamic retrieval

The Google Codelab provided the technical learning foundation for the implementation.

**Reference:**
[Google Codelab — Deploy a RAG AI Agent in Streamlit using Google ADK and Cloud Run](https://codelabs.developers.google.com/codelabs/cloud-run/build-streamlit-rag-agent-google-adk-cloud-run)

---

## Architecture Evolution

The POC demonstrates an initial architecture that can evolve as the business knowledge base becomes larger and more dynamic.

### Initial POC

```text
Streamlit
    ↓
Google ADK Agent
    ↓
Retrieval Tool
    ↓
Structured Menu
```

### Potential Production Architecture

```text
                    User
                     │
                     ▼
              Conversational UI
                     │
                     ▼
                AI Agent
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     Business Logic       Retrieval Layer
                                │
                                ▼
                       Vector / Knowledge
                             Store
                                │
                                ▼
                         Enterprise Data
```

A production implementation could introduce persistent data storage, semantic retrieval, stronger identity and access controls, monitoring, evaluation, and integration with business systems.

---

## Key Architecture Lessons

### 1. Grounding matters

An AI agent becomes more useful when its responses are connected to authoritative business information.

### 2. Knowledge should be separated from the agent

Keeping business knowledge in a separate data source allows the knowledge layer to evolve without redesigning the entire conversational experience.

### 3. Retrieval can scale beyond static data

A small structured file is appropriate for a learning POC. A production implementation can move toward managed databases and vector search as the knowledge base grows.

### 4. The agent is part of a larger system

The AI model itself is only one component.

A useful enterprise AI solution also requires:

**User Interface + Agent + Retrieval + Knowledge + Security + Deployment + Governance**

### 5. Production architecture requires additional controls

A POC demonstrates feasibility. A production implementation would require additional consideration of:

* Authentication and authorization
* Persistent session management
* Data security
* Observability
* Evaluation and testing
* Error handling
* Cost management
* Knowledge freshness
* Governance
* Operational monitoring

---

## Business Applications

Although the demonstration uses a coffee-shop scenario, the underlying architecture can be applied to many knowledge-grounded business assistants.

Potential applications include:

* Customer service assistants
* Internal knowledge assistants
* Product recommendation systems
* Employee support assistants
* Operations assistants
* Policy and procedure assistants
* Enterprise knowledge agents
* Domain-specific AI copilots

The key pattern is:

**Business Knowledge → Retrieval → AI Reasoning → Contextual Response**

---

## Relationship to AI-Native Operating Models

This POC is also an example of a broader AI-native operating model.

A repeatable business capability can evolve through:

```text
Business Process
       ↓
Structured Knowledge
       ↓
Retrieval
       ↓
AI Agent
       ↓
Human + AI Interaction
       ↓
Business Execution
```

This connects directly with the broader **AI-Native Operating Model** architecture documented elsewhere in this portfolio.

---

## Future Enhancements

Potential future enhancements include:

* Firestore-based dynamic menu management
* Vector Search
* Persistent conversation sessions
* Authentication
* Agent evaluation
* Observability and monitoring
* Business-system integration
* Multi-agent workflows
* Personalized recommendations
* Enterprise knowledge integration

These are potential architectural extensions rather than claims about the current POC implementation.

---

## Learning & Reference

This POC was developed as a hands-on exploration of Google's AI agent and cloud deployment technologies, using the Google Codelab as the technical learning reference.

The purpose of this repository is to document the **architecture, implementation experience, and lessons learned**, rather than reproduce the source tutorial.

---

## About

**Sajal Sharma**
Enterprise & Digital Transformation Advisor

AI & Cloud Strategy | System & Solution Architecture | Program & Portfolio Leadership | Project Recovery

**Sugmsoft Digital**

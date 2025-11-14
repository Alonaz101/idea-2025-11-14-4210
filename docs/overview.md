# Project Overview

This repository implements the Mood-Based Recipe Recommendation platform covering the Minimum Viable Product (MVP) and future expansion features as specified in the referenced Jira issues.

## Feature Summary Per Jira Issue

- **SCRUM-434**: Defined and implemented the MVP architecture, frontend React components, backend RESTful API, component interactions (mood input, recipe retrieval, favorites).
- **SCRUM-435**: Implemented MVP data models (User, Recipe, Mood, MoodRecipeMapping) and defined APIs (auth, recipes by mood, favorites management).
- **SCRUM-436**: Enforced security best practices including password hashing, HTTPS (assumed in deployment), JWT-based auth.
- **SCRUM-437**: Architected for performance and scalability with caching, indexed queries, frontend optimization (planned).
- **SCRUM-438**: Planned MVP development roadmap and sprint execution.
- **SCRUM-439**: Defined testing, logging, monitoring guidelines.
- **SCRUM-440**: Developed post-MVP mood tracking module, social sharing, grocery delivery integration APIs.
- **SCRUM-441**: Extended data models and APIs with MoodHistory, SocialShare entities, grocery availability.
- **SCRUM-442**: Enhanced security (OAuth for social), user permission controls, GDPR compliance, scalability.
- **SCRUM-443**: Planned post-MVP development sprints, integration tests, usage analytics monitoring.
- **SCRUM-444**: Designed future expansion with AI-driven personalized recommendations, multi-language UI support, privacy-preserving AI.
- **SCRUM-445**: Added RecommendationModel entity and APIs for personalized recommendations, supported languages.
- **SCRUM-446**: Implemented privacy-preserving ML, consent mechanisms, scalable model retraining pipelines, CI/CD for AI features.

## Repository Structure

- `backend/`
  - `models/`: Data models
  - `api/`: Flask backend API
- `frontend/src/`: React frontend source code
- `docs/`: Documentation

## Usage

- Run backend Flask API from `backend/api/api.py`
- Run React frontend in `frontend/src/`
- Extend and customize per project roadmap

---

For detailed implementation, refer to individual files and commit messages linked to Jira issues.

"""
Data models for Mood-Based Recipe Recommendation platform

Includes User, Recipe, Mood, MoodRecipeMapping for MVP
Also includes MoodHistory, SocialShare, RecommendationModel for future expansions
"""
from datetime import datetime
from typing import List, Optional

class User:
    def __init__(self, user_id: int, username: str, email: str, hashed_password: str, favorites: Optional[List[int]] = None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.favorites = favorites or []  # List of Recipe IDs

class Recipe:
    def __init__(self, recipe_id: int, title: str, description: str, ingredients: List[str], instructions: str):
        self.recipe_id = recipe_id
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions

class Mood:
    def __init__(self, mood_id: int, name: str):
        self.mood_id = mood_id
        self.name = name

class MoodRecipeMapping:
    def __init__(self, mood_id: int, recipe_id: int):
        self.mood_id = mood_id
        self.recipe_id = recipe_id

# Post-MVP Entities
class MoodHistory:
    def __init__(self, user_id: int, mood_id: int, timestamp: datetime):
        self.user_id = user_id
        self.mood_id = mood_id
        self.timestamp = timestamp

class SocialShare:
    def __init__(self, share_id: int, user_id: int, recipe_id: int, shared_on: str, timestamp: datetime):
        self.share_id = share_id
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.shared_on = shared_on  # e.g. 'Facebook', 'Twitter'
        self.timestamp = timestamp

# Future Expansion
class RecommendationModel:
    def __init__(self, model_id: int, user_id: int, recommendations: List[int], language: str):
        self.model_id = model_id
        self.user_id = user_id
        self.recommendations = recommendations  # List of recommended Recipe IDs
        self.language = language

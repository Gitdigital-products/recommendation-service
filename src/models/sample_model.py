# Placeholder ML model for recommendations
# Later: replace with collaborative filtering, content-based, or hybrid approaches

class SampleRecommender:
    def __init__(self):
        pass

    def recommend(self, user_id: int, limit: int = 5):
        # Mock: return static IDs
        return [{"item_id": i, "score": 1.0 - i*0.1} for i in range(limit)]

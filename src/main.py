from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Recommendation Service API",
    description="Provides AI-powered product and content recommendations",
    version="1.0.0"
)

class RecommendationRequest(BaseModel):
    user_id: int
    limit: int = 5

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "recommendation-service"}

@app.post("/recommendations")
def get_recommendations(req: RecommendationRequest):
    # For now, return mock recs
    recs = [
        {"item_id": 101, "score": 0.95},
        {"item_id": 202, "score": 0.91},
        {"item_id": 303, "score": 0.88},
    ][:req.limit]
    return {"user_id": req.user_id, "recommendations": recs}

"""Flask app for showcasing educational platform features and metrics."""

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Render the homepage with platform features and metrics."""
    features = [
        {
            "title": "Personalized Learning",
            "desc": "Adaptive lessons tailored to each student’s pace and interests."
        },
        {
            "title": "World-class Mentors",
            "desc": "On-demand mentoring from industry experts and top educators."
        },
        {
            "title": "Hands-on Projects",
            "desc": "Project-based curriculum that builds real portfolio-ready work."
        },
    ]
    metrics = {
        "students": "1M+",
        "courses": "2K+",
        "countries": "150+"
    }
    current_year = datetime.now().year
    return render_template(
        'index.html',
        features=features,
        metrics=metrics,
        current_year=current_year
    )

if __name__ == '__main__':
    app.run(debug=True)